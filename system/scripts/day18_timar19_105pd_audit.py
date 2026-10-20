#!/usr/bin/env python3
"""Compatibility entry for the corrected shared conditional-mixing audit.

Runs the same audit as the Nomura entry; it is not independent evidence.
Historical result-021 is never overwritten. See TI19-D18-2 through D18-6.
"""
from day18_nomura22_ibfm_wobbling_audit import main

if __name__ == '__main__':
    main()
