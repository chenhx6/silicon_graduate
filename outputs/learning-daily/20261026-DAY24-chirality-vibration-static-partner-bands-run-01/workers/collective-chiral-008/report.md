# Chen2013：一维集体哈密顿量补上左右隧穿，但保留角度与同spin比较边界

本轮限定原件单元，供leader核验后写回knowledge。全部新claims为`needs_review: true`、Codex self-audit，不是human review。仅写指定tmp和worker目录；未改canonical、raw、PLAN、Bib、Git、程序配置、session或课程学分，也未运行作者代码。

## 已核身份、版本与真实阅读

Q. B. Chen, S. Q. Zhang, P. W. Zhao, R. V. Jolos and J. Meng, **“Collective Hamiltonian for chiral modes”**, *Physical Review C* **87**, 024314 (2013), DOI **10.1103/PhysRevC.87.024314**。Crossref和INSPIRE独立核定，非凭候选题名/DOI记忆认领。

- 官方记录：`https://arxiv.org/abs/1212.2313`；标v1=2012-12-11、v2=2013-02-23，journal ref为PRC87,024314(2013)。
- 实际body下载：`https://arxiv.org/pdf/1212.2313`，200/application/pdf、987932 bytes，16页；PDF边栏明确`arXiv:1212.2313v2 [nucl-th] 23 Feb 2013`。可复制固定版本URL为`https://arxiv.org/pdf/1212.2313v2`。本轮只用**1条body路线**，未扩综述/第二篇/VoR。
- 本地：`tmp/day24-collective-chiral-008/chen2013-collective-chiral-arxiv.pdf`。
- SHA256：`bef6182263a6282ea6c4fc3e2fbae481bbf629e484dbf9668e3ea9e622342a2c`。
- PDF1正文typeset date另印“July24,2018”，与v2边栏及官方history不是同一字段；保留字面，不因此发明2018科学版本或把出版年改2018。未取得PRC VoR，也未宣称此PDF与VoR逐字相同。
- 实际读16页全文主线，包括references；视觉核PDF1、4–15，覆盖**全部8图、关键Eqs4–28**及参数/限制段。Eqs1–3位于PDF3，已读文本；未把单纯提取16页文本当作整套视觉认证。
- 下文PDF页与arXiv印刷页均为1–16；**不是PRC024314-n定位**。

## 它补上的理论层次

PDF2–3 Introduction明确区分：PRM为量子模型、总I为好量子数，可以给有限劈裂及隧穿；TAC提供平均场取向，却不能给左右手解之间的隧穿与doublet能隙；TAC+RPA可描述振动，但有限势垒区的左右隧穿超出其小振幅范围。作者因此在TAC约束能面上引入一个φ集体自由度并量子化。

这里应接入Day24的是 **平均场几何/局部近谐 → 量子集体波函数与有限能隙** 的层次。本文没有新增实验，也没有据一条双带能隙单独认证任何真实核素的手征性。

## 构造合同：坐标、势、质量、量子化和边界

| 对象 | 原件直接内容 | 适用限制及locator |
|---|---|---|
| 转动坐标 | ω向量为ω(sinθcosφ,sinθsinφ,cosθ)，0≤θ≤π/2、−π/2≤φ≤π/2；φ连接左右取向 | PDF3 Eq3；PDF4 Eq7及其后段。坐标不是形变γ，也不是真实核的“手征角实测” |
| 维度与势 | **一维φ**；对给定φ，V(φ)取TAC总Routhian E′(θ,φ)对θ最小值 | PDF4 Eq5，PDF5首段；PDF15明确忽略θ方向的势涨落。θ可沿最小化路径变化，但**没有θ的量子动力学/两维质量张量** |
| TAC输入 | h′=hdef−ω·j，j=jπ+jν，hdef为单j形变场；core项以−½ΣJkωk²进入E′ | PDF3–4 Eqs1–5。不是自洽CDFT多轨道或真实135Nd三准粒子输入 |
| 经典集体动能 | T=½B(φ)φdot² | PDF5 Eq9。质量随φ变，不能静默拿某常数代替 |
| 质量来源 | 对h′瞬时本征态做time-dependent推导；初态为最低态、激发幅度al≠0小，假设φddot=−Ω²φ，丢掉所示∝φ²项，得到Eq22的跃迁求和 | PDF5–6 Eqs15–22。是特定扰动/绝热结构，不是完全无近似的全量子惯量 |
| Ω处方 | 对振动，用V≈½Kφ²与B=K/Ω²联立Eq22；对rotation case近似Ω=0，化为Eq28 | PDF7 Eq23；PDF9 Eq28，并在ℏω≥.20MeV采用。**这是B的处方，不是最终双态ΔE=0** |
| Pauli量子化 | H=−ℏ²/(2√B) ∂φ[1/√B ∂φ]+V；体积元√B dφ | PDF5 Eqs10–14。Pauli指一般坐标动能的量子化处方，不是另一个排斥统计筛选 |
| basis/边界 | 偶φ：√(2/π)cos[(2n−1)φ]/B^(1/4)；奇φ：√(2/π)sin(2nφ)/B^(1/4)；n≥1；ψ(±π/2)=0 | PDF7 Eqs24–27。B^(−1/4)与√B测度配套归一；不能删去一个因子而照搬其它式 |
| wall近似 | 因±90°附近B很大而采用wall approximation，与盒basis相配 | PDF10末至PDF11首段。Dirichlet边界是作者明确选择的近似，不能当所有手征角空间自动具有的边界 |

