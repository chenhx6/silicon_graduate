# 041：WK22–L78 的 EM 归一字典可条件闭合，actual PROBMO 约定未获认证

本单元只读既有原件、canonical LLR78/WK22-39 与 worker032，不联网、不运行作者或未知程序、不读取旧114。保持同一 Day24；不打开下一张课程卡。写入仅限本 worker 前缀与指定 tmp 前缀；canonical、raw、PLAN、BibTeX、Git 提交和课程状态均未改动。

## 结论与相对已有覆盖的增量

032 和 WK22-39 已指出 WK22 的单竖线、moment/transition 名称、L78 的显式前因子与 actual 输出缺口。本单元新增的是**有明确前提的完整换算字典**：普通分量矩阵元与 RME 的 3j 因子；bare 磁矩到标准 M1 张量及 B/δ 的比例；E2 球谐积分与逐分量 Q-like 算符的对应；以及长度/电荷单位换算。它们不需要等待 actual header 才能作为数学命题成立，但不能自动用于作者输出。

方向反转代数已由 LLR78-D24-020/worker037 关闭，本单元对此为 verified no-op。没有新实验结果、模型数值或 actual PROBMO 复现，也没有证据支持指责论文或程序漏因子、报错 rate 或错误 δ。

## 原件与检查范围

| 原件 | 本轮直接 locator | SHA256 |
|---|---|---|
| WK22, *Triaxiality and Rotational bands in 133Ce* | physical PDF47–49 / printed36–38；重点视觉核 PDF48 Eqs3.21–3.24 | `48556dbfe5284efebdb901cd949f534ac5552c6504e2c744603afca386660080` |
| Larsson–Leander–Ragnarsson 1978, *Nuclear core-quasiparticle coupling*, NPA307,189–223 | physical PDF32 / printed220 Appendix A1–A4，视觉核公式与公式后段 | `108c29bed9de467d99f330c0b8cef47be82a290263a85e398ba3b4f2e97d77eb` |

路径与页数另见 `body.json`。复核已有覆盖：canonical `wakudyanaye-2022-triaxiality-rotational-bands-133ce.md` 的 WK22-39；canonical `larsson-1978-nuclear-core-quasiparticle-coupling.md` 的 LLR78-D24-006/007/020 及方向小节；worker `ce133-next-evidence-032/report.md` 的 EM 与字面对接小节。没有把这些输出当作新的独立物理证据。

## 字面对照：哪些字面相同，哪些不能直接等同

| 字段 | WK22 PDF48/printed37 | L78 PDF32/printed220 | 可作出的判断 |
|---|---|---|---|
| B 定义 | Eq3.21 为 `(2Ii+1)^−1 |⟨If|Γ|Ii⟩|²`，印单竖线；散文称 B 为 reduced transition probability | A1 印双竖线 RME，分母相同 | 若 WK 单竖线是 RME 简写，结构一致；若是指定 M 的普通分量 ME，须补 3j 字典。字面本身未裁决 actual 字段 |
| M1 | Eq3.22 明称 magnetic dipole **moment** operator；`gR R + Σ(gl l+gs s)`；未显式印 μN、1/ℏ 或 `√(3/4π)` | A3 的 RME 前因子为 `√[(3/4π)(2I+1)]`，随后为 coherent signed sums | 在相同磁矩及角动量单位约定下可识别标准 M1 因子；不能由论文的省略写法断言程序省略该因子 |
| E2 | Eq3.23 是 `∫d³r ρ(r) r²Y₂^μ`，随后说 core + odd particle | A4 前因子 `√[(5/16π)(2I+1)]`，核含 `Q0δ+q20` 与 `Q2δ+q22` | E2 需按各内禀分量定义比较。WK 的标准球谐积分已经含球谐归一，不能把 A4 前因子再整体乘一次 |
| δ | Eq3.24 单竖线，`√.7 Eγ × ⟨I|ΓE2|I−1⟩/⟨I|ΓM1|I−1⟩` | A2 双竖线，同样的 spin 顺序和 `√.7 Eγ` | 在同一 RME/算符/单位/辐射约定下可比较；仅相同数值系数不认证整套 convention |
| 计算程序 | PDF49 §3.4 描述 GAMPN→ASYMO→PROBMO 的职责 | A3/A4 为历史方法表达式，不是 2022 的执行清单 | historical formula 不等于 actual input/output/header |

A3/A4 原式以 real/sign convention 的 `a_final a_initial` 相干求和，未印复共轭星号；本报告若用一般 RME 复数表达，仅是线性代数约定，不冒作原式字面抄写。A4 后段明确将 stretched-basis 的 single-particle `q2μ` 表达转交 Ref23（Leander–Larsson, NPA239(1975)93）；本轮未读该原件，因此不能宣称恢复了实际 q library。

