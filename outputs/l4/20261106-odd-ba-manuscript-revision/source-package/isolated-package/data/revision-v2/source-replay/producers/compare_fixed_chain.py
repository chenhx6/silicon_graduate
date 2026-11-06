"""Source-frozen135/137Ba energy replay using the existing unchanged kernel.

No electromagnetic operator is constructed. No alternate parameters are tried.
"""

import os
import sys

sys.dont_write_bytecode = True
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
            "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[key] = "1"
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

import csv
import ctypes
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
CONTRACT = OUT / "comparison-contract.json"
CONTRACT_SHA = "cc3b8cc2f677635593f739cd450fb1c5fdcdac54dcdbe0a94075391a63b9f940"
SOURCE = OUT / "source-points-frozen.json"
SOURCE_SHA = "bc4dbed2c29f65ae8f9546cd146005efa6dbb64eb08ef23781ede6f907b91d22"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verify(c):
    assert sha(CONTRACT) == CONTRACT_SHA
    assert sha(SOURCE) == SOURCE_SHA
    for item in c["read_only_files"]:
        assert sha(ROOT / item["path"]) == item["sha256"], item["path"]


def write_new(name, data):
    with (OUT / name).open("x", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, allow_nan=False)
        f.write("\n")


def blas_threads():
    libraries = sorted({line.split()[-1] for line in Path("/proc/self/maps").read_text().splitlines()
                        if "openblas" in line.lower() and ".so" in line and line.split()[-1].startswith("/")})
    counts = []
    for path in libraries:
        library = ctypes.CDLL(path)
        for symbol in ("scipy_openblas_get_num_threads64_", "scipy_openblas_get_num_threads",
                       "openblas_get_num_threads64_", "openblas_get_num_threads"):
            try:
                function = getattr(library, symbol)
            except AttributeError:
                continue
            function.argtypes = []
            function.restype = ctypes.c_int
            count = int(function())
            assert count == 1
            counts.append({"library": path, "symbol": symbol, "threads": count})
            break
        else:
            raise RuntimeError(f"BLAS thread count unverified: {path}")
    assert counts
    return counts


