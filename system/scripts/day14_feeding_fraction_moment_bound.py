#!/usr/bin/env python3
"""Conditional feeding-fraction geometry from two published tensor pairs.

The relaxation permits any positive magnetic-substate remainder. Printed
centers and quoted-error boxes are inputs, not likelihoods or confidence sets.
"""
from __future__ import annotations

import argparse
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
import hashlib
from itertools import combinations
import json
from pathlib import Path

from day14_unobserved_feeding_transfer import kernel, tensor, transfer

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"
TOL = D("1e-50")


def dec(value):
    if isinstance(value, F):
        return D(value.numerator) / D(value.denominator)
    return D(str(value))


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def geometry(tj):
    v2, c2 = tensor(tj, 2)
    v4, c4 = tensor(tj, 4)
    points = sorted((v2[i], v4[i], tm) for i, tm in enumerate(range(-tj, tj+1, 2)) if tm >= 0)
    def chain(seq):
        out = []
        for point in seq:
            while len(out) >= 2 and cross(out[-2], out[-1], point) <= 0:
                out.pop()
            out.append(point)
        return out
    hull = chain(points)[:-1] + chain(points[::-1])[:-1]
    faces = []
    for a, b in zip(hull, hull[1:]+hull[:1]):
        dx, dy = b[0]-a[0], b[1]-a[1]
        faces.append(dict(a=dy, b=-dx, c=dy*a[0]-dx*a[1], m_twice=[a[2], b[2]]))
    return dict(points=points, hull=hull, faces=faces, constants=[c2, c4], vectors=[v2, v4])


def normalized_point(values, geo):
    return [dec(values[i])/dec(geo["constants"][i]).sqrt() for i in range(2)]


def slack(face, point):
    return dec(face["c"]) - dec(face["a"])*point[0] - dec(face["b"])*point[1]


def positive_certificate(point, geo):
    for a, b, c in combinations(geo["points"], 3):
        area = dec(cross(a, b, c))
        if not area:
            continue
        aa, bb, cc = [[dec(p[0]), dec(p[1])] for p in [a, b, c]]
        w1, w2 = cross(aa, point, cc)/area, cross(aa, bb, point)/area
        weights = [1-w1-w2, w1, w2]
        if min(weights) >= -TOL:
            return [(p[2], max(D(0), w)) for p, w in zip([a, b, c], weights)]
    raise ValueError("printed moment point has no positive-population certificate")


def population(cert, tj):
    result = {tm: D(0) for tm in range(-tj, tj+1, 2)}
    for tm, weight in cert:
        if tm == 0:
            result[0] += weight
        else:
            result[tm] += weight/2
            result[-tm] += weight/2
    return list(result.values())


