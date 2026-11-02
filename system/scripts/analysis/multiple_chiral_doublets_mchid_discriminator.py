#!/usr/bin/env python3
"""
Multiple Chiral Doublets (MChD) Multi-Configuration Discriminator & Alignment Arbitrator.

Physical Principle & Formalism:
Multiple Chiral Doublets (MChD) represent the simultaneous coexistence of two or more
distinct pairs of chiral doublet bands (Pair A: Bands 1 & 2; Pair B: Bands 3 & 4)
within the same atomic nucleus.

First predicted by Peng, Meng, and Zhang (PRC 2008) and experimentally established in
133Ce (Ayangeakaa et al. PRL 2013), 103Rh (Kuti et al. PRL 2014), and 136Nd (Petrache et al. PRC 2018).

Microscopic Origins of MChD:
1. Multi-Quasiparticle Configuration Coexistence:
   Pair A originates from configuration C1 (e.g., 1-qp nu h11/2 or 2-qp), whereas
   Pair B originates from an excited 3-qp or 4-qp configuration C2 (e.g., pi h11/2^2 (x) nu h11/2^-1).
2. Chiral Shape Coexistence (ChSR):
   The same or similar quasiparticle configurations couple to two different triaxial
   potential minima on the (beta, gamma) surface (e.g. beta1 ~ 0.22, gamma1 ~ 26 deg vs. beta2 ~ 0.32, gamma2 ~ 18 deg).

The 4-Fold MChD Arbitration Gates:
1. Gate 1: Chiral Energy Degeneracy Test:
   Both doublet pairs must exhibit twin band energy convergence at moderate-to-high spins:
     Delta E_A(I) = |E_2(I) - E_1(I)| <= Delta E_crit (~ 150 keV)
     Delta E_B(I) = |E_4(I) - E_3(I)| <= Delta E_crit (~ 180 keV)
2. Gate 2: In-Phase B(M1)/B(E2) Staggering Test (Koike Selection Rule):
   Both doublet systems must show in-phase signature staggering between their twin bands,
   confirming chiral restoration rather than octupole parity doubling or pseudospin partners.
3. Gate 3: Quasiparticle Alignment Separation Test:
   The experimental Routhian alignments of the two systems must be distinct and discrete:
     i_x(omega) = I_x - (J_0 * omega + J_1 * omega^3)
     Delta i_x = |i_x(Pair B) - i_x(Pair A)| >= 1.5 - 3.5 hbar
   confirming active participation of additional decoupled quasiparticle pairs.
4. Gate 4: Cross-Doublet Branching Suppression:
   Inter-doublet cross-talk branching ratios (Pair B -> Pair A) must be small:
     Branching(cross) = I_gamma(Pair B -> Pair A) / I_gamma(Pair B intra) <= 0.15
   verifying configuration or shape orthogonality.

This module implements:
1. Multi-band Routhian and alignment i_x(omega) extraction using Harris reference parameters.
2. Energy splitting trajectory Delta E(I) for both doublet pairs.
3. 4-Fold MChD gate evaluation and overall diagnostic classification.
4. Presets for classic MChD nuclei (133Ce, 136Nd, 103Rh).

Textbook & Literature References:
- Chirality and Wobbling in Atomic Nuclei (CRC Press 2025), Ch. 3 (J. Meng & P. W. Zhao), Ch. 10 (Q. B. Chen et al.)
- J. Meng & S. Q. Zhang, Phys. Rev. C 77, 021303(R) (2008)
- Ayangeakaa et al., Phys. Rev. Lett. 110, 172504 (2013)
- Kuti et al., Phys. Rev. Lett. 113, 032501 (2014)
- Petrache et al., Phys. Rev. C 97, 041304(R) (2018)
"""

import sys
import json
import argparse
import numpy as np

