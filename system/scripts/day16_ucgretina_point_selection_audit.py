#!/usr/bin/env python3
"""Run the unmodified selected IP-ranking loop on frozen permutation controls."""
from __future__ import annotations

import argparse
import ctypes as ct
import hashlib
import itertools
import json
from pathlib import Path
import subprocess


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--freeze", type=Path, required=True)
    p.add_argument("--build", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    freeze = json.loads(a.freeze.read_text())
    assert sha(a.source) == freeze["source_sha256"]
    raw = a.source.read_text()
    start = raw.index("    Int_t i1 = -1;", raw.index("// Polarization"))
    end = raw.index("    if(gretSim->Size() > 0", start)
    block = raw[start:end]
    cpp = '''#include <vector>
using Int_t=int;using Double_t=double;
struct Point {double e;double GetDecompE() const{return e;}};
struct Hit {std::vector<Point> p;int GetCrystalId() const{return 0;}
 int Size() const{return p.size();}const Point& GetInteractionPoint(int i)const{return p[i];}};
extern "C" void original_select(const double* energies,int n,int* out){
 Hit hit; for(int i=0;i<n;i++)hit.p.push_back({energies[i]});
'''+block+'''out[0]=i1;out[1]=i2;}
'''
    a.build.mkdir(parents=True, exist_ok=True)
    source, so = a.build/"original-point-loop.cc", a.build/"original-point-loop.so"
    source.write_text(cpp)
    cmd = ["g++", "-O0", "-std=c++17", "-fPIC", "-shared", str(source), "-o", str(so)]
    c = subprocess.run(cmd, capture_output=True, text=True)
    assert c.returncode == 0, c.stderr
    lib = ct.CDLL(str(so.resolve())).original_select
    lib.argtypes = [ct.POINTER(ct.c_double), ct.c_int, ct.POINTER(ct.c_int)]
    lib.restype = None
    rows = []
    vectors = [p for values in [(5., 3.), (7., 5., 3.), (9., 7., 5., 3.)]
               for p in itertools.permutations(values)]
    vectors += [(5., 5., 3.), (3., 5., 5.)]
    for energies in vectors:
        e = (ct.c_double*len(energies))(*energies)
        out = (ct.c_int*2)()
        lib(e, len(energies), out)
        indices = list(out)
        selected = [energies[i] if i >= 0 else None for i in indices]
        expected = sorted(energies, reverse=True)[:2]
        rows.append({"energies_declared_units": energies, "literal_indices": indices,
                     "selected_values": selected, "expected_two_largest": expected,
                     "correct": selected == expected,
                     "descending_input": list(energies) == sorted(energies, reverse=True),
                     "ties": len(set(energies)) != len(energies)})
    distinct = [r for r in rows if not r["ties"]]
    descending = [r for r in distinct if r["descending_input"]]
    assert all(r["correct"] for r in descending)
    assert any(not r["correct"] for r in distinct)
    result = {"source_sha256": sha(a.source), "script_sha256": sha(Path(__file__)),
              "freeze_sha256": sha(a.freeze), "literal_block_sha256": hashlib.sha256(block.encode()).hexdigest(),
              "block_start_line": raw[:start].count("\n")+1, "block_end_line": raw[:end].count("\n"),
              "build": {"command": cmd, "exit_code": c.returncode, "stderr": c.stderr},
              "distinct_permutations": len(distinct), "distinct_failures": sum(not r["correct"] for r in distinct),
              "descending_distinct_controls_all_correct": True, "tie_controls": [r for r in rows if r["ties"]],
              "rows": rows, "actual_TGretinaHit_input_order_established": False,
              "paper_error_or_actual_bias_inferred": False, "upstream_source_modified": False}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k != "rows"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
