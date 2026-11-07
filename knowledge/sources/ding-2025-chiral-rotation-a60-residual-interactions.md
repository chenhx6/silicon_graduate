---
type: source
title: "Ding等2025：A≈60手征与残余质中力（PRM正文精读）"
aliases: [Ding 2025 A60 chirality, Ding2025CPC, Ding 2025 CPC 49 074101]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
source_type: theory-article
reading_depth: deep-read
title_original: "Exploring chiral rotation in A≈60 nuclei: Role of residual interactions"
authors: [G. L. Ding, R. Dong, H. Y. Liu, J. Peng, Q. B. Chen]
journal: Chinese Physics C
year: 2025
volume: 49
pages: 074101
doi: 10.1088/1674-1137/adc3fd
canonical_source: "doi:10.1088/1674-1137/adc3fd"
citation_key:
raw_file: "raw/papers/Exploring chiral rotation in A ≈ 60 nuclei  Role of residual interactions.pdf"
raw_sha256: 5264bd9192b988021d2ee21f2861bce80f2f7ac04ba26f04ea3f0e8125be599e
archive_required: true
tags: [chirality, a60, residual-interaction, prm, cobalt-isotopes]
---
# Ding等2025：A≈60核区手征转动与残余质中相互作用（PRM正文精读）

## Bibliographic Record