PRESETS = {
    "133Ce_classic_mchid": {
        "nucleus": "133Ce",
        "description": "First experimental discovery of MChD in odd-A 133Ce (Ayangeakaa PRL 2013)",
        "harris_J0": 17.0,  # MeV^-1 hbar^2
        "harris_J1": 25.0,  # MeV^-3 hbar^4
        "pair_A": {
            "name": "Pair 1 (Bands 1 & 2)",
            "configuration": "nu h11/2^-1",
            "spins": [15.5, 17.5, 19.5, 21.5, 23.5],
            "energies_B1_keV": [2450.0, 2980.0, 3590.0, 4280.0, 5050.0],
            "energies_B2_keV": [2580.0, 3070.0, 3650.0, 4320.0, 5080.0],
            "bm1_be2_staggering_in_phase": True
        },
        "pair_B": {
            "name": "Pair 2 (Bands 3 & 4)",
            "configuration": "pi h11/2^2 (x) nu h11/2^-1",
            "spins": [19.5, 21.5, 23.5, 25.5, 27.5],
            "energies_B3_keV": [3850.0, 4420.0, 5060.0, 5770.0, 6550.0],
            "energies_B4_keV": [3990.0, 4520.0, 5130.0, 5820.0, 6590.0],
            "bm1_be2_staggering_in_phase": True
        },
        "cross_doublet_branching_ratio": 0.04
    },
    "136Nd_even_even_mchid": {
        "nucleus": "136Nd",
        "description": "Even-even 136Nd 4-quasiparticle MChD (Petrache PRC 2018)",
        "harris_J0": 20.0,
        "harris_J1": 30.0,
        "pair_A": {
            "name": "Pair 1 (Bands 1 & 2)",
            "configuration": "pi h11/2^2 (x) nu h11/2^-2 (yrast)",
            "spins": [14.0, 16.0, 18.0, 20.0, 22.0],
            "energies_B1_keV": [4100.0, 4720.0, 5410.0, 6170.0, 6990.0],
            "energies_B2_keV": [4220.0, 4810.0, 5480.0, 6220.0, 7030.0],
            "bm1_be2_staggering_in_phase": True
        },
        "pair_B": {
            "name": "Pair 2 (Bands 3 & 4)",
            "configuration": "pi h11/2^2 (x) nu h11/2^-1 d3/2^-1 (excited)",
            "spins": [15.0, 17.0, 19.0, 21.0, 23.0],
            "energies_B3_keV": [4650.0, 5290.0, 5990.0, 6750.0, 7570.0],
            "energies_B4_keV": [4780.0, 5390.0, 6070.0, 6810.0, 7620.0],
            "bm1_be2_staggering_in_phase": True
        },
        "cross_doublet_branching_ratio": 0.06
    },
    "103Rh_A100_mchid": {
        "nucleus": "103Rh",
        "description": "A~100 region MChD in 103Rh (Kuti PRL 2014)",
        "harris_J0": 14.0,
        "harris_J1": 18.0,
        "pair_A": {
            "name": "Pair 1 (Bands 1 & 2)",
            "configuration": "pi g9/2^-1 (x) nu h11/2^2",
            "spins": [13.5, 15.5, 17.5, 19.5, 21.5],
            "energies_B1_keV": [2800.0, 3350.0, 3980.0, 4690.0, 5480.0],
            "energies_B2_keV": [2920.0, 3430.0, 4030.0, 4720.0, 5500.0],
            "bm1_be2_staggering_in_phase": True
        },
        "pair_B": {
            "name": "Pair 2 (Bands 3 & 4)",
            "configuration": "pi p1/2^-1 (x) nu h11/2^2 (excited)",
            "spins": [14.5, 16.5, 18.5, 20.5, 22.5],
            "energies_B3_keV": [3450.0, 4040.0, 4710.0, 5460.0, 6290.0],
            "energies_B4_keV": [3570.0, 4130.0, 4780.0, 5510.0, 6330.0],
            "bm1_be2_staggering_in_phase": True
        },
        "cross_doublet_branching_ratio": 0.08
    }
}

