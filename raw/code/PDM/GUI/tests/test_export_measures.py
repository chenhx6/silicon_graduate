import hashlib
import json
from dataclasses import asdict, replace

import numpy as np
import pytest
from multipolepdm.contracts import GridSpec, OutputSpec
from multipolepdm.io.export import export_result, load_snapshot
from multipolepdm.io.input import example_data, job_from_dict
from multipolepdm.jobs.manager import freeze_arrays
from multipolepdm.jobs.workers import compute_job
from scipy.integrate import trapezoid


def test_exported_native_node_probability_sums_to_one(tmp_path):
    job = replace(
        job_from_dict(example_data()),
        grid=GridSpec(xi_points=61, sigma_points=31),
        output=OutputSpec(str(tmp_path), True),
    )
    result, summary = compute_job(job)
    export_result(result, summary, tmp_path)
    table = np.genfromtxt(tmp_path / "parameter_density.csv", delimiter=",", names=True)
    assert table["parameter_node_probability"].sum() == pytest.approx(1, abs=1e-11)
    assert (tmp_path / "observation_density.csv").exists()
    with np.load(tmp_path / "density.npz") as data:
        assert data["observed_pdf"].shape == (257, 257)


def test_snapshot_preserves_angle_and_reported_statistics_and_reopens_v1(tmp_path):
    job = replace(
        job_from_dict(example_data()), grid=GridSpec(xi_points=61, sigma_points=31)
    )
    result, summary = compute_job(job)
    assert export_result(result, summary, tmp_path) == "saved"
    manifest_path = tmp_path / "manifest.json"
    summary_path = tmp_path / "summary.json"
    manifest = json.loads(manifest_path.read_text())
    payload = json.loads(summary_path.read_text())
    assert manifest["schema"] == "multipolepdm-result-v3"
    assert manifest["summary_interpretation"]["default_interval_mass"] == 0.68
    assert manifest["invalid_response_nodes"] == int(np.count_nonzero(~result.response.valid))
    assert "delta" not in payload
    assert payload["delta_pdf"]["coordinate_name"] == "delta"
    assert payload["delta_pdf"]["statistics_evaluated_on_this_pdf"] is False
    assert not any(key in payload["delta_pdf"] for key in ("mode", "mean", "intervals"))
    transformed = payload["tan_angle_statistics"]
    assert transformed["evaluation_coordinate"] == "arctan_delta"
    assert "coordinate" not in transformed and "density" not in transformed and "std" not in transformed
    assert transformed["hdi_threshold_coordinate"] == "arctan_delta"
    assert transformed["statistic_labels"]["tan_mode"] == "tan{mode[arctan(δ)]}"
    assert transformed["statistic_labels"]["tan_mean"] == "tan{mean[arctan(δ)]}"
    assert transformed["intervals"][0]["statistic_labels"]["tan_hdi_segments"] == "tan{HDI68%[arctan(δ)]}"
    assert payload["arctan_delta"]["intervals"][0]["hdi_segments"][0]["mode_ranges"]
    for name, segment_key in (("arctan_delta", "hdi_segments"),
                              ("sigma_over_i", "hdi_segments"),
                              ("tan_angle_statistics", "tan_hdi_segments")):
        interval = payload[name]["intervals"][0]
        components = interval[segment_key]
        total = sum(part["mass"] for part in components)
        assert total == pytest.approx(.68, abs=2e-12)
        assert sum(part["mass_fraction"] for part in components) == pytest.approx(1.)
        for part in components:
            assert part["mass_fraction"] == pytest.approx(part["mass"] / total)
    assert (tmp_path / "marginal_arctan_delta.csv").is_file()

    def assert_marginals(reopened):
        for name in ("arctan_delta", "delta", "sigma_over_i"):
            expected = getattr(summary, name)
            actual = getattr(reopened, name)
            np.testing.assert_array_equal(actual.coordinate, expected.coordinate)
            np.testing.assert_array_equal(actual.density, expected.density)
            assert actual.intervals == expected.intervals
            assert actual.mean == expected.mean
            assert actual.std == expected.std
            assert actual.mean_bounds == expected.mean_bounds
            assert actual.mean_bound_flags == expected.mean_bound_flags

    _, reopened = load_snapshot(tmp_path)
    assert_marginals(reopened)

    legacy_payload = json.loads(json.dumps(asdict(summary), default=lambda value: value.tolist()))
    legacy_json = json.dumps(legacy_payload)
    manifest["schema"] = "multipolepdm-result-v2"
    manifest_path.write_text(json.dumps(manifest))
    summary_path.write_text(legacy_json)
    manifest_bytes = manifest_path.read_bytes()
    density_hash = hashlib.sha256((tmp_path / "density.npz").read_bytes()).hexdigest()
    _, reopened = load_snapshot(tmp_path)
    assert_marginals(reopened)
    assert summary_path.read_text() == legacy_json
    assert manifest_path.read_bytes() == manifest_bytes
    assert hashlib.sha256((tmp_path / "density.npz").read_bytes()).hexdigest() == density_hash

    manifest["schema"] = "multipolepdm-result-v1"
    manifest_path.write_text(json.dumps(manifest))
    old_summary = {
        name: {key: legacy_payload[name][key] for key in ("coordinate", "density", "median", "mode", "intervals")}
        for name in ("delta", "sigma_over_i")
    }
    old_json = json.dumps(old_summary)
    summary_path.write_text(old_json)
    _, reopened = load_snapshot(tmp_path)
    assert_marginals(reopened)
    assert summary_path.read_text() == old_json


def test_exported_delta_csv_is_transformed_density_not_relabelled_angle_pdf(tmp_path):
    job = replace(job_from_dict(example_data()), grid=GridSpec(xi_points=61, sigma_points=31))
    result, summary = compute_job(job)
    export_result(result, summary, tmp_path)
    table = np.genfromtxt(tmp_path / "marginal_delta.csv", delimiter=",", names=True)
    coordinate = table["delta"]
    expected = np.interp(np.arctan(coordinate), summary.arctan_delta.coordinate, summary.arctan_delta.density)
    expected /= 1 + coordinate**2
    expected /= trapezoid(expected, coordinate)
    np.testing.assert_array_equal(coordinate, summary.delta_pdf.coordinate)
    np.testing.assert_array_equal(table["probability_density_per_delta"], summary.delta_pdf.density)
    np.testing.assert_allclose(table["probability_density_per_delta"], expected, rtol=2e-12)


def test_preview_cannot_mutate_export_snapshot():
    job = replace(
        job_from_dict(example_data()), grid=GridSpec(xi_points=61, sigma_points=31)
    )
    result, summary = compute_job(job)
    freeze_arrays(result)
    freeze_arrays(summary)
    with pytest.raises(ValueError, match="read-only"):
        result.response.xi_rad[1] = 0
    with pytest.raises(ValueError, match="read-only"):
        summary.delta.density[0] = 1
