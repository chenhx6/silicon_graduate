from dataclasses import replace
import json

from multipolepdm.cli import forward_calibration
from multipolepdm.contracts import Transition
from multipolepdm.io.input import example_data, job_from_dict


def test_forward_calibration_keeps_full_physical_input(tmp_path):
    job = replace(job_from_dict(example_data()), target=Transition(4, 2, ("E2",)))
    forward_calibration(job, tmp_path)
    record = json.loads((tmp_path / "forward_calibration.json").read_text())
    assert record["input"]["target"]["spin_final"] == 2
    assert record["input"]["geometry"]["polarization_group"]["directions"][0]["theta_deg"] == 90
    assert record["observations_used_for_inference"] is False
    assert record["undefined_points"] == 0
