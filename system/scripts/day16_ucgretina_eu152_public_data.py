#!/usr/bin/env python3
"""Inspect actual public Eu152 source/background histograms without MC fitting.

The high-energy ratios are declared conditional background-only statistics;
they do not reproduce the supplied MC-template fit, polarization, or Q.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import ROOT


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def key_inventory(directory, prefix: str = "") -> list[dict]:
    result = []
    for key in directory.GetListOfKeys():
        path = prefix+key.GetName()
        cls = key.GetClassName()
        result.append({"path": path, "class": cls, "cycle": int(key.GetCycle()),
                       "compressed_bytes": int(key.GetNbytes())})
        if cls in ["TDirectory", "TDirectoryFile"]:
            result.extend(key_inventory(directory.Get(key.GetName()), path+"/"))
    return result


def hist_values(hist) -> dict:
    n = hist.GetNbinsX()
    values = [float(hist.GetBinContent(i)) for i in range(1, n+1)]
    error2 = [float(hist.GetBinError(i))**2 for i in range(1, n+1)]
    return {"class": hist.ClassName(), "title": hist.GetTitle(), "bins": n,
            "xmin": float(hist.GetXaxis().GetXmin()), "xmax": float(hist.GetXaxis().GetXmax()),
            "width_first": float(hist.GetBinWidth(1)), "entries": float(hist.GetEntries()),
            "integral_normal_bins": math.fsum(values),
            "underflow": float(hist.GetBinContent(0)), "overflow": float(hist.GetBinContent(n+1)),
            "sumw2_N": int(hist.GetSumw2N()), "effective_entries": float(hist.GetEffectiveEntries()),
            "negative_bins": sum(v < 0 for v in values),
            "max_fractional_bin_part": max(abs(v-round(v)) for v in values),
            "max_abs_error2_minus_abs_count": max(abs(e-abs(v)) for e, v in zip(error2, values)),
            "x_title": hist.GetXaxis().GetTitle(), "y_title": hist.GetYaxis().GetTitle()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    a = parser.parse_args()
    cfg = json.loads(a.input.read_text())
    assert cfg["identity"] == "UCGRETINA-EU152-PUBLIC-CALIBRATION-DATA-01"
    ROOT.PyConfig.IgnoreCommandLineOptions = True
    ROOT.gROOT.SetBatch(True)
    files, spectra = [], []
    for index, spec in enumerate(cfg["objects"]):
        path = Path(spec["path"])
        assert sha(path) == spec["sha256"] and path.read_bytes()[:4] == b"root"
        handle = ROOT.TFile.Open(str(path), "READ")
        assert handle and not handle.IsZombie()
        keys = key_inventory(handle)
        histogram = handle.Get(cfg["target_object"].split(",")[0])
        assert histogram and histogram.InheritsFrom("TH1") and histogram.GetDimension() == 1
        clone = histogram.Clone("run_owned_read_"+str(index))
        clone.SetDirectory(0)
        original = hist_values(clone)
        clone.Rebin(4)
        rebinned = hist_values(clone)
        assert math.isclose(original["integral_normal_bins"], rebinned["integral_normal_bins"], rel_tol=0, abs_tol=1e-6)
        files.append({"path": str(path), "sha256": spec["sha256"], "keys": keys,
            "original_egam": original, "rebin4_egam": rebinned,
            "TTree_keys": [v["path"] for v in keys if v["class"] in ["TTree", "TNtuple"]],
            "polarimetry_named_keys": [v["path"] for v in keys if any(s in v["path"].lower() for s in ["polar", "compton", "xi", "theta", "phi"])],
            "file_creation_metadata": str(handle.GetCreationDate().AsSQLString())})
        spectra.append(clone)
        handle.Close()
    background, source = spectra
    assert background.GetNbinsX() == source.GetNbinsX()
    assert all(abs(background.GetBinLowEdge(i)-source.GetBinLowEdge(i)) < 1e-12
               for i in range(1, source.GetNbinsX()+2))
    windows = []
    for low, high in cfg["preselected_windows_keV"]:
        ids = [i for i in range(1, source.GetNbinsX()+1) if low <= source.GetBinCenter(i) <= high]
        y = math.fsum(float(source.GetBinContent(i)) for i in ids)
        b = math.fsum(float(background.GetBinContent(i)) for i in ids)
        assert b > 0 and y > 0
        alpha = y/b
        sigma = alpha*math.sqrt(1/y+1/b)
        windows.append({"bounds_keV": [low, high], "selected_bins": len(ids),
            "first_bin_center": source.GetBinCenter(ids[0]), "last_bin_center": source.GetBinCenter(ids[-1]),
            "source_sum": y, "background_sum": b, "conditional_alpha": alpha,
            "conditional_sigma_finite_independent_background": sigma,
            "conditional_sigma_if_background_treated_exact": math.sqrt(y)/b,
            "published_macro_fixed_p0": .456734,
            "difference_not_a_z_test": alpha-.456734,
            "full_template_fit_reproduced": False})
    result = {"identity": cfg["identity"], "input_sha256": sha(a.input),
        "script_sha256": sha(Path(__file__)), "ROOT_version": ROOT.gROOT.GetVersion(),
        "files": files, "windows": windows,
        "original_data_files_modified": False, "matching_Morse_or_L26_response": False,
        "MC_simulation_histogram_available_in_this_input": False,
        "experimental_polarization_or_Q_reestimated": False,
        "Poisson_independence_sourcefree_window_are_assumptions": True}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"ROOT_version": result["ROOT_version"],
                     "file_summary": [{k:v for k,v in f.items() if k != "keys"} for f in files],
                     "key_counts": [len(f["keys"]) for f in files], "windows": windows}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