质量公式可按PDF6 Eq22写为

\[
B(\varphi)=2\hbar^2\sum_{l\ne0}
\frac{(E_l-E_0)\left|\frac{\partial\boldsymbol\omega}{\partial\varphi}\cdot
\langle l|\hat{\boldsymbol j}|0\rangle\right|^2}
{\left[(E_l-E_0)^2-\hbar^2\Omega^2\right]^2}.
\]

设置Ω=0使分母与分子约成Eq28的(E_l−E0)^3形式，但Pauli动能仍存在，解H后仍有有限离散能级劈裂。不能把惯量推导里Ω取零写成实验“零声子能隙”或严格左右超选。

## 系统、参数与冻结的自由度

PDF8 §III只计算**示意性、对称πh11/2粒子⊗νh11/2空穴 + rigid triaxial rotor**，无指定核素的数据拟合。γ固定−30°，Cπ=.25MeV、Cν=−.25MeV，J0=40ℏ²/MeV，称与Ref1(Frauendorf–Meng1997)一致。PDF4 Eq4包含particle/hole符号；实现时不能把Cν负号和该符号未加说明地重复计入。

核形变γ在此固定，只有φ量子化；没有γ软度的动力学、β振动、多轨道/3qp配置重排、真实BCS输入或目标核数据响应。PDF4提134Pr旧计算的φ比θ软只作为一维选择的动机，**不意味着本文已经计算/拟合134Pr，更不是135Nd或133Ce新结果**。

唯一数值小核验：按Eq6的 **Jk=J0sin²(γ−2πk/3)** 与PDF8参数，k=1,2,3得到 **[10,40,10]ℏ²/MeV**，残差≤1.5×10⁻14。没有4/3因子；不可把别文惯量参数同名便视作相同规范。此项仅检查参数和公式转录，未算真实核能谱/矩阵元。

## 全8图带来的直接新信息

| 图与页 | 实际内容 | 主张及边界 |
|---|---|---|
| Fig1 PDF9；PDF8说明 | 0.10/.20/.30/.40MeV的θ、φ TAC面，关于φ=0对称，最低点转为±φ | 平均场aplanar解的出现；不是量子局域化或实测取向 |
| Fig2 PDF10；PDF8说明 | V(φ)从≤.15MeV单阱到≥.20MeV双阱；ΔV从.001MeV(.20)到1.93MeV(.50) | 明确势垒而非仅一个harmonic curvature；双阱不保证最低量子态已受限于单一手性 |
| Fig3 PDF10；PDF9 Eq28说明 | B(φ)对称，边界大；≥.35MeV内区随|φ|明显变 | 不能只用势垒高度比较隧穿；质量与路径亦参与 |
| Fig4 PDF11 | 最低6态形成3对，频率升高成对接近 | 最低两态gap **1.19MeV@.25 → .01MeV@.50**，仍有限；不是实测差 |
| Fig5 PDF12 | 最低gap对势垒高度，点标.25到.50MeV | `.25`点对应Fig2的ΔV=.07MeV；PDF11末段笼统“1keV到2MeV”跨了.20–.50域，不能把1.19MeV gap误配到.20MeV/.001MeV势垒 |
| Fig6 PDF12 | 最低态ψ1为φ偶、ψ2为φ奇 | 量子态恢复平均场破缺的左右对称，不能将偶/奇φ称为核的正/负空间宇称 |
| Fig7 PDF13 | 图注明确画\|ψ\|²，.25/.30低态宽广，随ω升高两分布更像 | 作者在aplanar区起始仍强调chiral vibration；后来称good static chirality，是此模型的渐近regime解释 |
| Fig8 PDF14–15 | 同体系PRM的能量与I(ω)对照；高频PRM gap再增加、1D collective gap继续减小 | **本一维模型漏掉second chiral vibration**；不能把单调趋零当普适真实核定律 |

