from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re


ROOT = Path("/workspace/wiki")
OUT = ROOT / "outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G82"
SECTION = ROOT / "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-2-6.tex"
APPENDIX = ROOT / "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Appendices/AppendixC.tex"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def artifact(path):
    return {
        "path": str(path.relative_to(ROOT)),
        "sha256": sha256(path),
        "size_bytes": path.stat().st_size,
    }


def save_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def field(text, name):
    return re.search(r"^" + re.escape(name) + r":\s*(.*)$", text, re.M).group(1).strip('"')


def source_record(source_id, locator, actual_pages, scope):
    path = ROOT / "knowledge/sources" / (source_id + ".md")
    text = path.read_text()
    raw_path = ROOT / field(text, "raw_file")
    assert sha256(raw_path) == field(text, "raw_sha256"), source_id
    record = {
        "source_id": source_id,
        "source_page": artifact(path),
        "raw_file": artifact(raw_path),
        "archive_required": True,
        "locator": locator,
        "actual_read_pages": actual_pages,
        "actual_read_scope": scope,
        "evidence_layer": "published theoretical definitions/model, not new experimental evidence",
    }
    if raw_path.suffix == ".json":
        manifest = json.loads(raw_path.read_text())
        pdf = next(item for item in manifest["files"] if item["path"].endswith(".pdf"))
        pdf_path = ROOT / pdf["path"]
        assert sha256(pdf_path) == pdf["sha256"]
        record["reading_carrier"] = artifact(pdf_path)
    else:
        record["reading_carrier"] = artifact(raw_path)
    return record


PR = "prochniak-rohozinski-2009-bohr-collective-hamiltonian"
HI = "hinohara-2015-nambu-goldstone-inertia-response"
PK = "petrik-kortelainen-2018-rotational-tv-inertia"
MA = "matsuzaki-2004-nuclear-inertia-and-wobbling"
KV = "kvasil-2006-dy156-yb162-crpa-wobbling"


def attribution(source, locator):
    return {"source_id": source, "locator": locator}


