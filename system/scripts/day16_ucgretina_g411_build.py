#!/usr/bin/env python3
"""Build the fixed public G411 source in a repo-local, headless wrapper.

No install, source patch, original Makefile, GUI, or simulation is performed.
The generated metadata header records the public source commit explicitly.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import time


ROOT = Path(__file__).resolve().parents[2]


def data(path: Path) -> bytes:
    return os.readlink(path).encode() if path.is_symlink() else path.read_bytes()


def verify(source: Path, manifest: dict) -> None:
    for row in manifest["rows"]:
        assert hashlib.sha256(data(source/row["path"])).hexdigest() == row["sha256"], row["path"]


def bracket(s: str | Path) -> str:
    value = str(s)
    if "]]" in value:
        raise ValueError("Unsupported CMake path")
    return "[["+value+"]]"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--contract", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    cfg = json.loads(a.contract.read_text())
    assert cfg["identity"] == "UCGRETINA-G411-HEADLESS-SOURCE-BUILD-01"
    source = (ROOT/cfg["source"]).resolve()
    build = (ROOT/cfg["build_dir"]).resolve()
    source.relative_to(ROOT/"tmp")
    build.relative_to(ROOT/"tmp")
    manifest = json.loads((a.contract.parent/cfg["source_verification"]).read_text())
    assert manifest["verified_blobs"] == 724 and not manifest["mismatches"]
    verify(source, manifest)
    build.mkdir(parents=True, exist_ok=True)
    wrapper, generated = build/"wrapper", build/"generated"
    wrapper.mkdir(exist_ok=True)
    generated.mkdir(exist_ok=True)
    tempdir = build/"compiler-tmp"
    tempdir.mkdir(exist_ok=True)
    (generated/"Git_Hash.hh").write_text('#pragma once\n#define GIT_HASH "'+cfg["source_commit"]+'"\n#define GIT_BRANCH "'+cfg.get("branch_label", "geant4.11-fixed-public-archive")+'"\n')
    config = "/opt/geant4/11.4.2/bin/geant4-config"
    assert subprocess.check_output([config, "--version"], text=True).strip() == cfg["SDK"]
    cflags = shlex.split(subprocess.check_output([config, "--cflags-without-gui"], text=True))
    libs = shlex.split(subprocess.check_output([config, "--libs-without-gui"], text=True))
    includes = [generated, source/"include"]+[Path(x[2:]) for x in cflags if x.startswith("-I")]
    options = [x for x in cflags if not x.startswith(("-I", "-std="))]
    overlay_rules = []
    for row in cfg.get("overlay_files", []):
        assert hashlib.sha256((source/row["original_relative"]).read_bytes()).hexdigest() == row["original_sha256"]
        overlay = (ROOT/row["overlay_path"]).resolve()
        overlay.relative_to(ROOT/"tmp")
        assert hashlib.sha256(overlay.read_bytes()).hexdigest() == row["overlay_sha256"]
        overlay_rules += ['list(REMOVE_ITEM SOURCES '+bracket(source/row["original_relative"])+')',
                          'list(APPEND SOURCES '+bracket(overlay)+')']
    cmake = '\n'.join([
        'cmake_minimum_required(VERSION 3.16)',
        'project(UCGretinaFixedSource LANGUAGES CXX)',
        'set(CMAKE_CXX_STANDARD 17)',
        'set(CMAKE_CXX_STANDARD_REQUIRED ON)',
        'file(GLOB SOURCES CONFIGURE_DEPENDS '+bracket(source/"src/*.cc")+')',
        *overlay_rules,
        'add_executable(UCGretina '+bracket(source/"UCGretina.cc")+' ${SOURCES})',
        'target_include_directories(UCGretina BEFORE PRIVATE '+' '.join(bracket(x) for x in includes)+')',
        'target_compile_definitions(UCGretina PRIVATE G4V11 _FILE_OFFSET_BITS=64 '+' '.join(cfg.get("additional_definitions", []))+')',
        'target_compile_options(UCGretina PRIVATE -O2 '+' '.join(bracket(x) for x in options)+')',
        'target_link_libraries(UCGretina PRIVATE '+' '.join(bracket(x) for x in libs)+')',
        'target_link_options(UCGretina PRIVATE [[-Wl,-rpath,/opt/geant4/11.4.2/lib]])',
        '',
    ])
    (wrapper/"CMakeLists.txt").write_text(cmake)
    env = os.environ.copy()
    env["TMPDIR"] = str(tempdir)
    commands = [
        ["cmake", "-S", str(wrapper), "-B", str(build/"build"), "-G", "Ninja", "-DCMAKE_BUILD_TYPE=Release"],
        ["cmake", "--build", str(build/"build"), "--parallel", str(cfg["compile_parallel_jobs"])],
    ]
    records = []
    for i, cmd in enumerate(commands):
        log = build/("configure.log" if i == 0 else "build.log")
        started = time.monotonic()
        with log.open("w") as f:
            status = subprocess.run(cmd, env=env, cwd=ROOT, stdout=f, stderr=subprocess.STDOUT).returncode
        records.append({"command": cmd, "exit_code": status, "elapsed_s": time.monotonic()-started,
                        "log": str(log.relative_to(ROOT))})
        print(json.dumps(records[-1]), flush=True)
        if status:
            break
    verify(source, manifest)
    binary = build/"build/UCGretina"
    result = {"identity": cfg["identity"], "contract_sha256": hashlib.sha256(a.contract.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "source_commit": cfg["source_commit"], "source_blobs_after_build_unchanged": True,
              "overlay_files": cfg.get("overlay_files", []), "additional_definitions": cfg.get("additional_definitions", []),
              "generated_header_sha256": hashlib.sha256((generated/"Git_Hash.hh").read_bytes()).hexdigest(),
              "CMake_wrapper_sha256": hashlib.sha256((wrapper/"CMakeLists.txt").read_bytes()).hexdigest(),
              "commands": records, "binary": str(binary.relative_to(ROOT)) if binary.exists() else None,
              "binary_sha256": hashlib.sha256(binary.read_bytes()).hexdigest() if binary.exists() else None,
              "MC_executed": False, "global_install_or_configuration_changed": False,
              "polarized_EM_or_original_paper_response_validated": False}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    return records[-1]["exit_code"]


if __name__ == "__main__":
    raise SystemExit(main())
