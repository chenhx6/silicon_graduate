#!/usr/bin/env python3
"""Offline validation of the two captured official BrIcc reference responses."""
from __future__ import annotations

import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup


def decode(value: str, error: str) -> dict:
    v=Decimal(value)
    e=re.fullmatch(r"\((\d+)\)",error)
    assert e,(value,error)
    return {"printed":value,"printed_error":error,"value":float(v),
            "quoted_sigma":float(Decimal(e[1])*Decimal(10)**v.as_tuple().exponent)}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--query-input",type=Path,required=True)
    p.add_argument("--receipt",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    cfg=json.loads(args.query_input.read_text());receipt=json.loads(args.receipt.read_text())
    assert hashlib.sha256(args.query_input.read_bytes()).hexdigest()==receipt["input_sha256"]
    raw=json.loads(args.manifest.read_text())["two_raw_responses"]
    model=[]
    for response in receipt["requests"]:
        mode=response["parameters"]["multipole"]
        assert response["http_status"]==200 and response["automatic_retries"]==0
        found=[x for x in raw if x["mode"]==mode];assert len(found)==1
        path=Path(found[0]["raw"]);data=path.read_bytes()
        assert hashlib.sha256(data).hexdigest()==response["sha256"]==found[0]["sha256"]
        soup=BeautifulSoup(data,"html.parser")
        table=soup.find("table");assert table is not None
        rows=[[td.get_text(" ",strip=True) for td in tr.find_all(["td","th"],recursive=False)]
              for tr in table.find_all("tr",recursive=False)]
        flat=" ".join(" ".join(row) for row in rows)
        assert "BrIccS v2.3 (9-Dec-2011)" in flat
        assert "Z=70" in flat and "Ytterbium" in flat and "489.8" in flat
        assert "BrIccFO" in flat and "BrIccNH" not in flat
        start=next(i for i,x in enumerate(rows) if x[:2]==["Shell","E(ce)"])
        assert rows[start][2]==mode
        coefficients={};missing=[]
        for row in rows[start+1:]:
            if not row or row[0].startswith("Reference"):
                break
            if len(row)>=4 and row[2] and row[3]:
                coefficients[row[0]]={**decode(row[2],row[3]),"Ece_printed_keV":row[1] or None}
            elif row[0] in ("N6","N7"):
                missing.append(row[0])
        warnings=[x for x in soup.stripped_strings if "ICC could not be calculated" in x]
        assert len(warnings)==2 and set(missing)=={"N6","N7"}
        assert coefficients["Tot"]["value"]>coefficients["K"]["value"]>0
        major=sum(coefficients[k]["value"] for k in ["K","L-tot","M-tot","N-tot","O-tot","P-tot"])
        # A printed consistency check, not restoration of omitted shells.
        assert abs(major-coefficients["Tot"]["value"])<=coefficients["Tot"]["quoted_sigma"]
        model.append({"multipolarity":mode,"version":"BrIccS v2.3 (9-Dec-2011)",
                      "dataset":"BrIccFO","Z":70,"energy_keV":489.8,
                      "raw":str(path),"raw_sha256":response["sha256"],
                      "all_printed_rows":rows[start:],"coefficients":coefficients,
                      "missing_shells_not_filled":missing,"warnings":warnings,
                      "printed_major_sum":major,
                      "default_mass_in2008_TableB1":173,
                      "current_backend_mass_or_datafile_hash_not_exposed":True})
    assert {x["multipolarity"] for x in model}=={"M1","E2"}
    out={"query_identity":cfg["identity"],"query_input_sha256":receipt["input_sha256"],
         "capture_script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "query_receipt_sha256":hashlib.sha256(args.receipt.read_bytes()).hexdigest(),
         "model_inputs":model,"numerically_validated":True,
         "scope":"Two new nominal-energy theory lookups, not measured ICC. E uncertainty was not sent; missingN6/N7 retained. Program-reportedTot is used only with explicit coverage boundary, not declared complete total. No independent interpolation uncertainty added."}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"models":[{"multipolarity":x["multipolarity"],"Tot":x["coefficients"]["Tot"],
                                 "K":x["coefficients"]["K"],"missing":x["missing_shells_not_filled"],
                                 "warnings":x["warnings"]} for x in model]},ensure_ascii=False,indent=2))


if __name__=="__main__":
    main()
