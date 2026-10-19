#!/usr/bin/env python3
"""Fetch only the ten pinned, hash-verified inputs of the G3COMP audit."""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import requests


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--contract',required=True,type=Path);a=p.parse_args()
    c=json.loads(a.contract.read_text());assert c['identity']=='GEANT3-G3COMP-COMPONENT-BENCHMARK-01'
    root=Path(__file__).resolve().parents[2];rows=[]
    for f in c['source_files']:
        dest=root/f['local'];assert dest.resolve().is_relative_to(root/'tmp/day16-geant3-producer')
        assert not dest.is_symlink()
        if dest.is_file():data=dest.read_bytes();route='verified-existing-cache'
        else:
            expected='https://raw.githubusercontent.com/vmc-project/geant3/'+c['commit']+'/'+f['source_path']
            assert f['url']==expected
            try:
                r=requests.get(expected,timeout=30);r.raise_for_status();data=r.content;route='pinned-raw'
            except requests.RequestException:
                url='https://api.github.com/repos/vmc-project/geant3/git/blobs/'+f['git_blob_sha1']
                r=requests.get(url,timeout=30);r.raise_for_status();data=base64.b64decode(r.json()['content']);route='exact-blob-API'
        assert hashlib.sha256(data).hexdigest()==f['sha256']
        assert hashlib.sha1(('blob '+str(len(data))+'\0').encode()+data).hexdigest()==f['git_blob_sha1']
        if not dest.exists():dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        rows.append({'path':f['source_path'],'route':route,'sha256_verified':True,'git_blob_verified':True})
    print(json.dumps({'commit':c['commit'],'files':rows,'vendor_sources_kept_in_ignored_tmp':True},indent=2))


if __name__=='__main__':main()
