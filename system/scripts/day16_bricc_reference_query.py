#!/usr/bin/env python3
"""Issue each frozen BrIcc reference query once and retain typed HTTP receipts.

HTTP success is not numerical validation. The following offline audit must check
the actual program/data/parameter echo, coefficient rows and coverage warnings.
"""
from __future__ import annotations

import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path

import requests


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--receipt",type=Path,required=True)
    p.add_argument("--response-dir",type=Path,required=True)
    args=p.parse_args()
    root=Path(__file__).resolve().parents[2]
    for path in [args.input,args.receipt,args.response_dir]:
        assert path.resolve().is_relative_to(root),"Wiki paths only"
    cfg=json.loads(args.input.read_text())
    assert cfg["endpoint"]=="https://bricc.anu.edu.au/"
    assert cfg["max_queries"]==2 and len(cfg["requests"])==2
    assert all(x["dataset"]=="BrIccFO" and x["multipole"] in ("M1","E2")
               and x["atomic"]=="70" and x["energy"]=="489.8"
               and not x["eerror"] for x in cfg["requests"])
    input_hash=hashlib.sha256(args.input.read_bytes()).hexdigest()
    if args.receipt.exists():
        receipt=json.loads(args.receipt.read_text())
        assert receipt["input_sha256"]==input_hash
    else:
        receipt={"identity":cfg["identity"],"input_sha256":input_hash,
                 "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                 "requests":[],"numerical_validation_performed":False}
    args.response_dir.mkdir(parents=True,exist_ok=True)
    for params in cfg["requests"]:
        mode=params["multipole"]
        if any(x["parameters"]["multipole"]==mode for x in receipt["requests"]):
            print(json.dumps({"multipole":mode,"status":"already-attempted-no-repeat"}))
            continue
        out={"parameters":params,"attempt_started_at":datetime.now().astimezone().isoformat(),
             "status":"attempt-started","automatic_retries":0}
        receipt["requests"].append(out)
        args.receipt.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n")
        try:
            response=requests.post(cfg["endpoint"],data=params,
                                   headers={"User-Agent":"WikiResearchData/1.0"},timeout=(10,35))
            data=response.content
            path=args.response_dir/f"bricc-Z70-E489p8-FO-{mode}.html"
            assert not path.exists(),"Do not replace an earlier response"
            path.write_bytes(data)
            out.update({"status":"http-response","http_status":response.status_code,
                        "content_type":response.headers.get("Content-Type"),
                        "response":str(path),"bytes":len(data),
                        "sha256":hashlib.sha256(data).hexdigest(),
                        "redirect_statuses":[x.status_code for x in response.history]})
        except requests.RequestException as error:
            out.update({"status":"transport-failed","error_type":type(error).__name__,"error":str(error)})
        out["completed_at"]=datetime.now().astimezone().isoformat()
        args.receipt.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+"\n")
        print(json.dumps(out,ensure_ascii=False))


if __name__=="__main__":
    main()
