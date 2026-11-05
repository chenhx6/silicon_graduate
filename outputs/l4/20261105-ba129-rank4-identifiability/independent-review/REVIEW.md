# 129Ba rank-4 稿件：独立数学与科学反审

本轮审查 `main.tex` 与 `analysis/rank4_invariant.py`，并按用户追加消息只读
所供 Gizon1977 FULL JSON 及其 OCR 衍生文本。独立程序、依赖、
人为测试输入和结果全部位于本目录。未修改稿件、知识页或其分析程序；
未检索物理论文、未处理 get-paper、未 commit/push、未派生代理。
本报告不是领域新颖性的完整文献检索，也不是历史实验的重拟合。

## 结论

**−8/3 正确。现稿的数学核心是标准角分布形式主义下的条件相容性约束，
尚不是独立识别 signed delta 的新反演方法。**

必须修改三个科学层次问题：

1. rank-4 只约束 `f_E2*s4`；已知非零 `s4` 才能反演 `f_E2` 和 `|delta|`，
   仍不能区别 `+delta` 与 `-delta`。
2. 不同后选择导致的母态取向差异、参考线多极污染和 detector Q 因子属于不同
   物理层。不能把它们统一解释为“负 s4”。
3. 中央值和字面边际误差盒的相容性检查不是带覆盖率的实验拒绝检验。
   “direct falsifier”“public evidence fails”及“model-preferred root”等措辞须收紧。

## 实际执行证据

运行环境：Python 3.12.3，SymPy 1.14.0，mpmath 1.3.0。
两个现有 Python 入口最初均未提供 SymPy；依赖以 pip `--target`、
`--no-cache-dir --no-compile` 隔离安装于本目录 `deps/`，运行时禁用 pyc。
本轮未安装全局软件。

