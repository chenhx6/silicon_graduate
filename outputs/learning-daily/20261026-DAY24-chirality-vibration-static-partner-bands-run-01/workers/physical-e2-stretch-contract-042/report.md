# 042：指定伸缩下 physical E2 的五分量坐标恒等式

**可关闭明确约定下的几何转换缺口。** 现有LLR78-D24-008只给physical j/stretched l的桥并将single-particle q2μ指向Ref23；RS88-02强调physical算符与stretched basis不同；133Ce蓝本保留该operator缺口。这三处没有以下显式字典。因此本单元有窄增量，证据类型是**task-derived coordinate identity**，不是1975 Ref23原读、历史代码重建或Ce模型结果。本推导不依赖新下载；SI范围问题尚待回复，1975原件未取得/未读。

## 约定与对象

取右手physical坐标(x,y,z)，Condon–Shortley复球谐，定义单粒子几何算符

\[
q_{2\mu}=r^2Y_{2\mu}(\widehat{\boldsymbol r}),\qquad
A=\sqrt{5/(16\pi)},\quad B=\sqrt{15/(8\pi)},\quad C=\sqrt{15/(32\pi)}.
\]

q的量纲是length²；本单元**未包含有效电荷**。若物理电算符采用e_eff q，其量纲为charge·length²；历史文献或程序若用不同球谐/四极归一，还需显式桥接。

严格选定dimensionful stretch

\[
X=x_x^t=\sqrt{\omega_x/\omega_0}\,x,\quad
Y=\sqrt{\omega_y/\omega_0}\,y,\quad
Z=\sqrt{\omega_z/\omega_0}\,z,\qquad\omega_i,\omega_0>0.
\]

令a_i=ω0/ωi、d_i=√a_i，故x=d_xX、y=d_yY、z=d_zZ；X/Y/Z仍有length量纲。没有假定volume conservation、某核形变参数或ω0等于频率几何平均。其它stretch（例如double stretch）不在此合同内。

## 五个 pointwise 分量

只将physical Cartesian形式逐轴代入，得到

\[
q_{20}=A(2a_zZ^2-a_xX^2-a_yY^2),
\]
\[
q_{2,+1}=-B d_zZ(d_xX+i d_yY),\qquad
q_{2,-1}=+B d_zZ(d_xX-i d_yY),
\]
\[
q_{2,+2}=C(d_xX+i d_yY)^2,\qquad
q_{2,-2}=C(d_xX-i d_yY)^2.
\]

这是乘法算符的精确坐标重写，不依赖HO截断、配对或波函数。它不自动给出任何选定basis的积分矩阵元。

### 与普通 stretched 球谐及共同 r_t² 函数的字典

令r_t²=X²+Y²+Z²，并定义t_μ=r_t²Y2μ(X/r_t)，即将上述physical公式中的全部d设1。定义

\[
\alpha=(4a_z+a_x+a_y)/6,\qquad
\gamma=(2a_z-a_x-a_y)/3,
\]
\[
u=(a_x+a_y+2d_xd_y)/4,\qquad
v=(a_x+a_y-2d_xd_y)/4.
\]

完整字典为

\[
q_{20}=\alpha t_0+{a_y-a_x\over2\sqrt6}(t_{+2}+t_{-2})+A\gamma r_t^2,
\]
\[
q_{2,\pm1}={d_z\over2}\big[(d_x+d_y)t_{\pm1}-(d_x-d_y)t_{\mp1}\big],
\]
\[
q_{2,\pm2}=u t_{\pm2}+v t_{\mp2}
-{a_x-a_y\over2\sqrt6}t_0
+{C(a_x-a_y)\over3}r_t^2.
\]

这里共同的是**同一个函数r_t²**，不是五分量都加同一个常数。q20的系数是Aγ，q2±2各为C(ax−ay)/3，q2±1为零。ordinary stretched trace的出现，不表示physical E2混入物理E0；也不能删掉trace项以强行让q成为L^t下的pure rank2。

## 为什么必须使用 physical L

按链式法则，physical轨道生成元为（i,j,k循环）

\[
L_i=-i\hbar\left[{d_j\over d_k}X_j\partial_{X_k}
-{d_k\over d_j}X_k\partial_{X_j}\right]
=-i\hbar\left[\sqrt{\omega_k/\omega_j}X_j\partial_{X_k}
-\sqrt{\omega_j/\omega_k}X_k\partial_{X_j}\right].
\]

L_i^t则把两个比值都设1。仅在对应两轴频率相等时，某一分量Li才等于Li^t；一般不能以L^t代替L。特别

