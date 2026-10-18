#!/usr/bin/env python3
"""Compare original same-tensor angle and Stokes contraction conventions."""
from __future__ import annotations

import argparse
import ctypes as ct
import hashlib
import json
import math
from pathlib import Path
import shlex
import subprocess

import numpy as np

from day16_ucgretina_finite_product import density, tensor, finite_stokes, photon_trace
from day16_ucgretina_stokes_audit import configure, functions


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--build", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    cfg = json.loads(a.input.read_text())
    assert cfg["identity"] == "UCGRETINA-SAME-POL-ANGLE-KERNEL-COMPARISON-01"
    gpath = a.input.parent/cfg["general_input"]
    assert sha(gpath) == cfg["general_input_sha256"]
    general = json.loads(gpath.read_text())
    source = Path(cfg["old_legendre_source"])
    assert sha(source) == cfg["old_legendre_sha256"]
    old = functions(source.read_text(), "G4LegendrePolynomial::EvalAssocLegendrePoly")[0]
    code = '''#include "globals.hh"
#include "G4Pow.hh"
#include "G4Exp.hh"
#include "G4Log.hh"
#include <cmath>
#include <map>
using namespace std;
struct FrozenLegendre {
 double EvalAssocLegendrePoly(int,int,double,map<int,map<int,double>>* cache=nullptr);
};
'''+old.replace("G4LegendrePolynomial::", "FrozenLegendre::")+'''
extern "C" double old_associated(int l,int m,double x) {
 FrozenLegendre p; return p.EvalAssocLegendrePoly(l,m,x);
}
'''
    a.build.mkdir(parents=True, exist_ok=True)
    cpp, so = a.build/"old-associated.cc", a.build/"old-associated.so"
    cpp.write_text(code)
    config = "/opt/geant4/11.4.2/bin/geant4-config"
    cflags = shlex.split(subprocess.check_output([config, "--cflags"], text=True))
    libs = shlex.split(subprocess.check_output([config, "--libs"], text=True))
    cmd = ["g++", "-O0", "-fno-fast-math", "-shared", "-fPIC"]+cflags+[str(cpp), "-o", str(so)]+libs+["-Wl,-rpath,/opt/geant4/11.4.2/lib"]
    compiled = subprocess.run(cmd, capture_output=True, text=True)
    assert compiled.returncode == 0, compiled.stderr
    lp = ct.CDLL(str(so.resolve())).old_associated
    lp.argtypes = [ct.c_int, ct.c_int, ct.c_double]
    lp.restype = ct.c_double
    binary = Path(cfg["literal_binary"])
    assert sha(binary) == cfg["literal_binary_sha256"]
    lib = ct.CDLL(str(binary.resolve()))
    for name in ["old", "sdk"]:
        configure(lib, name)
    identities, rows, summaries = [], [], {}
    for rank in range(7):
        for q in range(rank+1):
            for theta in general["angles_deg"]:
                x = math.cos(math.radians(theta))
                leg = math.sqrt(math.factorial(rank-q)/math.factorial(rank+q))*lp(rank, q, x)
                for name in ["old", "sdk"]:
                    d = getattr(lib, "d_"+name)
                    identities.append({"rank": rank, "q": q, "theta_deg": theta, "helper": name,
                        "Pnorm_minus_d_q0": leg-d(2*rank, 2*q, 0, x),
                        "d_q0_minus_phase_d_0q": d(2*rank, 2*q, 0, x)-(-1)**q*d(2*rank, 0, 2*q, x)})
    for case in general["new_cases"]:
        rho = density(case)
        pol = tensor(case["Ji2"], rho)
        contracted = [np.array([(-1)**q*v for q, v in enumerate(row)]) for row in pol]
        amplitude_norm = 1+case["delta"]**2 if case["MP"] > 99 else 1
        ell = case["MP"]//200 if case["MP"] > 99 else case["MP"]//2
        residuals, source_errors, sampler_errors = [], [], []
        for theta in general["angles_deg"]:
            rad, x = math.radians(theta), math.cos(math.radians(theta))
            for phi in general["phi_rad"]:
                source = finite_stokes(case, pol, rad, phi, lib)
                variant = finite_stokes(case, contracted, rad, phi, lib)
                trace = photon_trace(case, rho, rad, phi)
                sampled = 0.0
                for rank in range(0, len(pol), 2):
                    f = lib.f_sdk(rank, ell, ell, case["Jf2"], case["Ji2"])
                    if case["MP"] > 99:
                        f += 2*case["delta"]*lib.f_sdk(rank, ell, ell+1, case["Jf2"], case["Ji2"])
                        f += case["delta"]**2*lib.f_sdk(rank, ell+1, ell+1, case["Jf2"], case["Ji2"])
                    for q, value in enumerate(pol[rank]):
                        sampled += ((1 if q == 0 else 2)*math.sqrt(2*rank+1)*f
                            *math.sqrt(math.factorial(rank-q)/math.factorial(rank+q))*lp(rank, q, x)
                            *(value*np.exp(1j*q*phi)).real/amplitude_norm)
                res = np.array(variant["IQUV"])-trace["IQUV"]
                residuals.append(abs(res))
                source_errors.append(abs(source["IQUV"][0]-trace["IQUV"][0]))
                sampler_errors.append(abs(sampled-trace["IQUV"][0]))
                rows.append({"case": case["id"], "theta_deg": theta, "phi_rad": phi,
                    "I_official_G4_sampler": sampled, "I_IT_same_tensor": source["IQUV"][0],
                    "photon_trace": trace, "diagnostic_equivalent_dq0_contraction": variant,
                    "diagnostic_IQUV_minus_photon": res.tolist()})
        summaries[case["id"]] = {"max_I_IT_same_tensor_error": max(source_errors),
            "max_I_official_sampler_error": max(sampler_errors),
            "max_diagnostic_IQUV_residual": np.max(residuals, axis=0).tolist()}
    result = {"identity": cfg["identity"], "input_sha256": sha(a.input), "script_sha256": sha(Path(__file__)),
        "old_Legendre_extract_sha256": hashlib.sha256(old.encode()).hexdigest(),
        "build": {"cmd": cmd, "exit_code": compiled.returncode, "stderr": compiled.stderr, "so_sha256": sha(so)},
        "max_Pnorm_dq0_error": max(abs(x["Pnorm_minus_d_q0"]) for x in identities),
        "max_d_transposition_identity_error": max(abs(x["d_q0_minus_phase_d_0q"]) for x in identities),
        "general_case_summary": summaries, "identity_rows": identities, "rows": rows,
        "upstream_modified_or_full_array_replayed": False,
        "diagnostic_variant_is_not_a_validated_universal_fix": True}
    a.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ["rows", "identity_rows", "build"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
