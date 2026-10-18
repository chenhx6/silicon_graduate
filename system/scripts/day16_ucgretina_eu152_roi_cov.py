#!/usr/bin/env python3
"""Reproduce frozen gross-ROI counts and conditional shared-alpha covariance."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import ROOT


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--audit", type=Path, required=True)
    p.add_argument("--freeze", type=Path, required=True)
    p.add_argument("--before", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    freeze = json.loads(a.freeze.read_text())
    assert sha(a.before) == freeze["sha256"]
    cfg = json.loads(a.audit.read_text())
    assert cfg["identity"] == "UCGRETINA-EU152-PUBLIC-CALIBRATION-DATA-01"
    ROOT.gROOT.SetBatch(True)
    spectra = []
    for i, obj in enumerate(cfg["files"]):
        assert sha(Path(obj["path"])) == obj["sha256"]
        f = ROOT.TFile.Open(obj["path"], "READ")
        h = f.Get("egam").Clone("roi_owned_"+str(i))
        h.SetDirectory(0)
        h.Rebin(4)
        spectra.append(h)
        f.Close()
    background, source = spectra
    rois = []
    for lo, hi in [(120, 128), (1404, 1412)]:
        ids = [i for i in range(1, source.GetNbinsX()+1) if lo <= source.GetBinCenter(i) <= hi]
        rois.append({"bounds_keV": [lo, hi], "bincenters_keV": [source.GetBinCenter(i) for i in ids],
                     "source_sum": sum(source.GetBinContent(i) for i in ids),
                     "background_sum": sum(background.GetBinContent(i) for i in ids)})
    y = np.array([x["source_sum"] for x in rois])
    b = np.array([x["background_sum"] for x in rois])
    models = []
    for row in cfg["windows"]:
        alpha = row["conditional_alpha"]
        variance = row["conditional_sigma_finite_independent_background"]**2
        diagonal = y+alpha**2*b
        cov = np.diag(diagonal)+variance*np.outer(b, b)
        assert np.linalg.eigvalsh(cov).min() > 0
        models.append({"normalization_window_keV": row["bounds_keV"], "alpha": alpha,
                       "conditional_var_alpha": variance, "gross_ROI_net_counts_conditional": (y-alpha*b).tolist(),
                       "conditional_covariance_counts2": cov.tolist(), "conditional_fixed_alpha_diagonal": diagonal.tolist(),
                       "conditional_correlation": (cov/np.sqrt(np.outer(np.diag(cov), np.diag(cov)))).tolist(),
                       "minimum_Cov_eigenvalue": float(np.linalg.eigvalsh(cov).min())})
    result = {"ROI_input_contract_sha256": sha(a.before), "script_sha256": sha(Path(__file__)),
              "actual_ROI_counts": rois, "normalization_covariance_models": models,
              "grossROI_not_fitted_peak_area": True,
              "Poisson_independence_and_sourcefree_highwindow_are_assumptions": True,
              "eventCov_or_Q_or_response_recovered": False, "original_ROOT_files_modified": False}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k != "normalization_covariance_models"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
