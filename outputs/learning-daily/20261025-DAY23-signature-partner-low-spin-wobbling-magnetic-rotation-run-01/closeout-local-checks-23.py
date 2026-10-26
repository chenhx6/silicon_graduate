"""Actual effective-deadline guarded report and verification; no credit mutation."""
from pathlib import Path
import sys,json,re,datetime,subprocess,os,hashlib
root=Path.cwd();sys.path.insert(0,str(root/'system/scripts'))
import run_daily_learning as runner
from wiki_learning_deadline import resolve_deadline_info,resolve_baseline_knowledge
b=root/'outputs/learning-daily/20261025-DAY23-signature-partner-low-spin-wobbling-magnetic-rotation-run-01';p=b.parent/'20261025-DAY23-signature-partner-low-spin-wobbling-magnetic-rotation.md';r=json.loads((b/'run.json').read_text());info=resolve_deadline_info(b/'run.json',r,root);now=datetime.datetime.now(runner.TIMEZONE)
assert os.environ.get('CODEX_SESSION_ID')==r['session_id'];assert info['effective_deadline']<=now<info['effective_closeout_end'];assert r['status']=='running'
statep=root/'outputs/learning-milestones/2026-09-one-month-state.json';state=json.loads(statep.read_text());assert state['next_day_index']==23 and state['completed_day_count']==22
before=b/'curriculum-state-before-closeout-23.json'
if not before.exists():before.write_text(json.dumps({'observed_at':now.isoformat(),'state':state},ensure_ascii=False,indent=2)+'\n')
s=p.read_text();s=re.sub(r'^# Day23：.*$', '# Day23：旋称伙伴、低自旋wobbling与磁转动（正式交付；133Ce重要补充）',s,flags=re.M);s=s.replace('- completed_day_indices: []','- completed_day_indices: [23]',1).replace('- partial_day_indices: [23, 24]','- partial_day_indices: [24]',1).replace('- status: active-checkpoint','- status: closeout-deliverables-complete (formal result in final-session-receipt-23.json)',1)
s=s.replace('当前继续研究；用户最新明确授权必要时约17:00开始收束，已采用该延长并保留原15:00记录，未授Day23学分。','研究已于明确授权effective17:00截止转收束；本节完成交付审计，正式信用仍以原runner finalizer及card-credit-23回执为准，原15:00历史保留。')
a=s.index('### Day 23 card progress audit');z=s.index('## Candidate pool and selection',a)
s=s[:a]+'''- Day 23 card audit: complete
- closeout_event_id: `closeout`

### Day 23 card completion audit

| Day23 matrix deliverable | Evidence/artifact | status |
|---|---|---|
| 回忆五机制并区分pseudospin | [[signature-partner-bands]]、[[magnetic-rotation]]、[[antimagnetic-rotation]]及本报告primed回忆；非盲测分数 | complete |
| 三anchor原件主线与实际缺口 | [[guo-2022-low-spin-wobbling-187au]] GU22-D23-001/002；[[lv-2022-evidence-against-wobbling-135pr]] L22-D23-001；[[signature-partner-bands]] Definition | complete |
| 支持—反证—依赖矩阵 | [[low-spin-wobbling-controversies]] Day23谱系/矩阵；[[signature-tip-shears-discrimination-contract]] 同线向量/派生秩/定标/真实新增观测 | complete |
| 冻结实测层的组态替代 | [[signature-tip-shears-discrimination-contract]] 冻结D与fixed-H mapping；[[133ce-thesis-analysis-blueprint]] WK22-33；run内configuration-reassignment-064 | complete |
| 争议谱系图与可证伪问题 | [[low-spin-wobbling-controversies]] Mermaid谱系；[[187au-longitudinal-wobbling-controversy]] 定标/同门身份与holdout问题；真实response/ledger缺口保留 | complete |
| 用户指定的重要学位论文补充 | [[133ce-thesis-analysis-blueprint]]及WK22-01–34；[[nobs-2017-spin-parity-102y-thesis]]；Ce正文逐段读本、模型/EM/BCS/投影、131/133分析迁移，长期课题未冒结项 | complete |

本卡交付完成不等于争议终结或所有真实L4输入就绪。只申请Day23一张正式卡；Day24已有知识仅partial[24]，下一prompt为准备且含133Ce附属问题，不创建新session/Day25或给预习学分。

'''+s[z:]
s=s.replace('## Verification and continuation\n','## Verification and continuation\n\n已到用户授权effective17:00，停止新增研究，进入同session收束。closeout-local-checks/原runner最终门、正式回执和H3依次实际执行；以下checkpoint为过程历史，不覆盖本次最终状态。\n',1);p.write_text(s)
kb,provenance=resolve_baseline_knowledge(b,r,root);results={}
for name,cmd in [('boundary',[sys.executable,'system/scripts/wiki_boundary_check.py','--root','.']),('lint',[sys.executable,'system/scripts/wiki_lint.py','--fail-on','error']),('diff',['git','diff','--check'])]:
 x=subprocess.run(cmd,capture_output=True,text=True);results[name]={'argv':cmd,'exit_code':x.returncode,'stdout_tail':x.stdout[-2200:],'stderr_tail':x.stderr[-1000:]};(b/f'check-{name}-closeout.stdout').write_text(x.stdout);(b/f'check-{name}-closeout.stderr').write_text(x.stderr);print(name,x.returncode,flush=True);assert x.returncode==0,results[name]
contracts={'report':runner.validate_report(p),'writeback':runner.validate_durable_knowledge(p,root,kb),'coverage':runner.validate_curriculum_coverage(p,23)};assert all(x['valid'] for x in contracts.values()),contracts;assert contracts['coverage']['completed_day_indices']==[23] and contracts['coverage']['partial_day_indices']==[24]
baseline=json.loads((b/'baseline-001.json').read_text());protected={q:hashlib.sha256((root/q).read_bytes()).hexdigest()==h for q,h in baseline['protected'].items()};assert all(protected.values())
out={'observed_at':datetime.datetime.now(runner.TIMEZONE).isoformat(),'scope':'actual local closeout checks and atomic report/writeback/card mapping only; substantive controls and105governance tests already passed064; no whole-library/experimental certification','commands':results,'runner_contracts':contracts,'baseline_provenance':provenance,'protected_unchanged':protected,'writeback_items':len(json.loads(re.search(r'```knowledge-writeback\n(.*?)\n```',p.read_text(),re.S)[1])['items']),'status':'passed'};(b/'required-checks-closeout-23.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
att={'status':'closeout-turn-completed','run_id':r['run_id'],'session_id':r['session_id'],'closeout_event_id':'closeout','hard_deadline':info['effective_deadline'].isoformat(),'original_hard_deadline':info['original_deadline'].isoformat(),'deadline_override_sha256':info['override_sha256'],'closeout_at':datetime.datetime.now(runner.TIMEZONE).isoformat(),'report_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'window_missed':False,'time_snapshot':runner.closeout_snapshot(datetime.datetime.now(runner.TIMEZONE),info['effective_deadline'],runner.next_scheduled_start_for_run_date(r['run_date'])),'scientific_scope':'Day23 deliverables complete; explicit actualinput/scientific unresolved boundaries retained'};(b/'interactive-closeout-attestation.json').write_text(json.dumps(att,ensure_ascii=False,indent=2)+'\n');print('local checks and genuine closeout attestation complete; finalizer/state still separate')
