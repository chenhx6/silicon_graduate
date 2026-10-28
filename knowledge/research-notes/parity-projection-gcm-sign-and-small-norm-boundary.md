---
type: research-note
title: "宇称投影核代数、零范数极限与 GCM：144Ba 的可证范围"
aliases: [parity-projection-gcm-sign-and-small-norm-boundary]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bernard-2016-144ba-sccm-octupole, robledo-2010-bcp-d1s-octupole-ra-ba]
created_from: "Day26 parity-projection and GCM kernel self-audit"
tags: [octupole, parity-projection, GCM, SCCM, overlap-kernel, evidence-boundary]
---

# 宇称投影核代数、零范数极限与 GCM：144Ba 的可证范围

## Research Trigger

核验“反射不对称 HFB 极小值经宇称投影，就能定量产生 144,146Ba 的约 800 keV 劈裂”这一推论。任务包含可解析的投影核代数、深双阱局域化条件、浅阱小范数极限，以及两篇原始研究中的组态混合处理。该命题目前缺少对应的 HFB 范数核和哈密顿量核，不能视为已完成核验的微观数值结果。

## Grounded Evidence

| 原始来源 | 实际方法与定位 | 本轮确认结果 |
|---|---|---|
| [[bernard-2016-144ba-sccm-octupole]] | PDF pp.1–2, Eqs.(1)–(5); pp.3–4, Figs.2–3, Table I | Gogny D1S 轴对称 HFB；同时恢复粒子数、角动量和宇称；在非正交投影基上解 HWG。图2不是纯宇称投影 PES，图3也不是仅对单一 HFB 态投影所得的谱。 |
| 同上 | PDF p.4, Fig.3 邻近正文 | 1D-β2、1D-β3、2D GCM 的基态总能量为 −1185.931、−1186.709、−1187.547 MeV；2D 分别多获得 1.616、0.838 MeV 关联能。两者均不是负宇称激发能。 |
| 同上 | PDF p.4, Table I | 0+↔3− 的约化 E3 矩阵元绝对值依次为 0.450、0.477、0.460 e b^(3/2)。2D 强度为作者给出的向下 B(E3)=25 W.u.；实验矩阵元为 0.65(+0.17,−0.23) e b^(3/2)。 |
| 同上 | PDF p.2 Fig.1; p.3 Fig.2; p.4, Fig.3 讨论 | HFB 极小值约 (β2,β3)=(0.2,±0.1)，八极方向软。β3=0 的内禀态投影到作者受限基空间的负宇称奇 J 态时范数为零。2D 改善相对能级排序，但谱仍过度伸展；缺少三轴和 cranking 是作者指出的限制。 |
| [[robledo-2010-bcp-d1s-octupole-ra-ba]] | PDF pp.3–4, Eqs.(1)–(11) | GCM+GOA 导出一维集体 Schrödinger 方程，实际使用 ATDHF 惯性、GCM+GOA 度规及混合 prescription 的零点修正。不是 Bernard 的完全 J、π、N、Z 投影二维 SCCM。 |
| 同上 | PDF p.3, Eqs.(5)–(7) 与邻文; p.10 Fig.9; pp.11–12 Fig.12 | E1/E3 用集体波函数积分和转子近似计算，未做精确角动量投影。144Ba 的 D1S 八极极小深度可达约 0.7 MeV；BCP1 则在零八极附近很平。Ba 的 1− 激发能绝对值通常约高估一倍，不能声称已精确重现实验劈裂。 |

两份原件分别为 6 页和 14 页，SHA256 及逐页阅读范围由配套审计 JSON 记录。来源页提供 raw 路径。以上属于作者模型结果及方法报告，不是新增实验。

## Provisional Reasoning

### 投影能量与劈裂的符号

对真正的宇称守恒哈密顿量，令 Π²=1、Π†=Π、[H,Π]=0，并定义

\[
P_\pm=(1\pm\Pi)/2,\quad
N=\langle\Phi|\Phi\rangle,\quad n=\langle\Phi|\Pi|\Phi\rangle,
\quad H_{00}=\langle\Phi|H|\Phi\rangle,\quad
h=\langle\Phi|H\Pi|\Phi\rangle.
\]

这些核在上述条件下为实数。投影范数是 \(\mathcal N_\pm=(N\pm n)/2\)，在其严格为正时

\[
E_\pm=\frac{H_{00}\pm h}{N\pm n},\qquad
\boxed{E_- -E_+=\frac{2(H_{00}n-hN)}{N^2-n^2}}.
\]

