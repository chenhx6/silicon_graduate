"""One genuine closeout queue to the existing Day23 session; real effective gate."""
from pathlib import Path
from datetime import datetime
import sys,json,os
sys.path.insert(0,str(Path.cwd()/'system/scripts'))
import run_learning_session_clock as clock
root=Path.cwd();receipt=root/'outputs/learning-daily/20261025-DAY23-signature-partner-low-spin-wobbling-magnetic-rotation-run-01/run.json'
r=json.loads(receipt.read_text());assert os.environ.get('CODEX_SESSION_ID')==r['session_id']
spec=clock.load_spec(root,receipt,r['session_id'],2)
now=datetime.now(clock.TIMEZONE)
assert spec.deadline<=now<spec.closeout_end, 'Only actual validated effective closeout hour is allowed.'
with clock.acquire_locks(clock.LOCK_PATHS):
 supervisor=clock.Supervisor(spec)
 supervisor.initialize_one_shot()
 event=next(e for e in supervisor.events if e.event_id=='closeout')
 supervisor.attempt(event,datetime.now(clock.TIMEZONE),r['status'])
 record=supervisor.state['events']['closeout']
 result={'observed_at':datetime.now(clock.TIMEZONE).isoformat(),'run_id':r['run_id'],'session_id':r['session_id'],'mode':'existing locks + fresh genuine one-shot initialization + single closeout attempt; no loop/start/restart','original_deadline':spec.original_deadline.isoformat(),'effective_deadline':spec.deadline.isoformat(),'deadline_override_sha256':spec.deadline_override_sha256,'event':record,'queue_acceptance_is_not_execution':True}
 (receipt.parent/'closeout-one-shot-queue-23.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(result,ensure_ascii=False))
 if record['status']!='queued':raise SystemExit(1)
