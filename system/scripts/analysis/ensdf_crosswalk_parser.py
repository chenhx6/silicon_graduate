#!/usr/bin/env python3
"""
NNDC Evaluated Nuclear Structure Data File (ENSDF) Parser & In-Beam Crosswalk Tool.

Based on:
  - J. K. Tuli, "Evaluated Nuclear Structure Data File: A Manual for Preparation of Data Sets",
    Brookhaven National Laboratory Report BNL-NCS-51655-01/02-Rev (2001)

Features:
  1. Robust fixed-width parsing of ENSDF Level (L) and Gamma (G) records.
  2. Extracts level energy, J_pi, T_1/2, E_gamma, I_gamma, multipolarity, and delta.
  3. Automatic crosswalk alignment between experimental in-beam peaks and evaluated ENSDF database.
"""

import re


def parse_ensdf_records(ensdf_text):
    """
    Parse standard 80-column ENSDF text dataset into structured levels and gamma transitions.
    Robust against leading whitespace and minor column shifts.
    """
    levels = []
    current_level = None
    
    lines = ensdf_text.splitlines()
    for line in lines:
        line_strip = line.strip()
        if len(line_strip) < 8:
            continue
            
        # Detect Record Type: search for standalone 'L' or 'G' within the first 12 characters
        m = re.match(r'^\s*([0-9]{1,3}[A-Za-z]{1,2})?\s*([LG])\s+(.*)', line)
        if not m:
            continue
            
        record_type = m.group(2).upper()
        rest = m.group(3)
        tokens = rest.split()
        if not tokens:
            continue
            
        if record_type == 'L':
            # Level record: tokens[0] is typically level energy
            e_str = tokens[0]
            e_clean = re.sub(r'[^\d.]', '', e_str)
            try:
                energy_keV = float(e_clean) if e_clean else 0.0
            except ValueError:
                energy_keV = 0.0
                
            # J_pi typically contains parentheses or +/-
            jpi_candidates = [t for t in tokens[1:] if any(c in t for c in ['+', '-', '(', ')'])]
            jpi_str = jpi_candidates[0] if jpi_candidates else (tokens[1] if len(tokens) > 1 else "")
            
            # Half life typically ends with PS, NS, US, MS, S, M, H, D, Y
            t12_candidates = [t for t in tokens[1:] if any(t.upper().endswith(u) for u in ['PS', 'NS', 'US', 'MS', 'S', 'M', 'H', 'D', 'Y'])]
            t12_str = t12_candidates[0] if t12_candidates else ""
            
            current_level = {
                "energy_keV": energy_keV,
                "energy_str": e_str,
                "jpi": jpi_str,
                "half_life": t12_str,
                "gammas": []
            }
            levels.append(current_level)
            
        elif record_type == 'G' and current_level is not None:
            # Gamma record: tokens[0] is E_gamma
            eg_str = tokens[0]
            eg_clean = re.sub(r'[^\d.]', '', eg_str)
            try:
                eg_keV = float(eg_clean) if eg_clean else 0.0
            except ValueError:
                eg_keV = 0.0
                
            # Relative intensity
            ig_val = 100.0
            if len(tokens) > 1:
                ig_clean = re.sub(r'[^\d.]', '', tokens[1])
                try:
                    ig_val = float(ig_clean) if ig_clean else 100.0
                except ValueError:
                    ig_val = 100.0
                    
            # Multipolarity (E1, E2, M1, M1+E2 etc)
            mult_candidates = [t for t in tokens[1:] if any(m in t.upper() for m in ['E1', 'E2', 'M1', 'M2', 'E3', 'M3'])]
            mult_str = mult_candidates[0] if mult_candidates else ""
            
            # Delta
            delta_val = 0.0
            for t in tokens[1:]:
                if t.startswith(('+', '-')) and re.sub(r'[^\d.]', '', t):
                    try:
                        delta_val = float(t)
                        break
                    except ValueError:
                        pass
                        
            gamma_item = {
                "eg_keV": eg_keV,
                "eg_str": eg_str,
                "ig": ig_val,
                "mult": mult_str,
                "delta": delta_val,
                "parent_level_energy": current_level["energy_keV"],
                "parent_jpi": current_level["jpi"]
            }
            current_level["gammas"].append(gamma_item)
            
    return levels


def crosswalk_match(measured_gamma_energies_keV, parsed_levels, tolerance_keV=1.0):
    """
    Match measured gamma peak energies against evaluated ENSDF dataset.
    
    Returns:
        dict with 'matched' and 'unmatched_new_candidates'.
    """
    all_ensdf_gammas = []
    for lev in parsed_levels:
        for g in lev["gammas"]:
            all_ensdf_gammas.append(g)
            
    matched = []
    unmatched = []
    
    for exp_e in measured_gamma_energies_keV:
        best_match = None
        min_diff = 999.0
        for g in all_ensdf_gammas:
            diff = abs(exp_e - g["eg_keV"])
            if diff <= tolerance_keV and diff < min_diff:
                min_diff = diff
                best_match = g
                
        if best_match is not None:
            matched.append({
                "exp_energy_keV": exp_e,
                "ensdf_energy_keV": best_match["eg_keV"],
                "diff_keV": exp_e - best_match["eg_keV"],
                "parent_level_energy": best_match["parent_level_energy"],
                "parent_jpi": best_match["parent_jpi"],
                "mult": best_match["mult"],
                "delta": best_match["delta"]
            })
        else:
            unmatched.append(exp_e)
            
    return {
        "matched": matched,
        "unmatched_new_candidates": unmatched
    }


if __name__ == "__main__":
    print("=== Benchmark: ENSDF Fixed-Width Parser & In-Beam Crosswalk ===")
    # Sample ENSDF block for 131Ce
    sample_ensdf = """
 131CE  L           0.0                 (7/2+)      10.2 M
 131CE  L         161.8               1 (11/2-)     4.8 PS
 131CE  G         161.8       1      100              M2+E3     -0.15          0.235
 131CE  L         450.2               2 (15/2-)
 131CE  G         288.4       2      100              E2                       0.045
 131CE  L         882.1               3 (19/2-)
 131CE  G         431.9       2      100              E2                       0.015
"""
    levels = parse_ensdf_records(sample_ensdf)
    print(f"  Parsed Levels: {len(levels)}")
    for lev in levels:
        print(f"    Level {lev['energy_keV']:6.1f} keV, J_pi = {lev['jpi']:8s}, T_1/2 = {lev['half_life']}")
        for g in lev["gammas"]:
            print(f"      -> Gamma {g['eg_keV']:6.1f} keV, Mult = {g['mult']:6s}, delta = {g['delta']:+5.2f}")
            
    # Test crosswalk with experimental list: [162.0, 288.1, 432.2, 595.0]
    test_exp = [162.0, 288.1, 432.2, 595.0]
    cw = crosswalk_match(test_exp, levels, tolerance_keV=1.0)
    print(f"\n  Crosswalk Matched Known Transitions ({len(cw['matched'])}):")
    for m in cw["matched"]:
        print(f"    Exp: {m['exp_energy_keV']:6.1f} keV <-> ENSDF: {m['ensdf_energy_keV']:6.1f} keV (diff: {m['diff_keV']:+4.1f} keV), J_pi = {m['parent_jpi']}, Mult = {m['mult']}")
    print(f"  Unmatched New Transition Candidates: {cw['unmatched_new_candidates']} keV")