若分子写成 \(2(hN-H_{00}n)\)，对应的是 \(E_+-E_-\)。这一符号不能由“劈裂应取正”随意修补；对任意试探态也没有仅从宇称代数推出偶宇称总是较低的定理。

令 \(E_0=H_{00}/N\)、\(s=n/N\)、\(k=h/N-E_0s\)，则

\[
\Delta E=-2k/(1-s^2).
\]

能量零点变换 \(H\mapsto H+C\) 给出 \(h\mapsto h+Cn\)、\(H_{00}\mapsto H_{00}+CN\)，所以连接核 k 与 ΔE 不变。这是核公式的直接校验。EDF 中密度依赖能量核还需要 prescription；Bernard p.2 明列 projected-density/mixed-density 处理，不能把代数检查当成已经消除了 EDF 的多参考问题。

### 零重叠不自动意味着简并

若 s→0，只能得到 ΔE→−2h/N；还需 h/N→0，或等价的 k→0，才能得到简并。一个精确反例是取宇称本征态 |e⟩、|o⟩，能量为 0、1.2 MeV，令 |Φ⟩=(|e⟩+|o⟩)/√2，则 N=1、n=0、H00=0.6 MeV、h=−0.6 MeV，投影能量仍为 0 和 1.2 MeV。正交局域态之间可以有有限的哈密顿量矩阵元。

对于局域动力学的深而宽双阱，额外的低能局域化条件可使连接核随穿越势垒的作用量衰减。WKB 在光滑、局域、近绝热等条件下给出

\[
\Delta E\sim A(E)\exp[-S(E)/\hbar],\qquad
S(E)=\int_{q_a(E)}^{q_b(E)}\sqrt{2B(q)[V_{\rm eff}(q)-E]}\,dq.
\]

积分区间是该能量的禁阻区，Veff 包括所选零点修正；一般不能把积分端点替换为两个势能极小。惯性、势垒宽度和有效势都进入结果。exp(−S/ℏ) 是劈裂/隧穿振幅的标度，不能直接称作穿透概率；相应的概率标度是 exp(−2S/ℏ)。浅阱若零点能超过势垒，深双阱 WKB 近似失去依据。

高斯波包近似下，若 σ 是单个波包的坐标标准差，两个中心为 ±q 的相同波包满足 s=exp[−q²/(2σ²)]。这只是特定波包模型；HFB 的多体重叠应由实际 Bogoliubov 态求出，不能从 β3、PES 深度直接读取 σ 或 s。

### 反射对称点的零范数不是零激发

若 |Φ(0)⟩ 本来是正宇称态，则 P−|Φ(0)⟩=0，E− 的表达式是未定义的 0/0。对可微路径

\[
|\Phi(q)\rangle=|e\rangle+q|o_1\rangle+O(q^2),
\]

归一化后的负宇称投影在 q→0 时可趋向 |o1⟩/||o1||，具有有限能量；分子分母同时趋零不意味着能量趋零。

一个可解析示例是单阱简谐振子的实相干态 |α⟩：s=e^(−2α²)，H00=ℏω(α²+1/2)，h=ℏω(1/2−α²)s，因此

\[
\Delta E=\frac{4\hbar\omega\alpha^2e^{-2\alpha^2}}{1-e^{-4\alpha^2}}
\xrightarrow[\alpha\to0]{}\hbar\omega.
\]

有限位移时这只是两种试探态的投影能量。α 很大时虽有小重叠与近简并，两种试探态能量都很高；这不构成单阱低能宇称双重态。该反例同时说明必须核对能量最优化和低能谱位置。

### 从单个投影态到 GCM

以 \(|q;J\pi NZ\rangle=P^JP^\pi P^NP^Z|\Phi(q)\rangle\) 构造多坐标叠加，HWG 方程为

\[
\sum_{q'}[H^{J\pi}(q,q')-E_\sigma^{J\pi}N^{J\pi}(q,q')]f_\sigma^{J\pi}(q')=0.
\]

单点投影只改变给定内禀态的对称性；GCM 再引入不同形状间的变分自由度。理想情况下，对嵌套且核 prescription 一致的同一 Jπ 子空间，扩大基底不能提高该子空间最低的绝对能量，但不同 Jπ 的下降量不同，所以激发能可以上升。Bernard 的 2D 谱更伸展与其绝对能量更低不矛盾。

f 是非正交基的系数，不能将 |f|² 直接当作形状概率；作者 Eq.(5) 的 F=N^(1/2)f 才是其集体振幅表述。q3 与 −q3 经宇称投影后互成 ± 倍数，作为基底会产生线性冗余，数值上须剔除零/极小范数自然态。

