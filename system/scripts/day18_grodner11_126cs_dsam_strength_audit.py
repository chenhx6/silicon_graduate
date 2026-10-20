#!/usr/bin/env python3
'Historical checkpoint serializer retired after primary-source audit. Upper limits and in/out line identities were mishandled; see GR126-D18-2 through D18-11.'

import sys

if __name__ == '__main__':
    sys.stderr.write('Superseded scientific serializer: Upper limits and in/out line identities were mishandled; see GR126-D18-2 through D18-11. Historical JSON remains archived; no outputs were regenerated. Use day18_source_boundary_controls.py for the corrected conditional checks.\n')
    raise SystemExit(2)
