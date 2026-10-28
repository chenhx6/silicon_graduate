#!/usr/bin/env python3
"""Conditional current/symmetry and frozen-gyro bifurcation calculation.

No measured current field, self-consistent 3D-TAC solution, phase boundary,
or experimental partner spectrum is inferred by this illustrative model.
Run: python3 tac-currents-shears-chiral-phase-017.py
The adjacent JSON is overwritten with deterministic rounded output.
"""
from __future__ import annotations

import json
import math
from pathlib import Path


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(c, a):
    return tuple(c * x for x in a)


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def rot(axis, a):
    """Proper rotation by pi; vector and axial vector have same rule."""
    return tuple(x if i == axis else -x for i, x in enumerate(a))


def vortex(r, centre, axis, circulation, width=0.8):
    """Solenoidal Gaussian vortex j = k exp(-u²/w²) (axis cross u).

    It is a phenomenological current with arbitrary units. A microscopic
    cranking current instead follows the occupied density matrix:
      j_p(r) = (hbar/2mi)[(nabla_r-nabla_r')rho(r,r')]_{r'=r}
               - (q/m) A(r) rho(r,r),
    plus spin magnetization j_M = nabla cross M where required. The density
    matrix is obtained by minimizing E[rho,kappa]-omega dot <J> subject to
    particle-number/shape constraints; this script has no EDF or orbitals.
    """
    u = tuple(x-y for x, y in zip(r, centre))
    return scale(circulation*math.exp(-dot(u, u)/width**2), cross(axis, u))


def mr(r):
    # One y-axis circulation in the yz shears plane; x is its normal.
    return vortex(r, (0.0, 0.0, 0.0), (0.0, 1.0, 0.0), 1.0)


def amr(r):
    # Two counter-circulating z-vortices at opposite x; integrated dipoles
    # cancel, yet j(r) and the local magnetization are generally nonzero.
    return add(vortex(r, (0.9, 0.0, 0.0), (0.0, 0.0, 1.0), 1.0),
               vortex(r, (-0.9, 0.0, 0.0), (0.0, 0.0, 1.0), -1.0))


def norm(a):
    return math.sqrt(dot(a, a))


def symmetry_error(field, axis, time_reverse):
    # g j(r) = sign R j(R^-1 r); R^-1 = R for a pi rotation.
    sign = -1 if time_reverse else 1
    err = 0.0
    for ix in range(-4, 5):
        for iy in range(-4, 5):
            for iz in range(-4, 5):
                r = (ix*0.35, iy*0.35, iz*0.35)
                transformed = scale(sign, rot(axis, field(rot(axis, r))))
                err = max(err, norm(add(transformed, scale(-1, field(r)))))
    return err


def time_error(field):
    return max(2*norm(field((ix*.35, iy*.35, iz*.35)))
               for ix in range(-4, 5) for iy in range(-4, 5)
               for iz in range(-4, 5))


def gyro_branch():
    """Frozen s/l gyroscopes and diagonal core inertia (Olbratowski 2002 v1).

    H(omega)=sum J_k omega_k²/2, I_k=J_k omega_k+s_k.
    Uniform rotation imposes omega cross I=0. At fixed |omega|, variation
    of R=H-omega dot I gives omega_s=s_s/(mu-J_s),
    omega_l=s_l/(mu-J_l), omega_m(mu-J_m)=0.
    Aplanar mu=J_m yields omega_m=±sqrt(omega²-omega_c²).
    These are intrinsic classical branches; their signs are mirror partners,
    not two quantum energies or a measurable S(I) splitting.
    """
    js, jm, jl, ss, sl = 8.5, 31.0, 20.0, 5.43, 5.0
    ws, wl = ss/(jm-js), sl/(jm-jl)
    wc = math.hypot(ws, wl)
    rows = []
    for w in (0.40, 0.50, wc, 0.60, 0.80):
        wm = math.sqrt(max(0.0, w*w-wc*wc)) if w >= wc else None
        rows.append({"hbar_omega_MeV": round(w, 9),
                     "omega_m_MeV_per_hbar": None if wm is None else round(wm, 9),
                     "aplanar_pair_exists": wm is not None and wm > 1e-10})
    return {"source_model": "Olbratowski et al. 2002 arXiv:nucl-th/0211075v1, PDF pp.2-3 Eqs.2-7",
            "J_hbar2_per_MeV": {"s": js, "m": jm, "l": jl},
            "gyro_hbar": {"s": ss, "l": sl},
            "hbar_omega_critical_MeV": round(wc, 9),
            "critical_I_hbar": round(jm*wc, 9), "branches": rows}