复跑命令：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B tmp/ba129-independent-review/independent_review.py
```

该命令只在本目录更新结果和三个明确标记的测试 CSV，不运行原稿 CLI。
独立证明完成后，才通过 import 加载待审程序，调用其纯计算函数作对照。

执行结果：102 项检查通过，包括标准 6j、rank-4 选择规则、14 个母态 m
的直接光子投影及归一、零信号极限、乘积不可识别性、门选择反例、
有限角响应、字面误差盒和程序负面输入控制。
“检查通过”包含成功复现待审程序漏检输入的情况，不是实验或论文认证。

首次读取及执行前后两个文件 SHA-256 相同：

| 文件 | SHA-256 |
|---|---|
| main.tex | `3c9d9a2bfded468af0069381115b3de112cbfff756adde94cd392770d3868f36` |
| analysis/rank4_invariant.py | `3ad6b43008cf24f1bbaf6d1ff3b7467be722cb85e46656580fe3061a99042c21` |

精确结果、全部检查和运行版本见 `result.json`。以下行号对应上述稿件版本。

## 两条独立核算路线

SymPy 标准 `wigner_6j` 给出：

\[
\begin{Bmatrix}13/2&13/2&4\\2&2&11/2\end{Bmatrix}
=-\frac{8\sqrt{12155}}{15015},\qquad
\begin{Bmatrix}13/2&13/2&4\\2&2&9/2\end{Bmatrix}
=-\frac{\sqrt{12155}}{5005}.
\]

两个 6j 自身之比为 `+8/3`，平方比为 `64/9`。采用明确的纯 E2 约定

\[
F_4(J_i,J_f;22)=(-1)^{J_i+J_f-1}
\sqrt{25(2J_i+1)}
\langle 2\,1,2\,-1|4\,0\rangle
\begin{Bmatrix}J_i&J_i&4\\2&2&J_f\end{Bmatrix},
\]

得到

\[
F_{4,t}=\frac{32\sqrt{2431}}{3003}=0.5253964397467514,\quad
F_{4,r}=-\frac{4\sqrt{2431}}{1001}=-0.19702366490503176,
\quad F_{4,t}/F_{4,r}=-8/3.
\]

负号来自辐射系数相位，不能仅凭 6j 平方比确定。

另一条路线完全不调用待审 CG/6j 或 `native_f`。用 SymPy 标准 CG 和
Wigner 小 d 矩阵构造纯多极光子分布：

\[
W_L(\theta|m)=\frac{2L+1}{2}
\sum_{m_f}|\langle J_fm_f,Lq|J_im\rangle|^2
\sum_{\lambda=\pm1}|d^L_{q\lambda}(\theta)|^2,\quad q=m-m_f.
\]

通过 Legendre 积分提取 A4，并对 `m=-13/2,...,+13/2` 全部 14 个 m
逐项核对 `A4t+(8/3)A4r=0`。因此共同对角布居的任意线性混合也成立，
不需要高斯布居。`m=±1/2` 控制给
`A4t=576/1001`、`A4r=-216/1001`。
这不是对非轴对称 gate 或任意探测响应的无条件证明。

M1/M1 的最大张量秩为 2，M1/E2 干涉的最大秩为 3；
标准 CG 的两项 rank-4 系数均严格为零。这才是目标 rank-4 项
只含辐射 E2 份额的原因。

## 用户新增 OCR 与 rank-2 独立核验

只读文件：

- `raw/papers/gpt/query/20261105-ba129-primary/gizon1977-full-json.json`
  的 `full-text-retrieval-response.originalText`，实测 33,742 字符；
- `tmp/ba129-primary-review/gizon1977-full.txt`，去除首尾空白后与上字段相同。

JSON SHA-256：
`1dd29020347823672adba2ef2f7e7955976236c8d09fe8cf00a12ee83025ef3e`。
衍生文本 SHA-256：
`51f4152221d0ea2fae48b595c3cce6e1af698ce27eb6af009fefe94b6d6484e1`。
读取前后哈希相同。本轮未下载来源。

从标准 Wigner/CG 系数独立求出纯 E2 参考归一的矩阵，确认用户结果：

\[
\frac{A_{2,t}}{A_{2,r}}=s_2g_2q(\delta),\quad
q(\delta)=\frac{(1,\delta)M(1,\delta)^T}{1+\delta^2},\quad
M=\begin{pmatrix}-7/10&7\sqrt{11}/10\\7\sqrt{11}/10&-1/10\end{pmatrix}.
\]

其中 `s2=Q2t/Q2r`，`g2=rho2t/rho2r`；共享后选择才有 `g2=1`。
该矩阵的 Rayleigh 商范围严格为

\[
\frac{-2-\sqrt{137}}5\le q(\delta)\le
\frac{-2+\sqrt{137}}5.
\]

下界是 `−2.740939982143925`；采用当前相位约定时，在
`delta=(3−2sqrt(137))/(7sqrt(11))` 达到。改变 delta 的符号约定等价于
翻转非对角元，不改变特征值范围。

公共中央比 `−0.70/0.22=−35/11=−3.181818...` 低于下界。
**这只是不相容于 `s2=g2=1` 的必要范围检查。**
若共享取向但 s2 可变，中央比所需最小正 s2 为
`25(sqrt(137)−2)/209=1.160849271617180`；
不能把 `s2>0` 偷换成 `s2=1`。

对两套误差分别测试，保留稿件中央值和符号：

| 误差输入情景 | 倍数 | rank-2 比值盒与 s2=1 允许范围 | rank-4 盒与 s4=1 允许像 |
|---|---|---|---|
| 当前 ENSDF：t2 .03、r2 .02、t4 .05、r4 .05 | 1 | 不相交 | 不相交 |
| 当前 ENSDF | 2 | 相交 | 不相交 |
| OCR 字面误差情景：t2 .05、r2 .04、t4 .05、r4 .06 | 1 | 相交 | 不相交 |
| OCR 字面误差情景 | 2 | 相交 | 相交 |

ENSDF 一倍 rank-2 比值盒上端为 `−67/24=−2.791667`，但只需
`s2=1.0185070395` 就能与缩放后的范围接触。
OCR 字面一倍盒范围为 `[-25/6,-5/2]`，已覆盖下界附近。
OCR 字面二倍 rank-4 参考盒为 `[-.04,.20]`，
映射像为 `[-8/15,8/75]`，与目标 `[.06,.26]` 相交。
这是**误差版本敏感性**，不能宣布原始数据已通过完整拟合。
两秩在此分开检查，没有证明它们存在同一 delta/正布居的联合解。

OCR 目前不能认证丢失的正负号或表格列归属。上表只是按用户提供和 OCR
可见数字构造的暂定误差情景，绝不覆盖 ENSDF 或补写原表缺失符号。
必须在 manuscript input ledger 中保留“评价值”和“未视觉核验的 OCR
字面值”两个版本，不能混用较小误差作更强结论。

用户指出的 p469 附近 OCR 段确在讨论 701.4-keV 跃迁时出现
`alpha2≈0.5` 与 `alpha4<0.2`。它提供了有价值的 correction-context 线索，
但不是 364.7/461.6 两支的逐线校准，不能推广成全局 alpha，
更不能把 nuclear attenuation alpha 当 detector Q 或 s 比值。

rank-2 检查适合作为对照：它的幅值界需要 s2 的范围；
rank-4 的异号必要条件只需 s4 的符号，不要求固定其正的大小。
这一区别可以明确稿件的实际用途，但两者共享来源和潜在拟合/校准协方差，
不能计为两次独立实验证实，也不建议拆成第二个新物理 claim。

执行命令：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B tmp/ba129-independent-review/rank2_addendum.py
```