## 闭合一：普通分量 ME 与 reduced ME

以下是声明约定后的数学推导，非作者程序输出。采用标准 3j Wigner–Eckart 约定，记

\[
R_X=\langle I_f\Vert T_{\lambda}\Vert I_i\rangle,\qquad
F_X=\langle I_fM_f|T_{\lambda q}|I_iM_i\rangle,
\]

\[
F_X=(-1)^{I_f-M_f}
\begin{pmatrix}I_f&\lambda&I_i\\-M_f&q&M_i\end{pmatrix}R_X.
\]

因此若实际字段是某个普通分量 ME，给定非零 3j 才能由

\[
B(X\lambda;I_i\to I_f)=
\frac{|F_X|^2}{(2I_i+1)
\left|\begin{pmatrix}I_f&\lambda&I_i\\-M_f&q&M_i\end{pmatrix}\right|^2}
\]

转回 B。3j 为零的分量不能用于反演。没有适用于所有 spin/M/q 的单一常数把普通 ME 变成 RME。对固定初始 `Mi` 求和全部允许 `Mf,q`，或对所有初末磁子态与 q 求和后平均初始磁子态，均得到同一 B：

\[
\sum_{M_fq}|F_X|^2=B,
\qquad
\frac1{2I_i+1}\sum_{M_iM_fq}|F_X|^2=B.
\]

M1 与 E2 的 λ 不同，故指定普通分量之比一般含不同 3j 因子；不能把 RME 比的方向/归一结论直接套给任意两个普通分量。静态磁矩 `⟨II|μ0|II⟩` 也先需要相应 diagonal 3j，而非仅乘一个辐射因子就成为跃迁 RME。

## 闭合二：bare 磁矩到标准 M1 跃迁张量

明确取物理磁矩（各角动量若有量纲则除以 ℏ）

\[
\mu_q=\mu_N\left[g_RR_q/\hbar+
\sum(g_ll_q+g_ss_q)/\hbar\right],
\qquad T_{M1,q}=\sqrt{\frac3{4\pi}}\,\mu_q.
\]

若角动量矩阵本来以 ℏ 为单位，方括号内直接使用无量纲矩阵即可。在同一态、同一 RME convention、相同 μN 单位下，定义 `Bμ=|⟨If∥μ∥Ii⟩|²/(2Ii+1)`，则

\[
B(M1)=\frac3{4\pi}B_\mu.
\]

再假设 E2 已为标准 `T(E2)=∫ρr²Y2`，使用同一个正 Eγ、同一单位制、同一辐射符号约定和非零 M1 分母。如果人为将 `√.7 Eγ` 直接乘上 E2/bare-μ RME 比，称结果为 `δbare`，则

\[
\delta_{\rm std}=\sqrt{\frac{4\pi}{3}}\,\delta_{\rm bare},
\qquad |\delta_{\rm std}|^2=\frac{4\pi}{3}|\delta_{\rm bare}|^2.
\]

这是两个**明确构造的算符 convention** 之间的换算；没有证据表明 WK22/PROBMO 实际输出的是这里的 `Bμ` 或 `δbare`。因此不能将这些比例写成作者结果的校正率，也不能在已有 δ 上再盲乘该因子。

## 闭合三：E2 必须逐分量建立 Q 字典

在标准归一、Condon–Shortley 相位的球谐函数与物理电荷密度下，WK22 Eq3.23 对应的各分量为

\[
\begin{aligned}
T_{20}&=\sqrt{5/(16\pi)}\int\rho(2z^2-x^2-y^2)d^3r,\\
T_{2,\pm1}&=\mp\sqrt{15/(8\pi)}\int\rho z(x\pm iy)d^3r,\\
T_{2,\pm2}&=\sqrt{15/(32\pi)}\int\rho(x\pm iy)^2d^3r.
\end{aligned}
\]

若**定义**一套 Q-like 球张量 `O2μ=√(16π/5) T2μ`，同一参考系内的逐分量字典才是

\[
\begin{aligned}
O_{20}&=\int\rho(2z^2-x^2-y^2)d^3r,\\
O_{2,\pm1}&=\mp\sqrt6\int\rho z(x\pm iy)d^3r,\\
O_{2,\pm2}&=\sqrt{3/2}\int\rho(x\pm iy)^2d^3r.
\end{aligned}
\]

此时 `T2μ=√(5/16π) O2μ` 对每个分量成立，而非只对 20 成立。若实际内禀 core/particle 的 `Q0+q20` 对应 `O20`，且 A4 的 `Q2+q22` 对应这套 `O22=O2,−2` 的实分量，那么 A4 的前因子与 WK 球谐积分可以一致；其 `ΔK=±2` 两个 CG 的和也与这两个实等分量的结构相容。这个判断是**充分的条件识别**，不是本原件已逐字给出的 q 定义。

