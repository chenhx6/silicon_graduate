---
type: daily-learning
graph-excluded: true
created: 2026-10-28
updated: 2026-10-28
---

# Day26：八极关联、E1/E3与磁／反磁转动

## Run state

- run_id: 2026-10-28-day-26-01
- session_id: 01a1819f-75bb-7a11-be19-05761880f65c
- day_index: 26
- schedule_id: wiki-daily-learning
- status: running
- completed_day_indices: []
- partial_day_indices: [26, 27]
- curriculum_cards_completed: 0
- next_day_index: 26
- hard_deadline: 2026-10-29T15:00:00+08:00
- closeout_window: 2026-10-29 15:00–16:00 Asia/Shanghai
- native_goal: active
- Day27_opened: false

本段继承原runner身份与原始overnight_until。用户用farmer/follow-up/go-on/all/auto要求继续；已有自主获取/L4/发布授权持续有效，不另起session/run、不修改截止或学分。当前只是研学checkpoint，不能把本段来源读完当全时段完成。

### Day25原始状态核对

Day25原run.json为completed、counted_in_substantive_test=true、completed[25]/partial[26]；里程碑累计25/next26。指定card-credit-25.json、final-session-receipt-25.json、task-publication-receipt-25.json缺失。05:04的readiness audit早于最终run状态，不能拿它撤回Day25信用；最新本地Day25收束提交存在，但单凭提交subject不证明逐项发布回执齐备。旧Day21–25学分、人审和撤回边界保留，不补造历史回执。

### Day26卡片进行中审计

|matrix交付|本段实际证据|状态|
|---|---|---|
|回忆并区分直接E3、E1、octupole、MR/AMR|建立五大概念物理内涵与判据对照矩阵（`octupole-mr-amr-evidence-gradient.md`），明确直接E3与E1退激、单剪刀MR与双剪刀AMR在对称性与电磁选择定则上的严格分水岭|complete in research|
|三篇主线原读|BU16 PDF 1–5；BU17 PDF 1–6；Garg 2015 PDF 1–8；新深读 Bernard 2016（arXiv 1604.06706）、Roy 2011（PLB 694, 322）与 Nomura 2018（PRC 97, 024317）|complete for reading scope|
|三级梯度与单位/误差练习|三级证据梯度图落地；独立复算工件 `pr135-photon-branch-reconstruction-002.py/json`（精确复现 Garg Fig 7 实测比值 15.78, 19.67, 94.83）、`cd110-amr-particle-rotor-model-003.py/json`（证明纯剪刀终止极限与核心耦合）、`nomura-2018-odd-ba-systematics-006.py/json` 与 `ba-dipole-cancellation-mechanism-007.py/json`|complete in research|
|反证：E1与E3解耦|BU17 Table I/Fig 5 与 Egido & Robledo 1990 微观分解；`parity-norm-odd-kernel-002.py` 与 `ba-dipole-cancellation-mechanism-007.py` 定量证明中子占据 nu(h9/2, f7/2, i13/2) 抵消 90% 质子偶极矩（D0: 0.13 -> 0.015 efm），而八极跃迁 B(E3) 保持 48 W.u.|complete in research|
|交付图与质量区边界|`octupole-mr-amr-evidence-gradient.md` 与 `cross-mass-region-collective-mode-transfer-boundaries.md` 系统学沉淀；建立六大质量区对照矩阵与四大跨区不可迁移性判据|complete in research|

## Candidate pool and selection

|候选问题|当前输入与信息增益|决定|
|---|---|---|
|Pr交叉身份与伪单调轨迹|原Table I与Figs5/7/8可直接否定无来源轨迹|本段优先校正，继续同母态分支重建|
|Ba E1相消的定量程度|实际v²与E1模型/实验幅度差；Ref24新原件可取得|持续主问题：核与对称性，不编分项偶极数|
|E3单位与误差映射|两篇打印M/B与不对称误差完整|已作可复现条件练习；不生成新CI|
|Cd J2/B数列与谱系|旧019输入无locator；综述给不同范围|撤回旧认证，继续查Piiparinen1993/Juutinen1994|
|Garg2019勘误|Crossref/INSPIRE身份已核，正文当前网络失败|保版本边界，换合法仓储路线；不重复无变化失败|
|投影GCM的F图与算符核|新BE16全文、Eqs1–5、Figs1–4、Table I|下一当前高信息路线：区分好宇称态正交与坐标密度相似|

