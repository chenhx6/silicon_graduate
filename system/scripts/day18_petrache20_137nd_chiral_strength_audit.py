#!/usr/bin/env python3
'Historical serializer retired after primary-identity audit. Weak-band denominators were out-of-band and two numerators also out-of-band; see P20-D18-2 through D18-12.'

import sys

if __name__ == "__main__":
    sys.stderr.write('Superseded scientific serializer: Weak-band denominators were out-of-band and two numerators also out-of-band; see P20-D18-2 through D18-12. Historical JSON is retained, not regenerated. See day18_parent_branch_identity_controls.py for the new scoped exercise.\n')
    raise SystemExit(2)