claims = [
    {
        "id": "2.6-C01",
        "text": "局部常正质量、稳定单坐标谐振模型满足omega²=C/B；能量间隔hbar omega及基态宽度约束不同参数组合，PES曲率本身不足以定频率。",
        "kind": "manuscript_derivation_in_declared_teaching_model",
        "equation_labels": ["local-hamiltonian", "local-frequency", "local-energy-units", "local-width"],
        "sources": [attribution(PR, "Secs.3.1,4.1; R2 crosswalk“对低能谱的缩放”及坐标质量约定")],
        "limits": ["q无量纲、B>0、C>0、小振幅、局部常质量", "电磁强度转换成q宽度另需算符映射；无实核数值"],
    },
    {
        "id": "2.6-C02",
        "text": "坐标质量随坐标变换；beta,gamma动能中的几何因子与实际绕轴惯量不能遗漏，量子势不自动等于未修正约束PES。",
        "kind": "source_kinetic_form_and_manuscript_chain_rule",
        "equation_labels": ["coordinate-mass", "mass-transform", "bohr-vibrational-mass", "bohr-rotational-mass"],
        "sources": [attribution(PR, "PDF14 Eqs.(3.5)–(3.8); Secs.4.1–4.3; R2 crosswalk")],
        "limits": ["gamma弧度；轴序与坐标约定固定", "M_gamma_gamma=beta² B_gamma_gamma；不是直接实验反演"],
    },
    {
        "id": "2.6-C03",
        "text": "IB原式用全单粒子空间求和；不重复两准粒子对表示的2因子须结合F20、时间反演相位和相干因子换算。",
        "kind": "source_original_formula_with_explicit_hbar_and_counting_conversion",
        "equation_labels": ["ib-full-sum", "ib-pair-sum"],
        "sources": [
            attribution(PR, "PDF34 Eq.(4.44); PDF30 Eqs.(4.21)–(4.25)"),
            attribution(HI, "APS PDF3 Eqs.(25),(32)–(33); PDF4 Eq.(34),(41), omitting induced fields for independent response"),
        ],
        "limits": ["零温、指定canonical BCS型偶偶时间反演参考、正准粒子能量", "未包含自洽诱导场；不将旋转IB式直接冒称完整振动质量"],
    },
    {
        "id": "2.6-C04",
        "text": "TV响应保留依赖X,Y的诱导场；实QRPA的NG归一涉及生成元实/虚分量及不同A±B分块。",
        "kind": "source_equations_with_frequency_variable_renamed_to_energy_z",
        "equation_labels": ["fam-induced-field", "ng-normalization", "tv-real-imag"],
        "sources": [attribution(HI, "APS PDF3 Eqs.(15),(18)–(23),(32)–(33)")],
        "limits": ["z=hbar omega_probe；A,B为能量单位QRPA核，非集体质量B", "只在相应可逆响应子空间使用逆；复参考、时间反演破缺用完整核", "NG条件需真实连续对称性破缺及一致残余项，非任意gamma软极限"],
    },
    {
        "id": "2.6-C05",
        "text": "按H+eta F定义S，NG静态支S(P;0)=-M；减能外场H-hj的正响应恢复空间hbar²得到TV惯量。",
        "kind": "source_static_branch_and_manuscript_units_conversion",
        "equation_labels": ["static-tv", "tv-susceptibility"],
        "sources": [
            attribution(HI, "APS PDF4 Eq.(41); PDF5 Eqs.(49)–(53), including separate finite/nonzero-frequency branch"),
            attribution(PK, "PDF4–5 Eqs.(12)–(18)"),
        ],
        "limits": ["P=j或N无量纲；外场符号、归一和单位均声明", "不以普通有限频率极限替代零频NG支；不宣称TV总大于IB"],
    },
    {
        "id": "2.6-C06",
        "text": "配对惯量dN/dlambda单位MeV^-1；本稿以总能量E写局部曲率，以正束缚能B_+=-E换号。",
        "kind": "source_response_and_manuscript_total_energy_taylor_expansion",
        "equation_labels": ["pairing-response", "pairing-curvature", "positive-binding-sign"],
        "sources": [attribution(HI, "APS PDF5 Eqs.(49)–(53); PDF8–9 Eqs.(66)–(67),Fig.4；已核2.3与T10/R2记法边界")],
        "limits": ["固定其它粒子数、平滑HFB态族、非奇异局部响应", "原文Eq.(66)的B与Fig.4 -Bexp记法差异保留，不猜作者程序错误", "连续HFB延拓不等固定N质量差分；局部规范角不等全局自伴角"],
    },
    {
        "id": "2.6-C07",
        "text": "沿带J(1),J(2)及相邻Delta I=2跃迁能有限差分描述同一有序解支，Kvasil的TV比较是同方向自洽检查。",
        "kind": "source_definitions_and_explicit_hbar_restoration",
        "equation_labels": ["band-inertias", "band-finite-difference"],
        "sources": [
            attribution(KV, "PDF4 Fig.3 caption and self-consistency paragraph"),
            attribution(MA, "PDF4–5 Eqs.(11)–(12) and Jx definition"),
        ],
        "limits": ["平滑驻定解支、正确自旋序列和对应", "带交叉、混合处不能无条件连续化；不等一般横向响应"],
    },
    {
        "id": "2.6-C08",
        "text": "Matsuzaki式横向有效惯量取物理根频率，冗余根在旋转框架为omega_n²=omega_rot²；实根不保证电磁模式识别。",
        "kind": "source_original_dispersion_relation_with_notation_mapping",
        "equation_labels": ["wobbling-response"],
        "sources": [attribution(MA, "PDF3 Eq.(8); PDF4 Eqs.(11)–(12); PDF5 Eq.(12)后Nilsson速度依赖与横向修正未给出的限制")],
        "limits": ["指定非轴cranked Nilsson+RPA，gamma!=0推导条件", "不替代全部轴对称极限；不以沿带J(2)填入横向惯量", "omega是角频率，hbar omega是激发能；未提供原程序或新计算"],
    },
    {
        "id": "2.6-C09",
        "text": "配对减弱不保证精确刚体；Kvasil的Dy/Yb带弯曲机制不同且带交叉附近使用指定配对隙处方。",
        "kind": "source_model_boundary_and_conditional_synthesis",
        "equation_labels": [],
        "sources": [
            attribution(PK, "PDF2 Inglis/Belyaev/TV背景；PDF5–7配对设置与比较；本节不引用数值"),
            attribution(KV, "PDF3 Eq.(6),PDF3–4 Figs.2–3"),
            attribution(PR, "PDF34 Eq.(4.44)的模型依赖"),
        ],
        "limits": ["作者模型解释与新实验事实分开", "不把所有QRPA、所有gamma软核视为同一极限；未声明普适阈值或增强倍率"],
    },
]

