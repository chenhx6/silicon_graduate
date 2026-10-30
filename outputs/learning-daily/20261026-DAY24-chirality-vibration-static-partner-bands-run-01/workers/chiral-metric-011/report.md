# 一维Pauli算符、测度与有限能隙波包：独立数学审查

本轮为CH13方法合同的独立推导和synthetic数值控制，供root审核写回。不是CH13 actual producer、不是133Ce/135Nd计算、没有数字化原图或反推原参数，没有建立普适手征判别门。仅写本worker目录和获准tmp，无canonical/raw/Git修改、无新session/credit。新增内容均为任务推导，`needs_review: true`，不改变既有人审。

原件校准入口是Chen et al., PRC87,024314(2013)的arXiv1212.2313v2，PDF5 Eqs12–14、PDF7 Eqs24–27；本轮重算既有staging PDF SHA仍为`bef6182263a6282ea6c4fc3e2fbae481bbf629e484dbf9668e3ea9e622342a2c`。root已全文读取；本轮不重复声称另一次16页原文精读。以下是数学审查，不是原论文新增claim。

## 1. 对象、假设及一个必须补齐的前提

在对称区间φ∈[−a,a]取

\[
\hat H\psi=-\frac{\hbar^2}{2\sqrt{B}}\frac{d}{d\varphi}
\left(\frac1{\sqrt B}\frac{d\psi}{d\varphi}\right)+V\psi,
\qquad
\langle f,g\rangle_B=\int_{-a}^a \sqrt B\,f^*g\,d\varphi.
\]

**本报告的regular Dirichlet合同：**B为实C²函数，整个闭区间有0<b_min≤B≤b_max<∞，V为实连续函数；ψ(−a)=ψ(a)=0。这些假设使x区间有限、各幺正变换可逆，并给标准regular Sturm–Liouville自伴问题。后述singular端点另行处理。

**V偶本身不保证完整H具有φ反射对称。** 还需B(−φ)=B(φ)，并且区间/边界在反射下不变。若B不偶，Pψ(φ)=ψ(−φ)一般连加权内积的unitarity都不保持，因为权重√B不随反射保持。不能仅由V双阱对称就推两本征态的左右概率相等。

量纲：φ按rad视无量纲，B、B0同为action²/energy，V为energy；以下通式保留ℏ，synthetic例才取ℏ=B0=1。

## 2. 加权空间中的Hermiticity和正动能

记p=B^(−1/2)、w=B^(1/2)、c=ℏ²/2。分部积分给

