#!/usr/bin/env python3
"""Conditional BGO veto model; defaults and legacy presets are synthetic.

Assumptions, rather than a detector transport calculation:
  W is the FULL gate width in ns, centered on a zero-mean Gaussian Ge-BGO
  prompt time difference with caller-specified standard deviation sigma.
  A(W) = erf(W / (2 sqrt(2) sigma)) is the prompt timing acceptance.
  c and p are the infinite-window correlated rejection probabilities,
  conditional on an unsuppressed continuum event or full-energy peak event.
  They already include geometry, escape fraction, threshold and event cuts.
  r_c = c A(W), r_p = p A(W).
  q = exp(-R W) is the no-hit probability for independent Poisson random veto
  triggers at the SAME threshold/cuts, with W converted to seconds.
  Peak and continuum acceptances are a_p = (1-r_p)q, a_c = (1-r_c)q.

Scintillation light decay is NOT the prompt time resolution. Energy, threshold
and decay are retained as descriptive metadata; no response is inferred from
them. A measured prompt response with non-Gaussian tails or class-dependent
timing needs a different response model. No preset predicts Gammasphere or
Euroball performance, and no numerical parameters here are literature fits.

For baseline peak fraction f, P/T = f a_p / (f a_p + (1-f) a_c).
The common q cancels from P/T but reduces counts and statistical sensitivity.
The separate selected ROI has baseline S0 and B0 at fixed exposure, with
S = S0 a_p, B = B0 a_c. This assumes ALL selected background responds like the
modeled continuum; full-spectrum P/T does not determine ROI S/B. The default
objective Z = S/sqrt(S+B) is a counting precision proxy with Poisson total
variance and negligible extra background-estimation variance, NOT a calibrated
discovery significance. The alternative objective is retained signal counts.

For compatibility, matrix_fom_enhancement now means the ratio of Z_pair**2
derived from normalized two-arm counts under IDENTICAL, INDEPENDENT arms:
S_pair = (f a_p)**2, T_pair = (f a_p + (1-f) a_c)**2.
It is diagnostic only, not the optimization objective. Actual cascades,
shared shields, inter-arm randoms and detector cross-talk need a joint response.
Migrate to objective_name/objective_value and the explicit count/acceptance
fields; the old key's numerical meaning has changed.

Local evidence context (not calibration of this model):
knowledge/sources/li-2025-imp-dragon-hpge-array.md, ID25-3 (PDF p.2,
Sec.2.1/Fig.2) and ID25-5 (PDF p.3, Sec.2.3) distinguish configuration-specific
suppression and an electronics veto window. No measured Gaussian sigma or
infinite-window rejection for this model has been extracted from that source.
"""

import sys
import json
import argparse
import math
from scipy.optimize import minimize_scalar

PRESETS = {
    "gammasphere_bgo_standard_1332keV": {
        "spectrometer": "Synthetic coaxial HPGe/BGO example (legacy Gammasphere key)",
        "description": "Synthetic inputs at 1332.5 keV; not measured Gammasphere performance",
        "E_gamma_keV": 1332.5,
        "pt_unsuppressed": 0.23,
        "bgo_singles_rate_kHz": 85.0,
        "bgo_scintillation_decay_ns": 300.0,
        "bgo_energy_threshold_keV": 80.0,
        "eval_veto_windows_ns": [20.0, 40.0, 60.0, 80.0, 100.0, 150.0, 200.0]
    },
    "high_rate_heavy_ion_in_beam_bgo": {
        "spectrometer": "Synthetic high-rate HPGe/BGO example",
        "description": "Synthetic 350 kHz random-trigger scenario at 850 keV",
        "E_gamma_keV": 850.0,
        "pt_unsuppressed": 0.25,
        "bgo_singles_rate_kHz": 350.0,
        "bgo_scintillation_decay_ns": 300.0,
        "bgo_energy_threshold_keV": 70.0,
        "eval_veto_windows_ns": [15.0, 30.0, 50.0, 75.0, 100.0, 150.0]
    },
    "clover_escape_suppressed_shield": {
        "spectrometer": "Synthetic clover/BGO example (legacy key)",
        "description": "Synthetic inputs at 511.0 keV; not measured Euroball/AFRODITE performance",
        "E_gamma_keV": 511.0,
        "pt_unsuppressed": 0.30,
        "bgo_singles_rate_kHz": 120.0,
        "bgo_scintillation_decay_ns": 300.0,
        "bgo_energy_threshold_keV": 60.0,
        "eval_veto_windows_ns": [25.0, 50.0, 75.0, 100.0, 150.0]
    }
}

