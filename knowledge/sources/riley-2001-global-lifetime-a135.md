---
type: source
title: "Riley等2001：A≈135全局寿命与差分四极矩"
aliases: [Riley 2001 global lifetimes, A135 global differential quadrupole moments]
created: 2026-10-15
updated: 2026-10-15
status: ai-draft
review_status: unreviewed
source_type: journal-conference-author-report-experiment-and-model
reading_depth: deep-read
title_original: "Global lifetime measurements of highly-deformed and other rotational structures in the A~135 light rare-earth region: Probing the single-particle motion in a rotating potential"
authors: [M. A. Riley, R. W. Laird, F. G. Kondev, D. J. Hartley, D. E. Archer, T. B. Brown, et al.]
journal: Acta Physica Polonica B
year: 2001
volume: 32
issue: 9
pages: 2683-2695
doi: ""
language: en
canonical_source: "https://www.actaphys.uj.edu.pl/fulltext?series=Reg&vol=32&page=2683"
citation_key: ""
raw_file: "raw/papers/2001-Riley-global-lifetime-A135.pdf"
raw_sha256: 09d58089a1985ef9d3d02432921b302a77c5d51eca9846bdea03dd9330d0d036
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
nuclei: [130Pr, 131Pr, 132Pr, 133Pr, 132Nd, 133Nd, 134Nd, 135Nd, 133Pm, 134Pm, 135Pm, 136Pm, 135Sm, 136Sm, 137Sm, 131Ce, 132Ce, 142Sm]
reactions: []
experiments: [Gammasphere-Microball-A135-global-lifetimes]
models: [FITFTAU-constant-Qt-extraction, cranked-Skyrme-Hartree-Fock, cranked-relativistic-mean-field]
observables: [Doppler-shift-attenuation, band-average-Qt, differential-Qt]
methods: [centroid-shift-DSAM, particle-gamma-coincidence, high-spin-gating]
tags: [a130, lifetime, quadrupole, side-feeding, source-table-semantics, data-lineage]
---

# Riley等（2001）：A≈135全局寿命与差分四极矩

## Bibliographic Record

