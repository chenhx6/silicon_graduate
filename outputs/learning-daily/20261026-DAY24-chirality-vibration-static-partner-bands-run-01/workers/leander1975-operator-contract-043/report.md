# 043：Leander–Larsson1975原件关闭历史坐标与轴对称对角 q 的定义，未给完整三轴跃迁库

**实际Ref23现已取得并完成本任务定向原读。** A1给dimensionless stretched坐标，A2/A3给一般spinor-harmonic角矩阵元及其CG归一；A7明确体积守恒定标；A8/A9给忽略γ后的同一MO本征态ν的quadrupole/hexadecapole期望值。故先前“Ref23未取得/未读”的来源缺口可按本范围关闭；**不能把A8的下标ν误作任意球张量μ，也不能把这些对角轴向表达当完整三轴transition library。**

## 真原件、scope与视觉核验

G. Leander and S. E. Larsson, *Potential-energy surfaces for the doubly even N = Z nuclei*, Nuclear Physics A **239** (1975) 93–113，DOI `10.1016/0375-9474(75)91136-7`。本轮输入是root已经取得的21页、1736708 bytes PDF：

`tmp/day24-leander1975-039/attachment-object-response.pdf`

SHA256 `35ce50a080755f3a11dac48cfbe2e2041659694038bc6bcaf28b452d72da562d`，本轮fresh hash/pdfinfo一致。它不是此前常规API返回的1页文件；不重新下载、不猜端点、不把1页文件当正文。

本单元连续读**physicalPDF3–6/printed95–98**方法与相关矩定义、**PDF19–20/printed111–112**整个Appendix；定向追加**PDF7/printed99 Table1表头、列名、脚注**。PDF1–2文字只用于核题名、作者与研究范围；全文提取只用于定位Table1，**未声称21页全文精读、全部PES或表内全部核素数值审计**。视觉核3–6/7/19–20，并对A1–A3、A7–A10、Eq5、Eq10–12和Table1另看放大图。截图在本单元tmp目录。

正文研究的是12≤A≤44的doubly-even N=Z核PES，不是133Ce；本轮只将可追溯的方法定义与已声明数学字典相接，不迁其势参数或结果给Ce。

## A1：原件实际是 dimensionless 坐标

PDF19 A1逐字结构为

\[
\xi=\sqrt{{m\omega_0\over\hbar}
 [1-\tfrac23\varepsilon\cos(\gamma+\tfrac{2\pi}3)]}\,x,
\]
\[
\eta=\sqrt{{m\omega_0\over\hbar}
 [1-\tfrac23\varepsilon\cos(\gamma-\tfrac{2\pi}3)]}\,y,
\qquad
\zeta=\sqrt{{m\omega_0\over\hbar}
 [1-\tfrac23\varepsilon\cos\gamma]}\,z.
\]

根号覆盖整个频率因子和方括号。它不是042的dimensionful X_i本身。定义b_x/y/z为三个方括号，**任务识别**ω_i=ω0 b_i且要求b_i>0，则恰落入042的dimensionless ξ_i=√(mω_i/ℏ)x_i字典；其dimensionful X_i=ℓ0 ξ_i，ℓ0²=ℏ/(mω0)。不需更改042的几何推导，但现在有原始历史coordinate convention可对应。

**频率记号已视觉分开：**A1、A8、A9是无圈ω0；A7和正文spin–orbit/orbit–orbit参考处另有上置小圆圈的`\overset{\circ}{\omega}_0`。不是可随OCR合并的同一符号，也不擅改成barred ω。下文把后者简称ω0°以便纯文本记录。原件的ε也不自动等于WK22的β。

## A2/A3：一般 angular ME，double bars并非唯一归一

PDF19 A2的bra有l′j′Ω′，ket是ljΩ；它是**一般角矩阵元**：

\[
\langle l'j'\Omega'|Y_{\lambda\mu}|lj\Omega\rangle
=r^{LL}_{l'j',lj;\lambda}
\langle j\lambda\Omega\mu|j'\Omega'\rangle.
\]

A3定义原文所谓reduced matrix element为