def cadmium_systematics():
    """Transcribe Roy 2011 Table 1 endpoints, then do arithmetic only.

    The table combines literature data for 106/108Cd with the 110Cd study;
    108Cd's I=22 entry is effective. A decline factor is descriptive and
    cannot assign AMR or infer a universal J(2)/B(E2) threshold.
    """
    entries = {
        "106Cd": {"spin_hbar": [18, 20, 22, 24], "BE2_e2b2": [.15, .14, .07, .05]},
        "108Cd": {"spin_hbar": [16, 18, 20, 22], "BE2_e2b2": [.15, .14, .09, .03]},
        "110Cd": {"spin_hbar": [16, 18, 20, 22, 24], "BE2_e2b2": [.14, .12, .11, .09, .06]},
    }
    for name, row in entries.items():
        row["first_to_last_BE2_factor"] = round(row["BE2_e2b2"][0]/row["BE2_e2b2"][-1], 6)
        row["table_locator"] = "Roy et al. 2011 Phys Lett B 694, printed p.323, Table 1"
        row["status"] = "reported source values; ratios calculated here; no propagated uncertainties"
        if name == "108Cd":
            row["I22_caveat"] = "effective value in source table"
    return entries


def main():
    current = {}
    for name, field in (("MR_toy", mr), ("AMR_toy", amr)):
        sample = field((0.45, 0.35, 0.35))
        current[name] = {
            "local_current_at_0p45_0p35_0p35_arbitrary": [round(x, 9) for x in sample],
            "T_error": round(time_error(field), 9),
            "Rz_pi_error": round(symmetry_error(field, 2, False), 9),
            "Rx_pi_T_error": round(symmetry_error(field, 0, True), 9),
            "Rz_pi_T_error": round(symmetry_error(field, 2, True), 9)}
    output = {
        "scope": "analytic toy current and conditional frozen-gyro branch; not a self-consistent TAC calculation or measured phase map",
        "units": "current arbitrary; omega MeV/hbar; J hbar^2/MeV; s and I hbar",
        "symmetry_convention": "x is normal to the yz MR plane; j is time odd; errors compare transformed vector fields on a symmetric grid",
        "current_symmetries": current,
        "gyro_bifurcation": gyro_branch(),
        "cadmium_BE2_table1_systematics": cadmium_systematics(),
        "inferences": {
            "nonzero_current_time_reversal": "nonzero j forbids separate T invariance of the intrinsic state",
            "AMR_cancellation": "opposite circulation gives zero integrated transverse moment by symmetry, not pointwise zero local current or all M1 matrix elements",
            "beta_boundary": "no universal beta2=0.20 MR/AMR-to-ER boundary follows from these equations",
            "gamma_boundary": "nonzero gamma alone is insufficient; require Jm>Js,Jl, both gyroscopes, and omega>omega_c",
            "quantum_observables": "S(I), B(M1)/B(E2), and partner splitting require band-resolved quantum spectra and transition operators; absent here"},
        "nucleus_evidence_routes": {
            "106Ag": "he-chuangye-2006-magnetic-chiral-106ag; rather-2014-ag106-transition-rates; competing assignments remain",
            "105Cd_106Cd": "kumar-2025-review-magnetic-antimagnetic-rotational-structures; original lifetime lineage needed per claim",
            "108Ag": "no direct source validated in this task",
            "130Cs": "starosta-2001-n75-chiral-vibrations; soft chiral vibration candidate",
            "132La": "starosta-2001-n75-chiral-vibrations; olbratowski-2002-critical-frequency-preprint"}}
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(path)
    print(json.dumps({"symmetry": current, "critical": output["gyro_bifurcation"]["hbar_omega_critical_MeV"]}, indent=2))


if __name__ == '__main__':
    main()
