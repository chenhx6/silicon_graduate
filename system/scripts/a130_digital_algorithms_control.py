#!/usr/bin/env python3
"""Bounded input mathematical test controls for Appendix E digital algorithms.

Tests:
1. Pure exponential input: direct discrete convolution vs Jordanov 4-step pipeline recurrence.
   Verify agreement within the declared numerical tolerance and flat-top amplitude Ak(M+1).
2. Non-zero baseline input: verify identical baseline subtraction on all delayed samples
   with x[n < 0] = 0, proving zero baseline residual.
3. CFD bipolar shaping and zero-crossing: verify C[n] = F[n-d] - f F[n] negative-to-nonnegative
   zero crossing, amplitude invariance, and linear sub-sample interpolation error formula.
"""

import numpy as np
import json
import hashlib
import sys
from pathlib import Path

def test_jordanov_pure_exponential():
    Ts = 10.0  # ns (100 MSPS)
    tau_d = 50000.0  # ns (50 us)
    alpha = np.exp(-Ts / tau_d)
    M = alpha / (1.0 - alpha)  # Exact M

    k = 200  # rise points (2 us)
    ell = 300  # flat-top end points (3 us), so flat top length is ell - k points
    A = 1000.0
    N = 1000

    # Input pure exponential arriving at n=0
    n = np.arange(N)
    v = np.zeros(N)
    v[n >= 0] = A * (alpha ** n[n >= 0])

    # 1. Pipeline recurrence (Section 5.3)
    # d[n] = v[n] - v[n-k] - v[n-ell] + v[n-k-ell]
    # p[n] = p[n-1] + d[n]
    # r[n] = p[n] + M*d[n]
    # s[n] = s[n-1] + r[n]
    d = np.zeros(N)
    p = np.zeros(N)
    r = np.zeros(N)
    s = np.zeros(N)

    def get_v(idx):
        return v[idx] if idx >= 0 else 0.0

    for i in range(N):
        d[i] = get_v(i) - get_v(i - k) - get_v(i - ell) + get_v(i - k - ell)
        p[i] = (p[i-1] if i > 0 else 0.0) + d[i]
        r[i] = p[i] + M * d[i]
        s[i] = (s[i-1] if i > 0 else 0.0) + r[i]

    # Expected flat-top amplitude
    expected_peak = A * k * (M + 1.0)
    flat_top_samples = s[k - 1 : ell]  # flat top is from n = k-1 to ell-1

    max_deviation_in_flat_top = np.max(np.abs(flat_top_samples - expected_peak))
    rel_flat_top_error = max_deviation_in_flat_top / expected_peak

    # 2. Impulse response of filter H(z) = [(M+1) - M z^-1] B_k(z) B_ell(z)
    bk = np.ones(k)
    bell = np.ones(ell)
    bk_bell = np.convolve(bk, bell)  # length k + ell - 1
    h = np.zeros(len(bk_bell) + 1)
    h[:len(bk_bell)] += (M + 1.0) * bk_bell
    h[1:len(bk_bell)+1] -= M * bk_bell

    # Direct convolution of input v with impulse response h
    s_conv = np.convolve(v, h)[:N]
    max_diff_recurrence_vs_conv = np.max(np.abs(s - s_conv))
    rel_diff_conv = max_diff_recurrence_vs_conv / expected_peak

    print(f"Test 1 - Pure Exponential:")
    print(f"  Exact M: {M:.6f}")
    print(f"  Expected peak: {expected_peak:.6f}")
    print(f"  Max flat-top deviation from theory: {max_deviation_in_flat_top:.2e} (rel: {rel_flat_top_error:.2e})")
    print(f"  Max diff (recurrence vs direct convolution): {max_diff_recurrence_vs_conv:.2e} (rel: {rel_diff_conv:.2e})")
    assert rel_flat_top_error < 1e-12, "Flat-top amplitude relative error exceeds the declared 1e-12 tolerance"
    assert rel_diff_conv < 1e-12, "Convolution vs recurrence relative error exceeds the declared 1e-12 tolerance"
    return {
        "M": M,
        "expected_peak": expected_peak,
        "max_flat_top_dev": float(max_deviation_in_flat_top),
        "rel_flat_top_error": float(rel_flat_top_error),
        "max_diff_conv": float(max_diff_recurrence_vs_conv),
        "status": "passed"
    }

def test_nonzero_baseline():
    Ts = 10.0
    tau_d = 50000.0
    alpha = np.exp(-Ts / tau_d)
    M = alpha / (1.0 - alpha)
    k = 200
    ell = 300
    A = 1000.0
    BL = 250.0  # Non-zero constant baseline
    N = 1000

    # Input with non-zero baseline arriving at n=100
    v = np.full(N, BL)
    n = np.arange(N)
    v[n >= 100] += A * (alpha ** (n[n >= 100] - 100))

    # Pipeline with baseline subtraction: x[n] = v[n] - BL, x[n < 0] = 0
    # Both current and delayed samples subtract the same baseline BL
    d = np.zeros(N)
    p = np.zeros(N)
    r = np.zeros(N)
    s = np.zeros(N)

    def get_x(idx):
        if idx < 0:
            return 0.0
        return v[idx] - BL

    for i in range(N):
        d[i] = get_x(i) - get_x(i - k) - get_x(i - ell) + get_x(i - k - ell)
        p[i] = (p[i-1] if i > 0 else 0.0) + d[i]
        r[i] = p[i] + M * d[i]
        s[i] = (s[i-1] if i > 0 else 0.0) + r[i]

    expected_peak = A * k * (M + 1.0)
    flat_top = s[100 + k - 1 : 100 + ell]
    max_dev = np.max(np.abs(flat_top - expected_peak))
    rel_dev = max_dev / expected_peak
    baseline_residual = np.max(np.abs(s[:90]))

    print(f"Test 2 - Non-zero Baseline (BL = {BL}):")
    print(f"  Pre-pulse baseline residual in s[n]: {baseline_residual:.2e}")
    print(f"  Max flat-top deviation: {max_dev:.2e} (rel: {rel_dev:.2e})")
    assert baseline_residual < 1e-12, "Baseline residual not zero"
    assert rel_dev < 1e-12, "Flat-top amplitude corrupted by baseline"
    return {
        "BL": BL,
        "baseline_residual": float(baseline_residual),
        "flat_top_dev": float(max_dev),
        "rel_dev": float(rel_dev),
        "status": "passed"
    }