def _finite(name, value, *, minimum=0.0, positive=False, maximum=None):
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must be a finite number") from exc
    if not math.isfinite(number):
        raise ValueError(f"{name} must be finite")
    if number < minimum or (positive and number == minimum):
        relation = ">" if positive else ">="
        raise ValueError(f"{name} must be {relation} {minimum}")
    if maximum is not None and number > maximum:
        raise ValueError(f"{name} must be <= {maximum}")
    return number


class BGOComptonSuppressionOptimizer:
    def __init__(self, E_gamma_keV=1332.5, pt_unsuppressed=0.23,
                 bgo_singles_rate_kHz=85.0, bgo_scintillation_decay_ns=300.0,
                 bgo_energy_threshold_keV=80.0, *, prompt_sigma_ns=20.0,
                 correlated_escape_rejection=0.8, correlated_peak_rejection=0.0,
                 signal_counts=1000.0, background_counts=4000.0,
                 objective="significance", response_provenance="synthetic"):
        self.E0 = _finite("E_gamma_keV", E_gamma_keV, positive=True)
        self.pt_unsupp = _finite(
            "pt_unsuppressed", pt_unsuppressed, positive=True, maximum=1.0)
        rate = _finite("bgo_singles_rate_kHz", bgo_singles_rate_kHz)
        self.R_BGO = _finite("bgo_singles_rate_Hz", rate * 1e3)
        self.tau_decay = _finite(
            "bgo_scintillation_decay_ns", bgo_scintillation_decay_ns,
            positive=True) * 1e-9
        self.E_thresh = _finite(
            "bgo_energy_threshold_keV", bgo_energy_threshold_keV)
        self.prompt_sigma_ns = _finite(
            "prompt_sigma_ns", prompt_sigma_ns, positive=True)
        self.escape_rejection = _finite(
            "correlated_escape_rejection", correlated_escape_rejection, maximum=1.0)
        self.peak_rejection = _finite(
            "correlated_peak_rejection", correlated_peak_rejection, maximum=1.0)
        self.signal_counts = _finite("signal_counts", signal_counts, positive=True)
        self.background_counts = _finite("background_counts", background_counts)
        _finite("signal_counts + background_counts",
                self.signal_counts + self.background_counts, positive=True)
        if objective not in ("significance", "signal_counts"):
            raise ValueError("objective must be 'significance' or 'signal_counts'")
        if not isinstance(response_provenance, str) or not response_provenance.strip():
            raise ValueError("response_provenance must be a nonempty string")
        self.objective = objective
        self.response_provenance = response_provenance

    def prompt_time_acceptance(self, tau_veto_ns):
        """Integral of the specified Gaussian over [-W/2, W/2], not light yield."""
        width = _finite("tau_veto_ns", tau_veto_ns)
        return math.erf((width / self.prompt_sigma_ns) / (2.0 * math.sqrt(2.0)))

    def compton_escape_rejection_efficiency(self, tau_veto_ns):
        """Correlated veto fraction of the baseline continuum, excluding randoms."""
        return self.escape_rejection * self.prompt_time_acceptance(tau_veto_ns)

    def random_survival(self, tau_veto_ns):
        """No uncorrelated trigger in the full gate, equally for peak and continuum."""
        width = _finite("tau_veto_ns", tau_veto_ns)
        return math.exp(-self.R_BGO * (width * 1e-9))

    def accidental_photopeak_loss(self, tau_veto_ns):
        """Random veto probability, evaluated accurately also for very small R W."""
        width = _finite("tau_veto_ns", tau_veto_ns)
        return -math.expm1(-self.R_BGO * (width * 1e-9))

    def evaluate_performance(self, tau_veto_ns):
        """Expected counts at fixed exposure, purity, and the chosen ROI objective.

        SF excludes random losses: it is 1/(1-r_c). None denotes an infinite
        SF or undefined ratio (zero denominator), so results remain strict JSON.
        P/T is evaluated before the common random factor to avoid underflow;
        if random survival underflows to zero it is a limiting composition,
        not an assertion that any events were observed.
        """
        width = _finite("tau_veto_ns", tau_veto_ns)
        timing = self.prompt_time_acceptance(width)
        rej_eff = self.escape_rejection * timing
        peak_rej = self.peak_rejection * timing
        q = self.random_survival(width)
        peak_correlated_survival = 1.0 - peak_rej
        continuum_correlated_survival = 1.0 - rej_eff
        a_peak = peak_correlated_survival * q
        a_cont = continuum_correlated_survival * q
        peak_before_random = self.pt_unsupp * peak_correlated_survival
        cont_before_random = (1.0 - self.pt_unsupp) * continuum_correlated_survival
        total_before_random = peak_before_random + cont_before_random
        pt_supp = (peak_before_random / total_before_random
                   if total_before_random else None)

        signal = self.signal_counts * a_peak
        background = self.background_counts * a_cont
        baseline_z = self.signal_counts / math.sqrt(
            self.signal_counts + self.background_counts)
        # Cancel q analytically before taking sqrt to preserve small probabilities.
        roi_before_random = (self.signal_counts * peak_correlated_survival
                             + self.background_counts * continuum_correlated_survival)
        z = (math.sqrt(q) * (self.signal_counts * peak_correlated_survival)
             / math.sqrt(roi_before_random) if roi_before_random else 0.0)
        objective_value = z if self.objective == "significance" else signal
        matrix_z_gain = (q * peak_correlated_survival**2 / total_before_random
                         if total_before_random else 0.0)

        return {
            "tau_veto_ns": width,
            "prompt_time_acceptance": timing,
            "correlated_continuum_rejection": rej_eff,
            "correlated_peak_rejection": peak_rej,
            "random_survival": q,
            "peak_acceptance": a_peak,
            "continuum_acceptance": a_cont,
            "normalized_peak_counts": self.pt_unsupp * a_peak,
            "normalized_continuum_counts": (1.0 - self.pt_unsupp) * a_cont,
            "total_acceptance": total_before_random * q,
            "rejection_efficiency_pct": rej_eff * 100.0,
            "suppression_factor_SF": (1.0 / continuum_correlated_survival
                                      if continuum_correlated_survival else None),
            "accidental_peak_loss_pct": self.accidental_photopeak_loss(width) * 100.0,
            "pt_suppressed": pt_supp,
            "singles_pt_gain_factor": (pt_supp / self.pt_unsupp
                                       if pt_supp is not None else None),
            "signal_counts": signal,
            "background_counts": background,
            "signal_to_background": signal / background if background else None,
            "significance_proxy": z,
            "significance_gain": z / baseline_z,
            "objective_name": self.objective,
            "objective_value": objective_value,
            "matrix_peak_peak_count_acceptance": a_peak**2,
            "matrix_signal_counts_normalized": (self.pt_unsupp * a_peak)**2,
            "matrix_background_counts_normalized": (
                2.0 * self.pt_unsupp * (1.0 - self.pt_unsupp) * a_peak * a_cont
                + ((1.0 - self.pt_unsupp) * a_cont)**2),
            "matrix_peak_peak_fraction": pt_supp**2 if pt_supp is not None else None,
            "matrix_significance_gain_squared": matrix_z_gain**2,
            "matrix_fom_enhancement": matrix_z_gain**2,
        }

    def optimize_veto_window(self, min_ns=0.0, max_ns=250.0):
        """Compare the interior optimum and exact endpoints; ties favor smaller gates."""
        lower = _finite("min_ns", min_ns)
        upper = _finite("max_ns", max_ns)
        if lower > upper:
            raise ValueError("min_ns must be <= max_ns")

        def value(tau_ns):
            return self.evaluate_performance(tau_ns)["objective_value"]

        candidates = [lower, upper]
        # Above 20 sigma erf has rounded to one: the response is constant and
        # random survival can only decrease. Scaling also resolves narrow prompts.
        scaled_lower = lower / self.prompt_sigma_ns
        scaled_upper = min(upper / self.prompt_sigma_ns, 20.0)
        if scaled_lower < scaled_upper:
            opt = minimize_scalar(
                lambda width: -value(width * self.prompt_sigma_ns),
                bounds=(scaled_lower, scaled_upper), method="bounded")
            if not opt.success or not math.isfinite(opt.fun):
                raise RuntimeError("Veto optimization failed")
            candidates.extend((float(opt.x) * self.prompt_sigma_ns,
                               min(upper, scaled_upper * self.prompt_sigma_ns)))
        best_tau = max(sorted(candidates), key=value)
        best_res = self.evaluate_performance(best_tau)
        return best_tau, best_res

