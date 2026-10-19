#!/usr/bin/env python3
"""Compile pinned unmodified G3COMP kernels for a bounded component audit.

The standalone harness supplies RNG and no-op energy-bin bookkeeping. It does
not run material transport, GR97's modified GCOMPOL, or a detector calibration.
"""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
from zoneinfo import ZoneInfo
import numpy as np

DRIVER = r'''#include "geant321/pilot.h"
      PROGRAM G3BENCH
#include "geant321/gcphys.inc"
#include "geant321/gctrak.inc"
#include "geant321/gcking.inc"
#include "geant321/gconsp.inc"
#include "geant321/gccuts.inc"
      INTEGER H(40),HP(16),N,IE,I,K,IP,MODE
      INTEGER*8 SEED,NCALLS,BASESEED
      COMMON/BENCHRNG/SEED,NCALLS
      DOUBLE PRECISION ES(3),E0,AXIS(3),P0(3),ROTAX(3)
      DOUBLE PRECISION RR,CC,PH,MEANR,MEANR2,MERR(6)
      DOUBLE PRECISION EB,PMOM(3),ERR,NORMV,MASSERR
      DOUBLE PRECISION REF(4,1000),REFCOS(1000)
      DOUBLE PRECISION PMAX,RMAX,CMAX,CUTERR(3),OLDPOL(3)
      CHARACTER*40 ARG
      CALL GET_COMMAND_ARGUMENT(1,ARG)
      READ(ARG,*) N
      CALL GET_COMMAND_ARGUMENT(2,ARG)
      READ(ARG,*) BASESEED
      ES=(/0.0005D0,0.0015D0,0.004D0/)
      AXIS=(/0D0,0D0,1D0/)
      P0=(/1D0,0D0,0D0/)
      ROTAX=(/0.36D0,0.48D0,0.8D0/)
      DO IE=1,3
         E0=ES(IE)
         SEED=BASESEED+IE-1
         NCALLS=0
         H=0
         HP=0
         MEANR=0D0
         MEANR2=0D0
         MERR=0D0
         DO I=1,N
            CALL RESET(E0,AXIS,P0,0D0,0D0,1)
            CALL G3COMP
            RR=DBLE(VECT(7))/E0
            CC=DOT_PRODUCT(DBLE(VECT(4:6)),AXIS)
            PH=ATAN2(DBLE(VECT(5)),DBLE(VECT(4)))
            IF(PH.LT.0D0) PH=PH+TWOPI
            K=MIN(40,MAX(1,INT((CC+1D0)*20D0)+1))
            IP=MIN(16,MAX(1,INT(PH/TWOPI*16D0)+1))
            H(K)=H(K)+1
            HP(IP)=HP(IP)+1
            MEANR=MEANR+RR
            MEANR2=MEANR2+RR*RR
            EB=DBLE(VECT(7))+DBLE(DESTEP)
            IF(NGKINE.GT.0) EB=EB+DBLE(GKIN(4,1))-EMASS
            MERR(1)=MAX(MERR(1),ABS(EB-E0)/E0)
            PMOM=E0*AXIS-DBLE(VECT(7))*DBLE(VECT(4:6))
     +            -DBLE(GKIN(1:3,1))
            MERR(2)=MAX(MERR(2),SQRT(SUM(PMOM**2))/E0)
            NORMV=SUM(DBLE(VECT(4:6))**2)
            MERR(3)=MAX(MERR(3),ABS(NORMV-1D0))
            MASSERR=ABS(DBLE(GKIN(4,1))**2
     +         -SUM(DBLE(GKIN(1:3,1))**2)-EMASS**2)
            MERR(4)=MAX(MERR(4),MASSERR/MAX(E0**2,EMASS**2))
            ERR=ABS(1D0/RR-1D0-E0/EMASS*(1D0-CC))
     +         /(1D0+2D0*E0/EMASS)
            MERR(5)=MAX(MERR(5),ERR)
            ERR=MAX(0D0,1D0/(1D0+2D0*E0/EMASS)-RR,RR-1D0)
            MERR(6)=MAX(MERR(6),ERR)
         ENDDO
         WRITE(*,'(A,1X,I1,1X,ES24.16,1X,I10,1X,I14)')
     +      'ENERGY',IE,E0,N,NCALLS
         WRITE(*,'(A,1X,2ES24.16)') 'MOMENTS',
     +      MEANR/N,MEANR2/N
         WRITE(*,'(A,1X,6ES24.16)') 'ERRORS',MERR
         WRITE(*,'(A,1X,40I10)') 'COSBINS',H
         WRITE(*,'(A,1X,16I10)') 'PHIBINS',HP
      ENDDO
C     Paired random-number controls: POLAR is present but unused by G3COMP.
      E0=ES(1)
      SEED=BASESEED
      NCALLS=0
      DO I=1,1000
         CALL RESET(E0,AXIS,P0,0D0,0D0,1)
         CALL G3COMP
         REF(1:3,I)=DBLE(VECT(4:6))
         REF(4,I)=DBLE(VECT(7))
         REFCOS(I)=DOT_PRODUCT(DBLE(VECT(4:6)),AXIS)
      ENDDO
      OLDPOL=(/0D0,1D0,0D0/)
      SEED=BASESEED
      PMAX=0D0
      DO I=1,1000
         CALL RESET(E0,AXIS,OLDPOL,0D0,0D0,1)
         CALL G3COMP
         PMAX=MAX(PMAX,MAXVAL(ABS(DBLE(VECT(4:6))-REF(1:3,I))),
     +      ABS(DBLE(VECT(7))-REF(4,I)))
         IF(MAXVAL(ABS(DBLE(POLAR)-OLDPOL)).GT.1D-6) STOP 81
      ENDDO
      SEED=BASESEED
      OLDPOL=(/-0.8D0,0.6D0,0D0/)
      RMAX=0D0
      CMAX=0D0
      DO I=1,1000
         CALL RESET(E0,ROTAX,OLDPOL,0D0,0D0,1)
         CALL G3COMP
         RMAX=MAX(RMAX,ABS(DBLE(VECT(7))-REF(4,I))/E0)
         CC=DOT_PRODUCT(DBLE(VECT(4:6)),ROTAX)
         CMAX=MAX(CMAX,ABS(CC-REFCOS(I)))
      ENDDO
      WRITE(*,'(A,1X,3ES24.16)') 'PAIRED',PMAX,RMAX,CMAX
C     These are transport cuts or a process flag, not electronics thresholds.
      DO MODE=1,3
         SEED=BASESEED
         IF(MODE.EQ.1) THEN
            CALL RESET(E0,AXIS,P0,2D0*E0,2D0*E0,1)
         ELSE IF(MODE.EQ.2) THEN
            CALL RESET(E0,AXIS,P0,0D0,2D0*E0,1)
         ELSE
            CALL RESET(E0,AXIS,P0,0D0,0D0,2)
         ENDIF
         CALL G3COMP
         EB=DBLE(VECT(7))+DBLE(DESTEP)
         IF(NGKINE.GT.0) EB=EB+DBLE(GKIN(4,1))-EMASS
         CUTERR(MODE)=ABS(EB-E0)/E0
         IF(NGKINE.NE.0) STOP 82
         IF(MODE.EQ.1.AND.ISTOP.NE.2) STOP 83
         WRITE(*,'(A,1X,I1,1X,2ES24.16,1X,I4)') 'CUT',
     +      MODE,DBLE(VECT(7)),DBLE(DESTEP),ISTOP
      ENDDO
      WRITE(*,'(A,1X,3ES24.16)') 'CUTERRORS',CUTERR
      CONTAINS
      SUBROUTINE RESET(E,D,P,CG,CE,IC)
      DOUBLE PRECISION E,D(3),P(3),CG,CE
      INTEGER IC
      VECT(1:3)=0.
      VECT(4:6)=REAL(D)
      VECT(7)=REAL(E)
      GETOT=REAL(E)
      GEKIN=REAL(E)
      DESTEP=0.
      NGKINE=0
      ISTOP=0
      NAMEC=0
      GKIN(:,1)=0.
      GPOS(:,1)=0.
      CUTGAM=REAL(CG)
      CUTELE=REAL(CE)
      ICOMP=IC
      POLAR=REAL(P)
      END SUBROUTINE
      END
'''

