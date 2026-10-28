import json
import math

def compute_mr_chiral_transition():
    # 134Pr (Z=59, N=75) benchmark case
    # pi(h11/2) x nu(h11/2)^(-1) coupled to triaxial core with gamma ~ -30 deg
    # Low-spin (I = 10 to 13): Planar Magnetic Rotation (Shears)
    # Mid-spin (I = 14 to 18): 3D Aplanar Chiral Rotation (Doublet Bands)
    # High-spin (I >= 19): Quasiparticle alignment, chiral collapse

    delta_g = 1.42 # mu_N
    jp = 5.5
    jn = 5.5

    spins = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    evolution = []
    for I in spins:
        if I <= 13:
            regime = "Planar Magnetic Rotation (Shears)"
            # Pure planar shears closing: I = jp*cos(th) + jn*cos(th) = 2*j*cos(th)
            cos_th = I / (2.0 * jp)
            cos_th = min(max(cos_th, -1.0), 1.0)
            theta_deg = math.degrees(math.acos(cos_th))
            sin2_th = 1.0 - cos_th**2
            bm1_in = (3.0 / (8.0 * math.pi)) * (delta_g**2) * ((jp * jn / I)**2) * sin2_th
            bm1_out = 0.0 # No partner band
            be2_in = 0.08 * (sin2_th**2) + 0.02 # weakly deformed core
            delta_E_partner_keV = None
            chiral_staggering_S = None
        elif 14 <= I <= 18:
            regime = "3D Aplanar Chiral Doublet Rotation"
            # Core rotation R along intermediate axis carries surplus spin
            R_core = I - 11.0 # core contribution
            # Chiral tunneling splitting Delta E decreases as barrier grows with spin
            delta_E_partner_keV = 350.0 * math.exp(-0.35 * (I - 14.0)) # decays from 350 keV down to 87 keV
            # Out-of-phase staggering in M1:
            # Staggering phase factor (-1)^I
            phase = (-1.0) ** I
            bm1_in = 1.20 + 0.40 * phase
            bm1_out = 0.80 - 0.35 * phase
            be2_in = 0.12 # stable triaxial E2
            theta_deg = 90.0 # mutually orthogonal blades in 3D chiral geometry
            chiral_staggering_S = round(bm1_in / be2_in, 2)
        else:
            regime = "High-spin Realignment (Chiral Collapse)"
            delta_E_partner_keV = 600.0 # partner band diverges
            bm1_in = 0.40
            bm1_out = 0.05
            be2_in = 0.25 # increased collectivity from aligned quasiparticles
            theta_deg = 30.0
            chiral_staggering_S = None

        evolution.append({
            "spin_I": I,
            "regime": regime,
            "shears_angle_theta_deg": round(theta_deg, 1) if theta_deg is not None else None,
            "partner_splitting_DeltaE_keV": round(delta_E_partner_keV, 1) if delta_E_partner_keV is not None else "no partner band",
            "BM1_intraband_muN2": round(bm1_in, 3),
            "BM1_interband_muN2": round(bm1_out, 3),
            "BE2_intraband_eb2": round(be2_in, 3),
            "BM1_BE2_ratio": round(bm1_in / be2_in, 2) if be2_in > 0 else None,
            "staggering_parameter": chiral_staggering_S
        })

    results = {
        "schema": "mr-to-chiral-topological-transition-066/v1",
        "nucleus": "134Pr",
        "valence_configuration": "pi(h11/2) x nu(h11/2)^(-1)",
        "evolution_trajectory": evolution,
        "key_physical_mechanisms": [
            "1. Planar Magnetic Rotation Stage (I = 10-13): The valence proton particle and neutron hole close in a common plane. Radiation is purely Delta I = 1 M1 within a single band, with B(M1) decreasing as shears close.",
            "2. Critical Chiral Bifurcation (I = 14): As rotational frequency reaches hbar*omega_c ~ 0.35 MeV, the intermediate-axis core rotation activates. Angular momentum enters 3D space, spontaneously breaking time-reversal x rotation symmetry S = T*R_y(pi).",
            "3. Chiral Doublet Stage (I = 14-18): Left- and right-handed aplanar states emerge. Quantum tunneling between chiral wells produces doublet partner bands with energy splitting Delta E collapsing from 350 keV to < 100 keV.",
            "4. Out-of-phase M1 Staggering: A decisive fingerprint of chiral symmetry breaking is the alternating odd-even staggering between intraband B(M1; I -> I-1) and interband B(M1; I -> I-1_partner), caused by signature-dependent tunneling interference.",
            "5. High-spin Realignment (I >= 19): Coriolis forces align a second quasiparticle pair, destroying the 3D orthogonal geometry and restoring planar alignment."
        ]
    }

    out_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/mr-to-chiral-topological-transition-066.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote", out_path)

if __name__ == "__main__":
    compute_mr_chiral_transition()
