#!/usr/bin/env python3
"""Compile a literal UCGretina Stokes core with fixed old and installed helpers.

Third-party source and generated binaries stay under repo tmp. This executes
the selected emission algebra, not a full Geant4 event/geometry simulation.
"""
from __future__ import annotations

import argparse
import ctypes as ct
import hashlib
import json
import math
from pathlib import Path
import re
import shlex
import subprocess

import numpy as np
import sympy as sp
from sympy.physics.wigner import clebsch_gordan

from day16_gretina_convention_audit import gaussian


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def functions(text: str, name: str) -> list[str]:
    found = []
    for match in re.finditer(r"G4double\s+"+re.escape(name)+r"\(", text):
        start = match.start()
        begin = text.index("{", start)
        depth = 1
        end = begin+1
        while depth:
            depth += (text[end] == "{") - (text[end] == "}")
            end += 1
        found.append(text[start:end])
    return found


def cpp_sources(base: Path) -> tuple[str, dict]:
    cg = (base/"geant4-v1074/G4Clebsch.cc").read_text()
    fc = (base/"geant4-v1074/G4PolarizationTransition.cc").read_text()
    original = (base/"pinned-head/src/ITDecay.cc").read_text()
    old_functions = [functions(cg, "G4Clebsch::"+n)[0] for n in
                     ["ClebschGordanCoeff", "TriangleCoeff", "Wigner6J", "WignerLittleD"]]
    w3 = next(f for f in functions(cg, "G4Clebsch::Wigner3J")
              if f.split("{")[0].count("G4int") == 6)
    old_functions.append(w3)
    old_functions.append(functions(fc, "G4PolarizationTransition::FCoefficient")[0])
    old_code = "\n\n".join(old_functions).replace("G4Clebsch::", "ReplayClebsch::")
    old_code = old_code.replace("G4PolarizationTransition::", "ReplayTransition::")
    start = original.index("      int Lbar;")
    end = original.index("      eOrGammaDyn->SetPolarization(P1,P2,P3);", start)
    body = original[start:end]
    # Every expression of the emission body is copied verbatim; wrappers only
    # supply its existing variables and expose the output for inspection.
    header = '''#include <cmath>
#include <complex>
#include <vector>
#include "globals.hh"
#include "G4ThreeVector.hh"
#include "G4PolarizationTransition.hh"
#include "G4Clebsch.hh"
#include "G4Pow.hh"
#include "G4Exp.hh"
#include "G4Log.hh"
using namespace std;
const G4int G4POWLOGFACTMAX=512;
struct ReplayClebsch {
 static double ClebschGordanCoeff(int,int,int,int,int);
 static double TriangleCoeff(int,int,int);
 static double Wigner3J(int,int,int,int,int,int);
 static double Wigner6J(int,int,int,int,int,int);
 static double WignerLittleD(int,int,int,double);
};
struct ReplayTransition {
 double FCoefficient(int,int,int,int,int) const;
};
'''
    result = header+old_code+"\n"
    for label, utility in [("old", "ReplayClebsch"), ("sdk", "G4Clebsch")]:
        if label == "old":
            result += "#define G4Clebsch ReplayClebsch\n#define G4PolarizationTransition ReplayTransition\n"
        result += f'''extern "C" void emit_{label}(int JP1,int JP2,int MP,double mpRatio,
 double theta,double phi,const double* realrho,const double* imagrho,int length,double* out) {{
 G4ThreeVector gammaDir(sin(theta)*cos(phi),sin(theta)*sin(phi),cos(theta));
 std::vector<std::vector<G4complex>> parentPol(length);
 int offset=0;
 for(int k=0;k<length;k++) for(int q=0;q<=k;q++,offset++)
   parentPol[k].push_back(G4complex(realrho[offset],imagrho[offset]));
'''+body+"\n out[0]=P1; out[1]=P2; out[2]=P3; out[3]=norm;\n}\n"
        result += f'''extern "C" double cg_{label}(int a,int b,int c,int d,int e)
 {{return G4Clebsch::ClebschGordanCoeff(a,b,c,d,e);}}
extern "C" double f_{label}(int a,int b,int c,int d,int e)
 {{G4PolarizationTransition p;return p.FCoefficient(a,b,c,d,e);}}
extern "C" double d_{label}(int a,int b,int c,double d)
 {{return G4Clebsch::WignerLittleD(a,b,c,d);}}
'''
        if label == "old":
            result += "#undef G4Clebsch\n#undef G4PolarizationTransition\n"
    metadata = {"literal_stokes_body_sha256": hashlib.sha256(body.encode()).hexdigest(),
                "body_start_line": original[:start].count("\n")+1,
                "body_end_line": original[:end].count("\n"),
                "old_utility_functions_sha256": hashlib.sha256("\n\n".join(old_functions).encode()).hexdigest(),
                "old_function_adaptation": "class names only; compiled against installed G4Pow/Exp/Log math services",
                "full_Geant4_event_run": False}
    return result, metadata


def configure(lib: ct.CDLL, label: str) -> None:
    dp = ct.POINTER(ct.c_double)
    f = getattr(lib, "emit_"+label)
    f.argtypes = [ct.c_int, ct.c_int, ct.c_int, ct.c_double, ct.c_double, ct.c_double,
                  dp, dp, ct.c_int, dp]
    f.restype = None
    for prefix in ["cg_", "f_"]:
        f = getattr(lib, prefix+label)
        f.argtypes = [ct.c_int]*5
        f.restype = ct.c_double
    f = getattr(lib, "d_"+label)
    f.argtypes = [ct.c_int, ct.c_int, ct.c_int, ct.c_double]
    f.restype = ct.c_double


