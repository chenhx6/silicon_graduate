#!/usr/bin/env python3
"""
a130_lifetime_response_figure.py
Produces:
1. RDDS decay curves (singles ratio Ru and Rs vs distance x for tau = 2, 5, 15 ps).
2. DSAM Doppler line shape with exact bin-integrated flight CDF and Gaussian resolution convolution.
Outputs:
- raw/writing/gpt/A130/these_2023_template/these_template/Img/lifetime-response-rdds-dsam.svg
- raw/writing/gpt/A130/these_2023_template/these_template/Img/lifetime-response-rdds-dsam.pdf
- outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G98/dsam_convergence_test.json
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf
import os
import json

def compute_dsam_spectrum(h, E0=1000.0, dE_max=20.0, tau_s=0.8, sig_det=1.2, tau_val=0.8,
                          energy_low=970.0, energy_high=1050.0, kernel_sigmas=6.0):
    """Computes DSAM spectrum with exact bin-integrated flight CDF and Gaussian convolution."""
    n_energy_bins = int(round((energy_high - energy_low) / h))
    E_edges = energy_low + np.arange(n_energy_bins + 1) * h
    E_centers = 0.5 * (E_edges[:-1] + E_edges[1:])
    N_bins = len(E_centers)

    # 1. Exact bin-integrated flight probabilities
    P_flight = np.zeros(N_bins)
    for j in range(N_bins):
        ea = max(E0, E_edges[j])
        eb = min(E0 + dE_max, E_edges[j+1])
        if eb > ea:
            tb = tau_s * (1.0 - (eb - E0) / dE_max)
            ta = tau_s * (1.0 - (ea - E0) / dE_max)
            P_flight[j] = np.exp(-tb / tau_val) - np.exp(-ta / tau_val)

    p_dens = P_flight / h
    f_stop = np.exp(-tau_s / tau_val)

    # 2. Gaussian resolution kernel on exact same grid spacing h
    # An odd number of bins places the kernel centre at zero. An even-bin
    # kernel combined with mode='same' shifts the spectrum by half a bin.
    radius_bins = int(np.ceil(kernel_sigmas * sig_det / h))
    k_edges = (np.arange(-radius_bins, radius_bins + 2) - 0.5) * h
    kernel = 0.5 * (erf(k_edges[1:] / (np.sqrt(2.0) * sig_det)) - erf(k_edges[:-1] / (np.sqrt(2.0) * sig_det)))

    y_flight = np.convolve(p_dens, kernel, mode='same')

    # 3. Stopped peak exact Gaussian CDF difference density
    y_stop = f_stop * 0.5 * (erf((E_edges[1:] - E0) / (np.sqrt(2.0) * sig_det)) - erf((E_edges[:-1] - E0) / (np.sqrt(2.0) * sig_det))) / h

    y_total = y_flight + y_stop
    area = float(np.sum(y_total) * h)
    # The centroid is a moment ratio; the density itself is not renormalized.
    centroid = float(np.sum(E_centers * y_total) * h / area)
    return E_centers, y_total, area, centroid

def run_convergence_tests():
    D = 20.0
    T = 0.8
    sig = 1.2
    E0 = 1000.0

    test_results = {}
    for tau in [0.1, 0.8, 5.0]:
        exact_shift = D * (1.0 - (tau / T) * (1.0 - np.exp(-T / tau)))
        runs = []
        spectra = {}
        for h in [0.05, 0.025, 0.0125]:
            E_c, y, area, centroid = compute_dsam_spectrum(h, E0=E0, dE_max=D, tau_s=T, sig_det=sig, tau_val=tau)
            shift = centroid - E0
            err = shift - exact_shift
            runs.append({
                "h_keV": h,
                "area": area,
                "centroid_keV": centroid,
                "centroid_shift_keV": shift,
                "error_vs_exact_keV": err
            })
            spectra[h] = (E_c, y)

        # Compute L1 norm convergence between h=0.05 and h=0.025, and h=0.025 and h=0.0125
        from scipy.interpolate import interp1d
        E3, y3 = spectra[0.0125]
        f1 = interp1d(spectra[0.05][0], spectra[0.05][1], bounds_error=False, fill_value=0.0)
        f2 = interp1d(spectra[0.025][0], spectra[0.025][1], bounds_error=False, fill_value=0.0)

        L1_12 = float(np.sum(np.abs(f1(E3) - f2(E3))) * 0.0125)
        L1_23 = float(np.sum(np.abs(f2(E3) - y3)) * 0.0125)

        E_wide, y_wide, area_wide, centroid_wide = compute_dsam_spectrum(
            0.025, E0=E0, dE_max=D, tau_s=T, sig_det=sig, tau_val=tau,
            energy_low=960.0, energy_high=1060.0, kernel_sigmas=8.0
        )
        E_base, y_base = spectra[0.025]
        support_l1 = float(np.sum(np.abs(
            np.interp(E_wide, E_base, y_base, left=0.0, right=0.0) - y_wide
        )) * 0.025)
        test_results[f"tau_{tau}_ps"] = {
            "exact_centroid_shift_keV": exact_shift,
            "grid_refinements": runs,
            "L1_diff_h05_to_h025": L1_12,
            "L1_diff_h025_to_h0125": L1_23,
            "L1_convergence_ratio": L1_12 / L1_23 if L1_23 > 0 else None,
            "support_widening": {
                "h_keV": 0.025,
                "energy_bounds_keV": [960.0, 1060.0],
                "kernel_sigmas": 8.0,
                "area": area_wide,
                "centroid_keV": centroid_wide,
                "L1_difference": support_l1
            },
            "checks": {
                "area_without_density_renormalization": all(
                    abs(run["area"] - 1.0) < 3e-9 for run in runs
                ),
                "centroid_errors_decrease": all(
                    abs(runs[j + 1]["error_vs_exact_keV"]) < abs(runs[j]["error_vs_exact_keV"])
                    for j in range(2)
                ),
                "support_difference_below_3e_9": support_l1 < 3e-9,
                "finite_nonnegative_spectra": all(
                    np.isfinite(y).all() and np.min(y) >= 0 for _, y in spectra.values()
                )
            }
        }

    out_dir = 'outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G98'
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'dsam_convergence_test.json'), 'w') as f:
        json.dump(test_results, f, indent=2)
    if not all(all(row["checks"].values()) for row in test_results.values()):
        raise AssertionError("A finite DSAM numerical control failed; inspect the JSON.")
    print("DSAM convergence tests saved to dsam_convergence_test.json.")

def main():
    img_dir = 'raw/writing/gpt/A130/these_2023_template/these_template/Img'
    os.makedirs(img_dir, exist_ok=True)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.8), dpi=300)

    # Panel (a): RDDS decay curves
    # v approx 6.0 um/ps corresponds to beta approx 0.02 c (0.02 * 299.8 um/ps approx 6.0 um/ps)
    v = 6.0  # um / ps
    x = np.linspace(0, 150, 300)  # um

    for tau, col, ls in [(2.0, '#1f77b4', '-'), (5.0, '#2ca02c', '--'), (15.0, '#d62728', '-.')]:
        Ru = np.exp(-x / (v * tau))
        Rs = 1.0 - Ru
        ax1.plot(x, Ru, color=col, ls=ls, lw=1.8, label=f'$\\tau = {tau:.0f}$ ps ($R_u$)')
        ax1.plot(x, Rs, color=col, ls=':', lw=1.4, alpha=0.8, label=f'$\\tau = {tau:.0f}$ ps ($R_s$)' if tau == 2.0 else None)

    ax1.set_xlabel(r'Target-to-Stopper Distance $x$ ($\mu\mathrm{m}$)', fontsize=10)
    ax1.set_ylabel(r'Normalized Intensity Fraction', fontsize=10)
    ax1.set_title(r'(a) RDDS Decay Curves ($v \approx 6\,\mu\mathrm{m/ps}$, $\beta \approx 0.02$ Toy)', fontsize=10.5)
    ax1.set_xlim(0, 150)
    ax1.set_ylim(-0.02, 1.05)
    ax1.grid(True, ls=':', color='gray', alpha=0.5)
    ax1.legend(loc='center right', fontsize=8.5)

    # Panel (b): DSAM line shape with conservative bin-integrated CDF
    h = 0.025  # keV fine step for publication rendering
    for tau_val, col, label in [(0.1, '#1f77b4', r'$\tau \ll \tau_{\mathrm{stop}}$ ($0.1$ ps)'),
                                (0.8, '#2ca02c', r'$\tau \approx \tau_{\mathrm{stop}}$ ($0.8$ ps)'),
                                (5.0, '#d62728', r'$\tau \gg \tau_{\mathrm{stop}}$ ($5.0$ ps)')]:
        E_c, spec, area, centroid = compute_dsam_spectrum(h, tau_val=tau_val)
        # Display normalization: scale maximum height to 1.0 solely for visual comparison
        ax2.plot(E_c, spec / np.max(spec), color=col, lw=1.8, label=label)

    ax2.set_xlabel(r'Observed Energy $E_{\mathrm{obs}}$ (keV)', fontsize=10)
    ax2.set_ylabel(r'Peak-Scaled Intensity (Display Normalized)', fontsize=10)
    ax2.set_title(r'(b) DSAM Line Shape vs Stopping Time ($\tau_{\mathrm{stop}} = 0.8$ ps Toy)', fontsize=10.5)
    ax2.set_xlim(992, 1028)
    ax2.set_ylim(-0.02, 1.1)
    ax2.grid(True, ls=':', color='gray', alpha=0.5)
    ax2.legend(loc='upper right', fontsize=8.5)

    fig.tight_layout()

    svg_path = os.path.join(img_dir, 'lifetime-response-rdds-dsam.svg')
    pdf_path = os.path.join(img_dir, 'lifetime-response-rdds-dsam.pdf')

    plt.savefig(svg_path)
    plt.savefig(pdf_path)
    plt.close(fig)

    print(f"Generated {svg_path}")
    print(f"Generated {pdf_path}")
    run_convergence_tests()

if __name__ == '__main__':
    main()