G. L. Ding (丁赣龙), R. Dong (董荣), H. Y. Liu (刘虹余), J. Peng (彭婧), Q. B. Chen (陈启博), "Exploring chiral rotation in A ≈ 60 nuclei: Role of residual interactions", *Chinese Physics C* **49**, 074101 (2025), DOI: [10.1088/1674-1137/adc3fd](https://doi.org/10.1088/1674-1137/adc3fd).
原件 PDF 共 9 物理页（含第 1 页下载封面，正文共 8 页，页码 074101-1 至 074101-8），SHA-256: `5264bd9192b988021d2ee21f2861bce80f2f7ac04ba26f04ea3f0e8125be599e`。

### Crossref 历史记录保留

在本轮获取正文 PDF 之前，曾于 2026-11-07 早先阶段获取 Crossref XML 元数据与摘要（文件 `raw/papers/gpt/query/20261107-round2-orientation-window/ding-full/ding-2025-cpc-jats.xml`，SHA-256: `504ec53861a4a00c6d2deb178c3d29d847fc7b938bb3c201617b26011a448244`）。当时受限于元数据边界，仅能核实摘要内容。现正文 PDF 已归档入库，完成全文深度精读。

## Scope and Reading Depth

### Covered scope

1. **全文 8 页正文（Physical pp. 2–9 / Article pp. 074101-1 至 074101-8）完整阅读**：
   - Sec. I 引言：核手征性背景、实验观测现状（A≥80）、A≈60 探索动机与先前理论（$^{60}\text{Ni}$、Co 同位素 CDFT 研究）（Physical pp. 2–3 / Article pp. 074101-1 至 074101-2）。
   - Sec. II 理论框架：粒子转子模型（PRM）包含残余质中相互作用 $V_{pn}$ 的哈密顿量构建、流体转动惯量 $\mathcal{J}_k = \mathcal{J}\sin^2(\gamma - 2\pi k/3)$、单粒子/单空穴本征哈密顿量 $\hat{H}_{\text{intr}}$、零程 $\delta$ 相互作用 $V_{pn}$、强耦合基底 $|IMK\phi\rangle$ 及 $D_2$ 对称化、角动量主轴投影概率 $P_K$ 与内禀方位角取向分布 $P(\theta, \phi)$（Physical pp. 3–4 / Article pp. 074101-2 至 074101-3）。
   - Sec. III 数值细节：理想组态 $\pi f_{7/2}^{-1} \otimes \nu g_{9/2}^1$、四极形变 $\beta=0.25$、转动惯量 $\mathcal{J}=10\ \hbar^2/\text{MeV}$、电磁跃迁参数 $Q_0=1.28\text{ eb}$、$g_R=0.48$、$g_p=1.336$、$g_n=-0.255$（Physical p. 4 / Article pp. 074101-3 至 074101-4）。
   - Sec. IV 结果与讨论：
     - 亚节 A：三轴形变参数 $\gamma$（$15^\circ$ 至 $45^\circ$）对能谱能差 $\Delta E(I)$、内带 $B(M1)$ 与 $B(E2)$ 的影响（Figs. 1–3，Physical pp. 4–6 / Article pp. 074101-3 至 074101-5）。
     - 亚节 B：残余质中相互作用 $V_{pn}$（$u_1=-0.2, -0.4, -0.6\text{ MeV}$，$u_0:u_1 = 3:1, 6:1, 9:1, 12:1$）对能谱差 $\Delta E(I)$、能量交错参数 $S(I)$、内带 $B(E2)$ 与 $B(M1)$ 的影响（Figs. 4–7，Physical pp. 5–7 / Article pp. 074101-4 至 074101-6）。
     - 亚节 C：手征模式的自旋演化，$K$ 分布（Fig. 8）与方位角取向图 $P(\theta, \phi)$（Fig. 9）（Physical pp. 6–8 / Article pp. 074101-5 至 074101-7）。
   - Sec. V 总结（Physical p. 8 / Article p. 074101-7）。
   - 读取参考文献列表；没有据此声称已取得或逐篇核验72份被引原文。

### Not covered

1. 论文未提供 PRM 的底层数值 Fortran 程序源码与矩阵截断维数。
2. 论文未给出零程 $\delta$ 力的谐振子频率参数 $\hbar\omega$ 明确数值及径向波函数积分值。
3. 论文**未包含任何真实钴同位素的实验测量能级、跃迁能量或分支比数据**，全部计算基于理想假设构型。

## Key Results

| ID | 论断内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| D25-01 | 采用单粒子-单空穴耦合三轴刚性转子模型（PRM）包含残余质中相互作用 $V_{pn}$，总哈密顿量为 $\hat{H}_{\text{PRM}} = \hat{H}_{\text{coll}} + \hat{H}_{\text{intr}} + V_{pn}$。 | model-result | direct | Physical p. 3 / Article p. 074101-2, Eqs. (1)–(3) | false |
| D25-02 | 转子采用无辐散流体惯量 $\mathcal{J}_k = \mathcal{J}\sin^2(\gamma - 2\pi k/3)$；本征单粒子耦合常数 $C = \frac{123}{8}\sqrt{\frac{5}{\pi}}\frac{2N+3}{j(j+1)}A^{-1/3}\beta\text{ MeV}$。 | model-result | direct | Physical p. 3 / Article p. 074101-2, Eqs. (2)–(4) | false |
| D25-03 | 零程残余力形式为 $V_{pn} = \sqrt{8\pi^3}(\hbar/m\omega)^{3/2}\delta(\mathbf{r}_p - \mathbf{r}_n)[u_0 + u_1\boldsymbol{\sigma}_p \cdot \boldsymbol{\sigma}_n]$，强度参数 $u_1 \in \{-0.2, -0.4, -0.6\}\text{ MeV}$，$u_0:u_1 \in \{3:1, 6:1, 9:1, 12:1\}$。 | model-result | direct | Physical p. 3 / Article p. 074101-2, Eq. (7); Physical p. 5 / Article p. 074101-4 | false |
| D25-04 | 针对不对称理想构型 $\pi f_{7/2}^{-1} \otimes \nu g_{9/2}^1$（忽略 $(fp)$ 壳贡献），扫描 $\gamma \in [15^\circ, 45^\circ]$ 发现能量简并度最好的极小能差发生在 $\gamma = 34^\circ$（$\Delta E = 64\text{ keV}$，位于 $I=10\hbar$），偏离对称组态的最大三轴性 $\gamma = 30^\circ$（$\Delta E = 171\text{ keV}$）。 | model-result | direct | Physical pp. 4–5 / Article pp. 074101-3 至 074101-4, Fig. 1 | false |
| D25-05 | 理想手征参数确定为 $\beta = 0.25$、$\gamma = 34^\circ$、$\mathcal{J} = 10\ \hbar^2/\text{MeV}$；电磁参数取 $Q_0 = 1.28\text{ eb}$、$g_R = 0.48$、$g_p = 1.336$、$g_n = -0.255$。 | model-result | direct | Physical p. 4 / Article pp. 074101-3 至 074101-4 | false |
| D25-06 | 在理想参数下，内带 $B(M1)$ 在 $I > 11\hbar$ 表现出奇偶交错（奇到偶自旋增强，偶到奇自旋受禁）；双重带内带 $B(E2)$ 几乎重合且在 $I \le 11\hbar$ 受阻，符合手征转动指纹。 | model-result | direct | Physical pp. 4–6 / Article pp. 074101-3 至 074101-5, Figs. 2–3 | false |
| D25-07 | 引入残余相互作用 $V_{pn}$ 后，双重带能差 $\Delta E(I)$ 在高自旋区显著增大，能量交错参数 $S(I) = [E(I)-E(I-1)]/2I$ 产生大振幅奇偶交错且双重带位相相反（由于三轴条件下 $V_{pn}$ 诱发的 signature inversion）；而 $B(E2)$ 与 $B(M1)$ 几乎不受 $V_{pn}$ 影响。 | model-result | direct | Physical pp. 5–7 / Article pp. 074101-4 至 074101-6, Figs. 4–7 | false |
| D25-08 | 作者按所扫模型的能谱/交错认为较小的 $\lvert u_0\rvert$ 与 $u_0:u_1$ 更有利于手征双带；几何分布条件另见D25-09。 | author-interpretation | direct | Physical p. 6 / Article p. 074101-5; Physical p. 8 / Article p. 074101-7 | false |
| D25-09 | 角动量主轴投影 $K$ 分布（Fig. 8）与方位角分布 $P(\theta, \phi)$（Fig. 9）在最大残余相互作用强度（$u_0 = -7.2\text{ MeV}, u_1 = -0.6\text{ MeV}$）下显示：$I=8, 9\hbar$ 为垂直于 $sl$ 平面的手征振动；$I=10\hbar$ 表现出明确的双峰非共面（aplanar）取向（带 A 位于 $(\theta \approx 55^\circ, \phi \approx \pm 70^\circ)$，带 B 位于 $(\theta \approx 55^\circ, \phi \approx \pm 30^\circ)$），表明静态手征性在强残余相互作用下依然存在；$I=12\hbar$ 转入 $li$ 平面内的新型手征振动。 | model-result | direct | Physical pp. 6–8 / Article pp. 074101-5 至 074101-7, Figs. 8–9 | false |
| D25-10 | 本文研究为理想模型研究，**未展示任何真实钴同位素（如 $^{57,58,59,60}\text{Co}$）的实验数据**，形变参数并非实测值，亦非微观自洽 PES 极小值。 | our-inference | direct | Physical pp. 2–8 / Article pp. 074101-1 至 074101-8 | false |

## Hamiltonian and Mathematical Formulation

### 1. 转子哈密顿量 $\hat{H}_{\text{coll}}$

$$
\hat{H}_{\text{coll}} = \sum_{k=1}^3 \frac{\hat{R}_k^2}{2\mathcal{J}_k} = \sum_{k=1}^3 \frac{(\hat{I}_k - \hat{J}_k)^2}{2\mathcal{J}_k} \quad (\text{Eq. 2})
$$
其中主轴取向惯量采用无辐散流体公式：
$$
\mathcal{J}_k = \mathcal{J} \sin^2\left(\gamma - \frac{2\pi k}{3}\right), \quad k=1, 2, 3 \quad (\text{Phys p. 3 / Art p. 074101-2})
$$
轴编号、量子化轴与方位分布须沿用原文约定，不能从惯量编号自行指定所有模型的长/中/短轴。

### 2. 本征单粒子单空穴哈密顿量 $\hat{H}_{\text{intr}}$

$$
\hat{H}_{\text{intr}} = \pm \left[ \frac{1}{2} C \left\{ \cos\gamma \left( \hat{j}_3^2 - \frac{j(j+1)}{3} \right) + \frac{\sin\gamma}{2\sqrt{3}} (\hat{j}_+^2 + \hat{j}_-^2) \right\} \right] \quad (\text{Eq. 3})
$$
质子空穴取负号（$\pi f_{7/2}^{-1}, j_p=7/2, N=3$），中子粒子取正号（$\nu g_{9/2}^1, j_n=9/2, N=4$）。耦合参数：
$$
C = \frac{123}{8} \sqrt{\frac{5}{\pi}} \frac{2N+3}{j(j+1)} A^{-1/3} \beta \text{ MeV} \quad (\text{Eq. 4})
$$

### 3. 残余质中相互作用 $V_{pn}$

$$
V_{pn} = \sqrt{8\pi^3} \left(\frac{\hbar}{m\omega}\right)^{3/2} \delta(\mathbf{r}_p - \mathbf{r}_n) \left[ u_0 + u_1 \boldsymbol{\sigma}_p \cdot \boldsymbol{\sigma}_n \right] \quad (\text{Eq. 7})
$$
扫描强度参数：$u_1 \in \{-0.2, -0.4, -0.6\}\text{ MeV}$，$u_0:u_1 \in \{3:1, 6:1, 9:1, 12:1\}$。最大扫描强度对应 $u_1 = -0.6\text{ MeV}, u_0 = -7.2\text{ MeV}$。

### 4. 方位角取向分布

原文Eq11以D函数、强耦合系数和内禀态求和定义P(θ,φ)。这里回到原式而不
用同一个φ同时代表内禀态标签和方位角。PDF7正文明确θ为总角动量与l轴夹角，
φ为其在si平面的投影相对s轴夹角；具体概率是模型输出，不是测得取向。

## Competing Interpretations and Limitations

1. **“弱残余相互作用利于手征”的适用条件与多重解读**：
   - 论文在能谱简并度 $\Delta E(I)$ 与能量交错参数 $S(I)$ 上发现，强 $V_{pn}$ 会导致高自旋能差发散，并诱发 signature inversion 导致双重带 $S(I)$ 呈现反相大奇偶交错，从能谱与交错指纹角度不利于理想手征。
   - **关键反例/竞争证据**：在微观角动量几何分布（方位角图 $P(\theta, \phi)$ 与 $K$ 分布，Figs. 8–9）中，即使在最大相互作用强度 $u_0 = -7.2\text{ MeV}, u_1 = -0.6\text{ MeV}$ 下，$I=10\hbar$ 处依然呈现严格的非共面（平面外）双峰静态手征取向，并未退化为共面转动！因此，“不利于手征”主要体现在高自旋能级简并度被破坏和 signature 交错，而非将手征几何直接摧毁为共面解。
2. **理想组态假设与真实核结构的脱离**：
   - 忽略 $(fp)^n$ 价核子对总角动量的贡献，将系统简化为严格的单粒子-单空穴。真实核需另确定跨壳代价、占据、组态混合和形变响应，本模型未给出这些量对所有A≈60核的统一值。
   - 刚性转子假设无法考虑核芯对激发态的极化响应；微观壳模型或包含 $(fp)$ 壳相互作用的 IBFFM/TAC-CDFT 可能改变相互作用矩阵元的主导符号与大小。
3. **实验数据对比的缺失**：
   - 论文没有任何实验能谱或跃迁率的拟合曲线。所有参数均为探索性模型输入，不能作为 A≈60 存在手征双重带的实验确证。

## Extracted Pages

- 规范存档文件：`raw/papers/Exploring chiral rotation in A ≈ 60 nuclei  Role of residual interactions.pdf`
- 物理页数：9 页（第 1 页为 IOP/CPC 官方下载封面，标注下载日期 07/11/2026 及 IP 地址；第 2–9 页为文章正式内容）。
- 正文页码：074101-1 至 074101-8。
- SHA-256：`5264bd9192b988021d2ee21f2861bce80f2f7ac04ba26f04ea3f0e8125be599e`。
- 详细分析与可计算输入合同见研究笔记 [[campaign-g03-ding60-fulltext-20261107]]。

## Agent Self-audit Triage

P0: none identified in PDF identity/hash。P1：总控视觉核PDF3 Eqs1–7并回查PDF4/7/8，
保留理论参数与实验事实的区别；“static chirality”仅是作者在给定PRM概率图中的分类，
不是有限实验室态已测得一个固定非共面取向。原文没有给软核完整计算。

## Summary

给定刚性PRM与残余力扫描中，能谱、能量交错与取向概率呈现不同敏感性；
其最优模型参数不是实测Co核形变，软芯与真实多组态输入仍待继续检验。
