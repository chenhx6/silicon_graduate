#!/usr/bin/env python3
"""Source-keyed branch arithmetic and point-fragment geometry; not a decay model."""
import hashlib
import json
import math
from pathlib import Path
import subprocess

ROOT = Path('/workspace/wiki')
HERE = Path(__file__).parent
YEAR_SECONDS = 365.25 * 86400  # declared conversion convention


def fingerprint(relative, pages_read, url):
    p = ROOT / relative
    b = p.read_bytes()
    info = subprocess.check_output(['pdfinfo', str(p)], text=True)
    n = int(next(x for x in info.splitlines() if x.startswith('Pages:')).split()[-1])
    archived_names = {
        '1107.1478.pdf': 'warda-2011-actinide-cluster-radioactivity-arxiv1107.1478v1.pdf',
        '1311.3810.pdf': 'denisov-2013-multidimensional-cluster-arxiv1311.3810v1.pdf',
    }
    archived_name = archived_names.get(p.name)
    if archived_name is None:
        nuc = p.name.replace('-adopted.pdf', '').lower()
        archived_name = f'nndc-{nuc}-adopted-cluster-20261029.pdf'
    archived = 'raw/papers/gpt/day26-20261028/' + archived_name
    return dict(path=relative, archived_file=archived, url=url, bytes=len(b), signature_hex=b[:8].hex(),
                sha256=hashlib.sha256(b).hexdigest(), pages=n, reading_coverage=pages_read,
                archival_hash_verified=hashlib.sha256((ROOT/archived).read_bytes()).digest()==hashlib.sha256(b).digest())


def branch_row(parent, Ac, Zc, A, Z, half, err, unit, percent, percent_err, locator, hfb):
    scale = {'s': 1, 'd': 86400, 'y': YEAR_SECONDS}[unit]
    t = half * scale
    b = percent / 100
    tp = t / b
    rel = math.hypot(err / half, percent_err / percent)
    return dict(parent=parent, channel=dict(cluster_A=Ac, cluster_Z=Zc,
                   daughter_A=A-Ac, daughter_Z=Z-Zc),
                total_half_life=dict(value=half, uncertainty=err, unit=unit),
                adopted_cluster_percent=percent, adopted_cluster_percent_uncertainty=percent_err,
                branch_fraction=b, partial_half_life_s=tp, log10_partial_half_life_s=math.log10(tp),
                approximate_first_order_partial_uncertainty_s=tp*rel,
                uncertainty_boundary='First-order independent propagation for reporting only; no full covariance or original likelihood available.',
                source_locator=locator,
                warda2011_log10_hfb_s=hfb,
                hfb_minus_adopted_log10_s=hfb-math.log10(tp),
                observed_over_hfb_half_life_ratio=tp/10**hfb)


def geometry(A, Z, Ac, Zc, name):
    Ad, Zd = A-Ac, Z-Zc
    return dict(channel=name, light_A=Ac, light_Z=Zc, heavy_A=Ad, heavy_Z=Zd,
                E1_coefficient_D0_per_eR=Zc-Z*Ac/A,
                E3_coefficient_M30_per_eR3_without_Y30=Zc*(Ad/A)**3-Zd*(Ac/A)**3,
                mass_moment_coefficients={str(l):Ac*(Ad/A)**l+(-1)**l*Ad*(Ac/A)**l for l in (1,3,5,7)},
                boundary='Two nonoverlapping point fragments with fixed A,Z and no internal polarization; coefficients do not measure cluster probability.')


