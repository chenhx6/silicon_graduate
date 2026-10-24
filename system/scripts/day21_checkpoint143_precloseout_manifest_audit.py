#!/usr/bin/env python3
"""Pre-closeout transition manifest and full-chain consistency verification for Day 21."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'

def main():
    # 1. Audit all generated Checkpoint JSON scopes
    key_artifacts = [
        "same-parent-identifiability-104.json",
        "same-parent-covariance-scope-127.json",
        "chiral-model-domain-scope-128.json",
        "multispin-chiral-inversion-scope-129.json",
        "quadrupole-homomorphism-scope-130.json",
        "m1-staggering-antiphase-scope-131.json",
        "chiral-phonon-softening-scope-132.json",
        "cross-pillar-synthesis-scope-133.json",
        "polarization-falsification-scope-134.json",
        "lifetime-convergence-scope-135.json",
        "oral-scorecard-audit-scope-136.json",
        "sn100-gt-scaling-scope-137.json",
        "sn100-ec-reconciliation-scope-138.json",
        "typographical-anomaly-scope-139.json",
        "curriculum-deliverable-scope-140.json",
        "shared-denominator-covariance-scope-141.json",
        "open-questions-closure-scope-142.json"
    ]

    missing_artifacts = [f for f in key_artifacts if not (RUN / f).exists()]
    assert len(missing_artifacts) == 0, f"Missing artifacts: {missing_artifacts}"

    # 2. Check protected paths
    p_diff = subprocess.run(["git", "diff", "--name-only", "HEAD"], cwd=ROOT, capture_output=True, text=True)
    modified_files = set(p_diff.stdout.splitlines())

    protected_violations = []
    for prot in ["PLAN.md", "raw/zotero/wiki-inbox.bib"]:
        if prot in modified_files:
            protected_violations.append(prot)
    assert len(protected_violations) == 0, f"Protected files modified: {protected_violations}"

    # 3. Verify writeback validation script
    p_wb = subprocess.run(["python3", "system/scripts/validate_writeback_items.py", "--report", "outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam.md"], cwd=ROOT, capture_output=True, text=True)
    wb_res = json.loads(p_wb.stdout)
    assert wb_res["valid"] is True
    assert wb_res["items"] == 104

    # 4. Verify boundary check
    p_bound = subprocess.run(["python3", "system/scripts/wiki_boundary_check.py", "--root", "."], cwd=ROOT, capture_output=True, text=True)
    bound_res = json.loads(p_bound.stdout)
    assert bound_res["ok"] is True

    res = {
        "title": "Day 21 Pre-Closeout Manifest and Full-Chain Verification",
        "all_key_artifacts_present": True,
        "key_artifact_count": len(key_artifacts),
        "protected_paths_clean": True,
        "writeback_valid": True,
        "writeback_item_count": wb_res["items"],
        "boundary_check_ok": True,
        "closeout_protocol_summary": {
            "time_window_status": "under-100-min-transition-to-90min-boundary",
            "rule": "Finish current bounded analysis; do not open new source or full card; at 15:00 hard deadline, proceed exclusively with closeout, final card audit, run receipt delivery, course state credit award, and non-force explicit path publication."
        }
    }

    out = RUN / 'precloseout-manifest-scope-143.json'
    out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({
        "output": str(out.relative_to(ROOT)),
        "artifacts_verified": len(key_artifacts),
        "writeback_items": wb_res["items"],
        "boundary_ok": bound_res["ok"]
    }))

if __name__ == '__main__':
    main()
