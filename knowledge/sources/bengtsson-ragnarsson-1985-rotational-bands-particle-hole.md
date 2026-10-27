---
type: source
title: "Bengtsson–Ragnarsson1985：Nilsson参数、组态追踪与高spin竞争"
aliases: [Bengtsson Ragnarsson1985 rotational bands, BR85]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: theory-method-and-applications
reading_depth: deep-read
title_original: Rotational bands and particle-hole excitations at very high spin
authors: [Tord Bengtsson, Ingemar Ragnarsson]
year: 1985
journal: Nuclear Physics A
volume: 436
issue: 1
pages: 14–82
doi: 10.1016/0375-9474(85)90541-X
canonical_source: https://doi.org/10.1016/0375-9474(85)90541-X
citation_key: ""
raw_file: raw/papers/1985_Bengtsson_Ragnarsson_RotationalBandsParticleHole.pdf
raw_sha256: 605e785734279f1a7a6dfd234f1d3ff6b136f983b134ccf9d6b766f3b027d6b8
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-bengtsson1985-046/attachment-object-response.pdf
nuclei: [187au, 158yb, 158er, 118te, 106pd, 122xe, 128ba, 130ce, 168yb, 168hf, 165yb, 171ta, 160yb]
models: [cranked-Nilsson-Strutinsky, nonpaired-mean-field, rotating-oscillator-basis]
observables: [transition-energy, moment-of-inertia, configuration-crossing, band-termination]
methods: [diabatic-orbital-tracking, shell-correction, deformation-minimization]
tags: [133Ce-method-blueprint, Nilsson-parameters, chirality-alternatives, evidence-layer]
---

# 原参数表已读，固定组态与实际能带仍须逐态辨认

## Bibliographic Record

Tord Bengtsson和Ingemar Ragnarsson，Nuclear Physics A436(1),14–82(1985)，DOI10.1016/0375-9474(85)90541-X。Crossref核身份；received1984-04-09/revised1984-08-24与1985出版年分开。实际69页、4596459bytes、SHA见frontmatter，physicalPDF页+13=printed页。由出版商FULL XML返回确切attachment EID，再经配置的标准Object Retrieval API取得完整PDF，首14/末82和哈希均核；未宣称OA许可证或可再分发。FULL inventory只识别main.pdf及首页图，不等穷尽证明无SI。

这是[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]所引Ref11参数来源，不是其Ref40历史QTR或实际2022 producer。原件在tmp，raw是未填归档槽；PDF/XML/OCR/整页图不随本run发布。

## Scope and Reading Depth

046入口只读PDF1/5/6/69及Table1，历史范围保留。其后048连续读PDF1–16并fresh逐页视觉，Eqs1–26/Figs1–4/Table1；049读17–46全部主线和范围内Figs5–21/Tables2–3/Eqs27–32；root050读47–69含§7.3后半、§8四例、§9–10和参考，视觉核Figs22–32/Table4/Eq33。合并为全部69页主线、32图、4表、33式，不声称root独立重读每页。

root另核方法PDF5–6/9–16、Table1/2/3及其原图，重点视觉PDF6/11/14/16/21/42/46，和离散部分PDF49–51/53–55/57/59–60/62–63/65。未逐篇新读所引实验/先前方法，没有重放作者程序、数值PES、pairing或EM计算；旧114未运行。

## Summary

原Table1的κ/μ列与N_rot定义现可直接核，关闭WK22参数谱系的原件缺口。本文提供同ω虚交叉/同I相互作用、粗configuration/连续band、yrast envelope/跟踪支及continuum/resolved观测的区分。这些方法合同可迁到133Ce；本核实际输入/BCS/λ零点和signedEM仍不由引用恢复。130Ce高spin例有真实比较价值，不是133Ce的3qp或手征证据。

## Experimental or Theoretical Setup

固定x轴cranking hω=h−ωjx，势含deformed HO、ε4、stretched l·s和l²修正。转动HO基内忽略不同N_rot的off-shell couplings，使N_rot=n1+n2+n3近似保留；Eq11在非转动求和中取N=N′=N_rot。按(N_rot,signature)组占据追踪，以Strutinsky平均和rotating liquid drop重整化能量，每个I/组态分别极小化ε/γ/ε4。Pairing未含，作者将其许可性留给具体高spin比较，明确极低spin详细定量谱不适用。