\[
r^{LL}_{l'j',lj;\lambda}
=\sqrt{{(2j+1)(2\lambda+1)\over4\pi(2j'+1)}}
\langle j\lambda\,-\tfrac12\,0|j'\,-\tfrac12\rangle
\,{1+(-1)^{l'+\lambda+l}\over2}.
\]

末尾是parity projector；l′、j′与Ω′的prime在放大图中实际存在。此处为Yλ的angular/spinor-harmonic积分，**没有径向HO积分或deformed-state系数**。不能因A8是对角式就说这篇完全没有一般angular ME；也不能从A2有prime扩成已发表任意ν′→ν的physical E2矩阵库。

与041采用的标准3j WE约定对齐时（相同CG相位），

\[
F=(-1)^{j'-\Omega'}
\begin{pmatrix}j'&\lambda&j\\-\Omega'&\mu&\Omega\end{pmatrix}
R^{std}
=\langle j\lambda\Omega\mu|j'\Omega'\rangle
{R^{std}\over\sqrt{2j'+1}},
\]
\[
\boxed{R^{std}=\sqrt{2j'+1}\;r^{LL}}.
\]

后一换算是**本任务根据A2所作的归一桥**，不是作者另印一条B定义。λ=0、同l/j的极限给rLL=1/√4π，而standard R=√(2j+1)/√4π，符合Y00的普通ME；这是定义层检查，不是核数据测试。不能只看double-bar字样就默认与041标准RME等值，也不把此角基约定直接指定为2022 PROBMO actual header。

## A7：体积定标是额外历史合同

PDF20 A7前句明确“ω0/ω0° is obtained from the volume conservation condition”。令b_i同A1，D为A7印出的角多项式，可写

\[
\left({\omega_0\over\omega_0^\circ}\right)^3
={1\over4\pi\sqrt{b_xb_yb_z}}
\int_0^\pi\!\int_0^{2\pi}
{\sin\theta\,d\theta d\varphi\over D(\theta,\varphi)^{3/2}},
\]
\[
D=1-\tfrac23\varepsilon\cos\gamma P_2
+\varepsilon\sin\gamma\sqrt{8\pi/45}(Y_{22}+Y_{2,-2})
+2\varepsilon_4P_4.
\]

A7的方括号同时含γ项及ε4项；不应把它无条件缩成单独的product-frequency规则。042故意没有假定volume conservation，仍是正确的一般coordinate identity；本轮新增的是**该历史方法具体怎样选择ω0**，不是要求所有coordinate stretch都采用A7。A4–A6还展示变形表面半径及physical/stretched角的转换，本任务未把这些表面公式冒作全部E2 radial矩阵。

## A8/A9：明确忽略 γ，打印同一 ν 的期望值

PDF20 A8前整句为“Transforming the single-particle quadrupole and hexadecapole matrix elements into stretched coordinates, **neglecting the γ-degree of freedom**, one readily finds that”。A8实际是

\[
q_{2\nu}=\left\langle\nu\left|
\sqrt{16\pi/5}\,r^2Y_{20}(\theta)\right|\nu\right\rangle
\]
\[
={\hbar\over m\omega_0}
{1\over(1+\varepsilon/3)(1-2\varepsilon/3)}
\left[\left\langle\nu\left|
\sqrt{16\pi/5}\,\rho^2Y_{20}(\theta_t)\right|\nu\right\rangle
+{2\varepsilon\over3}\langle\nu|\rho^2|\nu\rangle\right].
\]

两边所有bra/ket都是**同一ν，没有ν′**；q2ν下标是态标签。A9同样定义q4ν=〈ν|r⁴Y40(θ)|ν〉并给stretched展开；它的physical prefactor为[ℏ/(mω0)]²/[(1+ε/3)²(1−2ε/3)²]，内含ρ⁴Y40、ρ⁴Y20与ρ⁴的同态期望。A10给ρ²=ξ²+η²+ζ²；紧接文字说|ν〉为MO Hamiltonian对角化所得本征态。因此这些式子没有提供本次所需的实际signed ν系数或任意ν′ν、μ的数字矩阵。

**与041相接：**A8现在直接证实这个特定q2ν采用Q-like `O20=√(16π/5)r²Y20=2z²−x²−y²`，不是bare标准球谐q20。该历史0分量识别不再仅是条件猜测；仍没有从A8得到q22或完整tesseral库，也不证明L78/2022每个q字段自动沿用它。

**与042相接的任务代数核：**忽略γ后的轴向情形取p=1+ε/3、s=1−2ε/3，A1给x=ℓ0ξ/√p、y=ℓ0η/√p、z=ℓ0ζ/√s。于是pointwise

\[
2z^2-x^2-y^2
={\ell_0^2\over ps}
\left[(2\zeta^2-\xi^2-\eta^2)
+\tfrac23\varepsilon(\xi^2+\eta^2+\zeta^2)\right],
\]

正好给A8的ρ²附加项与length²尺度。这项不是物理E0混入；042已说明ordinary stretched scalar不等physical旋转scalar。该pointwise identity可在**同一固定stretch、相同内积**下对任意bra/ket取矩阵元；但这个一般化是任务推导，不能反写成A8实际印了off-diagonal式。A8本身没有恢复042全三轴五分量，后者仍应标task-derived。

## Eq10–12与Table1：Q0和Q40并非同一归一

PDF6/printed98实际定义

\[
Q_0=\sqrt{16\pi/5}\left\langle\Phi\left|
\sum_{p=1}^{Z}r_p^2Y_{20}(\Omega_p)\right|\Phi\right\rangle,
\qquad
Q_{40}=Z^{-1}\left\langle\Phi\left|
\sum_{p=1}^{Z}r_p^4Y_{40}(\Omega_p)\right|\Phi\right\rangle.
\]

Q0是总proton Q-like sum；Q40**显式除Z**，且没有Q0的球谐缩放。Eq12通过rotational-model CG及B(E2)推|Q0|，因而仅B(E2)不定其sign。不要因同叫Q就合并单位/归一，或把这些静态内禀moments称特定pair的transition RME。

PDF7/printed99 Table1标题为ground states的theoretical charge intrinsic quadrupole/hexadecapole moments；Theory有本工作micr./macr.、两种HF，Experiment分B(E2)、(e,e′)、(α,α′)。实际表头为**Q0 (fm²)**及**Q40 (fm⁴)**，不是e²b²的B表。表下注明microscopic波函数计算的ℏω0°=41 A^−1/3 MeV及macro charged-liquid-drop r0=1.2fm；它们是该历史表的单位/输入说明，不迁成133Ce实际参数。本文对照模型和由同一experimental observable转换的moment，也不都算新增独立实验。

## 对133Ce operator缺口的最终分层

| 字段 | 本轮状态 | 仍不能声称 |
|---|---|---|
|Ref23身份与真实body|21页hash与定向原读已关闭|1975的所有PES/原文全部被本单元审计|
|历史stretch与length²|A1 dimensionless、ω0/ω0°区别及A7体积约定已读|WK22实际选用同一频率/伸缩/ε映射|
|angular matrix-element归一|A2/A3一般角ME；明确CG形式，与standard RME的√(2j′+1)桥已给|actual PROBMO输出采用此历史double-bar归一|
|轴向diagonal q20|A8直接Q-like定义，γ忽略与ρ²项已闭合；与042轴向恒等式一致|A8是全三轴q2μ或已给q22、ν′ν transition matrices|
|general pointwise五分量|042已闭合，现有历史coordinate对应|历史原件逐字印出了042全部表达|
|radial/basis/signed input|仍缺当前实际数值与producer|完整GAMPN→ASYMO→PROBMO复跑、Ce B/δ/能谱预测|

建议canonical把“Ref23未读”改成明确日期/本scope的原读状态，并保留“该原件A8/A9仅给neglectγ的同态公式，不是完整q library”的独立缺口。任何一般off-diagonal extension、standard-RME换算或五分量推导都继续标任务代数。无新核计算、假数据、拟合或学分；只写043 worker与tmp，canonical/raw/PLAN/Bib/Git/session不动。

附：methodsPDF4 Eq8的ε5处方第二系数扫描残损，本单元放大后仍不据OCR定字；已向044报告该边界。本任务的A1/A2/A3/A7/A8/单位结论不依赖该系数。
