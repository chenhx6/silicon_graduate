#!/usr/bin/env python3
"""Signed odd-even mass filters with covariance, not an HFB gap solver.

Conventions: positive binding B; q=N on isotopic chains, q=Z on isotonic
chains. Delta4(q) is the LEFT average of Delta3(q-1), Delta3(q).
Delta5(q) = [Delta4(q) + Delta4(q+1)]/2.
Sources: Bohr--Mottelson I, pp. 169-171, Eqs. 2-92--2-96;
Satula et al., nucl-th/9804060v1 p. 1; Duguet et al.,
nucl-th/0105050v1 pp. 6-8. See the Wiki note for sign conversion and limits.
No preset below contains measured nuclear masses.
"""
import argparse
import json
import math
import re
import numpy as np

OFFSETS = (-2, -1, 0, 1, 2)
STENCILS = {
    "Delta_3_point_MeV": (0, -0.5, 1, -0.5, 0),
    "Delta_4_point_left_MeV": (0.25, -0.75, 0.75, -0.25, 0),
    "Delta_5_point_MeV": (0.125, -0.5, 0.75, -0.5, 0.125),
}
PRESETS = {
    "synthetic_even_chain": {
        "nucleus": "synthetic fixture (not measured 130Ba masses)",
        "A": 130, "Z": 56, "N": 74,
        "description": "B(q)=1000+8x-0.02x^2+(-1)^q*0.6 MeV, x=q-74",
        "data_origin": "synthetic",
        "binding_energies_isotopic_chain_MeV": {
            "N-2": 984.52, "N-1": 991.38, "N": 1000.60,
            "N+1": 1007.38, "N+2": 1016.52},
        "uncertainties_MeV": [0.01]*5,
    }
}


def _integer(value, name):
    if isinstance(value, bool):
        raise ValueError(f"{name} must be an integer")
    try:
        x = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be an integer") from exc
    if not math.isfinite(x) or not x.is_integer():
        raise ValueError(f"{name} must be an integer")
    return int(x)


def _number(value, name):
    if isinstance(value, bool):
        raise ValueError(f"{name} must be finite")
    x = float(value)
    if not math.isfinite(x):
        raise ValueError(f"{name} must be finite")
    return x


class NuclearPairingGapSolver:
    """Evaluate linear mass indicators on five neighbouring integer points."""

    def __init__(self, A=130, Z=56, N=74, binding_chain_MeV=None,
                 species="neutron", quantity="binding_MeV",
                 covariance_MeV2=None, uncertainties_MeV=None,
                 data_origin="caller-supplied; provenance not checked"):
        self.A = _integer(A, "A")
        self.Z = _integer(Z, "Z")
        self.N = _integer(N, "N")
        if self.A != self.Z + self.N or min(self.Z, self.N) < 0:
            raise ValueError("require A=Z+N and nonnegative Z,N")
        if species not in ("neutron", "proton"):
            raise ValueError("species must be neutron or proton")
        if quantity not in ("binding_MeV", "mass_excess_MeV", "mass_energy_MeV"):
            raise ValueError("quantity must be binding_MeV, mass_excess_MeV or mass_energy_MeV")
        self.species, self.quantity = species, quantity
        self.q = self.N if species == "neutron" else self.Z
        self.symbol = "N" if species == "neutron" else "Z"
        if self.q < 2:
            raise ValueError("a five-point window requires central particle number >= 2")
        self.origin = str(data_origin)
        self.b_chain = self._parse_chain({} if binding_chain_MeV is None else binding_chain_MeV)
        self.covariance = self._parse_covariance(covariance_MeV2, uncertainties_MeV)

    def _parse_chain(self, chain):
        if not isinstance(chain, dict):
            raise ValueError("chain must map absolute particle numbers or relative labels to MeV")
        values = {}
        for key, value in chain.items():
            text = str(key).strip()
            if re.fullmatch(r"\d+", text):
                q = int(text)
            else:
                # Match the WHOLE first token: 'N' must never match 'N-2'.
                token = text.split()[0] if text else ""
                match = re.fullmatch(rf"{self.symbol}([+-][12])?", token)
                if not match:
                    raise ValueError(f"invalid chain label {key!r} for {self.species}")
                q = self.q + int(match.group(1) or 0)
            if q in values:
                raise ValueError(f"duplicate point at {self.symbol}={q}")
            values[q] = None if value is None else _number(value, str(key))
        return values

    @staticmethod
    def _parse_covariance(covariance, uncertainties):
        if covariance is not None and uncertainties is not None:
            raise ValueError("provide covariance OR independent uncertainties, not both")
        if uncertainties is not None:
            errors = np.asarray(uncertainties, dtype=float)
            if errors.shape != (5,) or not np.all(np.isfinite(errors)) or np.any(errors < 0):
                raise ValueError("uncertainties_MeV must contain five finite nonnegative values")
            covariance = np.diag(errors**2)
        if covariance is None:
            return None
        c = np.asarray(covariance, dtype=float)
        if c.shape != (5, 5) or not np.all(np.isfinite(c)):
            raise ValueError("covariance_MeV2 must be a finite 5x5 matrix")
        scale = max(float(np.max(np.abs(c))), np.finfo(float).tiny)
        tol = 1e-10*scale
        if np.max(np.abs(c-c.T)) > tol:
            raise ValueError("covariance_MeV2 must be symmetric")
        c = 0.5*(c+c.T)
        if np.any(np.diag(c) < 0) or np.linalg.eigvalsh(c)[0] < -tol:
            raise ValueError("covariance_MeV2 must be positive semidefinite")
        return c

    def extract_multipoint_gaps(self):
        """Return signed finite differences; unavailable filters remain null."""
        parity = 1 if self.q % 2 == 0 else -1
        sign = 1 if self.quantity == "binding_MeV" else -1
        points = [self.q+k for k in OFFSETS]
        values = [self.b_chain.get(q) for q in points]
        filters, results, weights = {}, {}, []
        for name, stencil in STENCILS.items():
            w = np.asarray(stencil)*parity*sign
            needed = [i for i, x in enumerate(w) if x != 0]
            missing = [points[i] for i in needed if values[i] is None]
            value = None if missing else math.fsum(w[i]*values[i] for i in needed)
            sigma = None
            if value is not None and self.covariance is not None:
                sigma = math.sqrt(max(0.0, float(w @ self.covariance @ w)))
            filters[name] = {
                "value_MeV": value, "sigma_MeV": sigma,
                "weights_on_input": w.tolist(), "missing_particle_numbers": missing,
                "status": "missing-input" if missing else "computed",
            }
            results[name] = value
            weights.append(w)
        propagated = None
        if self.covariance is not None:
            w = np.asarray(weights)
            c = w @ self.covariance @ w.T
            propagated = [
                [float(c[i, j]) if results[a] is not None and results[b] is not None else None
                 for j, b in enumerate(STENCILS)] for i, a in enumerate(STENCILS)]
        results.update({
            "filters": filters, "filter_order": list(STENCILS),
            "particle_number_order": points,
            "indicator_covariance_MeV2": propagated,
            "uncertainty_status": "not-supplied" if self.covariance is None else "propagated",
            "Delta_empirical_12_over_sqrtA_MeV": 12.0/math.sqrt(self.A),
        })
        return results

    def execute_analysis(self):
        return {
            "nucleus_A": self.A, "nucleus_Z": self.Z, "nucleus_N": self.N,
            "species": self.species, "quantity": self.quantity, "data_origin": self.origin,
            "multipoint_pairing_gaps": self.extract_multipoint_gaps(),
            "interpretation": "odd-even mass indicators; not a measured BCS/HFB gap",
            "quasiparticle_properties": {
                "status": "not-inferred",
                "reason": "requires a specified Hamiltonian, active space and blocking calculation"},
        }


