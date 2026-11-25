"""JSON-only input, shared by the GUI, CLI and notebooks."""

import json
from dataclasses import asdict, replace
from importlib import resources
from pathlib import Path

from multipolepdm.contracts import (
    Geometry,
    GridSpec,
    JobRequest,
    Measurement,
    OutputSpec,
    Transition,
)
from multipolepdm.grid import recommend_grid
from multipolepdm.physics.detectors import DetectorDirection, DetectorGroup


def input_help(mode="P_ADO"):
    """Return fresh, noncomputational documentation for a saved input."""
    return {
        "format": "严格 JSON：双引号，无注释、尾逗号、NaN 或 Infinity。仅任务顶层及批量根层允许 _help 对象；其内容不参与计算。其它未知字段仍报错。",
        "mode": {
            "selected": mode,
            "P_ADO": "目标单线 P 与 R_ADO，无方向门。",
            "P_DCO": "目标单线 P（门无方向选择）与 R_DCO。",
            "PDCO": "方向选门条件下的目标 P 与 R_DCO；需另填偏振门组。",
        },
        "target": "spin_initial/spin_final 为初末态自旋（整数或半整数）；multipoles 按顺序填 [M1,E2] 或单一多极性。目标 delta 待反演，不填写真值。label 中的合成注入仅是说明，计算不读取标签。纯目标用 CLI --forward，不反演混合比。",
        "gate_and_path": "DCO 模式须填 gate 的初末态自旋、多极性及已知 delta；纯 E2 门写 multipoles:[E2], delta:0。target_first:true 表示目标在上游、门在下游；false 表示门在上游、目标在下游。intermediates 按实际衰变顺序列出未观测中间跃迁及已知 delta，所有端点自旋须衔接。P_ADO 不填 gate/intermediates。",
        "observations": "P 和 R_ADO 或 R_DCO 各填 value、err_minus、err_plus。P 是校正后的偏振度小数（-20% 写 -0.20）。两个误差均为正幅度，左端 value-err_minus，右端 value+err_plus；可不对称。P 与 R 的误差在模型中视为独立。",
        "geometry": {
            "groups": "ratio_group_a 是 A 组，ratio_group_b 是 B 组。R_ADO=W(A)/W(B)；R_DCO=W(目标A,门B)/W(目标B,门A)。polarization_group 是目标偏振组；PDCO 的 polarization_gate_group 独立指定方向门。",
            "directions": "各组 directions 为探测器行：theta_deg 是相对取向轴的极角（度，必填），phi_deg 是方位角（度，可省略，存储缺省0），weight 是有效非负权重（可省略，缺省1），每组总权重须正。",
            "normalization": "mean（缺省）按组内总权重归一；sum 直接使用原权重。先合成强度，再算比值或偏振，不平均角度或各探测器比值。",
            "azimuth": "推荐显式探测器组且 select_azimuth:false：无 phi 输入，在各 theta 环上平均强度，仍保留极角选门。指定方位时手动设 select_azimuth:true 并填写 phi_deg；PDCO 可用 ratio_azimuth_average 与 polarization_gate_azimuth_average 分别控制比值及偏振的环平均。旧标量 geometry 仍按旧接口语义读取。",
        },
        "grid": {
            "angle": "xi=arctan(delta)。JSON 的 xi_min_rad、xi_max_rad、xi_step_rad 始终用 rad；默认范围为 ±89度，即 ±1.5533430342749532 rad，严格在 ±pi/2 内。xi_input_unit 仅记录 GUI 显示单位，不转换 JSON 数字。",
            "width": "JSON 的 sigma_min、sigma_max、sigma_step 始终是内部 sigma。sigma_input_unit 仅记录显示单位。GUI 中用 sigma/I 时，范围与步长都乘共同源态自旋 I_ref 后存储；例如 I_ref=5 时 0.30 sigma/I 对应 sigma=1.5，步长0.005对应0.025。",
            "reference_spin": "P_ADO 或 target_first:true 时 I_ref=目标初态自旋；上游门 target_first:false 时 I_ref=门初态自旋，P 与 R 共用该源布居。源 sigma 不等于下游态宽度，不能改按下游目标自旋换算。I_ref=0 仅用于正向响应。",
            "recommended_manual": "推荐从 Load example 或 CLI 导出示例开始；省略 grid 或写空对象时按共同源自旋使用共享默认。sigma 默认下限为整数源自旋0.15、半整数0.20，上限为源自旋，步长0.005*I_ref。非空显式网格保留原输入，可手动改范围/步长并细化检查稳定性；末端点保留，最后一格可较短。旧 xi_points/sigma_points 输入仍兼容。",
        },
        "output": "directory 为结果目录，full_csv 控制完整网格 CSV。GUI 或 CLI --output-dir 可覆盖输出路径。",
    }