class MultipleChiralDoubletsDiscriminator:
    def __init__(self, harris_J0=17.0, harris_J1=25.0):
        self.J0 = float(harris_J0)
        self.J1 = float(harris_J1)

    def calculate_alignment(self, spins, energies_keV):
        """
        Calculates rotational frequency omega and aligned angular momentum i_x:
        omega(I) = (E(I) - E(I-2)) / 2
        I_x(I) = sqrt((I+1/2)^2 - K^2) ~ I + 1/2
        i_x(I) = I_x - (J_0 * omega + J_1 * omega^3)
        """
        spins = np.array(spins, dtype=float)
        energies_MeV = np.array(energies_keV, dtype=float) * 1e-3

        alignments = []
        omegas = []

        for i in range(len(spins)):
            if i == 0:
                if len(spins) > 1:
                    dE = energies_MeV[1] - energies_MeV[0]
                    dI = spins[1] - spins[0]
                    omega = dE / max(1e-3, dI)
                else:
                    omega = 0.2
            elif i == len(spins) - 1:
                dE = energies_MeV[i] - energies_MeV[i-1]
                dI = spins[i] - spins[i-1]
                omega = dE / max(1e-3, dI)
            else:
                dE = energies_MeV[i+1] - energies_MeV[i-1]
                dI = spins[i+1] - spins[i-1]
                omega = dE / max(1e-3, dI)

            I_x = spins[i] + 0.5
            I_x_ref = self.J0 * omega + self.J1 * (omega**3)
            i_x = I_x - I_x_ref

            omegas.append(float(omega))
            alignments.append(float(i_x))

        return np.array(omegas), np.array(alignments)

    def evaluate_pair(self, pair_data):
        """
        Evaluates energy splittings and alignment for a twin band pair.
        """
        spins = np.array(pair_data["spins"], dtype=float)
        e1 = np.array(pair_data["energies_B1_keV" if "energies_B1_keV" in pair_data else "energies_B3_keV"], dtype=float)
        e2 = np.array(pair_data["energies_B2_keV" if "energies_B2_keV" in pair_data else "energies_B4_keV"], dtype=float)

        delta_E = np.abs(e2 - e1)
        mean_delta_E = float(np.mean(delta_E))
        min_delta_E = float(np.min(delta_E))

        om1, ix1 = self.calculate_alignment(spins, e1)
        om2, ix2 = self.calculate_alignment(spins, e2)

        mean_ix = float(0.5 * (np.mean(ix1) + np.mean(ix2)))

        return {
            "name": pair_data.get("name", "Pair"),
            "configuration": pair_data.get("configuration", "Unknown"),
            "spins": spins.tolist(),
            "energy_splittings_keV": delta_E.tolist(),
            "mean_energy_splitting_keV": mean_delta_E,
            "min_energy_splitting_keV": min_delta_E,
            "mean_alignment_hbar": mean_ix,
            "staggering_in_phase": bool(pair_data.get("bm1_be2_staggering_in_phase", True))
        }

    def arbitrate_mchid(self, pair_A_data, pair_B_data, cross_branching_ratio=0.05, delta_ix_crit=1.5):
        """
        Executes the 4-Fold MChD Arbitration Gates.
        """
        res_A = self.evaluate_pair(pair_A_data)
        res_B = self.evaluate_pair(pair_B_data)

        # Gate 1: Energy Near-Degeneracy Test (Delta E <= 150 keV for Pair A, <= 180 keV for Pair B)
        gate1_pass = bool(res_A["min_energy_splitting_keV"] <= 150.0 and res_B["min_energy_splitting_keV"] <= 180.0)

        # Gate 2: In-phase Staggering Test
        gate2_pass = bool(res_A["staggering_in_phase"] and res_B["staggering_in_phase"])

        # Gate 3: Quasiparticle Alignment Separation Test (Delta i_x >= 1.5 hbar)
        delta_ix = abs(res_B["mean_alignment_hbar"] - res_A["mean_alignment_hbar"])
        gate3_pass = bool(delta_ix >= float(delta_ix_crit))

        # Gate 4: Cross-Doublet Suppression Test (Branching <= 0.15)
        cross_br = float(cross_branching_ratio)
        gate4_pass = bool(cross_br <= 0.15)

        # Overall Status
        all_passed = gate1_pass and gate2_pass and gate3_pass and gate4_pass

        if all_passed:
            diag = "CONFIRMED Multiple Chiral Doublets (MChD): 4/4 Gates Passed"
        elif not gate3_pass:
            diag = "REJECTED MChD: Insufficient Alignment Separation (Same Quasiparticle Configuration)"
        elif not gate1_pass:
            diag = "REJECTED MChD: Twin Bands Fail Energy Degeneracy Gate (Large Delta E)"
        else:
            diag = "INCONCLUSIVE: Partial MChD criteria met"

        return {
            "pair_A_analysis": res_A,
            "pair_B_analysis": res_B,
            "alignment_separation_Delta_ix_hbar": float(delta_ix),
            "cross_doublet_branching_ratio": cross_br,
            "gates_evaluation": {
                "gate1_energy_degeneracy": gate1_pass,
                "gate2_in_phase_staggering": gate2_pass,
                "gate3_alignment_separation": gate3_pass,
                "gate4_cross_suppression": gate4_pass
            },
            "is_mchid_confirmed": bool(all_passed),
            "diagnostic_verdict": diag
        }