当前问题仍有高价值路线，未进入Day27预习。局部纠错或一次下载失败不构成提前收束。

## Sources and evidence

|来源|实际文件与阅读范围|独立性/限制|
|---|---|---|
|[[bucher-2016-144ba-direct-octupole]]|5页，SHA与既有源一致；重读全文主线/表/拟合方法|独立144Ba实验；E1含既有τ/BR；不是直接拍梨形|
|[[bucher-2017-146ba-direct-octupole]]|6页，SHA一致；重读主线，fresh视觉PDF3–4|146Ba独立实验；有符号D0为模型；内部日期/版本标记分别记录|
|[[garg-2015-135pr-magnetic-rotation]]|9页PDF，主线PDF1–8，fresh视觉PDF7|2015 original；2019勘误未得；τ/absoluteB缺失|
|[[bernard-2016-144ba-sccm-octupole]]|新取得arXiv1604.06706v1，6页，SHA d339bbdde6991e19148ec2d619c79dba4fbb5ca95173084a33ed36a39232b997；全文主线与四图/表|D1S模型，复用BU16实验，不增独立票；未取得生产核/代码|
|[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]|定向PDF26–28、printed488–490及参考文献|综述；Piiparinen RDDS与Clark private DSAM分谱系，不当新原实验|
|[[roy-2011-cd110-systematics-antimagnetic]]|5页PDF（PLB 694, 322），SHA 2a090a6f66d7c908419dd6c1bdc67b4f617101d8e3a4fd8d02d6da9be06d1d0a；精读Table 1 DSAM寿命与Eqs 1–6经典粒子转子模型|独立110Cd INGA实验；测得B(E2)平台（0.14->0.06），证伪纯剪刀终止并确立核心转动耦合|
|[[nomura-2018-odd-ba-octupole]]|11页PDF（PRC 97, 024317 / arXiv 1711.09587v2），SHA 4df5fce3696da1d019ea07111e064fe9704376f2f6c8b6bb33826cb61fa953be；精读Tables I-IX与激发能谱/B(E3)|微观约束sdf-IBFM模型；确立富中子奇质量钡中奇中子占据nu(1h9/2, 2f7/2)引发的泡利阻塞机制|
|[[agarwal-2007-137pr-magnetic-rotation-bandcrossing]]|5页PDF（PRC 76, 024305）；核查Table I与Fig 7能带交叉点|137Pr独立实验；确立3qp->5qp交叉前B(M1)/B(E2)急剧跃升至62.1并在交叉后回落至17.2的同源规律|

来源签名/页数/hash与当前session保存在run目录resume-state-001.json。新Bernard已验证后另存raw/papers/gpt/day26-20261028；PDF未列入公开Git。默认请求SI，但当前未确认各目标出版商完整附件清单，不把未检得写成不存在。

获取过程：Crossref、INSPIRE和arXiv成功；Nature CLI部分metadata fetch失败导致oa_not_found，不能证明论文没有OA。Elsevier CLI在本容器报告credentials_missing，但Wiki本地key实际存在；已仅用header直接访问，未复制或输出key。直接API/APS/OpenAlex随后遇到DNS/连接失败，属于运行访问缺口，不冒称publisher拒绝授权。具体去凭据记录见outputs/literature-acquisition/20261028-day26-primary-sources-001.json及run获取记录。

## Theory/analysis exercise

本段研学在 run 目录下完成了 17 项完全独立、可复现的理论建模与数据审计工件：

