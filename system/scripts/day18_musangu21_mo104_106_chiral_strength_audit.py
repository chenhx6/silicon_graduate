#!/usr/bin/env python3
'Historical checkpoint serializer retired after primary-source audit. Printed limits had no specified confidence level; see MU21-D18-2 through D18-8.'

import sys

if __name__ == '__main__':
    sys.stderr.write('Superseded scientific serializer: Printed limits had no specified confidence level; see MU21-D18-2 through D18-8. Historical JSON remains archived; no outputs were regenerated. Use day18_source_boundary_controls.py for the corrected conditional checks.\n')
    raise SystemExit(2)
