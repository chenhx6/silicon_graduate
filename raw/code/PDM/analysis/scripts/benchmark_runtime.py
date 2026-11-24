"""Measure real computation, preview and export paths using synthetic jobs."""

from pathlib import Path
from dataclasses import replace
import argparse
import sys, json, time, tracemalloc

root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root / "GUI/src"))
parser = argparse.ArgumentParser(
    description="Instrumented calculation/render/export runtime audit."
)
parser.add_argument("--artifacts", type=Path, required=True)
args = parser.parse_args()
from multipolepdm.io.input import example_data, job_from_dict
from multipolepdm.jobs.workers import compute_job
from multipolepdm.io.export import export_result
from multipolepdm.plotting.overview import make_preview
from multipolepdm import __version__

results = []
artifacts = args.artifacts
artifacts.mkdir(exist_ok=True)
for mode in ("P_ADO", "P_DCO", "PDCO"):
    job = job_from_dict(example_data(mode))
    times = {}
    start = time.perf_counter()
    result, summary = compute_job(job)
    times["compute_seconds"] = time.perf_counter() - start
    start = time.perf_counter()
    preview = make_preview(result, summary)
    times["figure_construct_seconds"] = time.perf_counter() - start
    start = time.perf_counter()
    preview.figure.canvas.draw()
    times["figure_render_seconds"] = time.perf_counter() - start
    start = time.perf_counter()
    export_result(result, summary, artifacts / mode / "compact")
    times["compact_export_seconds"] = time.perf_counter() - start
    preview.figure.savefig(artifacts / f"{mode}.png", dpi=140)
    start = time.perf_counter()
    full = replace(result, job=replace(job, output=replace(job.output, full_csv=True)))
    export_result(full, summary, artifacts / mode / "csv")
    times["full_csv_export_seconds"] = time.perf_counter() - start
    tracemalloc.start()
    memory_result, memory_summary = compute_job(job)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    del memory_result, memory_summary
    results.append(
        dict(
            mode=mode,
            grid_shape=list(result.parameter_density.shape),
            timings=times,
            compute_tracemalloc_peak_bytes=peak,
            compact_bytes=sum(
                p.stat().st_size
                for p in (artifacts / mode / "compact").iterdir()
                if p.is_file()
            ),
            full_csv_bytes=sum(
                p.stat().st_size
                for p in (artifacts / mode / "csv").iterdir()
                if p.is_file()
            ),
        )
    )
    print(json.dumps(results[-1]), flush=True)
out = root / "analysis/benchmarks/runtime_v0_1_1"
out.mkdir(exist_ok=True)
(out / "results.json").write_text(
    json.dumps(
        dict(
            version=__version__,
            scope="One timing run per default synthetic job, without allocation tracing; memory is measured in a separate compute replay with tracemalloc (not total process RSS). Concurrent host workload and warm caches may affect timings; not universal performance.",
            results=results,
        ),
        indent=2,
    )
    + "\n"
)