RNG = r'''      SUBROUTINE GRNDM(R,N)
      REAL R(N)
      INTEGER N,I
      INTEGER*8 SEED,NCALLS
      COMMON/BENCHRNG/SEED,NCALLS
      DOUBLE PRECISION X
      DO I=1,N
         SEED=MOD(16807_8*SEED,2147483647_8)
         NCALLS=NCALLS+1
         X=DBLE(SEED)/2147483647D0
         R(I)=MIN(1.-EPSILON(1.),MAX(TINY(1.),REAL(X)))
      ENDDO
      END
      SUBROUTINE G3EKBIN
C     Explicit standalone bookkeeping shim; not a material transport run.
      RETURN
      END
'''


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def integrate_kn(a,b,E,me,nodes):
    x,w=np.polynomial.legendre.leggauss(nodes);x=(b-a)*x/2+(a+b)/2
    r=1/(1+E/me*(1-x));weight=r*r*(r+1/r-1+x*x)
    return float((b-a)/2*np.dot(w,weight)),float((b-a)/2*np.dot(w,weight*r))


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--contract',required=True,type=Path)
    ap.add_argument('--output',required=True,type=Path)
    args=ap.parse_args();cfg=json.loads(args.contract.read_text())
    assert cfg['identity']=='GEANT3-G3COMP-COMPONENT-BENCHMARK-01'
    root=Path(__file__).resolve().parents[2];build=root/'tmp/day16-geant3-producer/component-build'
    build.mkdir(exist_ok=True)
    files=[]
    for record in cfg['source_files']:
        original=root/record['local'];assert original.resolve().is_relative_to(root)
        assert sha(original)==record['sha256']
        data=original.read_bytes();blob=hashlib.sha1(('blob '+str(len(data))+'\0').encode()+data).hexdigest()
        assert blob==record['git_blob_sha1']
        dest=build/record['source_path'];dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        files.append({'path':record['source_path'],'sha256':sha(dest),'unmodified':True})
    driver=build/'component-driver.F';driver.write_text(DRIVER)
    rng=build/'component-shims.F';rng.write_text(RNG)
    exe=build/'component-benchmark';compiler=shutil.which('gfortran');assert compiler
    command=[compiler,'-cpp','-DCERNLIB_UNIX','-std=legacy','-ffixed-line-length-none','-O2','-I',str(build),
        str(driver),str(rng),*[str(build/x) for x in ['gphys/gcomp.F','gphys/gfang.F','gphys/gdrot.F']],'-o',str(exe)]
    compile_result=subprocess.run(command,cwd=root,capture_output=True,text=True)
    record={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'contract_sha256':sha(args.contract),'source_files':files,'compile':{'command':command,
        'exit_code':compile_result.returncode,'stdout':compile_result.stdout,'stderr':compile_result.stderr},
        'compiler_version':subprocess.check_output([compiler,'--version'],text=True).splitlines()[0],
        'driver_sha256':sha(driver),'shims_sha256':sha(rng)}
    args.output.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    if compile_result.returncode:
        print(compile_result.stderr);raise SystemExit(compile_result.returncode)
    run=subprocess.run([str(exe),str(cfg['events_per_energy']),str(cfg['base_seed'])],cwd=root,capture_output=True,text=True,timeout=90)
    record['execute']={'exit_code':run.returncode,'stdout':run.stdout,'stderr':run.stderr}
    record['executable_sha256']=sha(exe);args.output.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    if run.returncode:print(run.stdout,run.stderr);raise SystemExit(run.returncode)
    result_rows=[];current=None;controls={}
    for line in run.stdout.splitlines():
        fields=line.split();tag=fields[0]
        if tag=='ENERGY':
            current={'index':int(fields[1]),'E_GeV':float(fields[2]),'events':int(fields[3]),'RNG_draws':int(fields[4])};result_rows.append(current)
        elif tag in ['MOMENTS','ERRORS']:current[tag.lower()]=[float(x) for x in fields[1:]]
        elif tag in ['COSBINS','PHIBINS']:current[tag.lower()]=[int(x) for x in fields[1:]]
        elif tag=='PAIRED':controls['POLAR_orthogonal_max_output_difference'],controls['rotated_energy_max_relative_difference'],controls['rotated_cos_max_difference']=[float(x) for x in fields[1:]]
        elif tag=='CUT':controls.setdefault('cut_cases',[]).append({'case':int(fields[1]),'photon_energy_GeV':float(fields[2]),'local_deposit_GeV':float(fields[3]),'ISTOP':int(fields[4])})
        elif tag=='CUTERRORS':controls['cut_energy_relative_errors']=[float(x) for x in fields[1:]]
        else:raise AssertionError(line)
    tol=cfg['kinematic_relative_tolerance'];bound=math.sqrt(math.log(2*cfg['DKW_number_curves']/cfg['diagnostic_family_alpha'])/(2*cfg['events_per_energy']))
    for row in result_rows:
        E=row['E_GeV'];me=cfg['electron_rest_GeV'];edges=np.linspace(-1,1,cfg['cos_theta_bins']+1)
        norm,mean=integrate_kn(-1,1,E,me,512);n256,m256=integrate_kn(-1,1,E,me,256)
        assert abs(norm-n256)<1e-11 and abs(mean-m256)<1e-11
        predicted=np.array([0.]+[integrate_kn(-1,float(x),E,me,128)[0]/norm for x in edges[1:]])
        empirical=np.r_[0,np.cumsum(row['cosbins'])/row['events']]
        cosdiff=float(np.max(abs(empirical-predicted)))
        phi_empirical=np.r_[0,np.cumsum(row['phibins'])/row['events']]
        phidiff=float(np.max(abs(phi_empirical-np.linspace(0,1,17))))
        assert sum(row['cosbins'])==row['events']==sum(row['phibins'])
        assert max(row['errors'])<tol
        assert cosdiff<bound and phidiff<bound
        row.update(analytic_mean_energy_ratio=mean/norm,
            measured_mean_energy_ratio=row['moments'][0],cosCDF_max_difference=cosdiff,
            phiCDF_max_difference=phidiff,predeclared_DKW_diagnostic_bound=bound,
            quadrature256_512_difference=abs(norm-n256),
            simulated_iid_style_diagnostic_not_experimental_confidence=True)
    assert len(result_rows)==3
    assert controls['POLAR_orthogonal_max_output_difference']==0
    assert controls['rotated_energy_max_relative_difference']<tol and controls['rotated_cos_max_difference']<tol
    assert max(controls['cut_energy_relative_errors'])<tol
    record['analysis']={'rows':result_rows,'controls':controls,
        'all_predeclared_component_checks_passed':True,
        'scope':{'unmodified_pinned_three_kernels_only':True,'standalone_RNG_and_EKBIN_shims_explicit':True,
            'not_material_transport_or_1997_GCOMPOL':True,'not_detector_Q_merit_or_nuclear_delta_fit':True,
            'POLAR_field_does_not_make_this_Compton_callpath_polarized':True,
            'transport_cuts_not_electronics_threshold':True,'Day17_uncredited_preview':True}}
    args.output.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'compile_exit':0,'execute_exit':0,'rows':[{k:x[k] for k in ['E_GeV','events','measured_mean_energy_ratio','analytic_mean_energy_ratio','cosCDF_max_difference','phiCDF_max_difference','errors']} for x in result_rows],
        'controls':controls,'DKW_diagnostic_bound':bound},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
