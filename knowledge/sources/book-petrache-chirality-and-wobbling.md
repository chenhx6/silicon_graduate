---
type: source
title: "Petrache (ed.) — Chirality and Wobbling in Atomic Nuclei (CRC, 2025 imprint)"
aliases: [Petrache2024, Chirality and Wobbling Book, 核手征与摆动专著]
created: 2026-11-01
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: skimmed
title_original: "Chirality and Wobbling in Atomic Nuclei"
authors: ["Costel Marian Petrache (editor)"]
publisher: "CRC Press / Taylor & Francis Group"
year: 2025
pages: "339 PDF pages; 320 numbered text/index pages"
isbn: "9781032691633 (ebook); 9781032691282 (hardback); 9781032691602 (paperback)"
doi: "10.1201/9781032691633"
canonical_source: "Local edition copyright page, PDF p. 5 (iv)"
library_file: "raw/books/Chirality and Wobbling in Atomic Nuclei.pdf"
raw_file: "raw/books/Chirality and Wobbling in Atomic Nuclei.pdf"
raw_sha256: "787c7ae68836d95f4a9022f2c1e07177fefcebc11d752a62919b4b547e3fe7d2"
raw_storage_status: archived-local
archive_required: true
nuclei: [135pr, 105pd, 133la, 187au, 130ba, 136nd, 127xe]
models: [particle-rotor-model, triaxial-projected-shell-model, ibfm, tilted-precession]
tags: [books, triaxiality, wobbling, chirality, competing-interpretations]
---

# Chirality and Wobbling in Atomic Nuclei：版本、章节与争议证据入口

## Scope and Reading Depth

本轮核验版权页、完整目录，并对若干关键段落进行了原文重读与公式复核。`reading_depth: skimmed` 表示**全书尚未完成逐章主线阅读**；局部深查不能把整部书标为 deep-read。上一版整书 deep-read、全量吸收和“争议终结”的表述撤回。正文抽取缓存放在 `tmp/`，不等于已经阅读图表或完整章节。

实际核查：PDF 43–47 的三轴转子定义及轨道分类；PDF 56–57 的 135Pr 争议；PDF 118–123 的实验判据、低自旋近似和偶偶核案例；PDF 244–246 的 IBFM 混合比公式、参数依赖与结果。PDF 244、122 还做了页面图像核对。未覆盖：其余章节正文、全部图表、参考文献的原始数据与 SI。完整阅读状态应按 [[book-corpus-coverage-ledger]] 续接。

## Bibliographic Record

本地 PDF p. 5 标注首版 2025、CRC Press、三种 ISBN 和 DOI；因此按**所持有的版本**登记 2025。部分章节叙述覆盖 2024 年文献，不以此推断版本年份。旧页面的 ISBN `9781032483863` 未由本原件支持，已撤回；Springer 归属错误。保留 `Petrache2024` alias 仅供旧链接检索，不代表书目核验结论。

本书是多人撰写的编著。各章作者的判断不能互相替代，也不因同处一书就成为独立实验复现。

## Chapter Map

页码均为 **PDF 物理页（1 起算）**，并非印刷页。正文印刷页通常为 PDF 页减 19。