def tensor(lib: ct.CDLL, label: str, ji2: int, population: np.ndarray) -> np.ndarray:
    cg = getattr(lib, "cg_"+label)
    result = np.zeros(((ji2+1)*(ji2+2)//2), dtype=float)
    for k in range(ji2+1):
        # This is the exact Reaction.cc Pk0_z formula, preserving every rank,
        # including zero high-rank entries rather than silently trimming them.
        result[k*(k+1)//2] = sum(cg(ji2, m, ji2, -m, 2*k)/cg(ji2, m, ji2, -m, 0)
                                      /math.sqrt(2*k+1)*p
                                  for m, p in zip(range(-ji2, ji2+1, 2), population))
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--sources", type=Path, required=True)
    parser.add_argument("--build", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--geant4-config", default="/opt/geant4/11.4.2/bin/geant4-config")
    a = parser.parse_args()
    cfg = json.loads(a.input.read_text())
    assert cfg["identity"] == "UCGRETINA-STOKES-LITERAL-CORE-AUDIT-01"
    for path, digest in cfg["source_hashes"].items():
        assert sha(Path(path)) == digest
    code, meta = cpp_sources(a.sources)
    a.build.mkdir(parents=True, exist_ok=True)
    generated, binary = a.build/"literal-stokes.cc", a.build/"literal-stokes.so"
    generated.write_text(code)
    config = lambda flag: subprocess.check_output([a.geant4_config, flag], text=True).strip()
    cflags, libs = shlex.split(config("--cflags")), shlex.split(config("--libs"))
    libdirs = [flag[2:] for flag in libs if flag.startswith("-L")]
    command = ["g++", "-O0", "-fno-fast-math", "-fPIC", "-shared"]+cflags
    command += [str(generated), "-o", str(binary)]+libs+["-Wl,-rpath,"+p for p in libdirs]
    build = subprocess.run(command, capture_output=True, text=True)
    build_record = {"command": command, "exit_code": build.returncode,
                    "stdout": build.stdout, "stderr": build.stderr,
                    "sdk_version": config("--version"), **meta}
    (a.build/"build.json").write_text(json.dumps(build_record, indent=2)+"\n")
    if build.returncode:
        print(build.stderr)
        return build.returncode
    lib = ct.CDLL(str(binary.resolve()))
    for label in ["old", "sdk"]:
        configure(lib, label)
    # Independent exact CG oracle checks the inputs to the old and new calls.
    cg_errors = []
    for label in ["old", "sdk"]:
        cg = getattr(lib, "cg_"+label)
        for l in [1, 2]:
            for lp in [1, 2]:
                for rank in range(5):
                    for mp in [-1, 1]:
                        exact = float(clebsch_gordan(l, lp, rank, 1, mp, 1+mp))
                        cg_errors.append(abs(cg(2*l, 2, 2*lp, 2*mp, 2*rank)-exact))
    rows = []
    dp = ct.POINTER(ct.c_double)
    for case in cfg["cases"]:
        pop = np.array(case.get("population", gaussian(case["Ji2"], .56)), dtype=float)
        assert min(pop) >= 0 and math.isclose(float(pop.sum()), 1.0)
        for delta in case.get("deltas", [case.get("delta", 0.0)]):
            for label in ["old", "sdk"]:
                rho = tensor(lib, label, case["Ji2"], pop)
                zero = np.zeros_like(rho)
                for deg in cfg["angles_deg"]:
                    for phi in cfg["phi_rad"]:
                        out = np.empty(4)
                        getattr(lib, "emit_"+label)(case["Ji2"], case["Jf2"], case["MP"], delta,
                            math.radians(deg), phi, rho.ctypes.data_as(dp), zero.ctypes.data_as(dp),
                            case["Ji2"]+1, out.ctypes.data_as(dp))
                        rows.append({"case": case["id"], "helper": label, "delta": delta,
                                     "theta_deg": deg, "phi_rad": phi,
                                     "Stokes": [float(x) if math.isfinite(x) else None for x in out[:3]],
                                     "nonfinite_components": [i+1 for i, x in enumerate(out[:3]) if not math.isfinite(x)],
                                     "norm": float(out[3]) if math.isfinite(out[3]) else None})
    summary = {}
    for case in cfg["cases"]:
        subset = [r for r in rows if r["case"] == case["id"]]
        summary[case["id"]] = {"calls": len(subset),
            "finite_calls": sum(not r["nonfinite_components"] for r in subset),
            "nonfinite_calls": sum(bool(r["nonfinite_components"]) for r in subset),
            "all_norms_finite_and_positive": all(r["norm"] is not None and r["norm"] > 0 for r in subset)}
    result = {"identity": cfg["identity"], "input_sha256": sha(a.input),
              "script_sha256": sha(Path(__file__)), "build": build_record,
              "generated_cpp_sha256": sha(generated), "binary_sha256": sha(binary),
              "max_CG_oracle_error": max(cg_errors), "case_summary": summary,
              "rows": rows, "NaN_saved_as_null_with_explicit_component_list": True,
              "source_files_modified": False, "exact_paper_producer_certified": False,
              "full_detector_response_or_new_experimental_delta": False}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({"max_CG_oracle_error": max(cg_errors), "case_summary": summary,
                      "build_exit": build.returncode, "sdk_version": build_record["sdk_version"], **meta}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