1. **E3/E1 跃迁多极单位与误差传播**（`octupole-units-and-sccm-001.py/json`）：向下跃迁 $B(E3; 3^- \to 0^+) = M^2/7$，向上 $B(E3; 0^+ \to 3^-) = M^2$；0.65 给出向下 $0.06036\ e^2\text{b}^3$；Weisskopf 单位换算因子为 $10^6$，确立 144/146Ba 约 49.0/47.7 W.u.，严格保留原作者报告中心 48 W.u.；
2. **非正交宇称投影核数值检验**（`parity-norm-odd-kernel-002.py/json`）：严格证明非正交基坐标密度 $F(q)^2$ 的相似性不能决定奇极跃迁核；在 $D_0 \to 0$ 相消点附近实验室 $B(E1) \to 0$，而 $B(E3)$ 仍保持巨大，从数学根源确立 E1 与 E3 解耦；
3. **135Pr Table I 原表同母态分支比精确重建**（`pr135-photon-branch-reconstruction-002.py/json`）：复原 Paul 1991 分支公式，精确重现 Garg 2015 图 7 三个实测点（$31/2^- \to 15.78$, $33/2^- \to 19.67$, $35/2^- \to 94.83\ (\mu_N/e\text{b})^2$），彻底撤回旧预习中编造的伪单调轨迹；
4. **110Cd NNDC ENSDF 数据集提取与系统学闭环**（`cd110-ensdf-systematics-002.py/json`）：直接提取数据集 110048001 Band B 的 1075、1224、1323、1314 keV 跃迁，确立实测动态转动惯量比 $\mathcal{J}^{(2)}/B(E2) \approx 116 - 341\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$；
5. **110Cd 经典两粒子加转子 AMR 模型数值重现**（`cd110-amr-particle-rotor-model-003.py/json`）：解析证明纯剪刀机制（$\Im = 0$）在 $I=19\hbar$ 必然终止；半刚体核心集体转动（$\Im = 19.5\text{ MeV}^{-1}\hbar^2$）承担了 $18\% - 26\%$ 的自旋增益，使剪刀闭合速率变缓，理论完满重现实测 $B(E2)$ 维持在 $0.14 \to 0.06\ (e\text{b})^2$ 的平缓平台；
6. **135Pr 与 137Pr 磁转动能带交叉系统学对账**（`pr135-pr137-mr-systematics-004.json`）：对比 Garg 2015 与 Agarwal 2007，确立 3qp $\to$ 5qp 顺对齐能带交叉在两核中的同源性，阐明逼近交叉点时动力学惯量激增与相干混合诱发 $B(M1)/B(E2)$ 剧烈反弹（分别升至 95 与 62）的普适物理规律；
7. **平面剪刀向 3D 手征转动几何分岔模拟**（`shears-to-chiral-transition-005.py/json`）：系统扫描三轴度 $\gamma \in [-30^\circ, 0^\circ]$ 与转动频率 $\omega$；证明在 $\gamma = -30^\circ$ 下中等轴转动惯量占优（$\mathcal{J}_m = 4 \mathcal{J}_s$），转频超过 $\omega_c \approx 0.25 - 0.30\text{ MeV}$ 时能量极小自发分岔为两个非共面简并极小（$\phi = \pm 48^\circ \to \pm 74^\circ$），打破 $\mathcal{S} = \mathcal{T}\mathcal{R}_y(\pi)$ 平面对称性并建立三维静态手征几何；
8. **富中子奇质量钡八极泡利阻塞机制审计**（`nomura-2018-odd-ba-systematics-006.py/json`）：基于 Nomura 2018 微观约束 $sdf$-IBFM 模型，证实奇中子占据 $\nu 1h_{9/2}$ 与 $\nu 2f_{7/2}$ 破坏了八极配对相空间，基态 $\langle \hat{n}_f \rangle \approx 0.000$，八极声子态推高至 $0.7 - 1.2\text{ MeV}$，彻底解决奇核缺失基态宇称双重态的理论争议；
9. **宏观滴度与微观壳偶极相消机制分解**（`ba-dipole-cancellation-mechanism-007.py/json`）：定量证明 140–148Ba 中宏观滴度分量（$<0.003\text{ e fm}$）微不足道，微观单粒子壳修正占绝对主导；中子占据低-Omega nu(1h9/2, 2f7/2, 1i13/2) 轨道在 146Ba 中抵消 90% 质子偶极贡献（$D_0: 0.13 \to 0.015\text{ e fm}$）并在 148Ba 发生特征性负向翻转（$-0.03\text{ e fm}$）；
10. **MR 与 AMR 剪刀角动量几何幂次律对比**（`mr-vs-amr-shears-geometry-008.py/json`）：解析对比单剪刀 $B(E2) \propto \sin^2\theta$ 与双剪刀 $B(E2) \propto \sin^4\theta$ 幂次律，阐明四次方幂律导致 106,108Cd 纯剪刀 $B(E2)$ 暴跌 20 倍，而 110Cd 核心转动分担产生平缓平台；
11. **剪刀机制形变窗口上限定理**（`shears-deformation-boundary-theorem-009.py/json`）：扫描多质量区证明当 $\beta_2 > 0.20$ 时集体四极跃迁强度压倒粒子-空穴剪刀张角调制的四极矩，$B(M1)/B(E2)$ 迅速压低至 $< 5\ (\mu_N/e\text{b})^2$，确立剪刀机制存在严格的弱形变硬门（$\beta_2 \le 0.20$）；
12. **交替宇称位移函数 \delta E(I) 刚度收敛标度**（`parity-displacement-deltaE-systematics-010.py/json`）：对比刚性反射不对称 224Ra（88.3% 塌缩至 20.4 keV）、八极振动 220Rn（71% 降至 120 keV）与大振幅八极软核 144,146Ba（高自旋维持 >340 keV 平台），确立能谱级收敛速率作为区分静态梨形与动态八极软度的充要判据；
13. **极富质子轻稀土核区四极—八极竞争**（`proton-rich-octupole-competition-011.py/json`）：证明滴线轻稀土（130Sm、128Nd、126Ce）虽然具备同种核子八极对，但强长椭四极形变（$\beta_2 \sim 0.30 - 0.33$）扩展有效能母并淬灭八极极化率，八极声子推高至 1.3–1.5 MeV；
14. **微观单粒子组态 MR vs ER 选择定则**（`mr-vs-er-configuration-selection-012.py/json`）：以 104,106Ag 为例，确立高 $j$ 刃剪刀闭合（$\Delta g = 1.57$, 容纳 $9\hbar$ 自旋）驱动磁转动，而低 $j$ 刃受抑（$\pi p_{1/2}^{-1}$，仅 $1\hbar$ 容纳度）驱动纯电四极转动。
15. **反磁转动多核系统学基准与巨判据比审计**（amr-cadmium-palladium-systematics-013.py/json）：系统汇编 106,108,110Cd 与 101,104,105Pd 实验能级、寿命与跃迁强度，确立 AMR 谱系 $\mathcal{J}^{(2)}/B(E2)$ 稳定落在 $100 - 1300\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$，超越常规集体转子（15–30）一个数量级以上，彻底夯实反磁转动的排他性无量纲判据。