def run_compton_suppression_analysis(spectrometer="Generic Spectrometer",
                                     E_gamma_keV=1332.5, pt_unsuppressed=0.23,
                                     bgo_singles_rate_kHz=85.0,
                                     bgo_scintillation_decay_ns=300.0,
                                     bgo_energy_threshold_keV=80.0,
                                     eval_veto_windows_ns=None, *,
                                     prompt_sigma_ns=20.0,
                                     correlated_escape_rejection=0.8,
                                     correlated_peak_rejection=0.0,
                                     signal_counts=1000.0, background_counts=4000.0,
                                     objective="significance",
                                     response_provenance="synthetic",
                                     optimize_min_ns=0.0, optimize_max_ns=250.0):
    """Legacy positional API with explicit optional response/count inputs.

    Supplying energy or threshold alone does not recalibrate the response.
    response_provenance records a caller label, not verification of calibration.
    """
    if eval_veto_windows_ns is None:
        eval_veto_windows_ns = [20.0, 40.0, 60.0, 80.0, 100.0, 150.0, 200.0]

    optimizer = BGOComptonSuppressionOptimizer(
        E_gamma_keV=E_gamma_keV,
        pt_unsuppressed=pt_unsuppressed,
        bgo_singles_rate_kHz=bgo_singles_rate_kHz,
        bgo_scintillation_decay_ns=bgo_scintillation_decay_ns,
        bgo_energy_threshold_keV=bgo_energy_threshold_keV,
        prompt_sigma_ns=prompt_sigma_ns,
        correlated_escape_rejection=correlated_escape_rejection,
        correlated_peak_rejection=correlated_peak_rejection,
        signal_counts=signal_counts, background_counts=background_counts,
        objective=objective, response_provenance=response_provenance,
    )

    series = [optimizer.evaluate_performance(tau) for tau in eval_veto_windows_ns]
    best_tau, best_perf = optimizer.optimize_veto_window(optimize_min_ns, optimize_max_ns)

    return {
        "spectrometer": spectrometer,
        "E_gamma_keV": float(E_gamma_keV),
        "pt_unsuppressed": float(pt_unsuppressed),
        "bgo_singles_rate_kHz": float(bgo_singles_rate_kHz),
        "model_scope": "conditional Gaussian prompt response; no detector calibration",
        "response_provenance": optimizer.response_provenance,
        "response_parameters": {
            "prompt_sigma_ns": optimizer.prompt_sigma_ns,
            "correlated_escape_rejection": optimizer.escape_rejection,
            "correlated_peak_rejection": optimizer.peak_rejection,
            "bgo_energy_threshold_keV": optimizer.E_thresh,
            "bgo_scintillation_decay_ns": float(bgo_scintillation_decay_ns),
        },
        "baseline_signal_counts": optimizer.signal_counts,
        "baseline_background_counts": optimizer.background_counts,
        "objective_name": optimizer.objective,
        "optimization_bounds_ns": [float(optimize_min_ns), float(optimize_max_ns)],
        "assumptions": [
            "Gate is the full width centered on a Gaussian prompt mean of zero.",
            "Correlated probabilities include geometry, threshold and event cuts.",
            "Random triggers are stationary Poisson, independent of event class and tags.",
            "Energy, threshold and scintillation decay are metadata, not response laws.",
            "ROI background has the same acceptance as the modeled continuum.",
            "S/sqrt(S+B) assumes negligible extra background-estimation variance.",
            "Matrix diagnostics assume identical independent arms, including random vetoes.",
            "Default response and count inputs, including legacy presets, are synthetic.",
            "An optimum on a bound applies only to the requested search interval.",
        ],
        "migration_note": (
            "Use objective_name/objective_value and count/acceptance fields. "
            "matrix_fom_enhancement is a compatibility alias for "
            "matrix_significance_gain_squared under independent-arm assumptions; "
            "it is not optimized and its numerical meaning has changed."),
        "optimal_veto_window_ns": best_tau,
        "optimal_performance": best_perf,
        "veto_window_evolution": series
    }