\[
L_z={u_z+u_z^{-1}\over2}L_z^t
+{u_z-u_z^{-1}\over2}F_z^t,
\quad u_z=\sqrt{\omega_y/\omega_x},\quad
F_z^t=-i\hbar(X\partial_Y+Y\partial_X).
\]

这与LLR78已有jz桥的结构一致；这里是对所声明stretch独立链式推导，未据此认领其全部相位/程序约定。

因为这是同一个physical坐标算符与生成元的可逆重写，

\[
[L_z,q_{2\mu}]=\hbar\mu q_{2\mu},\qquad
[L_\pm,q_{2\mu}]=\hbar\sqrt{(2\mp\mu)(3\pm\mu)}q_{2,\mu\pm1}.
\]

`verify_coordinate_identity.py`在任意正d_i的符号Laurent多项式上直接核这些微分恒等式与五分量字典，没有采样核参数。伸缩后旋转作用是X→S R S⁻¹X，而非普通X→R X；这也是两套生成元不同的几何原因。spin与这些坐标乘法算符对易，故若加上独立spin，physical j=L+s下仍有相同tensor关系。

最直接的trace检验是

\[
[L_i,r_t^2]=-2i\hbar\left({d_j\over d_k}-{d_k\over d_j}\right)X_jX_k,
\]

一般非零。相反physical scalar r²=Σa_iX_i²与全部physical L对易。physical q仍满足∇r²q=0；换坐标后是Σa_i⁻¹∂Xi²q=0，**不是**普通∇t²q=0。这说明伸缩球谐分解里的trace只是坐标效应。

## dimensionless ξ 的 length² 字典

若ξ_i=√(mω_i/ℏ)x_i，令ℓ_i=√(ℏ/(mω_i))、ℓ0=√(ℏ/(mω0))，则

\[
x_i=\ell_i\xi_i,\qquad X_i=\ell_0\xi_i,\qquad\ell_i^2=\ell_0^2a_i.
\]

因此五分量为

\[
q_{20}=A(2\ell_z^2\xi_z^2-\ell_x^2\xi_x^2-\ell_y^2\xi_y^2),
\]
\[
q_{2,\pm1}=\mp B\ell_z\xi_z(\ell_x\xi_x\pm i\ell_y\xi_y),\qquad
q_{2,\pm2}=C(\ell_x\xi_x\pm i\ell_y\xi_y)^2.
\]

等价地在dimensionful字典中代X_i=ℓ0ξ_i，整个几何算符带ℓ0²。不能把dimensionless ξ二次式的数值直接标作fm²或b；length²转barn还需声明长度单位（1 b=100 fm²），charge及B(E2)平方单位另行处理。m是本坐标定义指定的质量参数，不自行选本核effective mass。

## 厄米性、轴对称与球形极限

- 正实ω使d、ℓ均实，逐点复共轭给q2μ†=(−1)^μq2,−μ；尤其q20实，q+1†=−q−1、q+2†=q−2。在physical内积下，Jacobian为常数d_xd_yd_z；正规化变换或保留此权重均不改变该伴随关系。不可从这一点声称实际截断basis的矩阵已审计。
- ωx=ωy=ω⊥时，令a⊥=ω0/ω⊥：q±2=a⊥t±2，q±1=√(az a⊥)t±1，q20=(2az+a⊥)t0/3+2A(az−a⊥)r_t²/3。Lz=Lz^t，μ轴标签相容；若ωz不同，完整physical L仍不等L^t，q20的r_t²项仍必需。
- ωx=ωy=ωz=ωs时，a_i=a，所有qμ=a tμ，scalar admixture及±μ混合消失，physical L=L^t。若再令ωs=ω0，直接q=t；dimensionless形式共同length²为ℏ/(mωs)。无需假定某个实际Ce频率来取得这些极限。

## 能关闭什么，仍缺什么

已关闭：**上述明确stretch、右手轴与球谐约定下**，五个physical r²Y2μ的pointwise转换、r_t² trace来源、dimensionless length²桥及physical tensor/Hermitian/退化恒等式。没有保留为需等1975下载才能进行的几何推导。

仍缺：1975 Ref23实际文本与历史归一/轴/相位；GAMPN→ASYMO→PROBMO使用的具体stretch、单位、有效电荷、径向HO矩阵及截断basis、 signed eigenvectors与实际RME。坐标恒等式不能单独关闭这些producer缺口，也不给Ce能谱、B、δ或新模型预测。LLR78/RS88原direct-source claims保持原证据层级，不能把本推导倒填为它们直接印出的公式。

仅写042目录。canonical/raw/PLAN/Bib/Git、课程学分与session状态未动；仍本Day24及恰好Day25未计分预习。