A4 的 0、±2 内禀核和 lab 张量分量不是同一索引清单：lab 仍由旋转/CG 构造完整 rank-2 张量；不能因 A4 没有单列 q21，就给任意 off-diagonal single-particle 分量补写零。实际 Q2 是否采用另一种 tesseral/Cartesian 定义、是否已吸收 `√(3/2)`、core 与 particle 电荷、轴标号和 stretched→physical 转换，均需 q library/输入或输出说明确认。不能只因 Q 字母相同就合并。

在上述**完整 Q-like 定义**下，`B(E2)=5/(16π) B(O2)`。若原始 E2 字段已经是 WK Eq3.23 的标准球谐张量，则对应因子为 1；再乘 `√(5/16π)` 会重复归一。若 E2 为这套 O2 而 M1 为 bare μ，则两算符一起变换时 δ 的因子为 `√(5/12)`，不能仅使用 bare-M1 情形的 `√(4π/3)`。

## 闭合四：单位及一般缩放规则

在同一 RME convention 下，`T_E=a_E O_E`、`T_M=a_M O_M` 给

\[
B_E=|a_E|^2B_{O_E},\quad B_M=|a_M|^2B_{O_M},\quad
\delta_T=(a_E/a_M)\delta_O
\]

最后一式要求两边使用相同 Eγ 系数、相同方向和相位规则，且 M1 非零。正实归一因子不改变 sign；一般相位变换仍须把 radiation convention 一并说明。

纯单位恒等式：`1 eb=100 e fm²`，`1 e²b²=10⁴ e²fm⁴`；MeV 与 keV 相差 10³。若选择通常的 `Eγ[MeV]`、E2 RME `[eb]`、M1 RME `[μN]` 数值 convention，才在这套 convention 内使用文中的 `√.7` 数值系数；这个系数的出现本身并不证明 actual 字段的单位。特别是 e fm² 数值必须先除以 100 才能代入使用 eb 的同一数值系数。这里没有从两篇排版公式反推出 actual 单位。

## 已关闭的方向问题：本轮 verified no-op

LLR78-D24-020 已保留：标准 3j WE 与 Hermitian spherical tensor 下，`Rfi=(−1)^(If−Ii) Rif*`。M1/E2 在相同 spin 端点的反向因子相同，real convention 下同正 Eγ 系数的 RME 比不另添相对负号；M1 time-odd 不等于 anti-Hermitian。各 B 仍满足 `(2Ii+1)B(i→f)=(2If+1)B(f→i)`。本单元未再次记为新增结论。

## actual 输出所需的最小字段

1. 每个数值字段到底是普通分量 ME、RME、静态 moment、B 或已组装的 δ；若为普通 ME，给出 Mi/Mf/q；给 WE 定义而非只写“matrix element”。
2. M1 是 bare μ 还是含 `√(3/4π)` 的 radiation tensor；角动量是否以 ℏ 计、μN 是否已吸收，g 和 recoil/stretched 处方是什么。
3. E2 是球谐积分还是 Q-like 量；明确 20、±1、±2/tesseral 字典，Q0/Q2 的 core 与 single-particle 归一、有效电荷、长度单位、轴和 stretched→physical 映射。L78 Ref23 未读的边界保留。
4. 初末态和 spin、signed coherent eigenvectors 的 phase convention；各输出是否来自同一组态/参数与同一计算。单纯乘归一常数不会恢复缺失态或相干振幅。
5. δ 的辐射/emission convention、Eγ 的单位与数值来源、RME 使用方向及符号；M1 为零时的 pure-E2 表示方式。

数学换算已经关闭的条件项不再笼统留作 unknown；实际字段属于上述哪一种，仍是独立的 producer 身份证据缺口。本轮没有取得 actual PROBMO 头或 transition output，故 actual 归一认证保持 open/needs_review。

## 可供父任务写回的最小增量

建议将本单元的条件字典压缩写回 LLR78/WK22 canonical：`T(M1)=√(3/4π)μ` 及条件 B/δ 比例；WK `∫ρr²Y2` 不再额外乘 E2 前因子；A4 的 Q-like 逐分量识别以实际定义为前提；普通分量到 RME 必须给 3j。方向项只引用既有 LLR78-D24-020。任何新增 claim 均应标为 task-derived conditional normalization dictionary，不能标 experimental、actual code validation 或 human-reviewed。

停止原因：狭窄任务的数学字典已闭合；继续判断 actual 结果需要本轮未提供的 producer 字段，不以自造数字、toy/test 或相似公式制造增量。未推进课程状态；下一步由父任务决定 canonical 的最小必要写回。