新增 25 项标准系数、谱界、误差情景及来源完整性检查通过；
完整结果及零基字符偏移见 `rank2-result.json`。

## 能识别与不能识别的量

在共享选后母态布居、纯 E2 参考、可作标量折叠且
`A4r != 0` 的条件下，定义

\[
z=-\frac38\frac{A_{4,t}}{A_{4,r}}=f_{E2}s_4.
\]

| 已知条件 | 能得到什么 | 仍得不到什么 |
|---|---|---|
| `s4` 大小和符号均未知 | 乘积 z | f、delta 大小与符号 |
| 仅知 `s4>0` | 非零 A4 的异号必要条件 | f 的唯一数值 |
| 非零 `s4` 已独立标定，正负均可 | `f=z/s4`；0≤f<1 时 `|delta|=sqrt(f/(1-f))` | delta 符号 |
| `0<s_min≤s4≤s_max` | z≥0 时 `f in [z/s_max,z/s_min] intersect [0,1]` | 一般仍不是点识别 |
| 共享 rho4=0 或目标 Q4=0 | rank-4 无目标灵敏度 | f 或 delta |
| 参考 Q4=0 或参考 A4=0 | 比值反演未定义 | 不可把零分母当校准 |

精确恒等式 `f(delta)=f(-delta)` 表明 rank-4 不辨符号。
它原则上可区别不同大小的根，例如 `|delta|=2` 与 `|delta|≈0.33`，
但前提是 s4 的标定和精度足够。不要把“大根/小根”和“正根/负根”混写。

不可识别性的明确反例：
`(f,s4)=(4/5,1)` 与 `(1/5,4)` 都给 `z=4/5`，分别对应
`|delta|=2` 和 `1/2`。两者可取共同 `Q4r=1/4`，而
`Q4t=1/4` 或 `1`；因此退化不依赖负 Q。
映射 `(f,s4)->f*s4` 的 Jacobian 秩为 1，沿 `(f,-s4)` 方向局部不变。

稿件第 275–278 行“确定负 s4 后停止”不正确。若独立确定 `s4=-1`，
现有中央乘积 `z=-3/4` 给 `f=3/4`、`|delta|=sqrt(3)`；
负号本身不阻止反演。这里仅说明数学可识别性，不是 129Ba 的新结果。

要识别 delta 符号，还需已校准的干涉敏感量。例如 rank-2 在适用模型内满足

\[
A_2(\delta)-A_2(-\delta)
=\frac{4\rho_2Q_2F_2(12)\delta}{1+\delta^2}.
\]

只有相关相位、rho2/Q2、系数层和误差都得到约束时，该差才可作根判别。
内转换率或寿命本身通常只提供强度信息，不能自动恢复 delta 符号。

## 同母态、不同 gate 与 Q 因子的区别

同一个能级只保证量子数相同，不保证被不同选择条件保留下来的母态系综相同。
在仍可写成标量模型的情况下，应先保留

