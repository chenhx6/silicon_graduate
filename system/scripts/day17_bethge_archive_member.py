#!/usr/bin/env python3
"""Retrieve one declared public archival PDF with capped HTTP Range requests."""
import hashlib
import io
import json
import re
import zipfile
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
DEST = ROOT / 'tmp/day17-bethge1966'
URL = 'https://edmond.mpg.de/api/access/datafile/200989'
SIZE = 50086033062


class PublicRangeReader(io.RawIOBase):
    def __init__(self):
        self.position = 0
        self.total = 0
        self.requests = []

    def seekable(self):
        return True

    def readable(self):
        return True

    def tell(self):
        return self.position

    def seek(self, offset, whence=0):
        self.position = offset + (0 if whence == 0 else self.position if whence == 1 else SIZE)
        if not 0 <= self.position <= SIZE:
            raise ValueError('invalid seek')
        return self.position

    def read(self, n=-1):
        if n < 0:
            n = SIZE - self.position
        n = min(n, SIZE - self.position)
        if n == 0:
            return b''
        if n > 8_000_000 or self.total + n > 32_000_000 or len(self.requests) >= 24:
            raise ValueError('bounded range budget exceeded')
        start, end = self.position, self.position + n - 1
        with requests.get(URL, headers={'Range': f'bytes={start}-{end}'},
                          stream=True, timeout=45) as response:
            # A server ignoring Range must be closed before its large body is read.
            if response.status_code != 206:
                raise ValueError(f'Range not honored: {response.status_code}')
            expected = f'bytes {start}-{end}/{SIZE}'
            if response.headers.get('Content-Range') != expected:
                raise ValueError('unexpected content range')
            data = response.raw.read(n + 1)
            if len(data) != n:
                raise ValueError('range length mismatch')
        self.position += n
        self.total += n
        self.requests.append({'range': expected, 'bytes': n,
                              'sha256': hashlib.sha256(data).hexdigest()})
        return data


def main():
    reader = PublicRangeReader()
    receipt = {'url': URL, 'dataset_doi': '10.17617/3.GRUJYR',
               'archive_size': SIZE, 'full_archive_downloaded_or_MD5_verified': False,
               'status': 'started', 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    try:
        with zipfile.ZipFile(reader) as archive:
            candidates = [x for x in archive.infolist()
                          if re.search(r'1966.*21a.*1052\.pdf$', x.filename, re.I)]
            receipt['archive_entries'] = len(archive.infolist())
            receipt['candidate_members'] = [x.filename for x in candidates]
            if len(candidates) != 1:
                raise ValueError('target archive member not unique')
            member = candidates[0]
            if member.file_size > 8_000_000:
                raise ValueError('unexpected PDF size')
            body = archive.read(member)  # ZIP CRC checked by stdlib.
            if not body.startswith(b'%PDF'):
                raise ValueError('member is not PDF')
            out = DEST / 'bethge1966-archive.pdf'
            if out.exists():
                if out.read_bytes() != body:
                    raise ValueError('refusing to replace different evidence')
            else:
                out.write_bytes(body)
            receipt.update({'status': 'downloaded-PDF-identity-pending', 'member': member.filename,
                            'member_bytes': len(body), 'member_CRC32': f'{member.CRC:08x}',
                            'member_sha256': hashlib.sha256(body).hexdigest(),
                            'path': str(out.relative_to(ROOT)), 'zip_CRC_check': 'passed'})
    except Exception as exc:
        receipt.update({'status': 'failed', 'error': str(exc)})
    finally:
        receipt['ranges'] = reader.requests
        receipt['total_bytes_read'] = reader.total
        (RUN / 'bethge1966-archive-member-receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
        print(json.dumps(receipt, indent=2), flush=True)
    if receipt['status'] == 'failed':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
