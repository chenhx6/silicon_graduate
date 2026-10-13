#!/usr/bin/env python3
"""Exact Doppler global-direction counterexample for Day13.

Use independent calibration emitters sharing a constant speed/direction and
known rest-photon energies. This is not an exact finite-mass cascade with
photon-recoil kicks. Material loss, feeding, detector/calibration uncertainty
and actual experimental geometry are absent. All directions are self-chosen.
Two coplanar photon directions and a known speed may yield two mirrored
emitter directions even if the local two-angle Jacobian is full rank.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def photon_energy(rest, speed, direction, photon_direction):
    return rest*math.sqrt(1-speed*speed)/(1-speed*(np.asarray(photon_direction)@direction))


def reconstruct_known_speed(energies, rest, speed, photons):
    gamma=1/math.sqrt(1-speed*speed)
    projection=(1-rest/(gamma*np.asarray(energies)))/speed
    plane=photons.T@np.linalg.solve(photons@photons.T,projection)
    normal=np.cross(photons[0],photons[1]);normal/=np.linalg.norm(normal)
    remaining=1-float(plane@plane)
    if remaining<0:raise ValueError('no unit-direction solution under the exact noiseless model')
    return [plane+sign*math.sqrt(remaining)*normal for sign in (-1,1)]


def tangent_jacobian(rest, speed, direction, photons):
    # Use two independent tangent directions on the emitter unit sphere.
    reference=np.array([1.,0.,0.])
    first=reference-float(reference@direction)*direction;first/=np.linalg.norm(first)
    second=np.cross(direction,first)
    tangents=np.column_stack((first,second))
    prefactor=rest*math.sqrt(1-speed*speed)*speed/(1-speed*(photons@direction))**2
    return prefactor[:,None]*(photons@tangents),tangents


def calculate():
    rest,speed=1000.,.07
    true=np.array([.03,.02,math.sqrt(1-.03**2-.02**2)])
    photons=np.array([[0.,0.,-1.],[.8,0.,-.6]])
    measured=photon_energy(rest,speed,true,photons)
    solutions=reconstruct_known_speed(measured,rest,speed,photons)
    family=np.column_stack((np.sin(np.linspace(.1,3.,101)),np.zeros(101),np.cos(np.linspace(.1,3.,101))))
    additional=np.array([0.,1.,0.])
    branches=[];max_coplanar=0.;max_jacobian=0.
    for direction in solutions:
        assert abs(np.linalg.norm(direction)-1)<1e-12
        assert float(direction[2])>.99  # Both satisfy a forward beam-cone prior.
        predicted=photon_energy(rest,speed,direction,photons)
        assert np.max(np.abs(predicted-measured))<1e-10
        coplanar_difference=float(np.max(np.abs(photon_energy(rest,speed,direction,family)-photon_energy(rest,speed,true,family))))
        max_coplanar=max(max_coplanar,coplanar_difference)
        jac,tangents=tangent_jacobian(rest,speed,direction,photons)
        singular=np.linalg.svd(jac,compute_uv=False)
        assert np.linalg.matrix_rank(jac)==2
        numeric=np.zeros_like(jac);step=1e-5
        for j in (0,1):
            plus=direction+step*tangents[:,j];plus/=np.linalg.norm(plus)
            minus=direction-step*tangents[:,j];minus/=np.linalg.norm(minus)
            numeric[:,j]=(photon_energy(rest,speed,plus,photons)-photon_energy(rest,speed,minus,photons))/(2*step)
        max_jacobian=max(max_jacobian,float(np.max(np.abs(jac-numeric))))
        branches.append({'emitter_direction':direction.tolist(),
                         'predicted_two_lab_photons_keV':predicted.tolist(),
                         'additional_noncoplanar_photon_keV':float(photon_energy(rest,speed,direction,additional)),
                         'local_two_tangent_Jacobian_keV_per_radian':jac.tolist(),
                         'local_Jacobian_singular_values':singular.tolist(),
                         'local_rank':int(np.linalg.matrix_rank(jac)),
                         'coplanar_family_max_difference_keV':coplanar_difference})
    difference=abs(branches[0]['additional_noncoplanar_photon_keV']-branches[1]['additional_noncoplanar_photon_keV'])
    assert difference>2.7 and max_coplanar<1e-9 and max_jacobian<2e-7
    full_photons=np.vstack((photons,additional))
    gamma=1/math.sqrt(1-speed*speed)
    full_data=photon_energy(rest,speed,true,full_photons)
    full_projection=(1-rest/(gamma*full_data))/speed
    recovered=np.linalg.solve(full_photons,full_projection)
    assert np.max(np.abs(recovered-true))<1e-12
    assert np.max(np.abs(photon_energy(rest,0.,true,family)-rest))==0.
    return {'schema_version':1,'kind':'synthetic known-speed common-emitter-direction calibration fixture',
            'parameters':{'rest_photon_keV':rest,'speed_beta':speed,'true_direction':true.tolist(),
                          'two_photon_directions':photons.tolist(),'third_photon_direction':additional.tolist()},
            'global_mirror_solutions':branches,'third_direction_energy_difference_keV':difference,
            'third_direction_recovered_emitter_direction':recovered.tolist(),
            'verification':{'exact_two_projection_and_unit_constraints_passed':True,
                            'both_local_Jacobians_rank2':True,
                            'all_coplanar_directions_mirror_symmetry_passed':True,
                            'max_coplanar_energy_difference_keV':max_coplanar,
                            'max_direction_Jacobian_finite_difference_error':max_jacobian,
                            'noncoplanar_recovery_passed':True,'static_limit_passed':True,'passed':True},
            'boundaries':['Local rank does not rule out disconnected/global solutions.',
                          'Independent calibration emitters share a constant vector; no finite-mass cascade is asserted.',
                          'Real multiple photons can have different emission stages and velocities; source geometry or a particle track may remove a mirror branch.',
                          'No inference is made about actual CR13 fitted vector, VD16, Mavela or LG20 data.'],
            'numpy_version':np.__version__}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args();result=calculate()
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.output),'verification':result['verification'],
                     'extra_direction_energy_difference_keV':result['third_direction_energy_difference_keV']}))


if __name__=='__main__':
    main()
