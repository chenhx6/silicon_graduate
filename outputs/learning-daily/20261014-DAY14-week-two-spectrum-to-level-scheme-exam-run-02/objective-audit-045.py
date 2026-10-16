#!/usr/bin/env python3
"""Recheck existing DAY14 deliverables; do not open a new research route or card."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib
import json
import re
import subprocess
import sys
import yaml
import pymupdf

ROOT = Path(__file__).resolve().parents[3]
RUN = Path(__file__).resolve().parent
REPORT = ROOT / 'outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam.md'
sys.path.insert(0, str(ROOT / 'system/scripts'))
import run_daily_learning as runner

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)

def frontmatter(s):
    return yaml.safe_load(s.split('---', 2)[1]) if s.startswith('---') else {}

def claim_flags(s):
    out = {}
    for line in s.splitlines():
        if re.match(r'^\|\s*[A-Z][A-Za-z0-9_-]*-\d+\s*\|', line):
            cells = [v.strip() for v in line.split('|')[1:-1]]
            if cells[-1] in ('true', 'false'):
                out[cells[0]] = cells[-1]
    return out

baseline = json.loads((RUN / 'entry-baseline.json').read_text())
run = json.loads((RUN / 'run.json').read_text())
report = REPORT.read_text()
checks, evidence = {}, {}
checks['report_headings'] = runner.validate_report(REPORT)['valid']
coverage = runner.validate_curriculum_coverage(REPORT, 14)
checks['formal14_only_partial15'] = coverage['valid'] and coverage['completed_day_indices'] == [14] and coverage['partial_day_indices'] == [15]
wb = runner.validate_durable_knowledge(REPORT, ROOT, baseline['knowledge_snapshot'])
blocks = re.findall(r'(?ms)^```knowledge-writeback[ \t]*\n(.*?)^```[ \t]*$', report)
writeback = json.loads(blocks[0]) if len(blocks) == 1 else {}
checks['one_atomic_grounded_writeback'] = len(blocks) == 1 and wb['valid']
checks['156items_44_changed_pages'] = len(writeback.get('items', [])) == 156 and len(wb['changed_paths']) == 44
paths = sorted({x['knowledge'] for x in writeback['items']})
review_differences, flag_differences, new_flag_issues = [], [], []
for path in paths:
    cur = (ROOT / path).read_text()
    current = frontmatter(cur)
    old = git('show', baseline['head'] + ':' + path)
    if old.returncode == 0:
        previous = frontmatter(old.stdout)
        for field in ('review_status', 'human_reviewed', 'human-reviewed', 'human_review', 'needs_review'):
            if current.get(field) != previous.get(field):
                review_differences.append([path, field, previous.get(field), current.get(field)])
        before_flags = claim_flags(old.stdout)
    else:
        before_flags = {}
        if current.get('review_status') == 'human-reviewed':
            new_flag_issues.append([path, 'new human-reviewed page'])
    if path.startswith('knowledge/sources/'):
        now_flags = claim_flags(cur)
        for cid, flag in before_flags.items():
            if now_flags.get(cid) != flag:
                flag_differences.append([path, cid, flag, now_flags.get(cid)])
        for cid in now_flags.keys() - before_flags.keys():
            if now_flags[cid] != 'true':
                new_flag_issues.append([path, cid, now_flags[cid]])
checks['all_existing_review_status_preserved'] = not review_differences
checks['all_old_claim_flags_preserved'] = not flag_differences
checks['new_source_claims_need_review'] = not new_flag_issues
evidence['review_audit'] = dict(review_differences=review_differences, flag_differences=flag_differences, new_flag_issues=new_flag_issues)

recall = RUN / 'active-recall-before-sources.md'
first_commit = run['publications'][0]['commit']
frozen = git('show', first_commit + ':' + recall.relative_to(ROOT).as_posix())
checks['recall_frozen_since_initial_publication'] = frozen.returncode == 0 and frozen.stdout == recall.read_text()
checks['recall_priming_and_original_timestamp'] = 'primed recall' in recall.read_text() and '2026-10-14T19:04:11.200337+08:00' in recall.read_text()
evidence['recall'] = dict(path=recall.relative_to(ROOT).as_posix(), sha256=sha(recall), locator='三层级联与门（先写后查）')

fixture = json.loads((RUN / 'level-scheme-fixture.json').read_text())
checks['anchor_raw_hash'] = sha(ROOT / fixture['raw_file']) == fixture['raw_sha256']
doc = pymupdf.open(ROOT / fixture['raw_file'])
checks['anchor_twenty_pages'] = len(doc) == 20
rows = {
    'L323.4': (3, ['323.4(1)', '1000(57)', '929', '15/2+', '13/2+', '0.74(4)', '−0.012(1)', 'M1']),
    'L299.2': (3, ['299.2(1)', '258(8)', '1228', '17/2+', '15/2+', '0.68(2)', '−0.032(1)', 'M1']),
    'L327.4': (3, ['327.4(1)', '196(6)', '1556', '19/2+', '17/2+', '0.68(2)', '−0.004(1)', 'M1']),
    'L319.8': (7, ['319.8(1)', '125(4)', '1875', '21/2+', '19/2+', '0.60(2)', '−0.039(2)', 'M1']),
    'L622.4': (3, ['622.4(1)', '121(5)', '1228', '17/2+', '13/2+', '1.30(16)', '0.086(10)', 'E2']),
    'L626.2': (3, ['626.2(1)', '102(4)', '1556', '19/2+', '15/2+', '1.48(6)', '0.094(9)', 'E2']),
    'L646.9': (3, ['646.9(1)', '108(4)', '1875', '21/2+', '17/2+', '1.47(6)', '0.091(4)', 'E2']),
}
row_evidence = []
for tr in fixture['transitions']:
    page, expected = rows[tr['id']]
    lines = doc[page-1].get_text().splitlines()
    i = lines.index(expected[0])
    got = lines[i:i+8]
    checks['direct_original_table_' + tr['id']] = got == expected
    row_evidence.append(dict(transition=tr['id'], page=page, cells=got, source=fixture['source'], locator=tr['locator']))
evidence['table_rows_directly_rechecked'] = row_evidence
figure_text = doc[7].get_text()
checks['figure2_five_labels_present'] = all(str(l['rounded_keV']) in figure_text for l in fixture['levels']) and 'FIG. 2.' in figure_text
checks['3198_in_other_transitions'] = doc[6].get_text().index('Other transitions') < doc[6].get_text().index('319.8(1)')
checks['doublet_footnote_real_counterevidence'] = 'ordering of these two transitions is not clear' in doc[6].get_text().replace('\n', ' ')
evidence['visual_recheck'] = ['PDF p.3 Table I', 'PDF p.7 Table I / footnote f', 'PDF p.8 Figure 2 (rotated)']
recheck = ROOT / 'tmp/day14-20261014/formal-level-scheme-recheck-045.json'
cmd = [sys.executable, 'system/scripts/day14_level_scheme_audit.py', '--fixture', str(RUN / 'level-scheme-fixture.json'), '--output', str(recheck)]
calc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
original = json.loads((RUN / 'level-scheme-analysis.json').read_text())
again = json.loads(recheck.read_text()) if calc.returncode == 0 else {}
checks['formal35_rerun_exit0'] = calc.returncode == 0 and again.get('checks_passed') == 35 and all(again['checks'].values())
checks['formal_analysis_semantically_frozen'] = original == again
evidence['formal_reconstruction'] = dict(command=cmd, exit_code=calc.returncode, checks_passed=again.get('checks_passed'), original_sha256=sha(RUN / 'level-scheme-analysis.json'), fixture_sha256=sha(RUN / 'level-scheme-fixture.json'))

method = (ROOT / 'knowledge/methods/level-scheme-reconstruction.md').read_text()
section = method.split('## Day14 五能级七跃迁逐边审计\n', 1)[1].split('\n## ', 1)[0]
checks['seven_explicit_ECMJ_rows'] = sum(1 for l in section.splitlines() if re.match(r'^\| (323\.4|299\.2|327\.4|319\.8|622\.4|626\.2|646\.9)\(1\)', l)) == 7 and 'E 表示' in section and 'C 表示' in section and 'M 表示' in section and 'J 表示' in section
checks['companion_and_independence_boundaries'] = all(t in method for t in ['标定、寿命与伴随观测的逐项契约', '153(10)', '并非七条独立实验', 'parent', 'ICC', 'δ'])
checks['experimental_criteria_matrix'] = '### 实验判据矩阵' in report and all(t in report for t in ['emitter/line identity','placement/order','multipolarity','configuration/shape/mode'])
scorepart = report.split('## Day 14 scorecard\n', 1)[1].split('\n## ', 1)[0]
scores = re.findall(r'^\| (理论|判图|误差|证据分层|反证|可证伪问题) \| ([0-4]) \|', scorepart, re.M)
checks['six_dimensions_each0to4_sum21'] = len(scores) == 6 and sum(int(v) for _, v in scores) == 21
reflect = report.split('## Day 14 weekly REFLECT\n', 1)[1].split('\n## ', 1)[0]
checks['weekly_reflect_substantive'] = len(reflect.strip()) > 200 and '第二周证据链的可复用认识修正' in method
weekly = (ROOT / 'outputs/learning-weekly/20261014-week-two-spectrum-to-level-scheme-reflect.md').read_text()
checks['weekly_extension_metadata_current'] = '2026-10-16 15:00' in weekly and '21/24' in weekly
checks['card_audit_minimum4_deliverables_complete'] = len(re.findall(r'^\|.*\| complete \|$', report.split('### Day 14 card completion audit', 1)[1].split('\n## ',1)[0], re.M)) >= 4

ding = ROOT / 'knowledge/sources/ding-2012-phd-thesis-127-128i-high-spin.md'
dingt = ding.read_text()
dingdoc = pymupdf.open(ROOT / 'raw/papers/degree dissertation/丁兵 - 博士论文.pdf')
cover = re.sub(r'\s+', '', dingdoc[0].get_text())
checks['ding_cover_submission_april_defense_may'] = '论文提交日期2012年4月' in cover and '论文答辩日期2012年5月' in cover and '论文提交日期：2012 年 4 月；论文答辩日期：2012 年 5 月' in dingt and '| D12-36 |' in dingt
base045 = json.loads((RUN / 'baseline-045.json').read_text())
dingold = git('show', base045['HEAD'] + ':' + ding.relative_to(ROOT).as_posix()).stdout
oldrows = [l for l in dingold.splitlines() if re.match(r'^\| D12-\d+ \|',l)]
checks['ding_prior35_rows_exact'] = len(oldrows)==35 and all(l in dingt.splitlines() for l in oldrows)
evidence['metadata_correction'] = dict(knowledge=ding.relative_to(ROOT).as_posix(), locator='D12-36', original_page='PDF p.1 cover', raw_sha256=sha(ROOT / 'raw/papers/degree dissertation/丁兵 - 博士论文.pdf'))

checks['PLAN_Bib_protected_hashes'] = all(sha(ROOT / p) == h for p, h in baseline['protected_hashes'].items())
raw_now = {p.relative_to(ROOT).as_posix(): [p.stat().st_size,p.stat().st_mtime_ns] for p in (ROOT/'raw').rglob('*') if p.is_file()}
checks['all_raw_metadata_preserved'] = raw_now == baseline['raw_metadata']
checks['same_session_thread_started'] = json.loads((RUN/'events.jsonl').read_text().splitlines()[0])['thread_id'] == run['session_id'] == '01a13a0e-e8bd-7251-b970-f6975679e281'
checks['only_actual_four_clock_acknowledgements'] = {x['clock_event_id'] for x in run['observed_clock_executions']} == {'checkpoint-001','checkpoint-002','checkpoint-005','checkpoint-008'}
checks['user_extension_research_and_delivery_split'] = run['planned_research_cutoff_at'] == '2026-10-16T15:00:00+08:00' and run['overnight_until'] == '2026-10-16T16:00:00+08:00'
ext = json.loads((RUN/'scheduler-extension-event.json').read_text())
checks['actual_extension_scheduler_event_preserved'] = ext['event'] in [json.loads(l) for l in (ROOT/ext['path']).read_text().splitlines() if l.strip()]
nextp = ROOT / 'outputs/learning-daily/prompts/20261016-DAY15-ado-angular-distribution-geometry.md'
nexts = nextp.read_text()
checks['next_prompt_actual_date_and_no_credit'] = '`run_date`: 2026-10-16' in nexts and '`window_closeout_at`: 2026-10-17T15:00:00+08:00' in nexts and '不启动会话、不计课程学分' in nexts and 'priming' in nexts
state = json.loads((ROOT/'outputs/learning-milestones/2026-09-one-month-state.json').read_text())
checks['course_not_advanced_before_closeout'] = state['next_day_index'] == 14 and state['completed_day_count'] == 13
publication_issues = []
for i in range(1,45):
    p = RUN/f'publication-{i:03d}.json'
    rec = json.loads(p.read_text())
    if rec.get('outcome') != 'published' or run['publications'][i-1].get('outcome') != 'published':
        publication_issues.append(p.name)
checks['44_prior_publications_have_success_receipts'] = not publication_issues
evidence['publication_issues'] = publication_issues
result = dict(at=datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(), run_id=run['run_id'], session_id=run['session_id'], scope='核验既有正式Day14与收束准备；不新开来源或课程卡', checks=checks, checks_passed=sum(checks.values()), checks_total=len(checks), all_passed=all(checks.values()), evidence=evidence, report=runner.validate_report(REPORT), coverage=coverage, writeback=wb, source_count_not_experiment_count=True, no_course_credit_changed=True, formal_score=21)
(RUN/'objective-audit-045.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(at=result['at'], checks_passed=result['checks_passed'], checks_total=len(checks), failed=[k for k,v in checks.items() if not v]),ensure_ascii=False))
sys.exit(0 if all(checks.values()) else 1)