def _without_help(data):
    if not isinstance(data, dict):
        raise ValueError("Input must be a JSON object.")  # noqa: TRY004 (JSON schema error)
    if "_help" in data and not isinstance(data["_help"], dict):
        raise ValueError("_help must be a JSON object.")
    return {key: value for key, value in data.items() if key != "_help"}


def _reject_constant(value):
    raise ValueError(f"Invalid JSON numeric constant: {value}")


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON field: {key}")
        result[key] = value
    return result


def _transition(data):
    return Transition(**data)


def _geometry(data):
    values = dict(data)
    for name in (
        "ratio_group_a",
        "ratio_group_b",
        "polarization_group",
        "polarization_gate_group",
    ):
        group = values.get(name)
        if group is not None:
            if set(group) - {"directions", "normalization"}:
                raise ValueError(f"Unknown detector group fields in {name}.")
            values[name] = DetectorGroup(
                tuple(DetectorDirection(**row) for row in group["directions"]),
                normalization=group.get("normalization", "mean"),
            )
    return Geometry(**values)


def job_from_dict(data):
    data = _without_help(data)
    allowed = {
        "mode",
        "label",
        "target",
        "gate",
        "target_first",
        "intermediates",
        "observations",
        "geometry",
        "grid",
        "output",
    }
    unknown = set(data) - allowed
    if unknown:
        raise ValueError(f"Unknown input fields: {', '.join(sorted(unknown))}")
    mode = data["mode"]
    ratio = "R_ADO" if mode == "P_ADO" else "R_DCO"
    observations = data["observations"]
    if set(observations) != {"P", ratio}:
        raise ValueError(f"{mode} requires observations P and {ratio}.")
    job = JobRequest(
        mode=mode,
        target=_transition(data["target"]),
        polarization=Measurement(**observations["P"]),
        angular_ratio=Measurement(**observations[ratio]),
        label=str(data.get("label", "Transition")),
        gate=_transition(data["gate"]) if data.get("gate") is not None else None,
        target_first=data.get("target_first", True),
        intermediates=tuple(_transition(t) for t in data.get("intermediates", [])),
        geometry=_geometry(data.get("geometry", {})),
        grid=GridSpec(**data.get("grid", {})),
        output=OutputSpec(**data.get("output", {})),
    )
    if not data.get("grid") and job.reference_spin > 0:
        job = replace(job, grid=recommend_grid(job.reference_spin))
    return job


def job_to_dict(job, *, include_help=False):
    data = {
        "mode": job.mode,
        "label": job.label,
        "target": asdict(job.target),
        "observations": {
            "P": asdict(job.polarization),
            job.ratio_name: asdict(job.angular_ratio),
        },
        "geometry": asdict(job.geometry),
        "grid": asdict(job.grid),
        "output": asdict(job.output),
    }
    data["target"].pop("delta")
    if job.mode != "P_ADO":
        data.update(
            gate=asdict(job.gate),
            target_first=job.target_first,
            intermediates=[asdict(t) for t in job.intermediates],
        )
    if include_help:
        data = {"_help": input_help(job.mode), **data}
    return data


def load_jobs(path):
    data = json.loads(
        Path(path).read_text(encoding="utf-8"),
        parse_constant=_reject_constant,
        object_pairs_hook=_unique_object,
    )
    data = _without_help(data)
    if "jobs" in data:
        unknown = set(data) - {"jobs"}
        if unknown:
            raise ValueError(f"Unknown batch fields: {', '.join(sorted(unknown))}")
        records = data["jobs"]
        if not isinstance(records, list) or not records:
            raise ValueError("Batch jobs must be a nonempty array.")
    else:
        records = [data]
    return tuple(job_from_dict(record) for record in records)


def save_input(job, path):
    Path(path).write_text(
        json.dumps(
            job_to_dict(job, include_help=True),
            indent=2,
            ensure_ascii=False,
            allow_nan=False,
        )
        + "\n",
        encoding="utf-8",
    )


def example_data(mode="P_ADO"):
    name = {
        "P_ADO": "example.json",
        "P_DCO": "example_P_DCO.json",
        "PDCO": "example_PDCO.json",
        "batch": "example_batch.json",
    }[mode]
    return json.loads(
        resources.files("multipolepdm")
        .joinpath("examples", name)
        .read_text(encoding="utf-8")
    )


def export_example(mode, path):
    Path(path).write_text(
        json.dumps(example_data(mode), indent=2, ensure_ascii=False, allow_nan=False)
        + "\n",
        encoding="utf-8",
    )
