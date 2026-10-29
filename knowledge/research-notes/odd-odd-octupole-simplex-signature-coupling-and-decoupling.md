---
type: research-note
title: "奇奇变形核八极四重态中的单纯形—旋称耦合与退耦常数"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [odd-odd octupole simplex signature coupling, octupole quadruplet decoupling]
tags: [odd-odd-nuclei, octupole, simplex-symmetry, signature-splitting, coriolis-decoupling]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: Day26 odd-odd octupole simplex-signature coupling and decoupling investigation
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, gaffney-2013-pear-shaped-rn-ra]
---

# 奇奇变形核八极四重态中的单纯形—旋称耦合与退耦常数

## Research Trigger

本轮任务聚焦 `^{220,222}Fr` 与 `^{224}Ac` 这一 A≈224 奇奇核候选区，要求把两个奇价粒子、反射不对称核芯、simplex/signature 分类、两粒子 Coriolis 项、$Omega=1/2$ 退耦和 E1/E2/M1 分支放进同一可复现框架。直接检索到的本地证据主要是 A≈224 反射不对称的综述框架和相邻 `^{220}Rn/^{224}Ra` 的 Coulomb-excitation 结果；本页因此把三种目标核的定量参数保留为现象学扫描，不把四重带或 `D_0` 数字写成实验事实。

## Grounded Evidence

### 1. 反射不对称与 A≈224 轨道机制

