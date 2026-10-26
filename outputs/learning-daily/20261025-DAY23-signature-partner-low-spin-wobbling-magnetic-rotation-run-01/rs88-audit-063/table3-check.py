"""Conditional arithmetic of RS88 Table3, not model or experiment validation."""
from pathlib import Path
import math,json

rows=[
 ('prolate_h11/2','13/2','11/2',164,1.46,.41,.256),
 ('prolate_h11/2','15/2','13/2',199,1.65,.67,.259),
 ('prolate_h11/2','17/2','15/2',232,1.54,.85,.260),
 ('prolate_h11/2','19/2','17/2',266,1.35,.96,.262),
 ('oblate_h9/2','11/2','9/2',288,.67,.075,-.72),
 ('oblate_h9/2','13/2','11/2',342,.73,.117,-.71),
 ('oblate_h9/2','15/2','13/2',395,.65,.147,-.69),
 ('oblate_h9/2','17/2','15/2',448,.55,.158,-.70)]
out=[]
for cfg,ji,jf,energy,be2,bm1,delta in rows:
    ratio=math.sqrt(.7)*energy/1000*math.sqrt(be2/bm1)
    badunit=math.sqrt(.7)*energy*math.sqrt(be2/bm1)
    assert math.isclose(badunit/ratio,1000,rel_tol=1e-12)
    out.append(dict(configuration=cfg,Ji=ji,Jf=jf,Egamma_keV=energy,
                    BE2_e2b2=be2,BM1_nm2=bm1,printed_model_delta=delta,
                    conditional_abs_delta=ratio,relative_abs_difference=abs(ratio/abs(delta)-1),
                    sign_inferred_from_strengths=False,source_locator='printed439 Table3'))
maximum=max(r['relative_abs_difference'] for r in out)
assert maximum<.015
result=dict(scope='Only Eq29/Table3 magnitude arithmetic conditional on MeV energy convention; no experimental inference',
            rows=out,max_relative_abs_difference=maximum,
            wrong_energy_unit_magnifies_by_exactly_1000=True,signs_not_reconstructed=True,
            producer_reproduced=False,experimental_CI_created=False,needs_review=True)
Path(__file__).with_name('table3-conditional-check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'max_relative_abs_difference':maximum,'conditions_pass':True}))