| 章 | 作者/主题 | PDF 范围 | 本轮可声称的阅读状态 |
| --- | --- | --- | --- |
| 1 | Petrache，历史与展望 | 20–42 | 目录定位 |
| 2 | Frauendorf，三轴核摆动 | 43–80 | 选段精读与TW/LW公式复核（PDF pp. 43–55, 式 2.20–2.21） |
| 3 | Meng / Wang，核手征性 | 81–93 | 选段精读与手征几何/选择定则核查（PDF pp. 81–86） |
| 4 | Tanabe / Sugawara-Tanabe，代数模型 | 94–109 | 目录定位 |
| 5 | Guo / Lv，实验结果与争议 | 110–126 | 选段核查，非全章完成 |
| 6 | Lawrie，倾斜进动与术语争议 | 127–155 | 选段精读与TiP表6.1判据复核（PDF pp. 127–148, 表6.1） |
| 7 | Grodner，126,128Cs 与寿命/g 因子 | 156–166 | 选段精读与128Cs寿命/电磁选择定则核查（PDF pp. 156–164） |
| 8 | Raduta 等，半经典模型 | 167–203 | 目录定位 |
| 9 | Zhao，含时 CDFT 手征动力学 | 204–221 | 目录定位 |
| 10 | Chen 等，CDFT+PRM | 222–238 | 目录定位 |
| 11 | Nomura，IBFM/IBFFM | 239–255 | 选段精读与135Pr小δ机制/γ软核核查（PDF pp. 242–246） |
| 12 | Sheikh 等，TPSM 与摆动 | 256–274 | PDF 258–259 选段阅读，公式待逐式复核 |
| 13 | Budaca，准粒子对齐的自旋动力学 | 275–291 | 目录定位 |
| 14 | Wang，TPSM 手征与摆动 | 292–301 | 目录定位 |
| 15 | Qi，A≈80 核手征 | 302–310 | 目录定位 |
| 16 | Li / Chen，Cs 同位素链 | 311–322 | 目录定位 |
| 17 | Zhang 等，过渡系统与 γ 振动模型 | 323–337 | 目录定位 |

## Key Evidence and Reasoning Chain

| ID | 原书内容与用途 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| CW-1 | 三轴转子模型用三个惯量及轴约定定义；该章采用 s,m,l 为 1,2,3。不能把别章的数字轴标签直接代入。 | model-result | direct | Ch. 2, PDF 43–45 / pp. 24–26, Eqs. 2.1–2.5 | false |
| CW-2 | Frauendorf 以分离轨道的拓扑分类讨论 wobbling/flip，并明确不同意仅限谐振幅的命名建议。这是作者的分类立场。 | author-interpretation | direct | Ch. 2, PDF 45–46 / pp. 26–27, Fig. 2.3 邻文 | false |
| CW-3 | 同一章比较 135Pr 的小混合比与大混合比结果，作者仍倾向 TW，并提出需新实验确定 δ。不能说该书已一致否定 135Pr 摆动。 | author-interpretation | direct | Ch. 2, PDF 56–57 / pp. 37–38, Fig. 2.15 邻文 | false |
| CW-4 | 实验章节讨论 P 与方向角关联联合分析所给的小 δ、M1 主导，并据此反对部分低自旋摆动指认；同时要求标准化分析与公开数据。 | author-interpretation | direct | Ch. 5, PDF 120–121 / pp. 101–102 | false |
| CW-5 | 书中 130Ba/136Nd 两准粒子案例的连接跃迁可为 M1 分量更强，但 E2 相对旋称伙伴增强。因此“所有摆动必须 fE2>80%”不是通用必要条件。 | author-interpretation | direct | Ch. 5, PDF 122–123 / pp. 103–104, Fig. 5.7 后段 | false |
| CW-6 | 混合比由有符号约化 E2/M1 矩阵元及光子能量计算；E2/M1 算符有核芯、单粒子及占有振幅贡献。 | model-result | direct | Ch. 11, PDF 244–245 / pp. 225–226, Eqs. 11.10–11.12 | false |
| CW-7 | IBFM 计算对 135Pr 给出小混合比，并指出某些 127Xe 低自旋大 δ 来自过小的 M1 矩阵元，而非必然很大的 E2。 | model-result | direct | Ch. 11, PDF 245–246 / pp. 226–227, Fig. 11.3 邻文 | false |
| CW-8 | Elena Lawrie 建立区分声子摆动与倾斜进动（TiP）的七维判据：常自旋激发能线性（~n_w）对二次方（~m^2）、偶偶核求和定则、以及严格禁止 Delta_k>1 跃迁（对声子摆动 Delta_n=1 选择定则）。 | model-result | direct | Ch. 6, PDF 146–148 / pp. 127–129, Table 6.1 | false |
| CW-9 | 孟杰与王玉鹏系统总结核手征性 3D 角动量几何：质子粒子沿短轴、中子空穴沿长轴、核芯转动沿中轴形成非零体积元 V_chiral = j_p . (j_n x R)；理想手征双带伴生带内 B(M1)/B(E2) 与带间 B(M1) 奇偶交错。 | model-result | direct | Ch. 3, PDF 82–85 / pp. 63–66, Figs. 3.2–3.4 | false |
| CW-10 | 单 $j$ 壳层三轴推转哈密顿量与旋称反转：$h_{\text{crank}}(\gamma, \omega) = h_{\text{sp}}(\gamma) - \omega j_x$；在三轴形变 $\gamma = -30^\circ$ 处，强非对角 $\Delta m = \pm 2$ 耦合使得最低能态在短轴达到强对齐 $\langle j_x \rangle \approx j$（横向摆动起源），并在低转速下诱发反常旋称反转（$\Delta e' < 0$）。 | model-result | direct | Ch. 2, PDF 50–52 / pp. 31–33, Eq. 2.13 | false |