\[
\langle f,Hg\rangle_B
=c\int p f'^*g'\,d\varphi+\int wVf^*g\,d\varphi
-c[f^*p g']_{-a}^{a}.
\]

Dirichlet使边界项消失，因此得到实对称二次型，动能项为非负的c∫p|ψ′|²。配合上述regular域可取自伴Dirichlet实现；不能仅写一个形式微分式就省去域/边界合同。

把方程乘w也得到适于离散的generalized Sturm–Liouville形式

\[
-c(p\psi')'+wV\psi=Ew\psi.
\]

## 3. x坐标使质量成为常数

任取常数B0>0，定义

\[
x(\varphi)=\int_0^\varphi\sqrt{\frac{B(s)}{B_0}}\,ds,
\qquad \frac{dx}{d\varphi}=\sqrt{B/B_0}>0.
\]

链式法则逐项给

\[
B^{-1/2}\partial_\varphi\psi=B_0^{-1/2}\partial_x\psi,
\qquad
B^{-1/2}\partial_\varphi(B^{-1/2}\partial_\varphi\psi)
=B_0^{-1}\partial_x^2\psi.
\]

因此在对应x区间[x(−a),x(a)]，

\[
H_x=-\frac{\hbar^2}{2B_0}\partial_x^2+V(\varphi(x)).
\]

测度为√B dφ=√B0 dx。若x空间采用普通dx范数，归一幅应定义

\[
\Psi(x)=B_0^{1/4}\psi(\varphi(x)),\qquad
\int|\Psi|^2dx=\int\sqrt B|\psi|^2d\varphi.
\]

regular端点下ψ=0与Ψ=0对应。**x中没有额外量子势**，但B并未失去物理作用：它改变x的区间长度和V(φ(x))的形状。B0只是坐标参考尺度，不能固定新x盒及V(x)后任意改B0却声称仍是同一个系统。

若B为偶，x(0)=0给x(−φ)=−x(φ)，对称φ盒映为对称x盒，V偶也映成偶Vx。若B不偶，这一步的反射对应关系不成立。

## 4. 保持φ坐标而改用flat measure的幅u

若希望在同一个φ坐标下以dφ为测度，应取

\[
u(\varphi)=B^{1/4}\psi(\varphi),
\qquad \int|u|^2d\varphi=\int\sqrt B|\psi|^2d\varphi.
\]

共轭变换H_u=B^(1/4)HB^(−1/4)给

\[
\boxed{
H_u=-\frac{\hbar^2}{2}\partial_\varphi
\left(B^{-1}\partial_\varphi\right)+V+Q_B,
\quad
Q_B=\frac{\hbar^2}{2}
\left[\frac{B''}{4B^2}-\frac{7(B')^2}{16B^3}\right].}
\]

连续推导的中间式为

\[
B^{1/4}\left[B^{-1}(B^{-1/4}u)''-
\frac{B'}{2B^2}(B^{-1/4}u)'\right]
=\frac{u''}{B}-\frac{B'}{B^2}u'
+\left[\frac{7(B')^2}{16B^3}-\frac{B''}{4B^2}\right]u.
\]

这核定Q_B中的**1/4与−7/16**，而不是任意添加的物理新势。仅将原算符中的质量换成1/B，再在flat dφ下求解而不带Q_B，会改了模型。

一个更紧凑的正动能表达是

\[
T_u=-cB^{-1/4}\partial_\varphi B^{-1/2}\partial_\varphi B^{-1/4},
\quad
\langle u,T_uu\rangle=c\int B^{-1/2}
|(B^{-1/4}u)'|^2d\varphi\ge0.
\]

regular合同下u同样满足Dirichlet，Hu在flat dφ下自伴。Q_B局部可负，并不破坏这个动能非负性。

两条变换彼此一致：u(φ)=(B/B0)^(1/4)Ψ(x(φ))，其平方正是dx/dφ的Jacobian。CH13基函数中的B^(−1/4)来自这一测度合同：√B与两份B^(−1/4)相消，剩普通sine/cosine正交积分。

## 5. 密度、反射与有符号奇量

同一物理概率可写为

\[
dP=|\psi|^2\sqrt B\,d\varphi
=|u|^2d\varphi=|\Psi|^2dx.
\]

因此\|ψ\|²是相对于collective volume √B dφ的密度；每单位φ的密度是√B\|ψ\|²=\|u\|²。不能把两张不同测度下的曲线直接比较峰高/面积，或用∫\|ψ\|²dφ重新归一后当成相同概率。本文不据此判CH13 Fig7作者画错；该图字面\|ψ\|²与Eq14测度必须一起解释。

在**B与V都偶**且对称Dirichlet域下，P为幺正且[H,P]=0。regular一维标量Sturm–Liouville本征值为simple，可将本征函数取为实、具有确定φ反射偶/奇性。对实乘法奇量f(−φ)=−f(φ)，

\[
\langle f\rangle_n=\int_{-a}^{a}w\,|\psi_n|^2f\,d\varphi=0.
\]

这里的反射parity不是核空间宇称。本轮的f=sgnφ只是synthetic取向代理，不是已恢复真实核的σ算符或实验手性。

在这一个regular、有限、一维标量盒模型内，最低偶态与第一奇态的gap严格为正；严格简并只能作为某种singular/无限势垒/其它域的极限另论。此数学结论不扩展为禁止真实核的各种精确简并。

## 6. 有限ΔE的局域packet不为定态

取最低偶/奇实本征态|0⟩、|1⟩，E1−E0=Δ>0，定义正交组合

\[
|L\rangle=(|0\rangle+|1\rangle)/\sqrt2,
\qquad |R\rangle=(|0\rangle-|1\rangle)/\sqrt2.
\]

若选择相对符号使L偏左，精确两态演化为

\[
|L(t)\rangle=e^{-i(E_0+E_1)t/(2\hbar)}
\left[\cos\frac{\Delta t}{2\hbar}|L\rangle
+i\sin\frac{\Delta t}{2\hbar}|R\rangle\right].
\]

因此t=πℏ/Δ到R（差整体相位），t=2πℏ/Δ返回L。对实奇乘法量，若f01=⟨0|f|1⟩为实，

\[
\langle f\rangle_{L(t)}=f_{01}\cos(\Delta t/\hbar).
\]

即使每个本征态的奇量期望都为零，局域组合仍可有非零随时间振荡的奇量。范数和平均能量(E0+E1)/2守恒。这是幺正闭系统的两态结论，不包括环境退相干、实验选择或永久自发局域化，也不提供核寿命时钟。

## 7. Synthetic离散：三条路线及解析极限

所有数值都取无量纲ℏ=B0=1、a=π/2；**与CH13参数、原V/B曲线及真实核无关**。正偶质量与偶双阱取

\[
B=1+0.7\varphi^2,
\qquad V=18(\varphi^2-0.85^2)^2.
\]

B在闭盒上有限、≥1，V(0)=9.3961125。没有据此设置任何“static chirality”阈值。

**路线A，加权generalized FV：**均匀φ内点，w_i=√B_i、面通量p_(i+½)=1/√B_(i+½)，M_i=h w_i，S_ii=c(pL+pR)/h+M_iV_i，S_(i,i+1)=−c pR/h；求Sψ=EMψ。使用M^(−1/2)SM^(−1/2)的实对称tridiagonal形式，不把非对称M⁻¹S交给对称solver。

**路线B，独立x-grid：**本质量的坐标有解析式

\[
x=\frac12\left[\varphi\sqrt{1+0.7\varphi^2}
+\frac{\operatorname{asinh}(\sqrt{0.7}\varphi)}{\sqrt{0.7}}\right].
\]

均匀x网格，Newton直接反解φ(x)，不插值A网格、势、矩阵或本征态；在x上用常质量central difference求谱。逆变换残差保存在JSON，接近浮点精度。

**路线C，flat-u：**均匀φ网格，按Hu的divergence-form 1/B通量和解析Q_B独立构造tridiagonal矩阵。这一路检验1/4、−7/16和measure变换；不能把直接由A矩阵相似变换的相同谱冒作独立discretization。三路本身仍均是二阶方法，必须继续看共同截断误差。

解析退化检查：V=0、B=1时E_n=n²/2；同一可变B但V=0时，有限x盒长度Lx给E_n=π²n²/(2Lx²)，数值前四态解析值为[.3255512502,1.3022050008,2.9299612519,5.2088200034]。这些极限不需要任何势能拟合。

| V=0解析极限，前4态最大绝对误差 | 127内点 | 255 | 511 | 1023 |
|---|---:|---:|---:|---:|
| B=1，FV与x-grid（此极限相同） | .00642346 | .00160625 | .000401587 | .000100398 |
| B=1+.7φ²，FV | .00442686 | .00110700 | .000276768 | .0000691931 |
| B=1+.7φ²，独立x-grid | .00418233 | .00104583 | .000261474 | .0000653696 |

每次网格间距减半，误差约降4倍，符合二阶截断。

## 8. 双阱谱、误差预算与packet结果

下表均为前4态最大绝对差，无量纲。参考为16383内点x-grid，仍有截断误差。

| 内点N | FV−x路线差 | flat-u−x路线差 | FV−x参考差 | x−x参考差 |
|---:|---:|---:|---:|---:|
|127|2.820e−4|4.192e−4|9.429e−3|9.711e−3|
|255|7.080e−5|1.052e−4|2.356e−3|2.427e−3|
|511|1.772e−5|2.631e−5|5.884e−4|6.061e−4|
|1023|4.431e−6|6.579e−6|1.467e−4|1.511e−4|
|2047|1.108e−6|1.645e−6|3.622e−5|3.733e−5|
|4095|2.770e−7|4.112e−7|8.609e−6|8.886e−6|

三路都以h²收敛。**路间差小于各自截断偏差，不能以4.1e−7的一致性宣称谱已准确到4.1e−7。** x-grid从8191到16383前4态最大变化1.776e−6；最低gap变化1.816e−8。16383参考前两态约3.79806946、3.99369585，gap≈**.1956264**。条件二阶Richardson外推gap≈.1956263972，仅为数值估计，不是严格误差界或实验CI。

在4095点FV本征态上，M-正交误差≤4.5e−16；u变换后的flat范数Gram与原加权Gram差≤7.2e−17。反射parity幅度残差及单本征态sgnφ期望约10⁻11，为当前浮点/求解误差量级。它们不是物理左右不对称。

两态packet的m01≈−.9907107625，左右泄漏仍有限，并非精确空间支持完全分离。Δ≈.1956262468给以下**无量纲时间**：

| Δt相位 | t | P(left)，中心点平分 | P(right) |
|---|---:|---:|---:|
|0|0|.99535538|.00464462|
|π/2|8.02958|.50000000|.50000000|
|π|16.05916|.00464462|.99535538|
|3π/2|24.08874|.50000000|.50000000|
|2π|32.11831|.99535538|.00464462|

各时刻范数约1，数值奇量与m01cosΔt相符。有限gap下L不是定态，且正交|L⟩/|R⟩不等于它们在φ半盒中严格没有尾部。未用这些时间作核时间尺度。

另一个直接显示measure影响的量：基态正确⟨φ²⟩≈.62625335；若错把\|ψ\|²用flat dφ重新归一，得到≈.59811412，相差约4.49%。这不是校正真实实验，只是相同synthetic态的错误测度反例。

**反射前提的负控制：**换成B=1+.3φ（全盒仍正且光滑），保持同一偶V，FV4095点ground ⟨sgnφ⟩≈+.9410463。V虽偶，质量/测度几何不对称，所以前述零奇量结论不适用。此反例不否定CH13采用的偶B，而是防止把“V偶”单独升级为一般定理。

## 9. Large/singular B与wall不能混同

本数值例满足finite regular合同；没有用它证明CH13边界处的实际B具有何种渐近形式。

若原端点B发散，则变换后长度由∫√(B/B0)dφ决定：可以有限，也可以无限。例如仅作解析分类，距端点s→0时B∼s^(−p)，p<2使x长度有限，p≥2使其无限。**“B大/发散”本身不普适推出ψ=0的硬墙，也不普适推出有限x盒。** 是否选Dirichlet及是否存在离散谱还须带着V、原边界/自伴域一起判断。

而且singular情形下u=B^(1/4)ψ可能改变端点衰减，不能从ψ→0自动跳到普通u-Dirichlet；必须传递整个域。CH13从large B选择wall approximation是一项明确近似，本报告只校核该选择后算符与测度的内部合同，不替作者证明它是唯一物理边界。

## 10. 可复现入口及知识影响

运行：

`python3 outputs/learning-daily/20261026-DAY24-chirality-vibration-static-partner-bands-run-01/workers/chiral-metric-011/metric_audit.py`

脚本只向自己目录的`results.json`写结果；依赖Python、NumPy、SciPy，具体版本在JSON。`artifact-manifest.json`记录代码/报告/结果SHA。没有作者代码、模型拟合、图点提取或外部状态变更。

可写回的新合同为：①B也须偶才能由φ反射推出奇量零；②x-constant与φ-flat-u是两种不同但幺正等价的表达，后者有明确Q_B而前者吸收Jacobian；③概率密度须连测度；④finite-gap局域packet演化与定态对称恢复分开；⑤数值路线一致性不能代替共同截断检查；⑥large/singular B不能自动当有限盒/硬墙。该合同加强Day24量子化层，不裁定任何真实候选带或模式。