M. A. Riley等，*Acta Physica Polonica B* **32**, No. **9**, 2683–2695 (2001)。出版商13页原PDF刊头、完整题名、首作者和起页均核。实际[公开入口](https://www.actaphys.uj.edu.pl/fulltext?series=Reg&vol=32&page=2683)返回416810 bytes PDF，SHA256如frontmatter；初候选URL的issue10被服务器按vol/page重定向，引用以实际No9刊头为准。未核DOI，不猜填。

本报告是High Spin Physics 2001会议的作者invited talk，不能自动等同后来Laird2002最终期刊稿。后者全文仍缺；[[matev-2007-a130-quadrupole-alignment-additivity]] MT07-8将两者作为同一实验工作的引用，不据发表数新增独立测量。

按daily-learning授权建立来源记录，但**未完成raw归档摄入**；`raw_file`是未填保留槽。实际只读输入为`tmp/day14-20261014/riley2001/riley2001-candidate.pdf`。citation key未匹配本地Bib，留空，原raw/Bib不改。字体提取丢失部分字符与符号，关键数字、b/c注和归一化负号均回原图视觉核验。

## Scope and Reading Depth

- **Covered scope**：13页全部主线；形变/极化背景、差分定义、实际反应与探测器、三类门选、FITFTAU/恒定Qt拟合及侧馈、Figs.1–3、Tables I–II、理论比较、总结和参考文献。关键图表/公式视觉核。
- **Not covered**：没有原始逐门/逐ring谱、centroid及共同Σ、逐transition能量/自旋/branch manifest、实际阻停/feeding响应或FITFTAU输入与代码运行。不是Laird2002最终版本的重读，也未取得外源Ce/Sm原实验全文。
- 源前与量化前回忆均标priming；本页`unreviewed`，全部RI01 claims保留`needs_review: true`。

## Summary

作者用Gammasphere+Microball的全局实验，在共同条件下比较多个核素的band-average Qt。质心位移DSAM、门选和侧馈假设进入提取；所谓减少公共系统差异不等于剩余绝对误差为零。论文同时展示原测量、外源Qt、结构模型和有效单粒子矩，必须按角色区分。表中没有可直接填入能级图的逐跃迁寿命。

## Experimental and Analysis Setup

173 MeV的35Cl束打在1 mg/cm²富集105Pd靶上，17 mg/cm² Au backing；Gammasphere使用97个Compton-suppressed HPGe，Microball识别蒸发带电粒子。名义fusion system为140Eu；逐产物实际exit/channel和event selection需原数据，不由守恒预算替代。

作者以质心位移构造`F(τ)=[Eγ(θ)−E0]/[E0 β′cosθ]`，β′定义为mid-target recoil velocity。低端fully-stopped gates、in-band moving double gates和最高spin in-band gates是不同选择。FITFTAU在带内Qt恒定的假设下拟合F曲线；TableI默认`Qt(side feeding)=Qt(band)`，不是`τsf=τband`。该流程产出带平均的衍生矩或限值，不是每个点的独立τ。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RI01-1 | 实验采用173 MeV 35Cl+105Pd、1 mg/cm²靶/17 mg/cm² Au、Gammasphere97个HPGe与Microball带电粒子选择，采集身份固定在这些束靶与探测条件。 | experimental-setup | direct | printed p.2687 Sec.3 | true |
| RI01-2 | 使用质心位移DSAM和F(τ)定义，β′是mid-target recoil velocity；stopped-gate选择用forward31.7°/37.4°与backward142.6°/148.3°，另有moving double gates和90°数据。没有给每点共享event/角度权重/Σ。 | reported-method-and-input-boundary | direct | printed p.2687 F(τ) paragraph | true |
| RI01-3 | 作者对强带用最高spin门来抑制/消除下方态的侧馈影响，报告相对底部stopped门约10%的Qt提高。TableI b注是above-level gate分析条件，不是独立新实验或物理形变已变。 | experimental-analysis-sensitivity | direct-and-derived | printed p.2687 high-spin-gating paragraph; printed p.2690 footnote b | true |
| RI01-4 | 用FITFTAU生成恒定Qt的带F曲线；TableI默认Qt(sf)=Qt，未给逐跃迁寿命。c注另假定τsf约1.2τband，不能把默认Qt相等解释成τ相等。 | analysis-model-and-scope | direct | printed p.2687 FITFTAU paragraph; printed p.2690 caption/footnote c | true |
| RI01-5 | 正文说阻停及侧馈可给绝对Qt附加15–20%系统误差、相对精度约5–10%；表注只说阻停10–15%。作用范围不同，未给置信覆盖或共同Σ，不合并成单一已知Gaussianσ。摘要“free”须受正文条件约束。 | source-uncertainty-budget-and-boundary | direct-and-derived | printed p.2687 final paragraph; printed p.2690 TableI caption | true |
| RI01-6 | 本次TableI转录为33原行、15核素、39有限值和3上限；slash/逗号/α/b/c分属不同语义。不是42个独立数据点或完整采集核素/能带census。 | our-table-ledger-and-scope | derived | printed p.2690 TableI | true |
| RI01-7 | TableI五个b注pair为133Nd5.8(2)→6.5(2)、135Nd5.1(2)→5.7(2)、136Pm band1/2各4.8→5.2、137Sm4.4(3)→4.8(4)eb；名义提高约8.3–12.1%，不能将其当每条未测带的统一修正。 | source-derived-Qt-and-analysis-condition | direct-and-derived | printed p.2690 TableI footnote-b rows | true |
| RI01-8 | 135Sm的5.8(4),6.4(4)c来自另一侧馈time-structure假设；不是第六个b门选pair。130Pr slash是band1/2，133Nd的两个α±pair是signature分支，也不是同带重复测量。 | source-table-semantics | direct | printed p.2690 TableI rows/footnotes | true |
| RI01-9 | Fig2/3明确把131/132Ce列为本报告Ref21旧资料、142Sm列为Ref24资料；采用相似target/backing与分析不等于同一次采集。142Sm也不是名义35Cl+105Pd fusion-evaporation系统的产物。 | source-lineage-and-conservation-guard | direct-and-derived | printed p.2689 Fig2 caption; printed p.2692 Fig3 caption | true |
| RI01-10 | Fig1与TableI有若干family级quoted值/误差差异，如133Pr ND3.4(3)/3.3(3)、134Pm f7/h9类3.9(3)/3.9(2)、135Sm6.4(5)/6.4(4)c；相同band/gate/fit绑定未提供，不静默覆盖或判typo。仅凭核素与中心值也不能唯一给133Nd ND3.5点配表行。 | figure-table-binding-boundary | direct-and-derived | printed p.2688 Fig1; printed p.2690 TableI | true |
| RI01-11 | Eq3取Qt=Q20+sqrt(2/3)Q22_R，随后明确Ref36变量Q22_code=−sqrt2 Q22_R；代数上转为Qt=Q20−Q22_code/sqrt3。负号被文字提取丢失，必须回原图；形式相容不认证Pr实际frame或不同版本代码变量身份。 | operator-normalization-and-scope | direct-and-derived | printed p.2691 Eq.(3) and normalization sentence | true |
| RI01-12 | 理论用无配对CSHF/SLy4与CRMF/NL1，以131Ce HD core、ω=.65 MeV比较；TableII的183/105是计算配置。Fig3所报core Qt7.75/7.57eb是理论baseline，不加到实验δQt上制造绝对实测值。 | model-input-output-and-provenance | direct | printed pp.2691–2693; Fig3 caption; TableII | true |
| RI01-13 | 正文的νi13带系统学是Qt随Z/N增加而下降；不是固定其他占据、只改变intruder数的同一比较。πg9 holes等也可驱动HD；ND带被模型预测为γ-soft/配对显著，作者警告不能简单按单粒子占据解释其Qt趋势。 | author-interpretation-and-transfer-boundary | direct-and-derived | printed pp.2688–2689; printed p.2692 Discussion | true |
| RI01-14 | 三个Qt<3.0上限无明确CL，不能当Qt=3点。仅在固定已识别E2能量、branch/geometry的条件下Qt上限才给相反方向的τ下限；本表不足以生成数值逐态τ。 | source-limit-and-our-domain-check | direct-and-derived | printed p.2690 TableI upper-limit rows | true |
| RI01-15 | 本报告Ref21是Clark等PRL76(1996)，未给页号；不是Matev2007 Ref21的Laird2002。Ref32为Laird submitted；2001作者报告不自动替代2002最终稿，也不按两个发表数计独立实验。 | citation-and-version-boundary | direct-and-contextual | printed p.2695 Refs21/32 | true |

## Table I：保留分析角色的33行账本

RI01-6–8/14；全部行对应印刷p.2690 Table I（PDF p.8）。原配置保留作者简写，非完整occupied inventory；括号为原报误差，覆盖概率未明。每个数紧随自身角色，逗号或slash不代表可平均。原表默认Qt(sf)=Qt；b为上方门，c为另一侧馈时序假设。

| 原行 | 核素 | 作者配置简写（转录） | 类型 | Qt / eb及角色 |
| --- | --- | --- | --- | --- |
| 1 | 130Pr | pi h11/2 x nu d5/2 | single | 3.4(2) [原表默认fit] |
| 2 | 130Pr | pi h11/2 x nu(f7/2,h9/2), bands1/2 | band_pair | 4.3(3) [band 1]；4.5(3) [band 2] |
| 3 | 130Pr | pi g9/2 x nu h11/2 | single | 6.1(4) [原表默认fit] |
| 4 | 131Pr | pi h11/2 | single | 3.3(3) [原表默认fit] |
| 5 | 131Pr | pi g9/2 | single | 5.3(4) [原表默认fit] |
| 6 | 132Pr | pi h11/2 x nu(f7/2,h9/2) | single | 4.1(3) [原表默认fit] |
| 7 | 132Pr | pi g9/2 x nu i13/2 | single | 7.0(7) [原表默认fit] |
| 8 | 133Pr | pi h11/2 | single | 3.3(3) [原表默认fit] |
| 9 | 132Nd | pi h11/2 | single | 4.2(2) [原表默认fit] |
| 10 | 133Nd | nu h11/2 | upper_limit | <3.0 [上限；CL未给] |
| 11 | 133Nd | nu h11/2 x pi(h11/2)^2 | single | 3.5(3) [原表默认fit] |
| 12 | 133Nd | nu g7/2, alpha+1/2/-1/2 | signature_pair | 3.4(2) [α=+1/2]；3.5(2) [α=−1/2] |
| 13 | 133Nd | nu(f7/2,h9/2), alpha+1/2/-1/2 | signature_pair | 4.2(3) [α=+1/2]；4.1(3) [α=−1/2] |
| 14 | 133Nd | nu i13/2 | gate_pair_b | 5.8(2) [默认分析]；6.5(2) [上方门 b] |
| 15 | 134Nd | pi h11/2 | single | 4.0(2) [原表默认fit] |
| 16 | 135Nd | nu h11/2 | upper_limit | <3.0 [上限；CL未给] |
| 17 | 135Nd | nu h11/2 x pi(h11/2)^2 | single | 3.0(3) [原表默认fit] |
| 18 | 135Nd | nu i13/2 | gate_pair_b | 5.1(2) [默认分析]；5.7(2) [上方门 b] |
| 19 | 133Pm | pi h11/2 | single | 4.0(2) [原表默认fit] |
| 20 | 133Pm | pi d5/2 | single | 4.1(2) [原表默认fit] |
| 21 | 133Pm | pi g9/2 | single | 5.0(4) [原表默认fit] |
| 22 | 134Pm | pi h11/2 x nu h11/2 | single | 3.3(2) [原表默认fit] |
| 23 | 134Pm | pi h11/2 x nu(f7/2,h9/2) | single | 3.9(2) [原表默认fit] |
| 24 | 135Pm | pi h11/2 | single | 3.3(2) [原表默认fit] |
| 25 | 135Pm | pi d5/2 | single | 3.5(2) [原表默认fit] |
| 26 | 136Pm | pi h11/2 x nu h11/2 | upper_limit | <3.0 [上限；CL未给] |
| 27 | 136Pm | pi h11/2 x nu i13/2 band1 | gate_pair_b | 4.8(3) [默认分析]；5.2(3) [上方门 b] |
| 28 | 136Pm | pi h11/2 x nu i13/2 band2 | gate_pair_b | 4.8(4) [默认分析]；5.2(4) [上方门 b] |
| 29 | 136Pm | pi g7/2 x nu i13/2 band1 | single | 5.7(6) [原表默认fit] |
| 30 | 136Pm | pi g7/2 x nu i13/2 band2 | single | 5.7(6) [原表默认fit] |
| 31 | 135Sm | nu i13/2 | feeding_assumption_pair_c | 5.8(4) [默认分析]；6.4(4) [侧馈时序假设 c] |
| 32 | 136Sm | nu(h11/2)^2 x pi(h11/2)^2 | single | 3.3(2) [原表默认fit] |
| 33 | 137Sm | nu i13/2 | gate_pair_b | 4.4(3) [默认分析]；4.8(4) [上方门 b] |

合计33行、15核素、39有限数值和3上限；不计为42项独立测量。完整原配置及b/c/a脚注以原PDF为准。机器输入另存JSON，以上为可长期检索的canonical副本。

## Quantitative/Design Exercise

27项程序断言核source hash、39有限token的原顺序、typed roles、limits、名义pair变化、守恒与归一转换；这些不是对原实验误差预算或FITFTAU重跑的全面验证。见[[transition-quadrupole-moment]]“全局Qt表的分析选择与数据身份”及[完整审计](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/riley2001-global-qt-audit.json)。

若固定同一已识别E2的Eγ/branch/geometry，Qt增加10%的条件响应为B增加21%、τ乘.826446。对表中各pair只作该相对敏感性，不生成原表没有的τ。133Nd/135Nd high-gate值的名义比5.7/6.5≈.876923、差−.8eb；若将括号误差当σ，未知相关性下比值一阶σ范围约.003787–.057751，差的σ范围0–.4eb。这不是实际CI或Σ恢复。

统一条件可以大减difference的绝对系统差异，却不自动使之为零：一个共同乘性scale保ratio但仍缩放非零difference。作者的相对精度声明不能由本任务的简化scale模型单独证实或推翻；原始响应、共享参数与选择权重仍缺。

## Competing Interpretations and Limitations

Qt是恒定带参数假设下的实验衍生量，configuration标签多为作者/上游结构解释的简写，不是完整occupied inventory或实测γ。不同带、不同signature、不同门、不同侧馈假设与censored bound不能被一个“两个数”规则合并。

Fig1只显示样例F曲线，TableI不给逐line能量/自旋/branch；故仅按中心Qt或核素给图点绑定表项，或据此对另一能级填τ，均缺必要身份信息。图表差异先保留其selection/fit条件，而不是选择一个数字统一。

## Counter-Evidence and Missing Companion Observables

强门选导致Qt改变、body保留15–20%绝对附加系统误差、ND带的配对/γ-soft解释限制，都是对“单一Qt唯一测得γ/构型、没有剩余系统误差”的直接限制。相对精度与名义Qt分类仍有信息，不因这些边界把原方法判失效。

L4原始refit缺ring/gate spectra、centroid/calibration与共同Σ、β′ producer与slowing/feeding histories、完整E2/branch/geometry及FITFTAU输入。当前只能审计已发表参数与条件缩放；无Pr136新τ/Qt、没有actual Laird2002最终版或外源Ce/Sm原分析重放。

## Related Knowledge and Project Relations

- `methodological-bridge` → [[doppler-shift-attenuation-method]]：质心位移与恒定Qt/门选/侧馈契约，不局限于lineshape。
- `limits` → [[transition-quadrupole-moment]]：band平均、带/门/假设身份、未知Σ与Qt→γ边界。
- `foundational-background` → [[matev-2007-a130-quadrupole-alignment-additivity]]：早期实验/理论作者报告；同计数或相同cohort不等不同版本计算可互换。
- `not-direct-evidence` → [[a130-model-choice-card]]：A130邻核方法校准，不把数据移给Pr136或ND131Ce Band1。

## Knowledge Impact and Learning Decision

Decision: **supports** 在共用条件下进行相对Qt比较，**limits** 把摘要措辞、恒定Qt参数、两个表数或配置简写直接变成独立τ/γ证据；**revises** 平铺数据与隐去门/侧馈假设的读法。持久化source、Qt observable、DSAM方法和上游数据谱系，不新建一批核素页或研究note。原formal21/24、Day14/partial15、Pr解释与PSM/TPSM覆盖2/7不变。overview update deferred：当前是同一证据链的primary补足。

## Agent self-audit triage

- **P0: none identified**。public publisher原件身份/hash/No9已核；raw未归档明确。
- **P1 / RI01-3–8、14**：门选与侧馈假设不同，quoted误差/accuracy不是已知Gaussianσ，未补逐τ或统一10%修正。
- **P1 / RI01-9、10、15**：表subset、外源plot、未定figure/table绑定与reference编号分开，不能按全部图点共采集或独立发表计证据。
- **P1 / RI01-11–13**：文字提取漏负号已回图；算符归一/模型baseline不作实验转轴或完整组态证明。
- **P2**：citation key空与raw保留槽在lint报告；原PDF、旧review与raw/Bib不改。

## Extracted Pages

- Observables: [[transition-quadrupole-moment]]
- Methods: [[doppler-shift-attenuation-method]]
- Related source: [[matev-2007-a130-quadrupole-alignment-additivity]]

## Provenance

- [Publisher PDF](https://www.actaphys.uj.edu.pl/fulltext?series=Reg&vol=32&page=2683)：本文全部直接locator与原件。
- [Typed TableI](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/riley2001-table-I-input.json)、[审计程序](../../system/scripts/day14_riley_global_qt_ledger.py)、[reading audit](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/riley2001-reading-audit.json)。
