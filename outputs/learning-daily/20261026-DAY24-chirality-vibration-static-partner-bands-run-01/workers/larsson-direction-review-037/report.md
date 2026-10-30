# L78 A2：反向 RME 的共同相位可闭合

**结论：root提出的条件推导正确。** 在标准3j形式的Wigner–Eckart约定、两种物理球张量均满足同一Hermitian adjoint约定、同一对初末态与一致态相位下，反向E2/M1的RME比只是正向比的复共轭。实RME约定下该比不变；对L78 A2的ΔI1，两种rank各自都有同一个负号，故不会额外改变δ的符号。历史公式的这一方向代数问题可以关闭，不必留成“永远方向未核”。

本单元只核已有数学与L78原A2，没有新paper、网络、数值toy、actual producer或模式结论。新表述为条件self-audit，`needs_review:true`；不改canonical/raw/Git/信用。

## 原件定位

L78实际文件`raw/papers/1-s2.0-0375947478906139-main.pdf`，35页，SHA256本轮重核为`108c29bed9de467d99f330c0b8cef47be82a290263a85e398ba3b4f2e97d77eb`。本次仅读/视觉PDF32、printed220的A1–A4和周围文字；不冒称重读整篇。

A1采用B(Oλ;Ii→If)=abs(〈If||M(Oλ)||Ii〉)²/(2Ii+1)。A2字面用〈I||M(E2)||I−1〉/〈I||M(M1)||I−1〉，即RME顺序为从I−1到I。`pdf32.png`与`A2-crop.png`保存原页/局部；方向讨论不改原式的正Eγ因子或单位。

## 有限推导

固定标准定义

\[
\langle f I_fM_f|T_{\lambda q}|i I_iM_i\rangle
=(-1)^{I_f-M_f}
\begin{pmatrix}I_f&\lambda&I_i\\-M_f&q&M_i\end{pmatrix}
\langle f I_f\Vert T_\lambda\Vert i I_i\rangle,
\]

并要求物理Hermitian球张量满足

\[
T_{\lambda q}^{\dagger}=(-1)^qT_{\lambda,-q}.
\]

将普通矩阵元反向、复共轭，再用3j的列交换和全磁量子数反号对称（两次相同的rank相关相位相消），得到

\[
\boxed{
\langle f I_f\Vert T_\lambda\Vert i I_i\rangle
=(-1)^{I_f-I_i}
\langle i I_i\Vert T_\lambda\Vert f I_f\rangle^* .}
\]

相位不依赖λ。磁张量在时间反演下time-odd，并不意味着它是anti-Hermitian；不能因此给M1另加一个反向负号。若实现先给某rank的张量人为乘i或采用不同的adjoint/WE归一，则须先转换到上述约定，不能直接套这个结论。

令Rλ↑=〈I||Mλ||I−1〉、Rλ↓=〈I−1||Mλ||I〉。两者都对应同一组核态，取同一套算符与相位约定，则

\[
R_{E2}^{\downarrow}=-R_{E2}^{\uparrow *},\qquad
R_{M1}^{\downarrow}=-R_{M1}^{\uparrow *},
\]
\[
\boxed{
\frac{R_{E2}^{\downarrow}}{R_{M1}^{\downarrow}}
=\left(\frac{R_{E2}^{\uparrow}}{R_{M1}^{\uparrow}}\right)^* .}
\]

分母非零时成立；M1振幅为零的pure-E2极限不能用有限比值表达。若采用同一实、正的辐射能量幅度因子κ(Eγ)，以同一个正的物理跃迁能量Eγ而非人为负“吸收能”定义δ，则δ↓=δ↑*；在实signed-RME约定中δ↓=δ↑。这不是对不同论文或不同multipole convention的无条件等号。

单个B的方向则有统计权重差：

\[
B(O\lambda;I_i\to I_f)
=\frac{2I_f+1}{2I_i+1}B(O\lambda;I_f\to I_i).
\]

因此不能从“E2/M1比的共同相位相消”进一步说单个反向B相等。两种multipole若绑定同一Ii/If，则该统计权重在它们的B比中也相消。

## 关闭与保留的边界

- **可关闭：**按上述标准约定，L78 A2使用upward-order RME本身不会在real E2/M1比中造成一个额外相对负号。032此前“需核Hermitian/WE”这一具体数学核验现已完成；保留原页顺序即可，无须继续把它当未解科学问题。
- **仍未认证：**WK22单/双竖线究竟消费full或reducedME；M1 moment operator与transition operator的√(3/4π)等归一；E2/磁矩/能量的eb、μN、MeV单位；所用radiation/emissionδ与电磁多极相位约定；GAMPN/ASYMO/PROBMO实际版本、header、输入/输出和signed numericalRME。以上均不能由共同Hermitian相位相消推定已相同。

本推导只消除一个可由定义闭合的方向疑点，不改变历史source数值、不重写真实δ测量、不认证2022实际工作流。保存后即停止此有界审查。
