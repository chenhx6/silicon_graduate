#!/usr/bin/env python3
"""Small fixed-N PNC-CSM response calculation for Cd AMR blocking.

This is a transparent CMPC/Fock-space calculation, not a rerun of the full
Zhang et al. Nilsson space.  It keeps two neutron orbits (d5/2 and g7/2),
constructs -omega Jx explicitly, diagonalises a monopole pairing Hamiltonian
at fixed N, and removes the selected blocked orbit from the pair-scattering
operator in the odd-A sectors.  The output therefore tests algebraic trends
(pair correlation, blocking, alignment, Q20 and a normalised V_pi-nu proxy),
not absolute Cd spectroscopy.

Dependencies: Python >=3.10, numpy, scipy.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import eigsh


OUT = Path(__file__).resolve().parent
VREF = 1.2  # MeV; Roy/Rather effective semiclassical reference, not a TBME.


@dataclass(frozen=True)
class Orbit:
    name: str
    j: float
    eps: float
    qcoef: float


ORBITS = (
    Orbit("nu_d5/2", 2.5, 0.00, -0.050),
    Orbit("nu_g7/2", 3.5, 0.28, -0.032),
)


def m_values(j: float) -> tuple[float, ...]:
    n = int(round(2 * j))
    return tuple(-j + i for i in range(n + 1))


STATES = tuple((a, m) for a, orb in enumerate(ORBITS) for m in m_values(orb.j))
INDEX = {s: i for i, s in enumerate(STATES)}
N_STATES = len(STATES)


def bitcount(x: int) -> int:
    return x.bit_count()


def basis_for_n(n: int) -> tuple[int, ...]:
    return tuple(mask for mask in range(1 << N_STATES) if bitcount(mask) == n)


def apply_annihilate(mask: int, idx: int) -> tuple[int, int] | None:
    if not (mask >> idx) & 1:
        return None
    phase = -1 if (mask & ((1 << idx) - 1)).bit_count() % 2 else 1
    return mask ^ (1 << idx), phase


def apply_create(mask: int, idx: int) -> tuple[int, int] | None:
    if (mask >> idx) & 1:
        return None
    phase = -1 if (mask & ((1 << idx) - 1)).bit_count() % 2 else 1
    return mask | (1 << idx), phase


def op_pair(mask: int, a: int, ma: float, b: int, mb: float) -> tuple[int, int] | None:
    """Apply P_a^dagger(ma) P_b(mb) to a Fock mask."""
    ibp = INDEX[(b, mb)]
    ibn = INDEX[(b, -mb)]
    iap = INDEX[(a, ma)]
    ian = INDEX[(a, -ma)]
    # P_b = a_{b,-m} a_{b,m}; rightmost operator acts first.
    x = apply_annihilate(mask, ibp)
    if x is None:
        return None
    mask1, s1 = x
    x = apply_annihilate(mask1, ibn)
    if x is None:
        return None
    mask2, s2 = x
    # P_a^dagger = a^dagger_{a,m} a^dagger_{a,-m}.
    x = apply_create(mask2, ian)
    if x is None:
        return None
    mask3, s3 = x
    x = apply_create(mask3, iap)
    if x is None:
        return None
    mask4, s4 = x
    return mask4, s1 * s2 * s3 * s4


def one_body_matrices(omega: float, basis: tuple[int, ...]) -> tuple[csr_matrix, csr_matrix, np.ndarray]:
    pos = {m: i for i, m in enumerate(basis)}
    rows: list[int] = []
    cols: list[int] = []
    hvals: list[float] = []
    jrows: list[int] = []
    jcols: list[int] = []
    jvals: list[float] = []
    qdiag = np.zeros(len(basis))
    for col, mask in enumerate(basis):
        for i, (a, m) in enumerate(STATES):
            if not (mask >> i) & 1:
                continue
            orb = ORBITS[a]
            qdiag[col] += orb.qcoef * (3.0 * m * m - orb.j * (orb.j + 1.0))
            x = apply_annihilate(mask, i)
            if x is None:
                continue
            mask1, s1 = x
            # Diagonal h0.
            x2 = apply_create(mask1, i)
            if x2 is not None:
                mask2, s2 = x2
                rows.append(pos[mask2]); cols.append(col)
                hvals.append(s1 * s2 * (orb.eps + omega * 0.0))
            # Jx connects m to m +/- 1 within one orbit.
            for mp in (m - 1.0, m + 1.0):
                if mp not in m_values(orb.j):
                    continue
                jmat = 0.5 * math.sqrt(max(0.0, orb.j * (orb.j + 1.0) - m * mp))
                ip = INDEX[(a, mp)]
                x2 = apply_create(mask1, ip)
                if x2 is None:
                    continue
                mask2, s2 = x2
                row = pos[mask2]
                jrows.append(row); jcols.append(col); jvals.append(s1 * s2 * jmat)
                rows.append(row); cols.append(col); hvals.append(-omega * s1 * s2 * jmat)
    dim = len(basis)
    h = coo_matrix((hvals, (rows, cols)), shape=(dim, dim)).tocsr()
    jx = coo_matrix((jvals, (jrows, jcols)), shape=(dim, dim)).tocsr()
    return h, jx, qdiag


def pairing_matrix(g: float, blocked: int | None, basis: tuple[int, ...]) -> csr_matrix:
    pos = {m: i for i, m in enumerate(basis)}
    rows: list[int] = []
    cols: list[int] = []
    vals: list[float] = []
    pair_channels = {
        a: tuple(m for m in m_values(orb.j) if m > 0)
        for a, orb in enumerate(ORBITS)
        if a != blocked
    }
    for col, mask in enumerate(basis):
        for b, m_bs in pair_channels.items():
            for mb in m_bs:
                for a, m_as in pair_channels.items():
                    for ma in m_as:
                        out = op_pair(mask, a, ma, b, mb)
                        if out is None:
                            continue
                        mask2, sign = out
                        rows.append(pos[mask2]); cols.append(col)
                        vals.append(-g * sign)
    return coo_matrix((vals, (rows, cols)), shape=(len(basis), len(basis))).tocsr()


def diagonalise(n: int, omega: float, g: float, blocked: int | None) -> dict:
    basis = basis_for_n(n)
    h0, jx, qdiag = one_body_matrices(omega, basis)
    hp = pairing_matrix(g, blocked, basis)
    h = (h0 + hp).tocsr()
    if h.shape[0] == 1:
        evals, vecs = np.array([h[0, 0]]), np.ones((1, 1))
    else:
        evals, vecs = eigsh(h, k=1, which="SA", tol=1e-11, maxiter=4000)
    v = vecs[:, 0]
    norm = np.vdot(v, v).real
    v = v / math.sqrt(norm)
    h0e = float(np.vdot(v, h0 @ v).real)
    hpe = float(np.vdot(v, hp @ v).real)
    align = float(np.vdot(v, jx @ v).real)
    # A static intrinsic <Q20> vanishes in the spherical omega=0 reference of
    # this deliberately small space.  Use the RMS one-body quadrupole instead
    # as the response observable; it is an explicitly labelled B(E2) proxy,
    # not an absolute transition matrix element.
    q20 = float(math.sqrt(max(0.0, np.dot(np.abs(v) ** 2, qdiag * qdiag))))
    occ = []
    for a, orb in enumerate(ORBITS):
        occ.append(float(sum(np.abs(v[k]) ** 2 * sum((mask >> i) & 1 for i, (aa, _) in enumerate(STATES) if aa == a) for k, mask in enumerate(basis))))
    corr = max(0.0, -hpe)
    return {
        "energy_MeV": float(evals[0]),
        "one_body_MeV": h0e,
        "pairing_energy_MeV": hpe,
        "pair_correlation_MeV": corr,
        "delta_corr_MeV": math.sqrt(max(0.0, g * corr)),
        "alignment_hbar": align,
        "Q20_proxy": q20,
        "occupation_d5_2": occ[0],
        "occupation_g7_2": occ[1],
        "pair_coherence": corr / g if g else 0.0,
        "dimension": len(basis),
    }


def derivative(rows: list[dict], key: str, xkey: str) -> None:
    groups: dict[tuple, list[dict]] = {}
    for row in rows:
        group = (row["nuclide"], row["sector"], row["blocked"])
        groups.setdefault(group, []).append(row)
    for group_rows in groups.values():
        group_rows.sort(key=lambda r: r[xkey])
        for i, row in enumerate(group_rows):
            if i == 0:
                val = (group_rows[1][key] - row[key]) / (group_rows[1][xkey] - row[xkey])
            elif i == len(group_rows) - 1:
                val = (row[key] - group_rows[i - 1][key]) / (row[xkey] - group_rows[i - 1][xkey])
            else:
                val = (group_rows[i + 1][key] - group_rows[i - 1][key]) / (group_rows[i + 1][xkey] - group_rows[i - 1][xkey])
            row[f"d{key}_domega"] = float(val)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def main() -> None:
    omegas = np.linspace(0.0, 0.80, 9)
    cases = (
        ("105Cd", "odd_unblocked_reference", 5, None, 0.80),
        ("105Cd", "odd_d5/2_blocked", 5, 0, 0.80),
        ("105Cd", "odd_g7/2_blocked", 5, 1, 0.80),
        ("106Cd", "even", 6, None, 0.45),
        ("108Cd", "even", 7, None, 0.45),
        ("110Cd", "even", 8, None, 0.45),
    )
    rows: list[dict] = []
    for nuclide, sector, n, blocked, g in cases:
        for omega in omegas:
            result = diagonalise(n, float(omega), g, blocked)
            result.update({
                "nuclide": nuclide,
                "sector": sector,
                "N_active_proxy": n,
                "blocked": "none" if blocked is None else ORBITS[blocked].name,
                "omega_MeV_over_hbar": float(omega),
                "G_MeV": g,
                "V_pinu_reference_MeV": VREF,
            })
            rows.append(result)
    # Reference-normalise the coherence and Q response within each sector.
    groups: dict[tuple, list[dict]] = {}
    for row in rows:
        groups.setdefault((row["nuclide"], row["sector"], row["blocked"]), []).append(row)
    for group_rows in groups.values():
        ref = group_rows[0]
        q0 = ref["Q20_proxy"]
        c0 = ref["pair_coherence"]
        for row in group_rows:
            row["B_E2_normalized"] = (row["Q20_proxy"] / q0) ** 2 if abs(q0) > 1e-12 else 0.0
            row["coherence_relative"] = row["pair_coherence"] / c0 if abs(c0) > 1e-12 else 0.0
            # Conditional proxy: effective V follows the exact pair density,
            # with no claim that this is a fitted bare proton-neutron TBME.
            row["V_pinu_proxy_MeV"] = VREF * row["coherence_relative"]
    derivative(rows, "alignment_hbar", "omega_MeV_over_hbar")
    derivative(rows, "Q20_proxy", "omega_MeV_over_hbar")
    derivative(rows, "B_E2_normalized", "omega_MeV_over_hbar")

    fields = [
        "nuclide", "sector", "blocked", "N_active_proxy", "omega_MeV_over_hbar", "G_MeV",
        "dimension", "energy_MeV", "one_body_MeV", "pairing_energy_MeV", "pair_correlation_MeV",
        "delta_corr_MeV", "pair_coherence", "coherence_relative", "V_pinu_reference_MeV",
        "V_pinu_proxy_MeV", "alignment_hbar", "dalignment_hbar_domega", "Q20_proxy",
        "dQ20_proxy_domega", "B_E2_normalized", "dB_E2_normalized_domega",
        "occupation_d5_2", "occupation_g7_2",
    ]
    csv_path = OUT / "pnc_blocking_response.csv"
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows({k: row.get(k, "") for k in fields} for row in rows)

    summary = {
        "model": "fixed-N two-orbit CMPC PNC-CSM toy response",
        "status": "reproducible pedagogical micro-response; not a full Cd calculation",
        "orbits": [orb.__dict__ for orb in ORBITS],
        "active_N_proxy": {"105Cd": 5, "106Cd": 6, "108Cd": 7, "110Cd": 8},
        "pairing_strengths_MeV": {"105Cd": 0.80, "106Cd": 0.45, "108Cd": 0.45, "110Cd": 0.45},
        "reference_V_pinu_MeV": VREF,
        "equations": {
            "hamiltonian": "H'=sum_i(e_i-q_i omega Jx_ij)a_i^dag a_j-G sum_ab P_a^dag P_b",
            "pair_correlation": "C_pair=-<H_pair> >=0; Delta_corr=sqrt(G*C_pair)",
            "V_proxy": "V_eff(omega)=1.2 MeV * C_pair(omega)/C_pair(0)",
            "B_E2_proxy": "[Q20_RMS(omega)/Q20_RMS(0)]^2",
            "J2_proxy": "d< Jx >/d omega",
        },
        "blocking_definition": "selected orbit is excluded from monopole pair-scattering channels while odd N is retained; Jx remains explicit in the Fock-space Hamiltonian",
        "interpretation": [
            "Fixed N preserves number exactly and the finite pair-scattering correlation, but the correlation gap is not a BCS anomalous field.",
            "The V_pinu output is a conditional screening/coherence proxy, not a microscopic extraction of the 1.2 MeV phenomenological parameter.",
            "Absolute B(E2), J(2), deformation and Cd isotope trends are not calibrated by this two-orbit toy space.",
        ],
        "source_locators": [
            "Zhang et al., PRC 87 054314 (2013), PDF pp.4-10 Eqs.(1-12), Figs.2-4",
            "Zhang, Chin. Phys. C 43 054107 (2019), PDF pp.2,4-7 Eqs.(1-11), Figs.3-7",
            "Wu et al., PRC 83 034323 (2011), PDF pp.2-5 Eqs.(1-12)",
            "Roy et al., Phys. Lett. B 711 (2012), printed pp.324-326 Eqs.(3-6), Fig.3",
        ],
    }
    (OUT / "pnc_blocking_response_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    provenance = {
        "script": str(csv_path.relative_to(Path.cwd())) if Path.cwd() in csv_path.parents else str(csv_path),
        "script_sha256": sha256(Path(__file__)),
        "command": "python3 pnc_blocking_response.py",
        "python": "3.x",
        "generated_files": ["pnc_blocking_response.csv", "pnc_blocking_response_summary.json"],
        "raw_inputs": "none; all numerical orbit energies/q coefficients are declared toy inputs",
        "evidence_boundary": "The four literature locator strings are source anchors; no numerical claim from this toy solver is presented as a paper result.",
    }
    (OUT / "provenance.json").write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"rows": len(rows), "csv": str(csv_path), "summary": str(OUT / 'pnc_blocking_response_summary.json')}, indent=2))


if __name__ == "__main__":
    main()