def analyze(precision):
    with localcontext() as ctx:
        ctx.prec = precision
        data = json.loads((RUN / "tm167-feeding-fraction-input.json").read_text())
        checks = {}
        def check(name, value):
            checks[name] = bool(value)
            if not value:
                raise AssertionError(name)
        ti, tf = data["parent"]["spin_twice"], data["target"]["spin_twice"]
        pg, tg = geometry(ti), geometry(tf)
        parent = [D(data["parent"]["rho2"]), D(data["parent"]["rho4"])]
        child = [D(data["target"]["rho2"]), D(data["target"]["rho4"])]
        for role in ["parent", "target"]:
            for rank in [2, 4]:
                x = D(data[role][f"rho{rank}"])
                f = D(data["radiation_crosswalk"][role][f"F{rank}"])
                obs = D(data["radiation_crosswalk"][role][f"IO_A{rank}"])
                tolerance = D(".0005") + abs(f)*D(".0005") + abs(x)*D(".000005") + D(".0000000025")
                check(f"source_rho_F_A_{role}_{rank}", abs(x*f-obs) <= tolerance)
        np, nc = normalized_point(parent, pg), normalized_point(child, tg)
        pc = positive_certificate(np, pg)
        positive_certificate(nc, tg)
        check("printed_parent_and_child_positive_feasible", all(slack(f, np) >= -TOL for f in pg["faces"]) and all(slack(f, nc) >= -TOL for f in tg["faces"]))
        ratios = [F(transfer(ti, tf, 2, rank)["rational_eigenvalue"]) for rank in [2, 4]]
        u = [dec(ratios[i]) * (dec(tg["constants"][i])/dec(pg["constants"][i])).sqrt() for i in range(2)]
        feed = [u[i]*parent[i] for i in range(2)]
        nf = normalized_point(feed, tg)
        check("known_transfer_component_positive_feasible", all(slack(f, nf) >= -TOL for f in tg["faces"]))
        candidates = []
        for f in tg["faces"]:
            n, den = slack(f, nc), slack(f, nf)
            if den > TOL:
                candidates.append((n/den, f, n, den))
        bound, active, numerator, denominator = min(candidates, key=lambda x:x[0])
        bound = min(D(1), bound)
        check("nontrivial_center_bound", 0 < bound < 1)
        rest = [(nc[i]-bound*nf[i])/(1-bound) for i in range(2)]
        check("bound_satisfies_all_facets", all(slack(f, rest) >= -TOL for f in tg["faces"]))
        endpoints = [next(p for p in tg["points"] if p[2] == tm) for tm in active["m_twice"]]
        fraction = (rest[0]-dec(endpoints[0][0]))/dec(endpoints[1][0]-endpoints[0][0])
        rc = [(endpoints[0][2], 1-fraction), (endpoints[1][2], fraction)]
        check("two_point_remainder_certificate", 0 <= fraction <= 1 and abs((1-fraction)*dec(endpoints[0][1])+fraction*dec(endpoints[1][1])-rest[1]) < TOL)
        check("slightly_above_bound_fails_active_facet", numerator-(bound+D(".000001"))*denominator < 0)
        k = kernel(ti, tf, 2)
        pp, rp = population(pc, ti), population(rc, tf)
        fp = [sum((dec(q)*p for q, p in zip(row, pp)), D(0)) for row in k]
        total = [bound*a+(1-bound)*b for a, b in zip(fp, rp)]
        reconstructed = [dec(tg["constants"][i]).sqrt()*sum((dec(v)*p for v, p in zip(tg["vectors"][i], total)), D(0)) for i in range(2)]
        check("explicit_positive_full_child_certificate", min(total) >= -TOL and abs(sum(total)-1) < TOL and all(abs(a-b) < TOL for a,b in zip(reconstructed, child)))
        # A box of quoted marginal half-widths has no probability interpretation.
        witness_parent, witness_child, intersections = [], [], []
        for i, rank in enumerate([2, 4]):
            pe, ce = D(data["parent"][f"quoted_error_rho{rank}"]), D(data["target"][f"quoted_error_rho{rank}"])
            plo, phi = sorted([u[i]*(parent[i]-pe), u[i]*(parent[i]+pe)])
            lo, hi = max(plo, child[i]-ce), min(phi, child[i]+ce)
            check(f"quoted_box_w1_intersection_rank{rank}", lo <= hi)
            v = (lo+hi)/2
            witness_child.append(v)
            witness_parent.append(v/u[i])
            intersections.append([lo, hi])
        wpn, wcn = normalized_point(witness_parent, pg), normalized_point(witness_child, tg)
        wpc = positive_certificate(wpn, pg)
        check("box_w1_witness_is_physical", all(slack(f, wpn) >= -TOL for f in pg["faces"]) and all(slack(f, wcn) >= -TOL for f in tg["faces"]))
        check("box_w1_witness_matches_transfer", all(abs(u[i]*witness_parent[i]-witness_child[i]) < TOL for i in range(2)))
        check("source_doublet_and_missing_covariance_preserved", data["target"]["multiplet"] == "D" and data["unknown_covariance"] is None and data["measured_target_feeding_weight"] is None)
        return dict(precision=precision, checks=checks, check_count=len(checks), passed=all(checks.values()),
                    center_bound=bound, minimum_other_population_fraction=1-bound,
                    active_remainder_m_twice=active["m_twice"], parent_positive_example=pc,
                    remainder_positive_example=rc, reconstructed_child_rho=reconstructed,
                    known_feeding_component_rho=feed, U=u, target_positive_pair_vertices=len(tg["points"]),
                    quoted_marginal_box_w1=dict(parent_rho=witness_parent, child_rho=witness_child,
                                               child_interval_intersections=intersections, parent_positive_example=wpc,
                                               confidence_or_likelihood_interpretation=None),
                    scope="sharp only for fixed printed tensors and declared positive-remainder relaxation, not a measured fraction or confidence limit",
                    measured_target_feeding_weight=None, actual_covariance=None)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN / "tm167-feeding-fraction-audit.json")
    args = parser.parse_args()
    low, high = analyze(80), analyze(110)
    assert abs(low["center_bound"]-high["center_bound"]) < D("1e-60")
    high["precision_80_vs_110_agreement_to_60digits"] = True
    high["dependency_sha256"] = hashlib.sha256((ROOT/"system/scripts/day14_unobserved_feeding_transfer.py").read_bytes()).hexdigest()
    high["source_input_sha256"] = hashlib.sha256((RUN/"tm167-feeding-fraction-input.json").read_bytes()).hexdigest()
    args.output.write_text(json.dumps(high, ensure_ascii=False, indent=2, default=str) + "\n")
    print(json.dumps({k:high[k] for k in ["passed", "check_count", "center_bound", "minimum_other_population_fraction", "active_remainder_m_twice", "quoted_marginal_box_w1", "precision_80_vs_110_agreement_to_60digits"]}, default=str))


if __name__ == "__main__":
    main()