## Key Results

新claims全部needs_review:true；原模型、引用实验、作者解释与本任务设计分开。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BR85-D24-001 | Table1 κμ按proton/neutron和N_rot分列；选参兼顾Ref25 rare-earth/actinide valence fit、light Z/N8/20/28 gaps及N平滑。不是2022 actual参数卡/ν编号或ε−λ零点。 | direct-parameter-lineage-and-transfer-boundary | direct-original | PDF5–6 printed18–19 Eq7/Table1 | true |
| BR85-D24-002 | N_rot=n1+n2+n3因删除跨壳V4/l·s/l²矩阵元而近似保留，Eq11另限N=N′=N_rot；不是完整Hamiltonian严格新守恒量、NilssonνID或qp数。 | explicit-space-approximation | direct-original | PDF6/9–10 Eqs8–17 | true |
| BR85-D24-003 | no-pairing为高spin计算选择，极低spin详细比较被作者排除；qualitative shape经验不等全部低spin能量/EM无需配对。§10未直接研究pairing消失，仅从所比高spin能量/惯量推其作用范围。 | approximation-and-quantifier-boundary | direct-original | PDF1–2/5; PDF65–67 Summary | true |
| BR85-D24-004 | 同量子数轨道在共同ω的虚avoided crossing与真实同I配置相互作用不同。作者去弱交互追踪构造平滑diabatic支，明确承认完全去交互not fully correct、低ω部分h11 crossing可疑；不测得V=0或actualEM核。 | direct-tracking-method-and-limit | direct-original | PDF2–4 Fig1; PDF11–14 Eqs18–22/Fig4 | true |
| BR85-D24-005 | 本文configuration固定各(N_rot,α)组占据数，band固定去虚交叉后的连续轨道；同configuration含多个bands。每ω global optimal、每I组内最低和连续band不是同一对象。 | direct-object-definition | direct-original | PDF14–15 §2.3/2.4; PDF21 Table2 | true |
| BR85-D24-006 | E_tot=E_sp−〈E_sp〉Strutinsky+E_rld，rld含ℏ²I²/(2Jrig)及r0=1.2fm；s.p.Routhian、lab s.p.sum与总能量零点不同。cutoff检验限166Yb/ω=0/ε≲.5等作者条件，不认证WK22九轨道收敛。 | energy-reference-and-convergence-scope | direct-original | PDF15–16 Eqs24–26 | true |
| BR85-D24-007 | J_eff/J_yrast/J_band依不同transition集合定义；unresolved bump/valley不提供逐线resolved同I双带。实验平均、resolution/背景扣除和模型cascade选择须保，不按惯量名合并。 | observable-and-source-independence-boundary | direct-original | PDF17 Eqs27–28; PDF40–41 Eqs30–31; PDF46–47 §7.3 | true |
| BR85-D24-008 | 187Au有实际两旋转方式的模型/历史数据比较，alignment不必伴drasticshape change；c3插值将应有backbend算成upbend、noncollective终止spin高于历史观测等限制保。c/ph标签不映现代GU22 Band2/3，也不给现代P/δ。 | original-support-and-adverse-results | direct-original-and-cited-experiment | PDF17–30 §4 Figs5–11/Table2 | true |
| BR85-D24-009 | 158Yb/Er终止例的近signature简并、118Te unresolvedE2 bump及106Pd/邻核平均各有模型解释，均不等sameI chiral pair已测。Pd二阶导/relativeband能与数据平均误差明确，Te两插值曲线不合保数值uncertainty。 | alternative-mechanism-and-data-scope | direct-original | PDF30–43 Figs12–20 | true |
| BR85-D24-010 | 128Ba Table3在该shape/ω下，[5237/2]α+轨道J2=−4.5、[6601/2]α+=.5，Eq32填入减挖空给+5ℏ²/MeV；high-j填入不必降低J2。原表.5不能按essentiallyzero静默写0。 | source-grounded-orbital-response-exercise | direct-table-plus-arithmetic | PDF45–46 Fig21/Table3/Eq32 | true |
| BR85-D24-011 | 168Yb Eγ/惯量有真实支持；Fig24分别扣exp .00805/calc .0077的I(I+1)参考并在I30归一theorygroundband，非全absoluteEx无调整比较。168Hf positive谱和p/n激发排序不佳同时保。 | support-reference-and-failure-boundary | direct-original | PDF48–53 Figs22–25/Eq33 | true |
| BR85-D24-012 | 171Ta原稿自称难全面再现，近20ℏ的Eγ相合却对应不同候选轨道，作者称probably of no relevance；160Yb观测仅到38，所推45–50 termination检验尚未发生在此数据中。 | explicit-counterexample-and-unobserved-prediction | direct-original | PDF56–59 Figs28–29 | true |
| BR85-D24-013 | 130Ce模型ε.20–.25的γsoft与ε.35/γ0极小竞争，后者约I25变yrast；跟踪前者配置仍可拟合已见离散Eγ。continuum J约52对discrete45的差用于作者推moredeformedcascade，所需带内跃迁尚待观测；不是实测两rigid shapes或133Ce配置。 | model-versus-resolved-data-and-inference | direct-original | PDF60–61 printed73–74 §8.4/Fig30 | true |
| BR85-D24-014 | Fig31区分alignment、shape gain及接近maxspin而无有利shape change的能量曲率；不同机制可改变J1/J2。源未给目标Ce或135Nd alternativefit/EM排他，不由一个近合/上翘/惯量比选唯一模式。 | direct-model-synthesis-and-transfer-design | direct-original-plus-explicit-task-boundary | PDF61–65 §9 Figs31–32 | true |