def main():
    started = datetime.now(timezone.utc).isoformat()
    clock = time.perf_counter()
    c = json.loads(CONTRACT.read_text())
    verify(c)  # Verify before any kernel import or solve.
    source = json.loads(SOURCE.read_text())
    assert source["frozen_at_utc"] < c["frozen_at_utc"] < started
    sys.path.insert(0, str(ROOT / "system/scripts/analysis"))
    import numpy as np
    import scipy
    from single_j_ibfm import IBFMKernel, IBFMParameters

    threads = blas_threads()
    points = source["original_figure"]["points"]
    rows, models, summaries = [], [], []
    for case in c["cases"]:
        p = IBFMParameters(**case["parameters"])
        kernel = IBFMKernel(p)
        s = kernel.solve(two_M=c["numerics"]["two_M"])

        def lowest(two_J):
            indices = s.indices_for_J(two_J)
            indices = indices[np.argsort(s.energies[indices], kind="stable")]
            assert len(indices)
            if len(indices) > 1:
                assert s.energies[indices[1]] - s.energies[indices[0]] > 1e-10
            return int(indices[0])

        ref = lowest(11)
        minimum = int(np.argmin(s.energies))
        h = hashlib.sha256(str(kernel.hamiltonian.shape).encode())
        for array in (kernel.hamiltonian.data, kernel.hamiltonian.indices, kernel.hamiltonian.indptr):
            h.update(np.ascontiguousarray(array).tobytes())
        models.append({
            "odd_A": case["odd_A"], "core_A": case["core_A"], "parameters": case["parameters"],
            "derived_gamma_jj": p.gamma_jj, "derived_beta_jj": p.beta_jj,
            "derived_exchange_coefficient": p.exchange_coefficient,
            "dimension_full": kernel.dimension, "dimension_M_half": s.basis.dimension,
            "Hamiltonian_csr_sha256": h.hexdigest(),
            "reference_index": ref, "reference_energy_MeV_arbitrary_constant": float(s.energies[ref]),
            "reference_vector_sha256": hashlib.sha256(np.ascontiguousarray(s.vectors[:, ref]).tobytes()).hexdigest(),
            "global_minimum_two_J": int(s.two_J[minimum]),
            "reference_is_global_negative_parity_minimum": minimum == ref,
            "solver_diagnostics": dict(s.diagnostics),
        })
        for point in points:
            if point["odd_A"] != case["odd_A"]:
                continue
            index = lowest(point["two_J"])
            model_keV = float(1000 * (s.energies[index] - s.energies[ref]))
            delta = model_keV - point["plot_grid_energy_keV"]
            tolerance = c["numerics"]["source_extraction_tolerance_keV"]
            rows.append({
                "odd_A": case["odd_A"], "state": point["source_legend_label"],
                "two_J": point["two_J"], "kernel_ordinal_zero_based": 0,
                "kernel_spectrum_index": index, "source_ordinal_printed": False,
                "source_locator": f"arXiv-v2 p7 Fig5(c), N={point['neutron_N']}, vector path{point['path_index']}",
                "source_plot_keV": point["plot_grid_energy_keV"],
                "source_recovered_keV": point["recovered_energy_keV"],
                "kernel_relative_keV": model_keV, "kernel_minus_source_plot_keV": delta,
                "inside_nearest_rounding_sensitivity": abs(delta) <= 0.5 + tolerance,
                "inside_one_grid_sensitivity": abs(delta) <= 1.0 + tolerance,
                "is_fixed_reference": point["two_J"] == 11,
            })
        selected = [r for r in rows if r["odd_A"] == case["odd_A"] and not r["is_fixed_reference"]]
        summaries.append({
            "odd_A": case["odd_A"], "nonreference_point_count": len(selected),
            "RMS_kernel_minus_source_keV": math.sqrt(sum(r["kernel_minus_source_plot_keV"]**2 for r in selected) / len(selected)),
            "max_abs_kernel_minus_source_keV": max(abs(r["kernel_minus_source_plot_keV"]) for r in selected),
            "inside_nearest_rounding_sensitivity_count": sum(r["inside_nearest_rounding_sensitivity"] for r in selected),
            "inside_one_grid_sensitivity_count": sum(r["inside_one_grid_sensitivity"] for r in selected),
            "source_sorted_shown_two_J": [r["two_J"] for r in sorted(
                [r for r in rows if r["odd_A"] == case["odd_A"]], key=lambda r: r["source_plot_keV"])],
            "kernel_sorted_shown_two_J": [r["two_J"] for r in sorted(
                [r for r in rows if r["odd_A"] == case["odd_A"]], key=lambda r: r["kernel_relative_keV"])],
        })
    verify(c)
    result = {
        "schema": "nomura-source-fixed-chain-energy-comparison/1",
        "source_json_sha256": SOURCE_SHA, "comparison_contract_sha256": CONTRACT_SHA,
        "energy_reference": c["energy_reference"], "models": models, "rows": rows,
        "summaries": summaries, "no_parameter_variants_or_fit": True,
        "no_EM_calculations": True, "no_nearest_energy_state_reassignment": True,
        "source_replay_is_not_experimental_validation": True,
    }
    write_new("comparison.json", result)
    with (OUT / "comparison.csv").open("x", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    write_new("run.json", {
        "status": "completed_fixed_comparison", "started_at_utc": started,
        "finished_at_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": time.perf_counter() - clock,
        "source_json_sha256": SOURCE_SHA, "comparison_contract_sha256": CONTRACT_SHA,
        "driver_sha256": sha(__file__), "comparison_json_sha256": sha(OUT / "comparison.json"),
        "comparison_csv_sha256": sha(OUT / "comparison.csv"),
        "all_locked_inputs_unchanged": True,
        "source_frozen_before_contract_and_run": True,
        "native_BLAS": threads, "python": sys.version.split()[0],
        "numpy": np.__version__, "scipy": scipy.__version__,
        "no_commit": True,
    })
    for row in rows:
        print(row["odd_A"], row["state"], "source", row["source_plot_keV"],
              "kernel", f"{row['kernel_relative_keV']:.6f}",
              "delta", f"{row['kernel_minus_source_plot_keV']:+.6f}")
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()