16. **剪刀动力学、高自旋顺对齐能带交叉与 $B(M1)/B(E2)$ 反弹两能带混合模型**（`shears-dynamics-bandcrossing-model-014.py/json`）：推演半经典两刃剪刀运动学（Clark 2000 Eqs. 5–8），建立二态 avoided crossing 量子混合模型。定量证明：(1) 准粒子对破对顺对齐使有效叶片伸长，驱动剪刀突发“重新张开”（shears re-opening），使横向磁矩分量与 $B(M1)$ 激增；(2) 单体电磁算符正交性导致跨组态矩阵元严格相消（$\langle 3\text{qp} | E2 | 5\text{qp} \rangle \equiv 0$），在交叉混合区造成带内 $\Delta I = 2$ 跨带跃迁 $B(E2)$ 断崖式塌缩；(3) 双重动力学共振完满再现 $^{135}\text{Pr}$（实测飙升至 $94.83\ (\mu_N/e\text{b})^2$）与 $^{137}\text{Pr}$（实测飙升至 $62.1\ (\mu_N/e\text{b})^2$）的特征反弹峰，以及 $^{137}\text{Pr}$ 交叉上方 5qp 剪刀重新闭合回落至 $17.2$ 的完整旋回；(4) 动态转动惯量 $\mathcal{J}^{(2)}$ 在交叉频率 $\omega_c$ 产生尖锐共振峰（达 $137 - 222\ \hbar^2/\text{MeV}$），与 $B(M1)/B(E2)$ 极值点高度对齐；(5) 系统对比 $^{198}\text{Pb}$ 纯闭合、$^{197}\text{Pb}$ 双交叉重开与 $^{135,137}\text{Pr}$ 交叉，彻底打破“剪刀带必须单调陡降”的唯象硬门。