\[
A_{4,t}=-\frac83 f_{E2}s_4g_4 A_{4,r},\qquad
g_4=\rho_{4,t}/\rho_{4,r}.
\]

共享后选择得到 `g4=1` 后，才能消去该因素。核取向/feeding/postselection
是 g4 的问题；有限角折叠是 s4 的问题。
非轴对称 gate、角关联符合选择、角秩混合等更一般情况需要完整响应，
连这个带 g4 的标量式也不一定适用。
即使 gate 名称相同，也要核对 detector-pair weighting、时间选择和条件密度。

独立正布居反例：同一母态初始是 `m=±1/2` 与 `m=±7/2` 的等权混合，
目标选前一组、参考选后一组。取两条 `Q4=1`、目标纯 E2 极限，
直接光子计算给

`A4t=576/1001 >0`，`A4r=184/1001 >0`，`g4=-27/23`。

两 A4 同号而 s4=1；带 g4 的式子严格成立。
这是理想正的子态选择反例，不宣称是旧实验的实际 gamma gate 模拟。

反过来，正的探测接受核也不保证 Q4>0。均匀立体角锥给

\[
Q_4(c)=c(1+c)(7c^2-3)/8,\qquad c=\cos\beta_{\max}.
\]

半角 60 度的正核给 `Q4=-15/128`。应写“两个 rank-4 响应因子同号”
或 `s4>0`，避免把“正响应”与非负效率混为一谈。

另一个正效率反例取
`W=1+P2/3`、未消除的极角效率 `h=1+P2/2`。
归一后 `Wh` 的 A4 为 `18/217`，而真实 A4=0。
因此一般效率误差可以混入其它角秩，不能都塞进乘法 Q4。

## 稿件逐项修订建议

| 优先级 | main.tex 行 | 发现 | 建议 |
|---|---|---|---|
| 高 | 15、55–62、105、284 | “identifiability gate”未明确究竟识别乘积、大小还是符号；核心结果主要是相容性必要条件 | 增加上述识别性表，标题可改为 “A conditional rank-4 consistency test for same-parent gamma-ray transitions: the 129Ba 365-keV case” |
| 高 | 180–185 | 把不同 postselection、系数 convention 和高阶多极都解释成负 s4，违背 s4=Qt/Qr 的定义 | 分列 g4、响应、系数换基、参考线多极污染。高阶多极会改变辐射因子及干涉项，不能算成仪器 Q |
| 高 | 275–278 | 噪声测量的正中央值被称为 direct falsifier；已知负 s4 也要求停止 | 分开精确假设的代数不相容与带噪声数据的统计检验；保留已知负 s4 的合法反演 |
| 高 | 244–250、288–297 | 新附加的参考条件未必是 2024 原作者实际采用条件；“model-preferred root”暗示未证实的选根动机 | 写成“当前公开摘要不足以验证本文附加的参考转移条件”；保留原文的 AD 联合最佳拟合归属 |
| 中 | 38–42 | 容易将单个 A2 的歧义泛化为所有角分布拟合都必须增加偏振 | 明确：已知取向及响应时，可靠 A4 与 A2 可以区别大小根；未知取向时另有退化 |
| 中 | 157–159 | 只给平方比与文字描述，不足以让读者独立核负号 | 列出两个标准 6j、辐射系数相位和有符号 F4 |
| 中 | 236–242 | “independent marginal intervals”可能被误读为已建立统计独立性；两误差盒不相交不稳健于 s4 | 改为 literal marginal-error boxes，标明 s4=1 是示例；加入 s4=9/8 时相交的敏感性控制 |
| 中 | 24–27 | 将 decreasing wobbling energy 同时泛化到 transverse/longitudinal 不够准确，也与本例的 increasing trend 论述不协调 | 改为一般的 spin dependence；若细分 TW/LW，明确模型条件后另核物理归属 |
| 中 | 191–208、271–272 | 用已知 f/s4 代入再代回只能验证恒等式；一个已知 multipolarity control 不能单独验证区间覆盖率 | 区分代数测试、独立响应 benchmark 和在声明观测模型下重复采样的覆盖率验证 |

## 数值与统计边界

