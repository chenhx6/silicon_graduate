# Day23检查点032：支持方AD向量与所选分支采样范围

原run2026-10-25-day-23-01/session01a172fd-cbfb-7a13-b715-cfa0c479e08e，原截止2026-10-26 15:00+08，仍active；completed=[]、partial=[23,24]、next23，Day24仅一张无学分预习，不打开Day25。Farmer2698保持，不重启；raw/PLAN/Bib/旧人审/Day21/22学分/继承文件/114隔离producer边界保持。

031已H3 published。032实际定向重读PRL p3方法段/p4 Fig3并fresh4xclip，raw SHA f348dce9976ad076fd9b1d5281a728e0923053aced33b0270f643d770729366a；thesis printed96–100/117–118、freshPDF119/139/140三图，raw954e6cc853536555f5a691d6eaa257aaa051f79960de5eb47942f28fb335ef74。没新全文重读。AU20-D23-4/5和SE21-D23-6/7已canonical新needs_review，旧flags不变。

支持PRLδ376.3−2.67(+.07/−.07)、461.8−2.98(+.02/−.02)；SP265.3−.06±.01、436.5−.10±.01，436.5的δ不等旧376P−.10(5)。333.8/413.7近纯E2控线smallδ也非targetM1/E2δ=0解释。PRL Ref26只有N.Sensharma etal(to be published)，不要自动称完整方法原附件已得。thesis具体步骤见下，但不新增第二次实验。

Table4.1：Au333.8参考α2exp=.84(1)、α4exp=.81(1)、adoptedσ/J=.2（runs2+3）。Table4.4：376.3 I11/2→9/2,r=.48(3),A2=−.730(2),A4=.523(1)；461.8 I15/2→13/2,r=.38(1),A2=−.699(1),A4=.502(1)。r是sourceDCO-like不是Guo Rac；αexp、A2/A4各自分层，未知共同Cov。方法先A2解候选根，各根χ²比较后选低者，再只在选根附近MCMC；A4不单独求二次根但仍用于后续W/χ²，初始独立不等最终Cov0。这个实际conditionalinformation不抹，也不预判另一谷等深；局部窄error不全球nuisanceprofile。

新day23_au187_supporting_fit_inputs.py五输入控制，sourceprinted端点在030历史标称376.3/462.1与名义FO下像[.049200,.050472]/[.028840,.028995]，与四旧αK各printed范围不交。它与031小δ端点像四intersection形成条件反证，但theory/E/primarynormalization/globalδ/共Cov未传播，不能统计排除或最终LW/SP。第二个comparisonE462.1不改support461.8；原primaryRupnik/Bourgeois仍未全文读，官方评价只转述。

下一当前A槽：用已有day23_halfspin_singles_response.py响应组件、phasebridge明确额外假设，再把这两actualpublishedA2/A4向量与nominalpointσ/I=.2、KS应用约定相对照。先033contract（sourcevalues+rawsha+核查范围+禁止actualfit/noequalvalleys），可复用RB amplitudes但必须sourceδ=KS还只是application假设。分开empiricalα2/.α4和Gaussianpopulation，不能把Table4.1直接当完整physicaldensity或忽略finitegate/attenuation。pointforward只能定位迁移条件，不认证原paper偏差；用实际coeff时不要仅把δsource当单独观测并重复票。无真实Σ不报χ²/CI或调参fit。

Pr逐线校准、SH26固定sigma条件大根支持、noequalvalleys、Au旧P/外标/支持band3SP及Lu/Ba/Nd/Pd支持边界全保持。原窗口尚约9h，不早收束；Day24始终仅无学分，noDay25。

Git指针main · Day23: recover Au angular vectors and branch sampling conditions；actualhash/H3仅task-publication-receipt-032.json。

到原15:00才作正式Day23逐卡审计/原runner收束回执、Day24准备与H3；当前只是进度号，不早收束。