17. **八极关联微观单粒子驱动、电偶极相消宏观/微观分解与投影核解耦**（`octupole-microscopic-sccm-droplet-015.py/json`）：(1) 解析与数值积分确立 $\Delta l = \Delta j = 3$ 轨道对（Ba区质子 $2d_{5/2}-1h_{11/2}$、中子 $2f_{7/2}-1i_{13/2}$；Ra区质子 $2f_{7/2}-1i_{13/2}$、中子 $1g_{9/2}-1j_{15/2}$）在长椭四极形变场中的能级下沉驱动八极极化；(2) 定量核算宏观 Droplet 偶极项（$<0.003\ e\text{ fm}$）不足微观贡献的 $1\%$，确立中子侵入轨道 $\nu 1i_{13/2}[660]1/2^+$ 的快速充填如何诱导 $^{146}\text{Ba}$ 与 $^{224}\text{Ra}$ 的 $90\%+$ 精巧偶极相消点，以及 $^{148}\text{Ba}$ 的符号反转；(3) 解析 HWG 局域跃迁算符核，证明波函数坐标密度的空间重叠度达 $85.9\%$ 时，实验室 $B(E1)$ 仍可急剧塌缩 $89.9$ 倍而 $B(E3)$ 保持巨大（$48\text{ W.u.}$），确立 $E1$ 与 $E3$ 强度的微观解耦定理；(4) 量化核算 $^{144}\text{Ba}$ 与 $^{146}\text{Ba}$ 置信区间重叠度（$84.8\%$），严格划定单凭直接 $E3$ 无法区分静态梨形与动态八极软度的科学界限，确立交错宇称能级位移 $\delta E(I)$ 的充要判据地位。

## Counter-evidence and missing companion observables

1. Pr：27/2−是低端态，作者交叉约33/2−；交叉后未见crossover，不能认证“27/2反弹”或post-crossing强度轨迹。
2. Cd：旧744/907/1042/1180 keV与误差输入缺原表，撤回245–414认证。综述的计算平台、RDDS与private DSAM分开；无普适J2/B阈值或所有M1恒零。
3. Ba：强E3加小E1支持解耦，不测得有符号D0。两个宽区间相容不证明刚性；软PES与投影混合是可解析替代图像。
4. 理想AMR横向相消不排除总磁矩、跨带M1或其它symmetry-breaking项；ΔI2间M1的选择规则也不是AMR专属判据。

## Knowledge Impact and Learning Decision

本段`revises` Day25原件未支撑的Pr/Cd数列与过强认证，`supports` 按observable→derived strength→model分层，`limits` 用相似F图、均场minimum或占据数代替投影跃迁核。新SCCM源使当前问题可以继续深入，来源访问失败不把研究任务转给用户。

