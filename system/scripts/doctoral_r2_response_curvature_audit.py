#!/usr/bin/env python3
"""Rebuild quoted Hinohara2015 curvature parameters and non-nuclear controls.

This does not rerun nuclear HFB/QRPA or diagnose the stability of a fixed-N,Z
reference state. See the canonical source and R2 evidence note for boundaries.
"""
import datetime
import sys
import numpy as np

print('utc:', datetime.datetime.now(datetime.timezone.utc).isoformat())
print('python:', sys.version.replace('\n', ' '))
print('numpy:', np.__version__)
C = np.array([[1/11.986, 1/-4.236], [1/-4.236, 1/2.909]])
print('130Xe, inverse response / energy curvature C (MeV):\n', C)
print('det(C) (MeV^2):', np.linalg.det(C))
print('eigenvalues(C) (MeV):', np.linalg.eigvalsh(C))
print('S=-inverse(C) (MeV^-1):\n', -np.linalg.inv(C))
print('coefficient for deltaN=deltaZ=t (MeV):', 0.5 * np.ones(2) @ C @ np.ones(2))
print('non-nuclear Hessian control, IB curvature 2, alternatives TV curvature 4 or 1:')
for curvature in [2., 4., 1.]:
    print('curvature:', curvature, 'susceptibility:', 1/curvature)