Butler–Nazarewicz 综述将反射不对称的实验判据分成相反宇称低能级、交替宇称带、增强 E1/E3 和模型一致的多极矩；其核心微观条件是费米面附近相反宇称轨道的 $Delta l=Delta j=3$ 耦合。该综述同时强调：静态八极极小、八极振动/软性和宇称投影后的实验室双重态不能合并为同一个结论（[[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]，Sec. III、Secs. IV–VII，review 页码 349–421）。

对 A≈224，真正的八极驱动轨道应以 opposite-parity `f_{7/2}–i_{13/2}` 或 `g_{9/2}–j_{15/2}` 一类 $Delta l=Delta j=3$ 对为代表。任务中举出的 `πh_{9/2}–πf_{7/2}` 和 `νg_{9/2}–νi_{11/2}` 在球形标签下分别是负宇称和正宇称内部的同宇称对，因此可以改变有效退耦和组态混合，却不能单独作为 E3 八极驱动对。这个宇称检查是本页的一个必要修正。

### 2. 相邻核的直接电磁证据与边界

Gaffney 等对 `^{220}Rn` 和 `^{224}Ra` 做了加速放射性束 Coulomb excitation，用 MINIBALL/GOSIA 约束 E1、E2、E3 矩阵元；报告的 `Q_2`、`Q_3` 在测量自旋范围内近似稳定，并将 `^{224}Ra` 的更连贯八极集体性与 `^{220}Rn` 的更振动性行为区分开来（[[gaffney-2013-pear-shaped-rn-ra]]，journal pp. 199–204，尤其 pp. 200–203、Figs. 3–5、Tables 1–2）。作者也明确保留静态四极—八极分布与八极振动之间的解释边界。

这些结果支持“E3 是更集体、E1 对质子—中子位移和相消敏感”的迁移框架，但不提供 `^{220,222}Fr` 或 `^{224}Ac` 的四条带逐线寿命、偏振、绝对 $B(E1)$ 或 $B(M1)$。因此本页不能把目标三核的四重带结构、强 E1 支线或 `D_0` 系统学标为已测量。

### 3. 对称性标签

对 odd–odd 核，质子与中子各为半整数角动量，总自旋序列为整数。取主轴半转动的 signature 本征值

$$r_\alpha=\exp(-i\pi\alpha),\qquad \alpha=0,1,$$

则 $r=+1,-1$。若 simplex 定义为 $\hat S_x=\hat P\hat R_x(\pi)$，有

$$s=p r,$$

并且在整数自旋序列上 $s=\pm1$。任务给出的 $s=p\exp(-i\pi I)$ 是另一种把旋转相位直接并入标签的约定；本工件同时输出两种相位，避免把 signature 指数、旋转相位和 simplex 本征值混用。四条平行带可暂以 $(p,r)=(+,+),(+,-),(-,+),(-,-)$ 标记，但“恰有四条实验带”仍需要逐线能级和连接证据。

## Provisional Reasoning

### 1. 两粒子—转子 Hamiltonian

令 $A=\hbar^2/(2\mathcal J)$，在固定 $I$ 的强耦合投影中，保留用户指定的 Coriolis 结构

$$
H_{\rm cor}=-A\left[(I_+j_{p-}+I_-j_{p+})+(j_{p+}j_{n-}+j_{p-}j_{n+})\right].
$$

第一组项改变总转动投影与质子内禀投影但保持总投影，第二组项在质子—中子空间内交换一个单位投影。脚本在固定 $M$ 的 $(m_I,m_p,m_n)$ 乘积基底中逐项使用

$$
\langle j,m\!\pm\!1|j_\pm|j,m\rangle=\sqrt{j(j+1)-m(m\pm1)}
$$

建立矩阵，并检查 $H_{\rm cor}=H_{\rm cor}^\dagger$。这一步是算符和量纲的诊断，不是完整 angular-momentum projected PRM 拟合。

### 2. $Omega=1/2$ 退耦与 parity asymmetry

在简化强耦合表达中，两个可能的 $Omega=1/2$ 贡献写作

$$
E_{\rm dec}(I,p,r)=(-1)^I r\left(I+\frac12\right)[a_p(p)+a_n(p)].
$$

反射不对称平均场使相反宇称轨道混合。对每个奇粒子用二能级约化

$$
\theta_q=\frac12\tan^{-1}\frac{2\beta_3v_{3q}}{\Delta\epsilon_q},\qquad
a_q(p)=a_{q0}+p\,\delta a_q\sin(2\theta_q),
$$

其中 $q=p,n$。于是 $a_p(+)-a_p(-)=2\delta a_p\sin(2\theta_p)$，中子项同理；若两个粒子的贡献符号相反，会出现某一宇称扇区中的部分相消或增强。这解释了“正、负宇称退耦不对称”作为模型机制的来源，但 `a_q` 不是由 Butler 或 Gaffney 直接测得的数值。

### 3. 四态 simplex 保持耦合

四态对角能量包含转动、宇称偏移、signature 偏移和上述退耦项。只允许

$$
(p,r)\longleftrightarrow(-p,-r)
$$

的非对角元，因而保持 $s=pr$。八极耦合和有效质子—中子项分别取

$$
t_3(I)=t_{30}\beta_3e^{-0.025I},\qquad
v_{pn}(I)=v_{pn}^{(0)}(1+0.06\beta_3I),
$$

并以相反符号进入两个 simplex block。四条能级随 $I$ 的交错由 parity-dependent $a_q$、$t_3$ 和 $v_{pn}$ 的相干叠加决定。脚本输出 `four_band_spectrum.csv`，并以

$$
S(I)=(-1)^I\left[E(I)-\frac{E(I-1)+E(I+1)}2\right]
$$

给出每一 $(p,r)$ 分支的局部交错残差 `staggering.csv`。

### 4. E1、E2、M1 选择定则与 $D_0$

一般宇称选择定则为

$$
E\lambda: p_f=p_i(-1)^\lambda,\qquad M\lambda:p_f=p_i(-1)^{\lambda+1}.
$$

所以 E1 连接正负宇称，E2 保持宇称，M1 保持宇称。四重态的最低阶带内规则可写为：

| 通道 | 主导条件 | 现象学矩阵元 | 边界 |
|---|---|---|---|
| E1 | $\Delta I=1$, $p_f=-p_i$ | $D_0$ 与八极混合振幅 | 强度对 $D_p+D_n$ 相消敏感，不能仅由近简并推出 |
| E2 | $\Delta I=2$, $p_f=p_i$, 同一 signature | $Q_0$ 与转子几何因子 | 需要寿命和内转换修正才能得绝对 $B(E2)$ |
| M1 | $\Delta I=1$, $p_f=p_i$, signature 改变 | $\Delta g$ 与横向角动量 | 强弱依赖有效 $g_s$、组态和相位，非群论必然 |

脚本用标准转子尺度

$$B(E1)\sim\frac{3}{4\pi}D_0^2C_1^2,\quad
B(E2)\sim\frac{5}{16\pi}Q_0^2C_2^2,\quad
B(M1)\sim\frac{3}{8\pi}(\Delta g)^2C_1^2,$$

输出相对分支与输入 $D_0$。`D0_efm` 在三个核素中只是扫描值，不能当作实测系统学；E1 “极强”只有在绝对寿命、分支和多极性已确认，并且相邻 E2/E3 通道同时闭合时才可主张。

### 5. 工件结果

运行

```text
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/odd-odd-simplex/odd_odd_simplex_coupling.py
```

会生成 `four_band_spectrum.csv`、`staggering.csv`、`transition_strengths.csv`、`results.json` 和谱图。结果中的 Hermiticity 检查应为零到机器精度；能谱的自旋依赖可用于比较 $a_p=a_n=0$、单粒子八极混合关闭和完整参数三种反事实，但这些反事实扫描仍是 toy model。

## Assumptions

- `I` 是 odd–odd 核的整数自旋，`A=\hbar^2/(2\mathcal J)` 用 MeV 表示；脚本采用 $j_p=9/2$、$j_n=11/2$ 的有效角动量作为 Coriolis 诊断空间。
- `K_0=3`、$\beta_3$、$Q_0$、$D_0$、$a_p$、$a_n$ 和 $v_{pn}$ 是现象学输入，未从具体核的 EDF、GCM 或寿命数据反演。
- 四态 branch Hamiltonian 将 parity restoration 后的实验室带标签作为有效 $(p,r)$ 分支；它不替代完整的 angular-momentum/parity projected particle-rotor calculation。
- 八极混合只用于产生退耦参数的不对称；同宇称用户示例轨道不会被错误地当作 E3 驱动。
- `B(E1)`, `B(E2)`, `B(M1)` 的转子因子是示意值，未包括内转换、feeding 协方差、具体 Clebsch–Gordan 相位和带混合拟合。

## Competing Explanations

1. **八极静态双阱**：相反宇称伙伴和稳定 E1/E3 网络可由局域化的 $\pm\beta_3$ 波包解释；但能级交错也可能由软振动和宇称投影产生。
2. **动态八极声子**：Gaffney 的相邻核结果保留静态梨形与振动的解释边界；若目标核 E3 连贯性随自旋不稳定，静态四重带解释应降级。
3. **低 j Coriolis/组态混合**：同宇称近邻轨道和质子—中子残余作用可产生 signature splitting，甚至不需要非零静态 $\beta_3$。
4. **带交叉或重标记**：看似四重态的四条带可能来自不同 $K$、两准粒子组态或带交叉；局部 $S(I)$ 不能独立证明四重带。
5. **E1 相消**：小 E1 不否定八极集体性；反过来孤立强 E1 也不证明静态八极形状，因为 $D_p$ 和 $D_n$ 的相位、阻塞和混合都很敏感。

## Transfer Conditions

- 将工件迁移到 `^{220,222}Fr` 或 `^{224}Ac` 前，需要逐线 $I^\pi$、带间连接、DCO/偏振、绝对寿命、内转换和 feeding 信息。
- 要把 $a_p$ 或 $a_n$ 的宇称不对称解释为八极场，需要同一组态空间中的 opposite-parity occupation、配对、$\beta_2$–$\beta_3$ 势能面和 Coriolis 对齐共同计算。
- `D_0` 的反演必须使用同一初态、同一 $E1/E2$ 单位、初态简并因子和方向约定；缺寿命的分支只能作相对量或上/下限。
- 要把四条带称为“四重带群”，至少需在同一自旋窗口看到四个可追踪序列，并由 E1/E2/M1 网络区分同一结构的伙伴关系。

## Failure Conditions

- 若在关闭 $\beta_3$ 后，纯 signature/Coriolis 模型已经复现所有 $S(I)$ 和分支强度，则八极—退耦因果不可识别。
- 若 `H_cor` 的 Hermiticity 检查非零、固定-M 基底不闭合或谱对步长/截断不稳定，不能解释输出的绝对能量。
- 若目标核的第四条带只有单个峰、无互相连接的自旋链，四重态命名应暂停。
- 若 E1 强度依赖未识别混合多极性、内转换或 feeding，不能报告“极强 E1”或反演 $D_0$。
- 若未来原件显示 `πh_{9/2}–πf_{7/2}` 或 `νg_{9/2}–νi_{11/2}` 的标签对应不同变形基底，须重新定义轨道对；本页的球形宇称检查不能替代具体 Nilsson 标记。

## Falsification or Reverse Tests

1. 对三个核素分别做 `beta3=0`、只保留质子混合、只保留中子混合和完整 `beta3` 四组扫描；若 `S(I)`、宇称差和 E1/E2/M1 不能联合改善，八极退耦解释被否定。
2. 在同一自洽 EDF/PRM 中强制相反宇称轨道不混合，检查 $a_p(+)-a_p(-)$ 和 $a_n(+)-a_n(-)$ 是否消失。
3. 用 partner-resolved lifetimes 测量绝对 $B(E1)$、$B(E2)$、$B(M1)$；若强 E1 不随四条带形成稳定异宇称网络，优先采用局部组态混合解释。
4. 对相邻 `220Rn/224Ra` 使用 Gaffney 式联合 E1/E2/E3 拟合，检查同一转子约定能否同时描述 $Q_2$、$Q_3$ 和 E1；不通过则不把 `D_0` 扫描迁移到 Fr/Ac。
5. 用不同 $K_0$、$j_p$、$j_n$ 和惯量各向异性重复 fixed-M Coriolis 矩阵，验证四重带结论不是单一基底截断的产物。

## Open Questions

- `^{220,222}Fr` 和 `^{224}Ac` 是否存在可逐自旋闭合的四条交替宇称/旋称序列，还是文献中的 quadruplet 主要是区域性概念？
- 在同一反射不对称平均场中，质子和中子退耦常数的宇称差是否与阻塞后的 `f_{7/2}–i_{13/2}`、`g_{9/2}–j_{15/2}` 占据变化同号？
- 对这三个奇奇核，最小可观测的 `E1/E2/M1/E3` 组合是什么，才能区分静态八极双阱、八极软振动和纯 Coriolis 组态混合？
- 是否可以从两种宇称下的 $S(I)$ 和绝对 E1/M1 共同反演 $a_p,a_n,t_3,v_{pn}$，还是存在不可辨识的参数谷？
- 相邻 `220Rn/224Ra` 的直接 $Q_3$ 体系学能否在同一实验条件下扩展到 Fr/Ac 的 odd–odd 阻塞组态？

## Human Review

本页为 Codex self-audit 的 `ai-draft`，`review_status: unreviewed`。需要人工复核的高优先级事项是：目标三核是否确有可引用的四重带原件；`D_0` 的实验单位和初态简并约定；以及将任务给定同宇称轨道对与真正 opposite-parity octupole pairs 分开的措辞。任何后续论文措辞都必须回到 `knowledge/sources/`、原始 PDF 和逐线 locator。

## Promotion or Rejection History

- 2026-10-29：创建为 provisional research note；保留 Butler–Nazarewicz 1996 与 Gaffney 2013 的来源边界。
- 2026-10-29：`supports` 反射不对称、E1/E3 多观测证据链和 A≈224 opposite-parity orbital mechanism；不把其邻近核结果升级为 Fr/Ac 的直接实验。
- 2026-10-29：`revises` 任务中把 `πh_{9/2}–πf_{7/2}`、`νg_{9/2}–νi_{11/2}` 直接当作八极 opposite-parity pairs 的表述；在球形标签下两者均为同宇称对。
- 2026-10-29：`rejects` 将本工件中的 `D_0`、四重带能级和“极强 E1”作为 `^{220,222}Fr` 或 `^{224}Ac` 的测量结论。