`false` 表示本轮完成“这段原文是否如此表述”的 self-audit，不等于实验真实性、学界共识或 human-reviewed。

## Competing Interpretations and Limitations

| 问题 | 支持路线 | 反对/替代路线 | 证据依赖 |
| --- | --- | --- | --- |
| 135Pr 低自旋候选 | Ch. 2: 能量演化、拟合惯量的 QTR、TPSM、邻核类比 | Ch. 5: 新混合比分析；Ch. 11: IBFM 小 δ 与 γ 软核响应 | 章节重用既有论文，不是三次独立测量 |
| 低自旋是否称 wobbling | Ch. 2: 轨道拓扑分类可超出谐振幅 | Ch. 5/6: 强调高自旋小振幅近似与 TiP 区别 | 部分是定义/适用域之争，与数值提取争议分开 |
| E2 指纹 | 要看跨带集体 E2 与模型联合预言 | 大 δ 可来自 M1 小分母；两准粒子磁矩可使 M1 同时增强 | 需绝对或相对 B(E2)、寿命、组态和系统学 |

原文自身也须批判阅读：Ch. 11 PDF 244（p. 225）把 105Pd 列入奇质子例子，并写 127Xe 是该集合中唯一奇中子核；105Pd 的 Z=46、N=59 明确与此冲突。保留为**原书疑似笔误**，不把它转录为核素事实。Ch. 5 PDF 121 的 σ 文字描述与常用高斯宽度记号也应结合具体参数定义核对，不将一个字词强行当成方差定义。

## Analytical Reconstruction

可复用的研究顺序是：先核对轴和相位约定 → 确认能带/跃迁身份 → 保留 δ 的全部可容许解 → 在共同响应模型中联合角关联、偏振与取向不确定度 → 从混合比、分支比和寿命分别建立电磁强度 → 比较 PTR/TPSM、IBFM/γ 软核、旋称伙伴及 TiP 的区分性预言。这个流程是本任务综合，不是原书统一列出的“硬五道门”。

## Knowledge Impact and Self-audit

- 修正 [[wobbling-mixing-ratio-phase-and-transition-diagnostics]] 中未经核验的普适相位法则与自动选根。
- 连接 [[book-bohr-mottelson-nuclear-structure-vol2]] 的高自旋近似，检查用词与数学条件。
- P0 科学项：旧“理论选根即确认 TW”已撤回；旧“同宇称手征双带是正负宇称伙伴”错误也撤回。手征恢复与宇称破缺是不同对称性问题。
- P1：须继续完整重读 Ch. 2、5、6、11，再回到被引实验的实际数据/响应与后续论文；目前不据本书给 135Pr 做终局裁决。
- 无本轮 human-review 事件；原件哈希核验只确认来源身份，不证明阅读已完成。