## Nilsson Parameter Contract

Table1原表如下，κ和μ均无量纲；μ是l²势参数，不是Fermi化学势λ。hω含−κ(N)ℏω0{2l_t·s+μ(N)[l_t²−〈l_t²〉N]}，t为stretched坐标。ε4项另有保轴对称的γ函数与可替代符号约定，不能用同名数字跨文互换。

|N_rot|protonκ|protonμ|neutronκ|neutronμ|
|---:|---:|---:|---:|---:|
|0|.120|.00|.120|.00|
|1|.120|.00|.120|.00|
|2|.105|.00|.105|.00|
|3|.090|.30|.090|.25|
|4|.065|.57|.070|.39|
|5|.060|.65|.062|.43|
|6|.054|.69|.062|.34|
|7|.054|.69|.062|.26|
|8|.054|.69|.062|.26|

Eq11的N=N′=N_rot限制是本表与实现的连接，不是所有模型中N与N_rot普适相等。1985 no-pairing cranking不等WK22含BCS QTR；即便WK22说adopted此表，也须actualinput/header确认具体壳/particle type、修改、频率/坐标、ν/K映射、完整系数、λ/Δ/阻塞与能量零点。绝不把表中protonμ.57和Nobs为不收敛改.32的另一模型混成默认Ce方案。

## Tracking, Energies and Observables

Eq18在fixeddeformation给deω/dω=−〈jx〉。实际追踪用overlap图和双向e/jx切线，Δj=.6、必要时跨两个ωstep并三次插值且保总e/jx；这些是作者算法容差/处方，不是实测混合或confidence阈值。Eq19 V<i²/(4Jc)属简单两级模型条件，不为Ce或135Nd反推V。去交互后的平滑energy不能提供原本被去掉的真实耦合/相干EM。

“configuration固定”在本文只保粗组计数，同组内轨道仍可穿Fermi面而发生bandcrossing。图上的yrast envelope也可换band；先明确追踪对象，再对同I的E_tot比较，不把eω、Σeω+ωI、减去参考抛物线的图线或Harris惯量混为一个输出。原rld用I²与未做good-I投影边界保留。

J1=I/ω、J2=dI/dω须保本源单位和finite-spin定义；J_band来自同band、J_yrast来自yrast序列，J_eff涉及many-E2 cascade统计。valley宽度/filledstripe和E2 bump可约束平均结构，却没有逐线γ/母末态身份。减aI(I+1)后图的残差二阶导还需加回2a才接absolute曲率；负残差曲率不自动意味着物理J2负。

## Applications and Counter-evidence

187Au的c1/c2/c3/ph等均为本源组态标签，历史Refs43–45与现代低spin/GU22采集无自动crosswalk。原§4用两类旋转/shape minima比较，c3在离网格区的插值错误和理论noncollective终止spin偏高照实保留；作者提出g/totaldecay time可分旋转方式是预测建议，不是新测g/τ。