def run_mchid_arbitration(nucleus="Generic", harris_J0=17.0, harris_J1=25.0,
                          pair_A=None, pair_B=None, cross_branching=0.05, delta_ix_crit=1.5):
    if pair_A is None:
        pair_A = PRESETS["133Ce_classic_mchid"]["pair_A"]
    if pair_B is None:
        pair_B = PRESETS["133Ce_classic_mchid"]["pair_B"]

    discrim = MultipleChiralDoubletsDiscriminator(harris_J0=harris_J0, harris_J1=harris_J1)
    res = discrim.arbitrate_mchid(pair_A, pair_B, cross_branching, delta_ix_crit=delta_ix_crit)
    res["nucleus"] = nucleus
    return res

def format_text_report(output, title="Multiple Chiral Doublets (MChD) Arbitration Report"):
    lines = []
    lines.append("=" * 76)
    lines.append(f"  {title}")
    lines.append("=" * 76)
    lines.append(f"Nucleus: {output['nucleus']}")
    lines.append(f"Verdict: {output['diagnostic_verdict']}")
    g = output["gates_evaluation"]
    lines.append(f"\n[1] 4-Fold MChD Arbitration Gates Evaluation:")
    lines.append(f"  Gate 1 [Twin Energy Degeneracy]:     {'PASS' if g['gate1_energy_degeneracy'] else 'FAIL'}")
    lines.append(f"  Gate 2 [In-Phase M1/E2 Staggering]:  {'PASS' if g['gate2_in_phase_staggering'] else 'FAIL'}")
    lines.append(f"  Gate 3 [Alignment Separation]:       {'PASS' if g['gate3_alignment_separation'] else 'FAIL'} (Delta i_x = {output['alignment_separation_Delta_ix_hbar']:.2f} hbar)")
    lines.append(f"  Gate 4 [Cross-Talk Suppression]:     {'PASS' if g['gate4_cross_suppression'] else 'FAIL'} (Branching = {output['cross_doublet_branching_ratio']*100.0:.1f} %)")

    pA = output["pair_A_analysis"]
    pB = output["pair_B_analysis"]
    lines.append(f"\n[2] Pair A Profile ({pA['name']}):")
    lines.append(f"  Configuration:                     {pA['configuration']}")
    lines.append(f"  Mean Alignment <i_x>:              {pA['mean_alignment_hbar']:.2f} hbar")
    lines.append(f"  Minimum Twin Splitting:            Delta E_min = {pA['min_energy_splitting_keV']:.1f} keV (Mean = {pA['mean_energy_splitting_keV']:.1f} keV)")

    lines.append(f"\n[3] Pair B Profile ({pB['name']}):")
    lines.append(f"  Configuration:                     {pB['configuration']}")
    lines.append(f"  Mean Alignment <i_x>:              {pB['mean_alignment_hbar']:.2f} hbar")
    lines.append(f"  Minimum Twin Splitting:            Delta E_min = {pB['min_energy_splitting_keV']:.1f} keV (Mean = {pB['mean_energy_splitting_keV']:.1f} keV)")

    lines.append("-" * 76)
    lines.append("Methodology Takeaway: Multiple Chiral Doublets (MChD) require independent")
    lines.append("quasiparticle alignments Delta i_x >= 1.5 hbar to eliminate spurious assignments.")
    lines.append("=" * 76)
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Multiple Chiral Doublets (MChD) Discriminator")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--cross-br", type=float, help="Cross-doublet branching ratio")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["133Ce_classic_mchid"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()
    if args.cross_br is not None:
        cfg["cross_doublet_branching_ratio"] = args.cross_br

    res = run_mchid_arbitration(
        nucleus=cfg.get("nucleus", "Generic"),
        harris_J0=cfg["harris_J0"],
        harris_J1=cfg["harris_J1"],
        pair_A=cfg["pair_A"],
        pair_B=cfg["pair_B"],
        cross_branching=cfg.get("cross_doublet_branching_ratio", 0.05)
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=f"Preset: {args.preset or '133Ce_classic_mchid'} ({cfg['description']})"))

if __name__ == "__main__":
    main()