“连续生成坐标混合”指形状坐标的积分或离散网格近似；普通有限 HO/GCM 基底并未自动描述散射连续谱或出射边界。

### E3 与能谱的对账

Bernard 的 2D 基态相对两条 1D 路径降低 1.616、0.838 MeV；其 E3 矩阵元位于两条 1D 结果之间，不能概括为“增加坐标总会增强 E3”。按约化矩阵元定义

\[
B(E3;3^-\to0^+)=|M|^2/7,
\]

M=0.460 e b^(3/2) 给出 0.03023 e²b³；反向强度为 0.2116 e²b³，必须保留因子 7。用标准单粒子 Weisskopf 估算、A=144、r0=1.2 fm 得约 24.54 W.u.，与作者取整的 25 W.u. 一致。该换算不是另一次测量。

Bernard 在固定受限内禀对称性下只得到偶 J 正宇称和奇 J 负宇称态，所以其 3−−0+ 激发能不是同 J 的宇称双重态劈裂。只做 Π 投影也没有固定 J。Robledo 又采用不同的 GOA/惯性/转子处理，不能把其一维负宇称集体本征值与 Bernard 的单点纯宇称投影结果等同。

## Assumptions

核公式推导假设宇称守恒的自伴哈密顿量和非零投影范数。高斯、相干态与 WKB 是明确指定的辅助模型。这里没有重新运行 Gogny HFB、计算 Pfaffian 重叠或重建 SCCM 核；来源中未提供的 σ、h、s、质量参数和单点纯宇称投影劈裂一律不补值。

## Competing Explanations

有限 β3 平均场极小可与大幅集体涨落、旋转稳定化、或局域化双阱共同出现。强 E3 支持八极集体性，但单个矩阵元和约 800 keV 的 3− 激发能不能独立裁定刚性梨形或“纯软振动”。相反，平均场软度也不能单独否决完整投影/混合后出现的旋转结构。

## Transfer Conditions

投影代数可用于任意良定义的宇称守恒多体哈密顿量。把模型推广到具体核素前，需要同一泛函、基底和核 prescription 下的实际范数/能量核、角动量与粒子数处理、惯性与收敛性。奇 A 阻塞态和 Coriolis 耦合不由偶偶核结果自动覆盖。

## Failure Conditions

把 n→0 当作简并的充分条件、把 E3 能级与同 J 双重态混用、把 GOA 集体解当作精确 SCCM、或把拟设波包参数当成 HFB 原始输出，均使具体数值结论失去证据支持。极小范数扇区还需要数值正则化，不能直接以机器精度相减验证奇态极限。

## Falsification or Reverse Tests

配套 `parity-projection-gcm-kernel-audit.py` 核对劈裂符号、能量平移不变性、s=0 但有限劈裂反例、小位移相干态极限、E3 强度因子和两条 GCM 关联能差。

它还以独立函数重算早期工件 `parity-projection-overlap-kernel-model-076.py` 的已列 q、V、B 输入：所得 144Ba 的启发式值约 10.0 keV、146Ba 约 28.7 keV，和该旧稿文字宣称的 832.5、815.2 keV 不一致。该重算只检验旧公式和其输入的一致性，不验证这些参数具有核素物理意义；旧稿数值与“严格证明纯软八极”结论应撤回，待实际核数据重新建立。

## Open Questions

1. 能否取得 144,146Ba 在同一 EDF 与约束网格上的 N(q,−q)、H(q,−q)，将纯 π、πNZ、JπNZ 及 GCM 四步分别对账？
2. 负宇称小范数自然态截断对浅阱谱和 E3 的影响多大？
3. 含三轴、cranking 和配对涨落的核会如何改变 Bernard 已指出的谱伸展？
4. 不以实验 3− 激发能回填惯性时，模型对寿命/E3 与能谱能否同时给出可迁移预测？

## Human Review

本笔记是 Codex 的来源自审与解析推导，保持 unreviewed；未获得或声称 human-reviewed。缺少原始 SCCM 核是研究数据缺口，不自动成为用户待办。

## Promotion or Rejection History

- 2026-10-29：建立投影核符号及小范数边界；否决“仅凭两篇来源已定量验证 Ba 的约 800 keV 纯宇称投影劈裂”这一措辞。保留八极集体性及模型依赖结论。

## Sources

- [[bernard-2016-144ba-sccm-octupole]]
- [[robledo-2010-bcp-d1s-octupole-ra-ba]]