def main():
    rows = [
        branch_row('222Ra',14,6,222,88,33.6,.4,'s',3e-8,1e-8,'NNDC 222Ra Adopted PDF2, ground-state comment',8.90),
        branch_row('224Ra',14,6,224,88,3.6316,.0023,'d',4e-9,1e-9,'NNDC 224Ra Adopted PDF1, ground-state comment',15.06),
        branch_row('226Ra',14,6,226,88,1600,7,'y',3.2e-9,1.6e-9,'NNDC 226Ra Adopted PDF1, ground-state comment',18.98),
        branch_row('228Th',20,8,228,90,1.9116,.0016,'y',1.13e-11,.22e-11,'NNDC 228Th Adopted PDF1, ground-state comment',19.53),
    ]
    fs = []
    for A, sym, coverage in [(222,'Ra','PDF2, ground-state T1/2 and 14C branch'),(224,'Ra','PDF1, ground-state T1/2 and 14C branch'),(226,'Ra','PDF1, ground-state T1/2 and 14C branch'),(226,'Th','PDF1, no cluster branch assigned in acquired Adopted table'),(228,'Th','PDF1, ground-state T1/2 and 20O branch')]:
        fs.append(fingerprint(f'tmp/day26-act-th/{A}{sym}-adopted.pdf',coverage,f'https://www.nndc.bnl.gov/ensnds/{A}/{sym}/adopted.pdf'))
    fs += [fingerprint('tmp/day26-cluster/1107.1478.pdf','PDF1–5, PDF10–13, PDF15–17; Eqs2–7, Figs1–3 and10, Table I, EDF limitations','https://arxiv.org/pdf/1107.1478v1'),
           fingerprint('tmp/day26-cluster/1311.3810.pdf','PDF1–2, PDF5–10; Eqs21–31, least-action mechanism and 228Th comparison','https://arxiv.org/pdf/1311.3810v1')]
    out = dict(schema='octupole-cluster-radioactivity-boundary/v1',status='bounded-source-self-audit',
               knowledge_note='knowledge/research-notes/octupole-cluster-radioactivity-preformation-boundary.md',
               year_conversion_seconds=YEAR_SECONDS,experimental_branch_arithmetic=rows,
               th226_boundary=dict(requested_channel='226Th -> 206Pb + 20O',
                    experimental_benchmark_status='No positive measured branch established by the acquired Adopted table or cited HFB paper.',
                    documented_comparison_channel='226Th -> 208Pb + 18O',
                    documented_log10_partial_half_life_lower_limit_s=16.76,
                    documented_partial_half_life_lower_limit_s=10**16.76,
                    hfb_log10_partial_half_life_s=17.31,
                    source='Warda2011 PDF13 Table I; original experiment Ref21 not reread.'),
               theory_cross_checks=dict(
                    warda224Ra_ground_state=dict(beta2=.18,beta3=.14,Q20_b=8.3,Q30_b_three_half=4.2,locator='Warda2011 PDF5, SecIII'),
                    warda224Ra_scission=dict(Q30_b_three_half=28,neck_density_fm_minus3=.09,transferred_nucleons_between_neck_configurations=4.9,locator='Warda2011 PDF12–13, Fig10'),
                    denisov228Th=dict(calculated_partial_half_life_s=5e20,reported_experimental_partial_half_life_s=5.29e20,reported_experimental_uncertainty_s=1.01e20,preformation_factor_assumed=1,locator='Denisov2013 PDF6 Eq21–24 and PDF9')),
               fragment_geometry=[geometry(222,88,14,6,'222Ra -> 208Pb + 14C'),geometry(224,88,14,6,'224Ra -> 210Pb + 14C'),geometry(226,88,14,6,'226Ra -> 212Pb + 14C'),geometry(228,90,20,8,'228Th -> 208Pb + 20O'),geometry(226,90,20,8,'226Th -> 206Pb + 20O; hypothetical comparison'),geometry(226,90,18,8,'226Th -> 208Pb + 18O; lower-limit channel')],
               inferred_preformation_probabilities=None,
               measured_beta5_beta7=None,
               rejected_universal_claims=['A larger ground-state beta3 necessarily increases cluster P0.','beta5 or beta7 has a universal positive enhancement factor.','A small E1 or D0 implies a small cluster formation amplitude.','GCM collective weights equal a cluster projector probability.','226Th 20O is an established positive experimental benchmark.'],
               retrieval_limitations=[dict(resource='Sawhney et al. PhysRevC83 064610 (2011)',doi='10.1103/PhysRevC.83.064610',metadata='title/authors verified with Crossref; publisher PDF 403, APS harvest401; not used for any quantitative beta5/beta7 claim')],
               fingerprints=fs,no_credit_or_deadline_change=True,commit_push='not performed')
    (HERE/'octupole-cluster-radioactivity-boundary.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    for r in rows:
        print(r['parent'],f"b={r['branch_fraction']:.5g}",f"Tpartial={r['partial_half_life_s']:.6g} s",f"log10={r['log10_partial_half_life_s']:.6f}")

if __name__ == '__main__':
    main()
