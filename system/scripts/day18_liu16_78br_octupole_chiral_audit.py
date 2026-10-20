#!/usr/bin/env python3
'Historical serializer retired after primary-identity audit. Unverified graph values and D0 geometry were used; see L16-D18-2 through D18-9.'

import sys

if __name__ == "__main__":
    sys.stderr.write('Superseded scientific serializer: Unverified graph values and D0 geometry were used; see L16-D18-2 through D18-9. Historical JSON is retained, not regenerated. See day18_parent_branch_identity_controls.py for the new scoped exercise.\n')
    raise SystemExit(2)
