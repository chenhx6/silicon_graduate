#!/usr/bin/env python3
"""AL11 Table II and local quadrupole-coordinate conditioning, not TAC/RPA.

Reads the identified public v2 PDF as data. The source's deferred raw archive
slot is not created. Applies the displayed phi=0 Jacobian only to phi=0 rows;
does not rotate phi=90 rows into that chart or fit actual vibration amplitudes.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

import numpy as np
import pymupdf

EXPECTED_SHA = 'becba964421bb8860fa657865071df117622a492a2bbb2b23d661d235296f29b'


def table_rows(pdf):
    text = pdf[4].get_text()
    lines = text[text.index('130Cs'):].strip().splitlines()
    rows, values, nucleus = [], [], None
    def flush():
        if len(values) % 6:
            raise ValueError('Table II row width changed')
        for i in range(0,len(values),6):
            raw = values[i:i+6]
            rows.append(dict(zip(['nuclide','hbar_omega_MeV','epsilon','gamma_deg',
                                  'theta_deg','phi_deg','hbar_Omega_MeV'],
                                 [nucleus]+[None if v=='-' else float(v) for v in raw])))
    for token in lines:
        if re.fullmatch(r'\d{3}[A-Z][a-z]?',token):
            if nucleus is not None:
                flush()
            nucleus, values = token, []
        elif token=='-' or re.fullmatch(r'\d+(?:\.\d+)?',token):
            values.append(token)
        else:
            raise ValueError(f'Unexpected Table II token: {token!r}')
    flush()
    if Counter(r['nuclide'] for r in rows) != {'130Cs':6,'132La':6,'134Pr':7,'136Pm':9,
                                               '138Eu':8,'140Tb':5,'130La':6,'134La':8}:
        raise ValueError('Table II nuclide/row counts changed')
    return rows


def orientation_jacobian(gamma, theta):
    c, s = np.cos(gamma), np.sin(gamma)
    return np.array([[-2*s,0.,-2*s*np.cos(theta)],
                     [0.,-s-np.sqrt(3)*c,0.],
                     [0.,0.,np.sin(theta)*(-s+np.sqrt(3)*c)]])


def diagonal_tensor(q0,q2):
    return np.diag([-q0/np.sqrt(6)+q2/np.sqrt(2),
                    -q0/np.sqrt(6)-q2/np.sqrt(2),2*q0/np.sqrt(6)])


def off_diagonal_components(t):
    return np.sqrt(2)*np.array([t[0,1],-t[0,2],-t[1,2]])


def rotate(t,axis,angle):
    n = np.asarray(axis,dtype=float)
    n /= np.linalg.norm(n)
    x,y,z = n
    k = np.array([[0,-z,y],[z,0,-x],[-y,x,0]])
    r = np.eye(3)+np.sin(angle)*k+(1-np.cos(angle))*(k@k)
    return r@t@r.T


def finite_difference_jacobian(t,theta,h):
    axes = [[0,0,1],[0,1,0],[np.sin(theta),0,np.cos(theta)]]
    return np.column_stack([(off_diagonal_components(rotate(t,a,h))-
                             off_diagonal_components(rotate(t,a,-h)))/(2*h) for a in axes])


def calculate(path):
    sha = hashlib.sha256(path.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        raise ValueError('Identified AL11 v2 PDF hash mismatch')
    pdf = pymupdf.open(path)
    if len(pdf)!=18:
        raise ValueError('Identified AL11 v2 page count mismatch')
    rows = table_rows(pdf)
    checks, geometry = [], []
    def check(name,ok):
        checks.append({'name':name,'passed':bool(ok)})
    for row in rows:
        if row['phi_deg']!=0:
            continue
        g,t = np.deg2rad([row['gamma_deg'],row['theta_deg']])
        j = orientation_jacobian(g,t)
        tensor = diagonal_tensor(np.cos(g),-np.sin(g))
        fine = finite_difference_jacobian(tensor,t,1e-5)
        coarse = finite_difference_jacobian(tensor,t,1e-4)
        tag = row['nuclide']+'_'+str(row['hbar_omega_MeV'])
        err = float(np.max(np.abs(j-fine)))
        check(tag+'_cartesian_derivative',err<2e-9)
        check(tag+'_derivative_convergence',err<np.max(np.abs(j-coarse))/20)
        sv = np.linalg.svd(j,compute_uv=False)
        check(tag+'_full_local_rank',sv[-1]>1e-8)
        # A finite active rotation changes orientation, not eigenvalues or norm.
        rotated = rotate(tensor,[.3,.5,.7],.37)
        check(tag+'_shape_invariants',np.max(np.abs(np.linalg.eigvalsh(tensor)-np.linalg.eigvalsh(rotated)))<1e-14
              and abs(np.sum(tensor*tensor)-np.sum(rotated*rotated))<1e-14)
        shape = np.array([[np.cos(g),-np.sin(g)],[-np.sin(g),-np.cos(g)]])
        check(tag+'_normalized_shape_jacobian',np.max(np.abs(shape.T@shape-np.eye(2)))<1e-14)
        geometry.append({**row,'normalized_singular_values':sv.tolist(),
                         'normalized_condition_number':float(sv[0]/sv[-1]),
                         'maximum_derivative_error':err})
    # Rank loss at an axial shape versus Euler-chart singularity: separate limits.
    check('axial_gamma0_rank2',np.linalg.matrix_rank(orientation_jacobian(0.,.8),tol=1e-12)==2)
    check('euler_theta0_rank2',np.linalg.matrix_rank(orientation_jacobian(.4,0.),tol=1e-12)==2)
    check('spherical_unnormalized_rank0',np.linalg.matrix_rank(0.*orientation_jacobian(.4,.8))==0)
    # Source table dashes stay missing. They are never assigned zero energy.
    pm = [r for r in rows if r['nuclide']=='136Pm']
    check('Pm_low_plane',[(r['phi_deg'],r['hbar_Omega_MeV']) for r in pm[:2]]==[(0.,.14),(0.,.09)])
    check('Pm_aplanar_missing_RPA',all(0<r['phi_deg']<90 and r['hbar_Omega_MeV'] is None for r in pm[2:6]))
    check('Pm_upper_plane_return',[(r['phi_deg'],r['hbar_Omega_MeV']) for r in pm[6:]]==[(90.,.15),(90.,.33),(90.,.42)])
    check('phi0_rows_only',len(geometry)==30)
    return {'kind':'source-table-and-conditional-Jacobian-audit','source':'knowledge/sources/almehed-2011-chiral-vibrations-a135.md',
            'actual_pdf':str(path),'sha256':sha,'pages':18,'locators':['PDF5 TableII','PDF14 Eqs24–26','PDF17–18 AppendixA'],
            'input_rows':rows,'phi0_geometry':geometry,'controls':checks,
            'all_controls_pass':all(x['passed'] for x in checks),
            'condition_number_range':[min(x['normalized_condition_number'] for x in geometry),max(x['normalized_condition_number'] for x in geometry)],
            'maximum_derivative_error':max(x['maximum_derivative_error'] for x in geometry),
            'limits':['Dimensionless q components are divided by C*epsilon, using radian increments and Euclidean coordinate norms.',
                      'This is local coordinate conditioning, not a mass tensor, physical mode norm, CI or RPA amplitude replay.',
                      'No phi=90 or aplanar row is decoded with the phi=0 chart.',
                      'No missing RPA energies or exact critical frequencies are interpolated; no 135Nd parameters are supplied.',
                      'Original quasiparticle/spurious-mode decomposition and actual producer remain unverified.']}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--pdf',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    result=calculate(args.pdf)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['all_controls_pass','condition_number_range','maximum_derivative_error']})+
          '\n'+str(len(result['controls']))+' controls')
    return 0 if result['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
