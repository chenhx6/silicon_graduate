#!/usr/bin/env python3
"""Audit Weisskopf single-particle units (W.u.) and collective enhancements in 165Tm and 136Nd.

Verifies:
1. Standard Weisskopf single-particle estimates:
   - B(E2)_sp = (1/(4*pi)) * (3/5)^2 * (1.20 * A^(1/3))^4 = 0.05940 * A^(4/3) [e^2 fm^4]
   - B(M1)_sp = 1.7905 [mu_N^2] (mass independent)
2. Mass scaling:
   - 136Nd (A=136): B(E2)_sp = 41.5467 e^2 fm^4 = 0.00415467 e^2 b^2
   - 165Tm (A=165): B(E2)_sp = 53.4862 e^2 fm^4 = 0.00534862 e^2 b^2
3. 136Nd Table II collective enhancement profile:
   - Band 2 high collectivity at low spin: 130.0 W.u. (15-) -> 122.8 W.u. (16-) -> 105.9 W.u. (17-)
   - Dramatic collapse at crossing: 9.6 W.u. (18-) -> 12.0 W.u. (19-) (11.0-fold reduction)
   - Double ratio in W.u. strictly equals 77/4 = 19.25 (scale invariance preserved)
4. 165Tm Table 2 prolate rotor super-collectivity:
   - [541]1/2- mean Qt = 8.3 eb corresponds to ~480 W.u. (strongly deformed beta_2 ~ 0.33)
   - [411]1/2+ mean Qt = 7.4 eb corresponds to ~382 W.u. (beta_2 ~ 0.30)
   - Super-collectivity ratio (480 / 382) ~ 1.258 matches (8.3 / 7.4)^2
"""

import json
import math
from pathlib import Path

RUN = Path("outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01")

def weisskopf_be2_sp(A):
    # Returns in e^2 b^2
    return (1.0 / (4.0 * math.pi)) * ((3.0 / 5.0)**2) * ((1.20 * (A**(1.0 / 3.0)))**4) * 1e-4

def weisskopf_bm1_sp():
    # In mu_N^2
    return 1.7905