## finite splitting、局域化和实验可辨量分开

**直接来源层：**PDF12–13说ψ1对称、ψ2反对称，最低偶态能量更低，左右手破缺被恢复；PDF13据高频两个\|ψ\|²趋近而称good static chirality。它没有把本征态画成只占左井/只占右井的静态态。

**我们的量子层推断：**若B、V对φ反射对称，则这两个非简并本征态的任何φ奇取向量的期望都为0（用Eq14的偶测度积分）。局域在左/右井的组合可由偶/奇态相干叠加构造，但有限ΔE时一般不为定态，会积累相对相位。故“static chirality regime”可以指强抑制隧穿、近简并及相似性质，不能改写成有限核的单个能量本征态永久只具有一个有符号手性。本文没有给实验退相干/测量局域化时间尺度。

**测度边界（源式+推断）：**Fig7字面画\|ψ(φ)\|²，Eq14却规定概率积分为∫√B\|ψ\|²dφ。若要解释“每单位φ”的概率密度，应包含√B；若以collective volume作测度，\|ψ\|²才是相应密度。图的峰不能不说明测度就当作平坦角度histogram或实验方向频数；本worker没有据此判图错或重画替代图。

**对实验的限制：**真实观测通常比较同一I、同一π的候选带能级差及逐态EM网络。本文求解于固定ω，I不是好量子数；作者PDF15明确说用ω比较而非spin，并列PRM两带在同I=12/16/20/24ℏ时ω差.06/0/.02/.04MeV。不能将Fig8在同ω的gap直接当同I实验ΔE，或用一个I(ω)curve替两带共同映射。PDF13的“laboratory frame/symmetry restored”文字不等于已经完成严格总角动量投影。

本论文没有自身新的EM、τ、δ实验，也没有给此collective模型的完整实验B(E2)/B(M1)预测表；PDF14只回指Ref1的旧TAC/PRM带内rate比较。相似\|ψ\|²或小ΔE不等于已经验证两带所有电磁性质。要把该层用于135Nd/133Ce，需要目标核约束的势/质量、遗漏坐标与配置检查、明确同I映射和EM算符/矩阵元；不能迁移此示意模型的.20/.35MeV阈值、1.19/.01MeV能隙或C/J0到目标核当实验事实。

## 与TAC、RPA、PRM的关系和失效域

- TAC给V和惯量所需的单粒子响应，经典双极小不能单独预测隧穿gap。
- TAC+RPA描述局部小振幅振动；本文在有限φ区间对量子H对角化，因而可描述跨井波函数。**这不使质量推导摆脱其自身小幅度/绝热假设。**
- PRM是该示意体系的exact quantal comparator；本文比的是固定参数的这种体系，不是“所有真实核的exact理论”。PRM高频gap重开及second-vibration已是本文自己的反例。
- PDF15明确θ涨落未纳入。要研究两维取向或后续高spin模式变化，不能把它们说成本1D结果已经描述；本轮未另开第二篇2D方法文或运行未知代码。

知识影响为`adds-a-quantization-layer-and-bounds-it`：可补Day24经典/近谐图像到finite量子态的桥，同时保存此桥的冻结自由度、边界条件、same-ω/good-I差和内建反例。不得把“引入集体H”升级为任意候选双带已认证。

## 产物与命令检查

`source-and-reading.json`保存身份/下载/版本/SHA/真实覆盖；`claim-ledger.json`提供11项新增待核claim及精确locator；`source-parameter-check.json`只有上述一项源参数惯量代数核验；`artifact-manifest.json`保存产物hash。tmp含官方metadata、abs页、PDF及16页text/render。

执行：rg现有knowledge/raw（无本篇现成命中）；requests exact Crossref/INSPIRE与1条官方arXiv body路线；%PDF/content-type与SHA/页数检查；PyMuPDF逐页text/render及实际view_image；JSON解析、惯量公式代数控制。没有下载SI、批量检索综述、作者代码、实验拟合、canonical变更或Git写入。正文可得路线已成功，未触发额外body路线。