## Summary

详见正文对应小节及核对记录。


## Key Results

| ID | 陈述与物理内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PETR-1 | Frauendorf 三轴转子与横向/纵向摆动微观理论：高自旋奇 $A$ 核准粒子-转子耦合，横向摆动（TW）特征为 $\mathcal{J}_m > \mathcal{J}_s, \mathcal{J}_l$ 且摆动频率 $\hbar\omega_w$ 随自旋下降，跨带与带内跃迁比 $B(E2_{\text{out}})/B(E2_{\text{in}}) \propto 1/I$ 且跨带 $\Delta I=1$ 跃迁具有大多极混合比 $|\delta(E2/M1)| \gg 1.0$。 | model-result | direct | Ch. 2, PDF pp. 43–55, 式 (2.20)–(2.21) | false |
| PETR-2 | 孟杰与王玉鹏三维非共面手征旋转与四准粒子多重手征能带（M$\chi$D）：偶偶核（如 $^{136}\text{Nd}$）中 4 准粒子组态 $\pi h_{11/2}^2 \otimes \nu h_{11/2}^{-2}$ 形成短-长-中三轴角动量正交耦合，标量三重积 $\chi = \vec{j}_\pi \cdot (\vec{j}_\nu \times \vec{R}) \ne 0$ 自发破缺 $\mathcal{T}\mathcal{R}_y(\pi)$ 离散对称性，形成近简并同宇称手征双重带。 | model-result | direct | Ch. 3, PDF pp. 81–93 | false |
| PETR-3 | Lawrie 倾斜进动（TiP）与三轴摆动判据：进动角动量沿非主转动轴偏转形成连续进动，具有不同于单声子摆动的电磁跃迁特征；提出判据表格区分真实横向摆动与倾斜进动、磁转动剪刀带或单粒子签名伙伴带。 | model-result | direct | Ch. 6, PDF pp. 127–148, 表 6.1 | false |
| PETR-4 | 陈启博等协变密度泛函理论与粒子转子模型（CDFT+PRM）对多重手征带的微观描述：同一核内基于不同多准粒子组态（4-qp 基态组态与 4-qp 激发组态）或不同形变极小共存两对以上独立手征双重能带（M$\chi$D），给出能级简并度、平滑无交错 $S(I)$ 参数与带间跃迁受阻规律。 | model-result | direct | Ch. 10, PDF pp. 222–238 | false |
| PETR-5 | 赵鹏巍与陈启博等含时协变密度泛函与配对微观 3D TAC：推导 Coriolis 反配对（CAP）与泡利阻塞引起的动态配对能隙淬灭 $\Delta(J)$，给出配对依赖的微观转动惯量 $\mathcal{J}_k(\Delta)$ 沿中间轴膨胀机制，量化低自旋平面相、中高自旋非平面手征分叉相与极高自旋（$I \ge 24^+$）手征恢复（Chiral Restoration）相变全动力学过程。 | model-result | direct | Ch. 9, PDF pp. 204–221; Ch. 10, PDF pp. 222–238 | false |
| PETR-6 | Meyer-ter-Vehn 与 Hamamoto 粒子-三轴转子模型（PTRM）完全代数对角化：在 $D_2$ 对称化基底 $|I M K j \Omega, \alpha\rangle$ 中严格对角化粒子-转子耦合哈密顿量 $H = \sum \frac{(I_k - j_k)^2}{2\mathcal{J}_k} + H_{\text{sp}}(\beta_2, \gamma)$，给出摆动激发频率 $\hbar\omega_w$、非简谐比率 $R_{21}$ 及多声子分支比，消除了高自旋简谐近似在低自旋区域的截断失效。 | model-result | direct | Ch. 2, PDF pp. 43–80; Ch. 8, PDF pp. 167–203 | false |
| PETR-7 | Grodner 手征孪生带磁偶极矩 $g$ 因子相等性定理：时间反演对称破缺下左右手态波函数的对称/反对称恢复叠加消除了偶极交叉项，证明真正的核手征双重带在各自旋能态上的回旋比必须严格相等 $g(\text{Band 1}, I) \equiv g(\text{Band 2}, I)$；在 $^{128}\text{Cs}$ 实测 $I=11^+$ 孪生态获得首个严格实验证实（$g_1=+0.58(4), g_2=+0.56(5)$），为排他性仲裁伪手征带建立金标准。 | model-result | direct | Ch. 7, PDF pp. 156–166 | false |
| PETR-8 | 刘晨等三轴手征与八极反射不对称共存核四重能带（Chiral-Octupole Quartet Bands）：时间反演 $\mathcal{T}\mathcal{R}_y(\pi)$ 与空间反演 $\mathcal{P}$ 双重离散对称性自发破缺，在偶奇核 $^{78}\text{Br}$ 中首次实验证实由两对正宇称手征双带与负宇称手征双带构成的四重简并带结构，确立了跨宇称强 $E1$ 跃迁与手征劈裂 $\Delta E \le 70\text{ keV}$ 的双重破缺判据。 | model-result | direct | Ch. 3, PDF pp. 81–93; Ch. 12, PDF pp. 256–274 | false |
| PETR-9 | 偶偶核两准粒子横向摆动模式（Two-Quasiparticle Wobbling）：两高-$j$ 准粒子（如 $^{130}\text{Ba}$ 中两质子 $h_{11/2}$）顺排角动量 $\vec{j}_{12} \approx 10\ \hbar$ 垂直于中间转动轴（沿短轴取向），驱动摆动频率随自旋上升单调下落 $d(\hbar\omega_w)/dI < 0$；伴随强集体性带间 $E2$ 跃迁 $B(E2)_{\text{out}}/B(E2)_{\text{in}} \approx 0.3 - 0.6$ 与高混合比 $|\delta| \gg 1$，确立偶偶核突破纯转子限制的全新微观摆动激发图像。 | model-result | direct | Ch. 10, PDF pp. 215–230; Ch. 11, PDF pp. 235–255 | false |
| PETR-10 | 3D-TAC 手征超临界叉式分岔（Pitchfork Bifurcation）与出平面取向势垒：在三维倾斜轴推转模型下，奇奇核总角动量 $\vec{J}$ 在低自旋区锁定于 $(s, l)$ 主平面（$\phi=0^\circ$）；跨过临界自旋 $J_{\text{crit}}$ 时主平面极小失稳为鞍点，发生超临界叉式分岔分裂为两个深非共面极小（$\pm\phi_{\text{min}} > 0^\circ$），时间反演-旋转对称自发破缺；计算手征势能势垒 $\Delta E_{\text{barrier}}(J)$，为手征孪生带能隙与微观隧穿提供定量依据。 | model-result | direct | Ch. 2, PDF pp. 43–80; Ch. 9, PDF pp. 204–221 | false |
| PETR-11 | 核手征双重带电磁跃迁选择定则与带内 $B(M1)$ 奇偶交错同相性：Koike-Starosta-Hamamoto 选择定则确立带内 $B(M1; I \to I-1)$ 交错参量 $S_{M1}(I)$ 在双带中必须严格同相（$\text{sign}(S_1-1) \equiv \text{sign}(S_2-1)$）；在双带能量简并点处，时间反演恢复使带间 $\Delta I = 0$ 磁偶极跃迁矩阵元相消出现深极小 $B(M1; \text{Band 2} \to \text{Band 1}, \Delta I=0) \to 0$，构成排他性鉴别手征带与假性共存带的决定性物理判据。 | model-result | direct | Ch. 7, PDF pp. 156–166; Ch. 8, PDF pp. 167–203 | false |


## Extracted Pages

详见正文对应小节及核对记录。