appendix_attributions = {
    "eq:app-c-static-susceptibility": ("manuscript_definition_units", [attribution(HI, "APS PDF5 Eqs.(49)–(53); R2 crosswalk")]),
    "eq:app-c-field-components": ("source_operator_expansion", [attribution(HI, "APS PDF3 Eq.(25)")]),
    "eq:app-c-independent-response": ("manuscript_algebra_omitting_induced_fields", [attribution(HI, "APS PDF3 Eqs.(32)–(33), PDF4 Eq.(41)"), attribution(PR, "PDF34 Eq.(4.44), counting boundary")]),
    "eq:app-c-qrpa-kernel": ("source_static_response", [attribution(HI, "APS PDF4 Eq.(34); PDF5 Eq.(49)")]),
    "eq:app-c-strength-convention": ("source_strength_definition", [attribution(HI, "APS PDF4 Eq.(41)")]),
    "eq:app-c-ng-local-equations": ("source_real_imaginary_components", [attribution(HI, "APS PDF3 Eqs.(20)–(21)")]),
    "eq:app-c-ng-inertia": ("source_real_imaginary_components", [attribution(HI, "APS PDF3 Eqs.(22)–(23)")]),
    "eq:app-c-matsuzaki-factorization": ("source_dispersion_factorization", [attribution(MA, "PDF4 Eq.(11); gamma!=0 condition")]),
}