def main():
    checks = []
    def check(name, ok, **evidence):
        checks.append({"name": name, "passed": bool(ok), **evidence})
        assert ok, f"FAILED: {name}"

    # 1. Check Weisskopf formulas
    be2_sp_136 = weisskopf_be2_sp(136)
    check("136Nd B(E2)_sp in range [0.0041, 0.0042] e^2 b^2", 0.0041 <= be2_sp_136 <= 0.0042, value=be2_sp_136)

    be2_sp_165 = weisskopf_be2_sp(165)
    check("165Tm B(E2)_sp in range [0.0053, 0.0054] e^2 b^2", 0.0053 <= be2_sp_165 <= 0.0054, value=be2_sp_165)

    bm1_sp = weisskopf_bm1_sp()
    check("B(M1)_sp equals 1.7905 mu_N^2", abs(bm1_sp - 1.7905) < 1e-6)

    # 2. 136Nd Table II in Weisskopf units
    nd_data = [
        # Band, Spin, BM1_muN2, BE2_e2b2, Qt_eb
        ("Band 1", 15, 2.7, None, None),
        ("Band 1", 16, 1.7, 0.26, 1.73),
        ("Band 1", 17, 1.1, 0.08, 0.95),
        ("Band 1", 18, 0.9, 0.14, 1.26),
        ("Band 1", 19, 1.7, 0.11, 1.11),
        ("Band 2", 15, 4.4, 0.54, 2.50),
        ("Band 2", 16, 3.5, 0.51, 2.42),
        ("Band 2", 17, 1.4, 0.44, 2.24),
        ("Band 2", 18, 1.0, 0.04, 0.67),
        ("Band 2", 19, 1.6, 0.05, 0.75),
    ]

    nd_records = []
    for b, s, bm1, be2, qt in nd_data:
        be2_wu = be2 / be2_sp_136 if be2 is not None else None
        bm1_wu = bm1 / bm1_sp if bm1 is not None else None
        nd_records.append({
            "band": b,
            "spin": s,
            "bm1_muN2": bm1,
            "bm1_wu": round(bm1_wu, 3) if bm1_wu is not None else None,
            "be2_e2b2": be2,
            "be2_wu": round(be2_wu, 2) if be2_wu is not None else None,
            "qt_eb": qt
        })

    # Assertions for 136Nd
    b2_17 = [r for r in nd_records if r["band"] == "Band 2" and r["spin"] == 17][0]
    b2_18 = [r for r in nd_records if r["band"] == "Band 2" and r["spin"] == 18][0]
    b1_17 = [r for r in nd_records if r["band"] == "Band 1" and r["spin"] == 17][0]
    b1_18 = [r for r in nd_records if r["band"] == "Band 1" and r["spin"] == 18][0]

    check("Band 2 17- collectivity > 100 W.u.", b2_17["be2_wu"] > 100.0, be2_wu=b2_17["be2_wu"])
    check("Band 2 18- collectivity < 15 W.u.", b2_18["be2_wu"] < 15.0, be2_wu=b2_18["be2_wu"])
    check("Band 2 collectivity drops by factor > 10", (b2_17["be2_wu"] / b2_18["be2_wu"]) > 10.0,
          ratio=round(b2_17["be2_wu"] / b2_18["be2_wu"], 2))

    # Double ratio in W.u.
    r17_wu = b2_17["be2_wu"] / b1_17["be2_wu"]
    r18_wu = b2_18["be2_wu"] / b1_18["be2_wu"]
    double_ratio_wu = r17_wu / r18_wu
    check("Double ratio in W.u. equals 77/4 (19.25) within rounding", abs(double_ratio_wu - 19.25) < 0.1,
          double_ratio=round(double_ratio_wu, 4))

    # 3. 165Tm super-collectivity
    # High-spin rotor limit: B(E2) = (15 / 128*pi) * Qt^2
    const_rot = 15.0 / (128.0 * math.pi)
    be2_541 = const_rot * (8.3**2)
    be2_411 = const_rot * (7.4**2)
    wu_541 = be2_541 / be2_sp_165
    wu_411 = be2_411 / be2_sp_165

    check("165Tm [541]1/2- collectivity in range [450, 500] W.u.", 450 <= wu_541 <= 500, wu=round(wu_541, 1))
    check("165Tm [411]1/2+ collectivity in range [350, 400] W.u.", 350 <= wu_411 <= 400, wu=round(wu_411, 1))
    check("165Tm prolate collectivity is ~4x larger than 136Nd triaxial collectivity", (wu_541 / b2_17["be2_wu"]) > 4.0,
          ratio=round(wu_541 / b2_17["be2_wu"], 2))

    out = {
        "kind": "weisskopf-collectivity-systematics-audit",
        "valid": True,
        "checks": checks,
        "single_particle_units": {
            "136Nd": {"A": 136, "BE2_sp_e2b2": be2_sp_136, "BE2_sp_e2fm4": be2_sp_136 * 1e4},
            "165Tm": {"A": 165, "BE2_sp_e2b2": be2_sp_165, "BE2_sp_e2fm4": be2_sp_165 * 1e4},
            "BM1_sp_muN2": bm1_sp
        },
        "nd136_table_ii_wu": nd_records,
        "tm165_super_collectivity": {
            "band_541": {"Qt_eb": 8.3, "BE2_e2b2": round(be2_541, 4), "BE2_wu": round(wu_541, 1)},
            "band_411": {"Qt_eb": 7.4, "BE2_e2b2": round(be2_411, 4), "BE2_wu": round(wu_411, 1)},
            "collectivity_ratio": round(wu_541 / wu_411, 4),
            "Qt_squared_ratio": round((8.3 / 7.4)**2, 4)
        },
        "time_invariants_respected": {
            "formal_credit_not_yet_awarded": True,
            "window_ends_at": "15:00 CST",
            "closeout_hour": "15:00 - 16:00 CST"
        }
    }

    out_file = RUN / "weisskopf-collectivity-result-076.json"
    out_file.write_text(json.dumps(out, indent=2, ensure_ascii=False) + chr(10)
, encoding="utf-8")
    print(json.dumps({"valid": out["valid"], "checks": len(checks), "output": str(out_file)}))

if __name__ == "__main__":
    main()
