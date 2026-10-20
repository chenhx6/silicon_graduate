#!/usr/bin/env python3
'Historical serializer retired after primary-identity audit. Suzuki values and spin identities did not match the primary; different parity bands were conflated; see KU14-D18-2 through D18-11.'

import sys

if __name__ == "__main__":
    sys.stderr.write('Superseded scientific serializer: Suzuki values and spin identities did not match the primary; different parity bands were conflated; see KU14-D18-2 through D18-11. Historical JSON is retained, not regenerated. See day18_parent_branch_identity_controls.py for the new scoped exercise.\n')
    raise SystemExit(2)