def run_pairing_gap_analysis(nucleus="Generic", A=130, Z=56, N=74,
                             binding_chain=None, species="neutron", quantity="binding_MeV",
                             covariance_MeV2=None, uncertainties_MeV=None,
                             data_origin="caller-supplied; provenance not checked"):
    solver = NuclearPairingGapSolver(
        A=A, Z=Z, N=N, binding_chain_MeV=binding_chain, species=species,
        quantity=quantity, covariance_MeV2=covariance_MeV2,
        uncertainties_MeV=uncertainties_MeV, data_origin=data_origin)
    result = solver.execute_analysis()
    result["nucleus"] = nucleus
    return result


def format_text_report(output, title="Odd-even mass indicators"):
    lines = [title, f"Input: {output['data_origin']}",
             f"Axis: {output['species']}; quantity: {output['quantity']}", output["interpretation"]]
    gaps = output["multipoint_pairing_gaps"]
    for name, row in gaps["filters"].items():
        if row["value_MeV"] is None:
            lines.append(f"{name}: unavailable (missing {row['missing_particle_numbers']})")
        else:
            err = "uncertainty not supplied" if row["sigma_MeV"] is None else f"+/- {row['sigma_MeV']:.6f}"
            lines.append(f"{name}: {row['value_MeV']:.6f} MeV ({err})")
    lines.append(f"Empirical comparison only: 12/sqrt(A) = {gaps['Delta_empirical_12_over_sqrtA_MeV']:.6f} MeV")
    lines.append("BCS gap, pair-breaking threshold and blocked gap: not inferred.")
    return "\n".join(lines)


def result_from_args(args):
    if args.input:
        with open(args.input, encoding="utf-8") as stream:
            obj = json.load(stream)
        if any(x not in obj for x in ("A", "Z", "N", "chain")):
            raise ValueError("input JSON requires A, Z, N and chain")
        return run_pairing_gap_analysis(
            nucleus=obj.get("label", "caller supplied"), A=obj["A"], Z=obj["Z"], N=obj["N"],
            binding_chain=obj["chain"], species=obj.get("species", "neutron"),
            quantity=obj.get("quantity", "binding_MeV"), covariance_MeV2=obj.get("covariance_MeV2"),
            uncertainties_MeV=obj.get("uncertainties_MeV"),
            data_origin=obj.get("data_origin", "caller supplied; provenance not checked"))
    p = PRESETS[args.preset or "synthetic_even_chain"]
    return run_pairing_gap_analysis(
        nucleus=p["nucleus"], A=p["A"], Z=p["Z"], N=p["N"],
        binding_chain=p["binding_energies_isotopic_chain_MeV"],
        uncertainties_MeV=p["uncertainties_MeV"], data_origin=p["data_origin"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--preset", choices=list(PRESETS))
    group.add_argument("--input", help="JSON with A,Z,N, chain, convention and optional covariance")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = result_from_args(args)
    except (ValueError, TypeError, OSError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, allow_nan=False) if args.json else format_text_report(result))


if __name__ == "__main__":
    main()
