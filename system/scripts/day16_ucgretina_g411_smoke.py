#!/usr/bin/env python3
"""Run frozen gamma/decay smoke macros in new repo-local working directories."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time


ROOT = Path(__file__).resolve().parents[2]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--contract", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    cfg = json.loads(a.contract.read_text())
    assert cfg["identity"] in {
        "UCGRETINA-G411-EU152-SMOKE-01",
        "UCGRETINA-G411-SOURCE-MACRO-01",
    }
    binary = (ROOT/cfg["binary"]).resolve()
    assert sha(binary) == cfg["binary_sha256"]
    work = (ROOT/cfg["work_root"]).resolve()
    work.relative_to(ROOT/"tmp")
    assert not work.exists(), "Never overwrite a previous MC working directory"
    work.mkdir(parents=True)
    env = os.environ.copy()
    dataset_lines = subprocess.check_output(["/opt/geant4/11.4.2/bin/geant4-config", "--datasets"], text=True)
    datasets = []
    for line in dataset_lines.splitlines():
        label, variable, path = line.split(maxsplit=2)
        assert Path(path).is_dir()
        env[variable] = path
        datasets.append({"label": label, "environment_variable": variable, "path": path})
    result = {"identity": cfg["identity"], "contract_sha256": sha(a.contract),
              "script_sha256": sha(Path(__file__)), "binary_sha256": sha(binary),
              "datasets": datasets, "modes": [], "source_originals_modified": False,
              "full_response_or_Q_validated": False}
    failure_patterns = [r"COMMAND NOT FOUND", r"command not found", r"Illegal parameter", r"Illegal application state",
                        r"ERROR: Can not open", r"FatalException", r"Batch is interrupted",
                        r"execution is aborted", r"G4Exception :.*Fatal"]
    for mode in cfg["modes"]:
        directory = work/mode["id"]
        directory.mkdir()
        for item in cfg["input_files"]:
            source = ROOT/item["path"]
            assert sha(source) == item["sha256"]
            if source.suffix == ".mac":
                continue
            shutil.copyfile(source, directory/item["name"])
        source_macro = next(x for x in cfg["input_files"] if x["name"] == mode["macro"])
        text = (ROOT/source_macro["path"]).read_text()
        if mode.get("sourceframe_after_initialize", False):
            frame = "/Target/sourceFrame eu152_Z2707"
            assert text.count(frame) == 1 and text.count("/run/initialize") == 1
            text = text.replace(frame+"\n", "")
            text = text.replace("/run/initialize\n", "/run/initialize\n"+frame+"\n")
        if mode.get("tracking_verbose", 0):
            assert mode["tracking_verbose"] == 1
            text = text.replace("/run/beamOn ", "/tracking/verbose 1\n/run/beamOn ")
        text = re.sub(r"(?m)^/Mode2/Filename\s+\S+", "/Mode2/Filename "+mode["output_file"], text)
        text = re.sub(r"(?m)^/run/beamOn\s+\d+", "/run/beamOn "+str(mode["events"]), text)
        text = "/control/verbose 1\n/run/verbose 1\n/random/setSeeds "+" ".join(map(str, mode["seeds"]))+"\n"+text
        macro = directory/"smoke.mac"
        macro.write_text(text)
        tmp = directory/"runtime-tmp"
        tmp.mkdir()
        scoped = env.copy()
        scoped["TMPDIR"] = str(tmp)
        scoped["G4WORKDIR"] = str(directory)
        log = directory/"run.log"
        started = time.monotonic()
        with log.open("w") as f:
            exit_code = subprocess.run([str(binary), macro.name], cwd=directory, env=scoped,
                                       stdout=f, stderr=subprocess.STDOUT,
                                       timeout=cfg.get("timeout_seconds", 600)).returncode
        output = directory/mode["output_file"]
        logtext = log.read_text(errors="replace")
        hits = [{"pattern": pattern, "count": len(re.findall(pattern, logtext, re.I))}
                for pattern in failure_patterns if re.search(pattern, logtext, re.I)]
        exception_blocks = re.findall(r"G4Exception-START(.*?)G4Exception-END", logtext, re.S)
        accepted, unreviewed = [], []
        counts = {}
        for block in exception_blocks:
            match = next((w for w in cfg.get("reviewed_warning_blocks", [])
                          if "G4Exception : "+w["code"] in block
                          and w["message_contains"] in block
                          and "This is just a warning message." in block), None)
            if match is None:
                unreviewed.append(block)
            else:
                counts[match["code"]] = counts.get(match["code"], 0)+1
                accepted.append({"code": match["code"], "block": block})
                if counts[match["code"]] > match["max_count"]:
                    unreviewed.append(block)
        if unreviewed:
            hits.append({"pattern": "unreviewed_G4Exception_block", "count": len(unreviewed)})
        row = {"mode": mode["id"], "events_requested": mode["events"], "seeds": mode["seeds"],
               "exit_code": exit_code, "elapsed_s": time.monotonic()-started,
               "working_directory": str(directory.relative_to(ROOT)),
               "macro_sha256": sha(macro), "log": str(log.relative_to(ROOT)),
               "sourceframe_after_initialize": mode.get("sourceframe_after_initialize", False),
               "tracking_verbose": mode.get("tracking_verbose", 0),
               "declared_event_count_found": f"Simulating {mode['events']} events." in logtext,
               "run_completion_time_found": "Real time:" in logtext,
               "source_commit_found": cfg["source_commit"] in logtext,
               "failure_pattern_hits": hits, "output": str(output.relative_to(ROOT)),
               "reviewed_warning_blocks_retained": accepted,
               "unreviewed_exception_blocks": unreviewed,
               "output_exists": output.exists(), "output_bytes": output.stat().st_size if output.exists() else 0,
               "output_sha256": sha(output) if output.exists() else None,
               "copied_inputs_after_run": {x["name"]: sha(directory/x["name"]) == x["sha256"]
                                          for x in cfg["input_files"] if Path(x["name"]).suffix != ".mac"}}
        result["modes"].append(row)
        a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
        print(json.dumps(row, ensure_ascii=False), flush=True)
        if exit_code or hits or not row["declared_event_count_found"] or not row["run_completion_time_found"]:
            return 1
    assert all(sha(ROOT/x["path"]) == x["sha256"] for x in cfg["input_files"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
