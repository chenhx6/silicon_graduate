"""Manual reconciliation for the explicit user extension; no scheduler emulation."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib,json,re,subprocess,sys
root=Path.cwd().resolve();sys.path.insert(0,str(root/'system/scripts'))
import run_daily_learning as runner
r=root/'outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02'
report=root/'outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam.md'
state_path=root/'outputs/learning-milestones/2026-09-one-month-state.json'
cutoff=datetime.fromisoformat('2026-10-16T15:00:00+08:00');delivery=datetime.fromisoformat('2026-10-16T16:00:00+08:00')
now=lambda:datetime.now(ZoneInfo('Asia/Shanghai'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
run=json.loads((r/'run.json').read_text());base=json.loads((r/'entry-baseline.json').read_text())
assert run['run_id']=='2026-10-14-day-14-02' and run['session_id']=='01a13a0e-e8bd-7251-b970-f6975679e281'
assert cutoff<=now()<=delivery,'Only execute in the user-authorized closeout hour'
assert run['planned_research_cutoff_at']==cutoff.isoformat() and run['overnight_until']==delivery.isoformat()
assert run['status']=='running','Stop and inspect an existing closing/completed receipt; never repeat credit blindly'
assert json.loads((r/'publication-045.json').read_text())['outcome']=='published'
assert json.loads((r/'objective-audit-045.json').read_text())['all_passed']
assert all(sha(root/p)==h for p,h in base['protected_hashes'].items())
raw={p.relative_to(root).as_posix():[p.stat().st_size,p.stat().st_mtime_ns] for p in (root/'raw').rglob('*') if p.is_file()}
assert raw==base['raw_metadata']
state=json.loads(state_path.read_text());assert state['next_day_index']==14 and state['completed_day_count']==13
state_before_sha=sha(state_path)
observed=now().isoformat()
run.update(status='closing-out',research_status='closed-at-user-extended-cutoff',execution_status='same-session-manual-closeout',research_stopped_at=observed,research_stop_reason='User-extended research cutoff reached; final phase contains verification/receipt/credit/publication only',completion_mode='authorized-extension-same-session-manual-reconciliation',original_runner_exit_code=None,original_runner_exit_code_note='No successful terminal original CLI result was observed; manual checks are recorded separately',last_checkpoint_at=observed)
run['last_closeout_snapshot']={'now_local':observed,'hard_deadline':delivery.isoformat(),'planned_research_cutoff_at':cutoff.isoformat(),'decision':'closeout-only; no research or new source/card'}
write(r/'run.json',run)
s=report.read_text();s=re.sub(r'(?m)^- research_status:.*$',f'- research_status: closed-at-user-extended-cutoff；实际收束观察 `{observed}`；15:00后仅核验、回执、课程对账和发布。',s,count=1)
s+='''\n\n### 最终收束（用户授权加时）\n\n研究截止2026-10-16 15:00上海已实际观察。当前会话沿用原run/session，未重新启动每日调度器；原runner没有可核的成功退出码，本次采用明确标注的手动对账，不伪造normal-runner或clock-closeout事件。既有分析核验于13:41完成，后续前台监督等待逐条记录在[监督日志](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/window-supervision-045.jsonl)，等待不计研究成果。\n\n正式Day14完成：Herzáň原图/表的五节点七跃迁、逐边E/C/M/J证据、35项重建检查、实验判据矩阵、六维自评21/24和weekly REFLECT；来源前回忆明确受Day13 priming影响。最终整体审计41/41，唯一knowledge-writeback156项、44份修改知识页。可复用的方法与证据留在knowledge，全部科学内容已通过前批显式发布。\n\n保留的实质边界是128I原文与评价的102-keV placement/ECC绑定冲突，以及实际gate、δ、响应和协方差缺口；未读2012正文、未完成事件级L4重拟合，没有新的spin/B值或模式裁决。Day15只列partial，不给学分；下一正式入口为20261016 Day15 prompt，未启动Day15。最终课程只计14一次至next15/count14。\n\n最终检查实际退出码、警告分类、状态前后值、报告哈希与发布文件清单分别保存在[最终验收](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/final-checks-046.json)、[课程对账](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/course-state-reconciliation-046.json)与[最终发布清单](20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/publication-manifest-046.json)。最终稳定指针为main / `Complete DAY14 extended study and credit only Day14`，精确hash与真实push结果只写本run回执。\n'''
report.write_text(s)
# Checks against the pre-credit state. Required tools are not emulated.
pre={}
def command(name,args):
 c=subprocess.run(args,cwd=root,capture_output=True,text=True,timeout=180)
 (r/(name+'.txt')).write_text(c.stdout+c.stderr)
 return {'command':args,'exit_code':c.returncode,'log':(r/(name+'.txt')).relative_to(root).as_posix(),'stdout':c.stdout,'stderr':c.stderr}
for name,args in [('boundary-final-precredit-046',['python3','system/scripts/wiki_boundary_check.py','--root','.']),('lint-final-precredit-046',['python3','system/scripts/wiki_lint.py','--fail-on','error']),('diff-final-precredit-046',['git','diff','--check'])]:
 pre[name]=command(name,args);assert pre[name]['exit_code']==0,(name,pre[name]['stderr'])
coverage=runner.validate_curriculum_coverage(report,14);wb=runner.validate_durable_knowledge(report,root,base['knowledge_snapshot'])
assert runner.validate_report(report)['valid'] and coverage['valid'] and wb['valid']
assert coverage['completed_day_indices']==[14] and coverage['partial_day_indices']==[15]
nextp=root/'outputs/learning-daily/prompts/20261016-DAY15-ado-angular-distribution-geometry.md';assert nextp.exists()
assert (r/'continuation-prompt.md').exists() and '21/24' in report.read_text()
# Only this original, verified pre-credit state may be advanced once.
assert sha(state_path)==state_before_sha
updated=runner.update_state_for_curriculum_cards(state,run['run_id'],run['run_date'],coverage)
assert updated['next_day_index']==15 and updated['completed_day_count']==14 and updated['last_run_id']==run['run_id']
write(state_path,updated)
reconciliation={'at':now().isoformat(),'method':'run_daily_learning.update_state_for_curriculum_cards pure function; guarded once from next14/count13','before':state,'before_sha256':state_before_sha,'after':updated,'after_sha256':sha(state_path),'credit_delta':1,'credited_day_indices':[14],'partial_day_indices':[15],'Day15_credit':False,'course_status':updated['status'],'last_success_semantics':'logical run_date 2026-10-14, despite user-authorized Oct16 closeout','precredit_required_exit_codes':{k:v['exit_code'] for k,v in pre.items()}}
write(r/'course-state-reconciliation-046.json',reconciliation)
# Final user-facing execution metadata. Scientific content is already frozen.
s=report.read_text().replace('- course_credit: 尚未推进；需report/writeback/checks/continuation/publication通过后才计Day14，持续研究不重复计卡。','- course_credit: 已按最终审计一次只计Day14；next_day_index=15、completed_day_count=14。Day15仍为无学分预习。')
report.write_text(s)
weekly=root/'outputs/learning-weekly/20261014-week-two-spectrum-to-level-scheme-reflect.md';t=weekly.read_text().replace('正式卡完成后继续同session学习，当前仍待最终回执、检查与课程状态对账。','正式卡完成后继续同session学习，现已到研究截止并完成最终交付审计；课程只计Day14，next15/count14，Day15仍为无学分预习。');weekly.write_text(t)
cont='''# DAY14 已完成：同session只交付或讨论既有成果\n\n先读run.json核对最终状态。Run2026-10-14-day-14-02/session01a13a0e-e8bd-7251-b970-f6975679e281；用户断网加时研究2026-10-16 15:00上海止、16:00前交付。不要由Farmer/clock旧提醒重开研究，不新建session/goal/daemon。\n\nResume `codex resume 01a13a0e-e8bd-7251-b970-f6975679e281 -C /workspace/wiki -s danger-full-access -a never`。正式Day14：primed冻结回忆、Herzáň20页一图一表、七边35checks、判据矩阵、六维21/24、weekly REFLECT；整体审计41/41，唯一writeback156项44份修改知识页，旧review/raw/PLAN/Bib保留。D12-36只纠正封面提交4月/答辩5月。\n\n课程已只计14一次至next15/count14；completed14/partial15。Day15正式入口outputs/learning-daily/prompts/20261016-DAY15-ado-angular-distribution-geometry.md仅准备，未启动Day15。其正式run须新session和自身primed回忆；不能把本次预习当正式学分，当前不打开Day16。\n\n2012 PRC86,034302正文未得；Ding/CPL与ENSDF2015的102/ECC绑定冲突、actualgate/δ/finiteQ/Σ仍未裁决。所有反事实/条件计算不等新实验spin/B或L4重拟合，不重试相同失败访问。\n\n最终门/课程前后值/实际发布见final-checks-046.json、course-state-reconciliation-046.json、publication-046.json与run.json。标准normalfinalizer不支持此用户延期，已做真实时间同session手动对账，未伪造clock ledger或原runnerexit0。恢复时若publication失败，只处理已授权本地提交的H3重试与交付；不重计卡。Preserve inheritedDay6–9/Day13/log/daemon/raw/PLAN/Bib/credentials/review。\n'''
(r/'continuation-prompt.md').write_text(cont)
p=root/'system/handoff.md';t=p.read_text();a=t.index('## Active handoff');b=t.index('## Previous active handoff',a)
t=t[:a]+'''## Active handoff — DAY14 completed after authorized extension\n\nRun2026-10-14-day-14-02/session01a13a0e-e8bd-7251-b970-f6975679e281在用户断网加时后于2026-10-16 15:00上海研究截止收束；15:00后仅验收/回执/课程对账/发布。同session未新建daemon/goal，原runner成功exit未观察，手动对账与实际scheduler事件已分开保存，不伪造normalfinalizer或clock ledger。\n\n正式14 primed回忆、Herzáň20页一图一表、五节点七边35checks、判据矩阵、21/24及REFLECT完整；整体审计41/41，唯一writeback156项44份修改知识页，旧review/claims/raw/PLAN/Bib保留。D12-36只纠正提交4月/答辩5月。最后的监督等待不计研究；实际检查与警告分类见final-checks-046.json。\n\n课程只计14一次：next15/count14，completed14/partial15；Day15入口outputs/learning-daily/prompts/20261016-DAY15-ado-angular-distribution-geometry.md已准备未启动，不开Day16。2012body/102-ECC绑定冲突及actualgate/δ/response/Σ缺口保持，无newspin/B/模式或实验L4结论。\n\nFinal publication subject main / `Complete DAY14 extended study and credit only Day14`，精确hash/H3/push仅runreceipt/publication-046.json；completed回执只交付或讨论既有成果，不重启研究或重计卡。Farmer仅监督瞬时错误，无Git角色，保留现有watcher。Resume `codex resume 01a13a0e-e8bd-7251-b970-f6975679e281 -C /workspace/wiki -s danger-full-access -a never`。Preserve inheritedDay6–9/Day13/log/daemon/raw/PLAN/Bib/credentials/review，exactmanifest/H3非force发布。\n\n'''+t[b:];p.write_text(t)
# Re-run the required gates after final metadata edits; publication is still gated.
final={}
for name,args in [('boundary-final-046',['python3','system/scripts/wiki_boundary_check.py','--root','.']),('lint-final-046',['python3','system/scripts/wiki_lint.py','--fail-on','error']),('diff-final-046',['git','diff','--check'])]:
 final[name]=command(name,args);assert final[name]['exit_code']==0,(name,final[name]['stderr'])
lint=final['lint-final-046']['stdout'];summary=re.search(r'^SUMMARY.*$',lint,re.M)[0]
assert 'errors=0 ' in summary and 'warnings=145' in summary
wb=runner.validate_durable_knowledge(report,root,base['knowledge_snapshot']);assert wb['valid']
finished=now();assert finished<=delivery
report.write_text(report.read_text()+'\n最终实际验收：wiki_lint --fail-on error exit0，0 errors/145 warnings（114 citation key、28未填raw保留槽、3 reaction parser）；git diff --check exit0；boundary exit0。日报、唯一知识写回与续接入口存在且验收通过；课程只计Day14。\n')
final_record={'at':finished.isoformat(),'report':runner.validate_report(report),'coverage':coverage,'writeback':wb,'knowledge_items':156,'changed_knowledge_pages':44,'formal_reconstruction_checks':35,'whole_objective_checks':41,'formal_self_score':21,'formal_prior_priming':True,'required_exit_codes':{k:v['exit_code'] for k,v in final.items()},'lint_summary':summary,'lint_errors':0,'lint_warnings':145,'warning_breakdown':{'CITATION_KEY_MISSING':114,'RAW_MISSING':28,'REACTION_PARSE':3},'PLAN_Bib_hashes_preserved':True,'raw_metadata_preserved':True,'course_state_guarded_once':True,'next_day_index':15,'completed_day_count':14,'next_prompt':nextp.relative_to(root).as_posix(),'next_prompt_exists':True,'continuation_prompt_exists':True,'new_session_or_daemon_started':False,'report_sha256':sha(report),'completion_mode':'same-session manual reconciliation for explicit user deadline extension','original_runner_exit_code':None,'no_new_scientific_content_after_cutoff':True,'all_deliverables_passed':True,'closeout_on_time':True}
write(r/'final-checks-046.json',final_record)
run.update(status='completed',research_status='closed',execution_status='same-session-manually-reconciled-completed',completed_at=finished.isoformat(),finished_at=finished.isoformat(),last_checkpoint_at=finished.isoformat(),deliverables_passed=True,closeout_on_time=True,counted_in_substantive_test=True,curriculum_cards_completed=1,completed_day_indices=[14],partial_day_indices=[15],next_day_index=15,manual_validation_exit_code=0,final_checks=final_record,course_state_reconciliation='course-state-reconciliation-046.json',next_prompt=nextp.relative_to(root).as_posix(),next_prompt_file=nextp.relative_to(root).as_posix(),final_publication_subject='Complete DAY14 extended study and credit only Day14')
write(r/'run.json',run)
event={'event':'user-extended-run-manually-completed','at':finished.isoformat(),'schedule_id':'wiki-daily-learning','run_id':run['run_id'],'run_date':run['run_date'],'day_index':14,'session_id':run['session_id'],'resume_command':run['resume_command'],'completed_day_indices':[14],'partial_day_indices':[15],'next_day_index':15,'completed_day_count':14,'deliverables_passed':True,'original_runner_exit_code':None,'manual_validation_exit_code':0,'completion_mode':run['completion_mode'],'overnight_until':run['overnight_until'],'research_cutoff_at':cutoff.isoformat(),'new_session_created':False,'daemon_restarted':False,'published_scientific_content_receipt':'publication-045.json'}
scheduler=root/'outputs/learning-milestones/2026-09-one-month-scheduler.jsonl';existing=[json.loads(l) for l in scheduler.read_text().splitlines() if l.strip()]
assert not any(x.get('event')==event['event'] and x.get('run_id')==event['run_id'] for x in existing)
with scheduler.open('a') as h:h.write(json.dumps(event,ensure_ascii=False)+'\n')
write(r/'scheduler-completion-event.json',{'path':scheduler.relative_to(root).as_posix(),'event':event,'publication':'isolated actual event copy; inherited global scheduler log remains unstaged'})
print(json.dumps({'completed_at':finished.isoformat(),'status':run['status'],'final_checks':final_record['required_exit_codes'],'warnings':145,'course_state':'next15/count14; onlyDay14credited','report_sha256':final_record['report_sha256'],'next_prompt':run['next_prompt'],'original_runner_exit_code':None},ensure_ascii=False))
