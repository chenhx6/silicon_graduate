import json,numpy as np
from pathlib import Path
p=Path(__file__).resolve().parents[1] / 'cases/followup/source_only_audit.json'
a=json.loads(p.read_text())['190Tl_observation_contract']
out=[]
for c in a['cases']:
 px=c['plot_pixels'];ticks=np.array(px['y_ticks']);slope,intercept=np.polyfit(ticks[:,0],ticks[:,1],1);center,upper,lower=np.array(px['y_center_upper_lower'])*slope+intercept
 out.append({'label':c['label'],'P':center,'err_minus':center-lower,'err_plus':upper-center,'two_pixel_readout':abs(2*slope),'tick_fit_max_residual':float(np.max(abs(ticks[:,0]*slope+intercept-ticks[:,1])))})
print(json.dumps(out,indent=2))
(p.parent / 'digitization_check.json').write_text(json.dumps(out,indent=2)+'\n')