def main():
    now = datetime.now(timezone.utc).isoformat()
    sources = [
        source_record(PR, "PDF14 Eqs.(3.5)–(3.8),PDF30 Eqs.(4.21)–(4.25),PDF34 Eq.(4.44)", [14, 30, 34], "Selected kinetic and cranking formula passages; PDF13–16,27–35 extracted for local navigation, not claimed fully read"),
        source_record(HI, "APS PDF3–5 Eqs.(15),(18)–(25),(32)–(34),(41),(49)–(53);PDF8–9 Eqs.(66)–(67),Fig.4", [3, 4, 5, 8, 9], "Selected normalization, static-response and total/binding-energy passages; no full paper read or numerical replay"),
        source_record(PK, "PDF2 Inglis/Belyaev background;PDF4–5 Eqs.(12)–(18)", [2, 4, 5], "Selected background and rotational NG/FAM passages; no quantitative reproduction"),
        source_record(MA, "PDF3–5 Eqs.(8)–(12), subsequent Nilsson limitation", [3, 4, 5], "Selected cranked RPA equations and limits, no rereading/recalculating full results"),
        source_record(KV, "PDF3 Eq.(6),PDF4 Fig.3 and its self-consistency discussion", [3, 4], "Selected pairing prescription, longitudinal inertia and alternative Dy/Yb mechanism; no full CRPA replay"),
    ]
    equations = []
    for claim in claims:
        for name in claim["equation_labels"]:
            equations.append({
                "label": "eq:2-6-" + name,
                "attribution": claim["kind"],
                "claim_id": claim["id"],
                "sources": claim["sources"],
                "limits": claim["limits"],
            })
    for label, (kind, references) in appendix_attributions.items():
        equations.append({"label": label, "attribution": kind, "sources": references})
    section_text = SECTION.read_text()
    appendix_text = APPENDIX.read_text()
    labels = re.findall(r"\\label\{([^}]+)\}", section_text + appendix_text)
    equation_labels = [label for label in labels if label.startswith("eq:")]
    assert set(equation_labels) == {entry["label"] for entry in equations}
    assert len(labels) == len(set(labels))
    environment_checks = []
    for path in [SECTION, APPENDIX]:
        text = path.read_text()
        stack = []
        for found in re.finditer(r"\\(begin|end)\{([^}]+)\}", text):
            action, environment = found.groups()
            if action == "begin":
                stack.append(environment)
            else:
                assert stack.pop() == environment, (path, environment)
        assert not stack
        assert not re.search(r"^#{1,6}\s|^\s*---\s*$|```|\[\[|\[@", text, re.M)
        assert "₊" not in text
        environment_checks.append({
            "path": str(path.relative_to(ROOT)),
            "nested_environments_balanced": True,
            "no_markdown_residue": True,
        })
    all_label_occurrences = Counter()
    for path in SECTION.parent.glob("*.tex"):
        all_label_occurrences.update(re.findall(r"\\label\{([^}]+)\}", path.read_text()))
    all_label_occurrences.update(re.findall(r"\\label\{([^}]+)\}", appendix_text))
    assert all(all_label_occurrences[label] == 1 for label in labels)
    bibliography = ROOT / "raw/writing/gpt/A130/these_2023_template/these_template/Biblio/ref.bib"
    keys = {key.strip() for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", section_text + appendix_text) for key in group.split(",")}
    existing_keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)", bibliography.read_text()))
    assert not keys - existing_keys, sorted(keys - existing_keys)
    run_records = json.loads((OUT / "smoke-runs.json").read_text())
    assert all(item["returncode"] == 0 for item in run_records)
    log = (OUT / "smoke.log").read_text(errors="replace")
    compile_check = {
        "kind": "section_2_6_and_response_appendix_only",
        "engine": "xelatex, ctexbook fontset=fandol, 146.6mm text width",
        "bibliography": "read existing canonical BibTeX, no modification",
        "bibliography_input": artifact(bibliography),
        "commands": run_records,
        "overfull_hbox_count": log.count("Overfull \\hbox"),
        "missing_character_count": log.count("Missing character:"),
        "undefined_citation_count": len(re.findall(r"LaTeX Warning: Citation", log)),
        "undefined_reference_count": len(re.findall(r"LaTeX Warning: Reference", log)),
        "output": re.findall(r"Output written[^\n]*", log),
        "pdf": artifact(OUT / "smoke.pdf"),
        "limitation": "Local format/syntax check only; G76 owns integrated compilation, parent owns scientific acceptance",
    }
    assert not any(compile_check[key] for key in ["overfull_hbox_count", "missing_character_count", "undefined_citation_count", "undefined_reference_count"])
    inputs = [
        OUT / "outline.json",
        OUT.parent / "next-wave-contracts.json",
        ROOT / "knowledge/research-notes/doctoral-thesis-architecture-and-section-map-20261108.md",
        ROOT / "knowledge/research-notes/doctoral-thesis-notation-and-evidence-style-20261108.md",
        ROOT / "knowledge/research-notes/doctoral-r2-collective-inertia-response-crosswalk-20261108.md",
        ROOT / "knowledge/research-notes/a130-rewrite-bcs-convention-and-model-hamiltonian-boundaries-20261108.md",
    ]
    ledger = {
        "section_id": "2.6",
        "title": "势能、惯量与微观响应",
        "version": "G82-latex-v1",
        "recorded_at": now,
        "worker": "G82",
        "status": "submitted_for_parent_scientific_acceptance",
        "latex_output": artifact(SECTION),
        "appendix_output": artifact(APPENDIX),
        "inputs": [artifact(path) for path in inputs],
        "sources": sources,
        "claims": claims,
        "equations": equations,
        "new_complex_derivations": [],
        "model_examples": [
            {"model": "positive-mass stable local oscillator", "identity": "teaching model, not real nuclear data", "equations": ["eq:2-6-local-hamiltonian", "eq:2-6-local-frequency", "eq:2-6-local-width"]},
        ],
        "evidence_layer_policy": "原作公式、本文单位/坐标换写、局部教学推导和作者具体模型解释分列；无新增实核数值/个人成果",
        "competing_conditions": [
            "低频可由曲率、质量、组态混合和算符/态对应差异产生",
            "TV与IB比较需相同参考和方向，不采用普适固定增强倍率",
            "沿带同方向自洽检查不能替代横向有效惯量色散根或电磁网络",
            "有限推转冗余根频率不能与静止NG零频无变换相等",
        ],
        "source_internal_boundaries": [
            "Hinohara Eq.(66) binding-energy B与Fig.4 -Bexp边界保留；本稿独立定义E=-B_+",
            "Matsuzaki未给出Nilsson速度依赖的横向对应修正，不虚构该修正",
            "Kvasil Eq.(6)配对处方保留；不将“自洽”理解为所有输入唯一无近似",
        ],
        "unresolved_for_parent": [
            "未来具体核/阻塞或倾斜参考的NG归一、残余相互作用与横向修正需指定实现；本文未产生新的普适推导",
            "附C仅补响应约定；一般坐标依赖质量、量子势和全体边界条件不在此处臆造",
        ],
        "knowledge_reuse": "本节复用已有R2 crosswalk、BCS约定页及各source；新增ESPE核查已在阶段A回写knowledge，不把本输出当唯一长期事实源",
        "syntax_checks": environment_checks,
        "compile_check": compile_check,
    }
    ledger_path = ROOT / "raw/writing/gpt/A130/latex-evidence-ledger/section-2-6.json"
    save_json(ledger_path, ledger)
    receipt = json.loads((OUT / "receipt.json").read_text())
    receipt["stage_b"] = {
        "status": "ready_for_parent_acceptance",
        "recorded_at": now,
        "artifacts": [artifact(SECTION), artifact(APPENDIX), artifact(ledger_path), artifact(OUT / "outline.json")],
        "equation_count": {"main": sum(label.startswith("eq:2-6-") for label in equation_labels), "appendix": sum(label.startswith("eq:app-c-") for label in equation_labels)},
        "compile_check": compile_check,
        "unresolved": ledger["unresolved_for_parent"],
    }
    layout_checks = json.loads((OUT / "layout-check.json").read_text())
    layout_artifacts = []
    for entry in layout_checks:
        section_number = entry["section"]
        tex_path = SECTION.parent / ("sec-" + section_number + ".tex")
        assert sha256(tex_path) == entry["after_sha256"], section_number
        layout_artifacts.extend([
            artifact(tex_path),
            artifact(ROOT / ("raw/writing/gpt/A130/latex-evidence-ledger/section-" + section_number + ".json")),
        ])
    receipt["layout_repair"]["artifacts"] = layout_artifacts
    protected_changed = []
    for relative, expected in receipt["protected_baseline"].items():
        if any(relative.endswith("sec-" + number + ".tex") or relative.endswith("section-" + number + ".json") for number in ["2-1", "2-2", "2-3"]):
            continue
        if sha256(ROOT / relative) != expected:
            protected_changed.append(relative)
    receipt["protected_checks"] = {
        "section_2_4_tex_and_ledger_unchanged": all(sha256(ROOT / relative) == expected for relative, expected in receipt["protected_baseline"].items() if "2-4" in relative),
        "authorised_layout_exceptions": ["2.1", "2.2", "2.3"],
        "other_concurrent_changes_observed": protected_changed,
    }
    receipt["recorded_at"] = now
    receipt["stage_a"]["artifacts"] = [artifact(ROOT / item["path"]) for item in receipt["stage_a"]["artifacts"]]
    verified_manifest = ROOT / "raw/papers/gpt/query/20261108-a130-espe-primary/manifest.t12-verified.json"
    manifest_entries = json.loads(verified_manifest.read_text())["files"]
    for entry in manifest_entries:
        path = ROOT / entry["path"]
        assert sha256(path) == entry["sha256"]
        assert path.stat().st_size == entry["size"]
    receipt["stage_a"]["manifest_verification"] = {
        "recorded_at": now,
        "file_hashes_and_sizes_checked": len(manifest_entries),
        "original_pdf_xml_and_manifests_unchanged": True,
    }
    receipt["task_status"] = "scoped_delivery_complete_pending_parent_scientific_acceptance"
    receipt["validation"] = {"recorded_at": now, "unique_new_labels": len(labels), "equation_attributions_complete": True, "canonical_citation_keys_found": sorted(keys), "integrated_compilation_owner": "G76"}
    save_json(OUT / "receipt.json", receipt)
    save_json(OUT / "validation.json", {"recorded_at": now, "syntax_checks": environment_checks, "compile_check": compile_check, "new_label_count": len(labels), "equation_count": len(equation_labels), "protected_checks": receipt["protected_checks"]})
    print(json.dumps({"main_equations": receipt["stage_b"]["equation_count"]["main"], "appendix_equations": receipt["stage_b"]["equation_count"]["appendix"], "new_labels_unique": len(labels), "local_compile": compile_check["output"], "receipt": str(OUT / "receipt.json")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