def format_text_report(output, title="Conditional BGO Compton Suppression Model"):
    def number(value, spec=".3f"):
        return format(value, spec) if value is not None else "undefined"

    lines = []
    lines.append("=" * 76)
    lines.append(f"  {title}")
    lines.append("=" * 76)
    lines.append(f"Spectrometer: {output['spectrometer']} | Gamma Energy: {output['E_gamma_keV']:.1f} keV")
    lines.append(f"Unsuppressed Baseline: P/T_0 = {output['pt_unsuppressed']*100.0:.1f} % | BGO Rate: R_BGO = {output['bgo_singles_rate_kHz']:.1f} kHz")

    opt = output["optimal_performance"]
    lines.append(f"Response provenance (caller label): {output['response_provenance']}")
    lines.append("SYNTHETIC defaults; no measured array performance is predicted.")
    lines.append(f"Objective: {output['objective_name']} | fixed-exposure ROI S0/B0: "
                 f"{output['baseline_signal_counts']:g}/{output['baseline_background_counts']:g}")
    lines.append("\n[1] Conditional optimum within the requested bounds:")
    lines.append(f"  Optimal Veto Gate Window:          tau_veto_opt = {output['optimal_veto_window_ns']:.1f} ns")
    lines.append(f"  Suppressed P/T fraction:           {number(opt['pt_suppressed'])}")
    lines.append(f"  Correlated-only continuum SF:      {number(opt['suppression_factor_SF'])}")
    lines.append(f"  Accidental Photopeak Loss:         Loss_acc     = {opt['accidental_peak_loss_pct']:.2f} %")
    lines.append(f"  Peak count acceptance:             {opt['peak_acceptance']:.6f}")
    lines.append(f"  Retained ROI S, B:                  {opt['signal_counts']:.3f}, {opt['background_counts']:.3f}")
    lines.append(f"  S/sqrt(S+B) counting proxy:         {opt['significance_proxy']:.3f}")
    lines.append(f"  Independent-arm matrix Z^2 gain:   {opt['matrix_significance_gain_squared']:.3f}")

    lines.append("\n[2] Veto Window Evolution & Trade-off Trajectory:")
    lines.append("  Full gate (ns)     P/T     Peak acceptance     ROI S/sqrt(S+B)")
    lines.append("  ---------------------------------------------------------------------------------")
    for pt in output["veto_window_evolution"]:
        lines.append(f"      {pt['tau_veto_ns']:8.1f}    {number(pt['pt_suppressed']):>9}    "
                     f"{pt['peak_acceptance']:12.6f}    {pt['significance_proxy']:12.3f}")

    lines.append("-" * 76)
    lines.extend(f"Assumption: {item}" for item in output["assumptions"])
    lines.append("=" * 76)
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="In-Beam BGO Compton Suppression Optimizer")
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Preset configuration")
    parser.add_argument("--energy", type=float, help="Gamma-ray energy (keV)")
    parser.add_argument("--rate", type=float, help="BGO singles rate (kHz)")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON format")
    args = parser.parse_args()

    cfg = PRESETS["gammasphere_bgo_standard_1332keV"].copy()
    if args.preset:
        cfg = PRESETS[args.preset].copy()
    if args.energy is not None:
        cfg["E_gamma_keV"] = args.energy
    if args.rate is not None:
        cfg["bgo_singles_rate_kHz"] = args.rate

    res = run_compton_suppression_analysis(
        spectrometer=cfg.get("spectrometer", "Generic Spectrometer"),
        E_gamma_keV=cfg["E_gamma_keV"],
        pt_unsuppressed=cfg["pt_unsuppressed"],
        bgo_singles_rate_kHz=cfg["bgo_singles_rate_kHz"],
        bgo_scintillation_decay_ns=cfg.get("bgo_scintillation_decay_ns", 300.0),
        bgo_energy_threshold_keV=cfg.get("bgo_energy_threshold_keV", 80.0),
        eval_veto_windows_ns=cfg.get("eval_veto_windows_ns")
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=f"Preset: {args.preset or 'gammasphere_bgo_standard_1332keV'} ({cfg['description']})"))

if __name__ == "__main__":
    main()
