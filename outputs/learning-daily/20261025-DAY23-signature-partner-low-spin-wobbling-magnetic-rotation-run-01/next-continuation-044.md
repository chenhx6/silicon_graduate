# Day23检查点044：固定无配对PRM的有限I闭环

原run2026-10-25-day-23-01/session01a172fd-cbfb-7a13-b715-cfa0c479e08e，原截止2026-10-26 15:00+08，仍active；completed=[]、partial=[23,24]、next23，Day24仅一张无学分预习，不打开Day25。Farmer2698保持，不重启；raw/PLAN/Bib/旧人审/Day21/22学分/继承文件/114隔离producer边界保持。

043已经H3 published。044newday23_unpaired_ph_prm.py，inputcontract044先固定sourceZH07v1Eq1/2/4/6/7/p9unpairedlimit。j_p=j_h=11/2，pureparticlehsp+、pureholehsp−（fermiconstantsdrop只改零点），C.3MeV γ30 J0=30hbar²/MeV，axes1i/2s/3l、inertias30/7.5/7.5。不对源Δ1配对曲线做exact复现，不映射135Nd/Au/Pr核态，不调参fit实测。

full|K,Ωp,Ωn> productbasis，Ibody=(Jx,-Jy,Jz)anomalous、particlej普通，K−Ωp−Ωneven，reversepairphase(-1)^(I−jp−jn)，K>0或K0 Ωp>0 canonical，E两项/sqrt2。D2dimensionD=(2I+1)(2jp+1)(2jn+1)/4，I9/14/18为684/1044/1332(fullproduct4倍)。R=Ibody−jp−jn，HcollΣR²/(2J)，Hintrsourcehsp两块。HfullE−EHproject/leak/hermiticity/orthogonality过，freej.5+.5/C0/isotropicJ30：I1三谱[0,.1,.1]、I2五谱[.1,.1,.1,.1,.2]MeV，误差1.1e−16。

eigsh最低6、seed44000+I/tol1e−11/ncv48，与不同seed54000+I/tol3e−12/ncv72比，maxspectrumshift1.96e−14MeV、resid1.5e−11MeV、orth3.6e−15。fullO Eψ算RMS，不能用(E†O E)²替E†O²E，因为vectors可改变D2irrep；I²/jp²/jn²Casimir误差1.14e−12hbar²，Hcoll+Hintr重建差1.2e−14MeV。八controls过，code/inputs/result044已canonical新ZH07-D24P-008/009、概念/方法needs_review，oldflags/credit保持。

最低ordinalgap I9=381.26100098keV、I14=37.65869163、I18=87.34211431，是模型输出非实测/普适criticalspin/handednessproof。RMS I和各j/R存在输出JSON；γ30sourceexchange对称使s/l对应量相等，不能RMS非零认经典三矢量正交/静态手征。没有M1/E2/g/Q/δ/τ/CI或设施rate/time。原完整sourcepaired/multiqpproducer和真实dataoperator/response/Cov仍缺。

下一045有界固定H概率诊断（还未contract/实现）：复用model/solve但重新直接算源H，冻结044filehash/params，不以历史passed为科学事实。fullstate Eψ reshape(K,ΩpΩn)，traceintrinsic得ρ_K，再对各Ibodyaxis的谱投影得各自P_axis(m)。I这里integer9/14/18，所以m0确实在谱，别挪135Ndhalf-K0表述。检查ρPSD/trace、P≥0/归一、m反射/mean0与Σm²P=044fullRMS²；三轴projection互不对易，不能把三个marginal peaks拼成jointorientation。比较最低两态TV/Bhattacharyya和各P(m0)/峰位只作model描述，不赋confidence、tunnelingrate或静态chirality。RMS接近或marginal接近都不是relativephase/完整geometry证据。可先I9/14/18少点，不开新nucleus/source/card。

若后续EM路线需要，sourceZH07Eq15coreE2/18M1已041实际核，但当前未实现；必须先完整相位/归一/独立matrix/极限控制，再给该variant modelB，不可任意复制old114producer或认证实际实验。仍Day24唯一无学分preview、formalDay23/noDay25。原Pr/SH26conditional/noequalvalleys、AuP/外标/SP、Pt同源spin8vs6和Lu/Ba/Nd/Pd正支持校准全保。原约07:40还有7h20继续不早收束，15:00后才formalDay23/原runnerreceipt/Day24prep/H3。

Git指针main · Day23: verify a finite-spin particle-hole rotor variant；actualhash/H3仅task-publication-receipt-044.json。

到原15:00才作正式Day23逐卡审计/原runner收束回执、Day24准备与H3；当前只是进度号，不早收束。