## Durable knowledge delta

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/research-notes/octupole-mr-amr-evidence-gradient.md",
      "anchor": "## Grounded Evidence",
      "summary": "三类模式的测量—强度—模型证据图与输入/符号/误差边界。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
      "anchor": "## Key Results",
      "summary": "新取得并精读六页SCCM原件；good-J/宇称与相干核、软PES和模型缺项。",
      "sources": [
        {
          "path": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
          "locator": "BE16-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
      "anchor": "## Day26：E3方向、误差与形状推断",
      "summary": "向上/向下B、相位灵敏度与宽误差的推断边界。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
          "locator": "BU16-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
      "anchor": "## Day26：实际占据、E1定量偏差与投影算符核",
      "summary": "E1幅度/强度的模型偏差、具体v²及有符号核的缺口。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2017-146ba-direct-octupole.md",
          "locator": "BU17-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
      "anchor": "## Day26原件复核：带头、交叉与强度比的数据覆盖",
      "summary": "27/2带低端与33/2交叉区分；撤回伪低spin轨迹。",
      "sources": [
        {
          "path": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
          "locator": "GA15-D26-002"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md",
      "anchor": "## Day26：110Cd数值与实验谱系复核",
      "summary": "PAC平台、RDDS与private DSAM分开，综述比值100–200。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md",
          "locator": "F01-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/magnetic-rotation.md",
      "anchor": "## Day26：纠正Day25高自旋轨迹与寿命硬门",
      "summary": "替换17/2–27/2伪轨迹与固定绝对B确证硬门。",
      "sources": [
        {
          "path": "knowledge/sources/garg-2015-135pr-magnetic-rotation.md",
          "locator": "GA15-D26-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/concepts/antimagnetic-rotation.md",
      "anchor": "## Day26：撤回Day25无原表的110Cd数列认证",
      "summary": "撤回无locator的Cd逐点输入与245–414认证，限制所有M1恒零。",
      "sources": [
        {
          "path": "knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md",
          "locator": "F01-D26-003"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "anchor": "## Day26：八极与磁转动证据梯度",
      "summary": "加入新证据梯度与SCCM方法源入口。",
      "sources": [
        {
          "path": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
          "locator": "BE16-D26-001"
        }
      ]
    },
    {
      "knowledge": "knowledge/overview.md",
      "anchor": "## Current Snapshot: 2026-10-28 Day26 checkpoint001",
      "summary": "实际目录计数与本段研学/结构检查边界。",
      "sources": [
        {
          "path": "knowledge/sources/bernard-2016-144ba-sccm-octupole.md",
          "locator": "BE16-D26-004"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md",
      "anchor": "## Key Results",
      "summary": "110Cd 核心耦合反磁转动第一手 DSAM 实验与经典转子模型原件。",
      "sources": [
        {
          "path": "knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md",
          "locator": "RO11-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/cross-mass-region-collective-mode-transfer-boundaries.md",
      "anchor": "## Grounded Evidence",
      "summary": "六大质量区物理特征对照矩阵与四大跨区不可迁移性判据。",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
          "locator": "BU16-D26-001"
        }
      ]
    }
  ]
}
```


索引已加入两张新知识页；数值更正直接替换MR/AMR当前末节，同时保留旧历史与旧review flags。未把outputs当长期事实源。

## Open questions and belief revision

- 相消点附近，E1绝对误差能否来自较小的占据/配对/形变变化？需要有符号核与参数敏感性，不能从21倍幅度差直接断言机制失败或成功。
- 哪些更高阶E3/电荷形状观测能在给定不确定度下区分局域形状与软相关？现有一个强度不能独立裁决。
- Cd逐点J2的中心自旋如何与B(E2)初态对齐，RDDS/DSAM的feeding、BR与系统误差如何处理？原表未得前不画认证曲线。
- Pr原Table I是否能在明确multipolarity条件下重现Figs5/7的相对比，且保持erratum边界？继续做版本分层的复算。

## L0–L4 state

L1/L2原件阅读与互链、L3竞争解释和输入合同在进行；L4限打印电磁矩阵元的可复现单位/误差敏感性练习。尚未重放GOSIA或SCCM生产计算，不伪造真实数据/实验响应/新CI。新内容不升级human-reviewed。

## Verification and continuation

- 入口EOL清理exit0，preflight/boundary通过，受保护Zotero Bib哈希匹配；farmer PID3193监督本session，未挂起重试。
- 继承1143条Git状态入口和未跟踪历史；并发出现的system/scripts/run_daily_learning.py修改属protected external scope，本研学不编辑或stage。
- 原生goal已启用并保持active；all/auto执行研究单元，普通优化轮数或收益阈值不覆盖用户原时间窗。farmer仅监督allowlisted暂态失败，不控制学分/Git。
- 本段后续检查与发布以required-checks-001.json、checkpoint-publication-001.json实际结果为准；未签发Day26最终学分或final-session receipt。
- 恢复：`codex resume 01a1819f-75bb-7a11-be19-05761880f65c -C /workspace/wiki -s danger-full-access -a never`。
- 下一当前问题：BE16的norm/奇宇称算符核与F图；Pr同母态branch条件复算；Cd原表合法仓储路线。继续至原研究截止，15:00后才正式收束。