128Ba/122Xe提醒粗h11占据标签可隐藏πg9/2 holes和不同shape；Table3/Eq32给填入减挖空的J2差，.5−(−4.5)=+5只在该ω/shape的source模型合同下成立。Pd比较含邻核平均、二阶导敏感和relativeband能对j-shell位置的依赖，15–24模型值与约26引用值不静默抹平。Te Fig18不同插值在I33–45不能严格重合，原文以此说明计算uncertainty。

168Yb的高spin Eγ和约62.5对65ℏ²/MeV惯量比较有真实支持；Fig24两个抛物线系数不同和I30归一同时保留。171Ta则提供反例：近合曲线所配候选轨道不同，作者自己不将之当可靠身份验证；移动s.p.能级又会破坏邻Yb/Hf比较。单核拟合不能任意调参后仍称共同输入独立预测。

### 130Ce：global yrast与tracked band的分开实例

§8.4/Fig30实际引用到32+及30−的离散谱。模型I10–22在ε约.25 nearprolate，I15–40另有ε.35/γ0极小并约I25成为yrast；较小形变的同配置thinbranches仍符合离散Eγ到高spin。正带πh11²/负带额外质子提升为130Ce本例模型，不接到WK22的133Ce低spinν1qp。

(+0)calc/exp均I28 backbend是支持，源归因为neutron h9/2–f7/2 orbital填充；(-0)exp止I30、calc在32不能叫相同spin已验证，J2尤其正带不佳。continuum的J_band^(2)约52ℏ²/MeV（ℏω>.62）与discrete约45的差，使作者推cascade可能走更deformedbands，并明确希望观测其带内transitions。这个推断不能变已resolved ε.35band、实测rigid shape或实际133Ce3qp crossing，也不搬52/45成Ce Harris输入。

## Competing Interpretations and Limitations

本文真实贡献是把多种非配对highspin mechanism接到具体能量/惯量和模型路径；不提供本次目标的全EM/响应/Cov。§10的“standard parameters以外无freeparameters”不等参数从未定标，pairing结论限所比核区/高spin观测，不推出普适I30门或低spinBCS可删。源主动保留方法任意性、插值/空间限制、部分s.p.排序不佳和若干当年未见预测；本页不因历史Au争议连带撤销Lu/Ba/Nd/Pd等其它来源的真实支持。

supports的是WK22参数谱系可原读及具体竞争机制检查；limits的是由同名参数/能带、单曲线匹配或同核名称恢复actual2022。当前完整signed波函数、单位零点、input/header、阻塞、coreR/Harris和逐线EM仍缺，不运行114或造替代参数卡。

## Extracted Pages

- [[133ce-thesis-analysis-blueprint]]：原κμ表、轨道/能带追踪、实际参数消费的分层。
- [[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]：Ref11已原读，actual应用仍按输出核。
- [[135nd-chiral-partner-resolved-evidence-map]]：sameω/同I、组态交叉与形状竞争的真实源例。
- [[chirality-shape-coexistence-companion-matrix]]：tracked与yrast、continuum与resolved资料不能拼接成完整向量。


## Ref63直接实验续核：谷宽量与primary assignment边界

[[nolan-1983-ce130-high-spin-moment-inertia]] NO83-D24-001–007已取得/读5页原件。root另fresh视觉本稿physicalPDF61/printed74，原句明确J_band^(2)而非J_eff；本轮初稿“effective moment”泛称已更正，不能混同§6计数定义的Jeff。NO83来自同150MeV Mo+S campaign的不同选门/关联样本，129Ce/La约20%污染与mostlikely归属边界保留；另NaI数据是独立引用入口。

本稿说离散到32+与(-)30，是作者在1985结合Refs63/77后的陈述；Ref63 primary里1242定26+，三条最高yrast线order难定、isomer确认28−/30−possible。Ref77仅metadata未读，不能把本稿概括倒写为Ref63已给逐条32+拓扑。本文52vs45属本稿模型比较语境，Ref63的谷宽值是justabove50，52是ε.25下rigidreference，未给literaldiscrete45/联合误差；不能据二者构造新精确差/shape认证。原数据与本稿支持保留，两篇对shape解释各自按模型/推断列，不强合成单一实测结论。