def test_cfd_zero_crossing():
    Ts = 10.0  # ns
    d_samp = 5  # delay 50 ns
    f = 0.25  # fraction

    # Fast filtered pulse F(t): smooth sigmoidal rising edge
    t0 = 200.0  # ns
    tau_r = 15.0  # ns

    N = 100
    t_grid = np.arange(N) * Ts

    def gen_cfd(A):
        F = A / (1.0 + np.exp(-(t_grid - t0) / tau_r))
        # Bipolar C[n] = F[n - d] - f * F[n] (negative to non-negative zero crossing)
        C = np.zeros(N)
        for i in range(N):
            F_del = F[i - d_samp] if (i - d_samp) >= 0 else 0.0
            C[i] = F_del - f * F[i]
        return F, C

    F1, C1 = gen_cfd(1000.0)
    F2, C2 = gen_cfd(5000.0)  # Amplitude x 5

    # Find zero crossing from negative to non-negative: C[n] < 0 <= C[n+1]
    def find_zc(C):
        for i in range(len(C) - 1):
            if C[i] < 0.0 and C[i+1] >= 0.0:
                t_sub = -C[i] / (C[i+1] - C[i]) * Ts
                t_zc = i * Ts + t_sub
                return i, t_sub, t_zc
        return None

    zc1 = find_zc(C1)
    zc2 = find_zc(C2)

    print(f"Test 3 - CFD Zero Crossing:")
    print(f"  Amp = 1000: n0 = {zc1[0]}, t_sub = {zc1[1]:.4f} ns, t_zc = {zc1[2]:.4f} ns")
    print(f"  Amp = 5000: n0 = {zc2[0]}, t_sub = {zc2[1]:.4f} ns, t_zc = {zc2[2]:.4f} ns")
    time_walk = np.abs(zc1[2] - zc2[2])
    print(f"  Time walk between A=1000 and A=5000: {time_walk:.2e} ns")
    assert time_walk < 1e-10, "CFD not amplitude-invariant"

    return {
        "zc_amp1000": zc1[2],
        "zc_amp5000": zc2[2],
        "time_walk_ns": float(time_walk),
        "status": "passed"
    }


def test_mismatch_sign():
    alpha = np.exp(-0.002)
    true_m = alpha / (1-alpha)
    k, ell, length = 20, 30, 1000
    v = 1000 * alpha**np.arange(length)
    bkbell = np.convolve(np.ones(k), np.ones(ell))
    result = {}
    for ratio in (0.8, 1.2):
        adopted_m = ratio*true_m
        h = np.zeros(len(bkbell)+1)
        h[:-1] += (adopted_m+1)*bkbell
        h[1:] -= adopted_m*bkbell
        out = np.convolve(v,h)[:length]
        index = k+ell+20
        adopted_alpha = adopted_m/(adopted_m+1)
        sign = np.sign(1-adopted_m/true_m)
        assert np.sign(out[index]) == sign
        assert np.sign(adopted_alpha-alpha) == np.sign(adopted_m-true_m)
        result[str(ratio)] = {"adopted_alpha":float(adopted_alpha),
                              "true_alpha":float(alpha),
                              "tail_sample":float(out[index])}
    return {"inputs":"positive pure exponential; four-step trapezoid, no physical detector fit",
            "cases":result,"status":"passed"}


def test_secant_error_leading_sign():
    phase, quadratic = 0.3, 0.4
    result=[]
    # C(t)=t+q*t² has an exact selected root t=0 and slope1 there.
    for step in (0.02,0.01,0.005):
        left,right=-phase*step,(1-phase)*step
        y0,y1=left+quadratic*left**2,right+quadratic*right**2
        estimate=left-y0*step/(y1-y0)
        leading=-quadratic*phase*(1-phase)*step**2
        assert estimate < 0
        assert abs(estimate/leading-1) < 0.01
        result.append({"Ts":step,"error":estimate,"leading":leading})
    assert 3.9 < result[0]["error"]/result[1]["error"] < 4.1
    return {"shape":"smooth quadratic C(t), root0; arbitrary compatible time units",
            "samples":result,"status":"passed"}


if __name__ == "__main__":
    summary = {
        "test_jordanov":test_jordanov_pure_exponential(),
        "test_baseline":test_nonzero_baseline(),
        "test_cfd":test_cfd_zero_crossing(),
        "test_mismatch":test_mismatch_sign(),
        "test_secant_leading":test_secant_error_leading_sign(),
        "all_passed":True,
        "boundary":"Finite mathematical controls; no detector/FPGA/experimental certification.",
        "provenance":{"python":sys.version.split()[0],"numpy":np.__version__,
                      "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    }
    out=Path(__file__).resolve().parents[2]/"outputs/l4/20261114-A130-digital-algorithms-controls"
    out.mkdir(parents=True,exist_ok=True)
    (out/"results.json").write_text(json.dumps(summary,indent=2)+"\n")
    print("All five bounded mathematical controls passed; results in",out)
