# 完整有限tensor设计前的推导合同

在eθ/eφ Jones基中Aθ=(-A+ +A-)/sqrt2、Aφ=-i(A+ +A-)/sqrt2。若τhh′=Tr(Ah rho Ah′†)，则Q=-2Reτ+−、U=+2Imτ+−、V=τ−−−τ++；因此Q+iU=-2τ+−*。这个complexconjugation来自Jones基代数，不是事后flipU追拟合。

定义fullq S_km=Σ(q=−k..k)rho_kq exp(iqφ)d^k_(q,m)(θ)，negativeq由rho_k,-q=(-1)^q rho_kq*重构。偶k的T0=Σsqrt(2k+1)Fmix S_k0、T2=Σsqrt(2k+1)Hmix S_k2，奇k T3同Fmix。source邻接multipole实δ下Fmix=Fll+2δFlh+δ²Fhh；Hmix=Hll−2δHlh−δ²Hhh。令sEM为lower M:+1/E:−1，Namp=1+δ²，则I=T0/Namp，Q=ReT2/(sEM Namp)，U=−ImT2/(sEM Namp)，V=T3/Namp。必须逐项核规范/phase，不能在失败后改此合同。

下一独立验证使用此前已暴露的六PSDcases作regression，并以事前固定seed20261019产生新的PSD密度；spin1、2、3/2、7/2、9/2路径，pureE1/M1/E2与相邻M1/E2/E1/M2，必要高multipole只在明确L域。每个case先核Hermitian/unittrace/PSD，再比全IQUV/|S|≤1与photontrace；rotation/trueIzero/pureδ0/largeδ要带amplitude归一，不clip。

即使模型全闭合，也只认证所声明singleemitter和realδ数学合同；非完整UCGretina patch，原source/binary不改，原data/arrayresponse/Cov/实验δ未重拟合；Morseκ0pureE2反证保留。若新general失配，保存具体失败而非再挑sign或坐标。