中央乘积 `z=-3/4`、一倍盒在 s4=1 下的目标像 `[-26/75,0]`、
二倍盒的像 `[-12/25,4/75]` 均核对正确。
二倍盒的间隙仅 `1/150=0.0066667`；s4 改为 `9/8=1.125`，
取 `f=1`、`A4r=-0.02` 即可碰到目标下界 `0.06`。
这不影响两个严格正系数在 s4>0 下的符号定理，却说明固定 s4=1 的二倍盒
“不相交”不能当普适稳健结论。

程序的独立对角高斯距离也核对正确：

`D(f)=256(4f+3)^2/[25(64f^2+9)]`，
在 `[0,1]` 的最小值位于 `f=1`，
`Dmin=12544/1825=6.873424657534247`。

它只属于人为独立高斯、s4=1 模型，不是实验 p-value。
参考系数 `0.08` 仅为其 quoted error `0.05` 的 1.6 倍；
正式分析宜拟合原系数/角计数及共同 nuisance，而不是把比值当近似高斯。
补齐 covariance 可改善统计量，不能消除 f 与未知 s4 的结构退化。

## 程序审查

既定 `(13/2,11/2,9/2)` 输入的 `native_f`、区间像和对角距离数值正确。
程序仍缺少如下防错：

- `rank4_invariant.py:223` 只读取 target 的 Ji，reference 的 Ji 被忽略。
  在本目录将 reference 的 `Ji_twice` 改为 15 后，`analyze` 仍通过并输出
  与 canonical 输入相同的 algebra。必须验证共同母态 ID 和自旋；
  目前字段只能校验自旋，还不能证明同一能级。
- `rank4_invariant.py:161` 只检查标签集合，三行含重复 target 仍通过，
  随后 dictionary 覆盖。应同时检查行数和标签唯一性。
- `rank4_invariant.py:230` 把 `exact_ratio=-8/3` 写死，再检查浮点比及精确平方比。
  本轮独立计算已核实该值，但程序输出的 “exact” 字段本身不是独立导出。
  应由精确平方比、6j 符号和完整相位合成有符号精确结果。
- 加入明确的输入域检查：有限数、正误差、非零参考系数、相同母态、
  支持的自旋序列。纯 E2、gate 和 Q 标定属于数据合同，不能靠默认字段认证。
- 增加 `delta_sign_identified: false`、`identified_quantity: f_E2*s4`
  等输出；`s4` 未独立给定时不要输出新的 f 或 delta 估计。

## 新颖性判断与可保留的最强主张

本轮没有做外部新颖性检索，不能断言无人做过，也不能断言整项工作已经发表。
但 rank 上限、共同统计张量约消和本自旋序列的 −8/3 都直接来自标准角动量代数。
将标准关系包装为 “gate” 不自动构成新的识别方法；现有合成往返也没有展示
新的推断能力、统计覆盖率或核结构结论。

稿件可保留的贡献是：把这一必要关系落实为**定义和条件明确、可重放的
legacy coefficient consistency diagnostic**，并用本例说明缺失什么输入会
阻止参考转移。要提高为完整方法稿，需要一般适用域、真实可闭合的独立控制、
明确的 nuisance 处理，以及相对已有分析流程新增信息的展示。
仅凭当前两个未闭合摘要值，创新性风险仍高。

建议的正文核心措辞：

> Specializing the standard angular-distribution formalism, we obtain an exact
> rank-4 consistency relation for a mixed M1/E2 line and a pure-E2 companion
> from a common selected parent ensemble. The relation constrains the product
> of the radiative E2 fraction and the rank-4 response ratio. With an independently
> calibrated nonzero response ratio it can constrain the magnitude, but not the
> sign, of the mixing ratio. The published central coefficients and the stated
> literal marginal-error box are incompatible with the additional common-ensemble,
> pure-reference, positive-ratio assumptions. This does not constitute a
> calibrated experimental rejection of either the historical data or the
> 2024 mixing-ratio result.

本轮建议是 **major revision**：保留 −8/3，重写识别性、gate/Q 分层、
统计结论及新颖性措辞。primary-source retrieval 由用户本地继续处理，
本审查不代替该步骤。
