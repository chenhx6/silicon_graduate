#!/usr/bin/env python3
"""Reproduce declared kinematic quantities; no TAC/RPA or experimental fit."""
import json
import math

rotation = []
for angle in [1, 5, 10, 30, 40]:
    phi = math.radians(angle)
    exact = math.sin(2*phi)
    rotation.append({"angle_degrees": angle,
                     "exact": exact, "linear": 2*phi,
                     "relative_excess_over_exact": 2*phi/exact-1,
                     "Cartesian_minus_rank2": 2*math.sin(phi)*math.cos(phi)-exact})
C, epsilon, gamma, depsilon, dgamma = 2., .2, .4, .001, .002
q0, q2 = C*epsilon*math.cos(gamma), -C*epsilon*math.sin(gamma)
dq0 = C*(math.cos(gamma)*depsilon-epsilon*math.sin(gamma)*dgamma)
dq2 = -C*(math.sin(gamma)*depsilon+epsilon*math.cos(gamma)*dgamma)
norm = q0*q0+q2*q2
print(json.dumps({"scope": "kinematics only; no actual RPA correction or CI",
                  "rotation": rotation,
                  "recovered_depsilon_over_epsilon": (q0*dq0+q2*dq2)/norm,
                  "recovered_dgamma": (q2*dq0-q0*dq2)/norm,
                  "Jacobian_determinant": -C*C*epsilon}, indent=2))
