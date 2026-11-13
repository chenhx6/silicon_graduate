import hashlib

content = r'''\section{$A\approx 130$、稀土与重区的取向对照}\label{sec:4-4}

在前述章节中，我们系统建立了原子核非轴对称形变与转动运动的微观响应与宏观表象：在第\ref{sec:2-6}节中，推演了微观转动惯量对空间形变坐标 $(\beta, \gamma)$、超流配对以及四极场的动力学响应，阐明微观惯量受单粒子结构与配对微商调控，既非纯粹无旋流体亦非简单刚体，其数值可能位于两者包络之内，亦可在特定推转频率下超出该范围；在第\ref{sec:3-2}节中，推演了三轴刚体转子绕主惯量轴的小振幅微扰摆动几何；在第\ref{sec:3-3}节与第\ref{sec:3-6}节中，分别讨论了奇核子--转子模型中准粒子取向的动力学重塑以及取向振动与形状振动的模式耦合~\cite{book-bohr-mottelson-nuclear-structure-vol2,frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei}。当读者从孤立能带走向跨质量区的宏观谱学比较时，容易产生一种经验上的归约倾向：既然在平均场势能面计算中，不同质量区的原子核都被赋予了非零的三轴形变角 $\gamma$（或非轴对称四极不变量 $q_2, q_3$），或者在寿命测量中测得了相近的跃迁四极矩 $Q_t$，甚至其奇核子都占据了相似的高 $j$ 唯一宇称入侵轨道（如稀土区的 $\pi i_{13/2}$ 与 $A\approx 130$ 区的 $\pi h_{11/2}$），那么这些原子核在旋转时是否展现出相同机制的集体取向运动模式？

实验观测与理论模拟的发展表明，非零的三轴形变参数 $\gamma$ 或相近的跃迁四极矩 $Q_t$，并不必然唯一锁定原子核的动力学取向运动（Orientation Motion）。在稀土区（如 $^{163}\mathrm{Lu}$）的三轴超形变带中，体系表现出较为充分的横向摆动（Transverse Wobbling, TW）特征，其带间 $\Delta I = 1$ 跃迁展现出宏观的集体 $E2$ 增强；然而在 $A\approx 130$ 区（如 $^{135}\mathrm{Pr}$），最初被赋予横向摆动的低自旋带在经过严格的极化双根检验与分支比重测后，却呈现出以 $M1$ 为主的退激特征，其机制引发了平面转动（Planar Rotation）、单粒子对准重新取向、微观玻色子-费米子耦合或能带混合等多元竞争解释~\cite{lv-2022-evidence-against-wobbling-135pr,nomura-2022-questioning-wobbling-ibfm}；在 $A\approx 180$ 邻区的超铪/钨高 $K$ 转动态中，原本反映三轴摆动恢复力的横向激发序列在轴对称几何极限下平滑演化为绕对称轴的高 $K$ 进动转动带（High-$K$ Precession）~\cite{shimizu-2005-high-k-precession}；而在更重的金/铂/汞区（如 $^{187}\mathrm{Au}$ 与 $^{190}\mathrm{Hg}$），原子核又涉及三轴软度、扁椭球演化以及多重形状共存的复杂竞争~\cite{guo-2022-low-spin-wobbling-187au}。

同一个描述粒子--转子耦合的哈密顿量，为何会在不同核区诱导出横向摆动、纵向摆动、高 $K$ 进动以及平面转动等截然不同的动力学表现？决定取向运动稳定与失稳的微观控制机制究竟是什么？作为比较章节，本节将重点聚焦于跨核区取向动力学的物理对照：第\ref{sec:4-4-1}小节在统一约定下严格推导电荷空间几何半轴的相对尺度，显式建立几何轴与局部冻结顺排（FA）坐标系的置换映射，解构惯量主轴排序、准粒子对准趋势以及摆动模式的模型内定义；第\ref{sec:4-4-2}小节基于 $^{163}\mathrm{Lu}$ 的实测原表数据，确立经典三轴超形变摆动的实验证据与采用量依赖边界；第\ref{sec:4-4-3}小节剖析 $A\approx 130$ 区围绕 $^{135}\mathrm{Pr}$ 展开的在束角分布代数多义性、能级分支比检验与多元微观模型竞争；第\ref{sec:4-4-4}小节阐述轴对称高 $K$ 进动作为摆动运动的几何退化边界，澄清参考系频率关系与首间距微商，并探讨重区 $^{187}\mathrm{Au}$ 的实验检验与形状共存演化；第\ref{sec:4-4-5}小节提炼取向运动跨区迁移的物理条件与失效机制，系统辨析物理不变量与微观模型参数的映射边界。图~\ref{fig:4-4-orientation-modes}给出了 $^{163}\mathrm{Lu}$ 的实测原表数据、带间 $B(E2)$ 集体增强判定与跨核区取向对准几何示意图。

\begin{figure}[!htbp]
\centering
\includegraphics[width=\textwidth]{Img/orientation-comparison-modes.pdf}
\caption{跨核区典型非轴对称取向动力学模式对比：(a) $^{163}\mathrm{Lu}$ 带内跃迁四极矩 $Q_t$ 实测数据分布（取自 Görgen 2004 Table I）；(b) $^{163}\mathrm{Lu}$ TSD2 向 TSD1 带间连接跃迁 $B(E2)$ 强度及集体增强判定（取自 Görgen 2004 Table II）；(c) 横向摆动（TW）、轴对称高 $K$ 进动以及平面转动/重对准三类典型取向模式的几何与角动量配置示意图。}\label{fig:4-4-orientation-modes}
\end{figure}

\subsection{取向自由度、主轴惯量排序与准粒子对准几何}\label{sec:4-4-1}

为了在同一物理约定下跨越不同质量区比较取向运动，首先必须严格厘清电荷空间几何主轴与转动惯量主轴的物理分离，显式给出几何坐标与动力学展开坐标的映射关系，并从微观壳层驱动力出发明确准粒子取向的对准机制。

\subsubsection{电荷几何主轴与转动惯量主轴的物理分离}

在内禀参考系中，非轴对称变形核的电荷表面在小形变近似展开下由形变参数 $\beta_2$ 与三轴不对称角 $\gamma$ 描述。在标准的 Lund 约定下，空间电荷几何半径的三轴标度为：
\begin{equation}\label{eq:4-4-radii-def}
R_k = R_0 \left[ 1 + \sqrt{\frac{5}{4\pi}}\beta_2 \cos\left(\gamma - \frac{2\pi}{3} k\right) \right], \qquad k = 1, 2, 3.
\end{equation}
为了严格确定三个几何主轴的相对尺度，令无量纲形变因子 $a \equiv \sqrt{\frac{5}{4\pi}}\beta_2 > 0$。在标准三轴扇区 $0^\circ < \gamma < 60^\circ$ 内，逐一考察式~\eqref{eq:4-4-radii-def} 中的余弦因子：
\begin{itemize}
\item 对于 $k=1$：$\cos\left(\gamma - \frac{2\pi}{3}\right) = \cos\left(120^\circ - \gamma\right)$。由于 $0^\circ < \gamma < 60^\circ$，其自变量满足 $60^\circ < 120^\circ - \gamma < 120^\circ$，因此 $\cos\left(\gamma - \frac{2\pi}{3}\right) \in \left(-\frac{1}{2}, \frac{1}{2}\right)$；
\item 对于 $k=2$：$\cos\left(\gamma - \frac{4\pi}{3}\right) = \cos\left(240^\circ - \gamma\right) = \cos\left(120^\circ + \gamma\right)$。其自变量满足 $120^\circ < 120^\circ + \gamma < 180^\circ$，因此该因子在全扇区恒取负值且满足 $\cos\left(\gamma - \frac{4\pi}{3}\right) \in \left(-1, -\frac{1}{2}\right)$；
\item 对于 $k=3$：$\cos\left(\gamma - 2\pi\right) = \cos\gamma$。其自变量满足 $0^\circ < \gamma < 60^\circ$，该因子恒取正值且满足 $\cos\gamma \in \left(\frac{1}{2}, 1\right)$。
\end{itemize}
比较上述三个区间的取值，可知在整个标准三轴扇区 $0^\circ < \gamma < 60^\circ$ 内，三角因子严格满足单调偏序：
\begin{equation}\label{eq:4-4-cos-order}
\cos\left(\gamma - \frac{4\pi}{3}\right) < \cos\left(\gamma - \frac{2\pi}{3}\right) < \cos\gamma.
\end{equation}
将式~\eqref{eq:4-4-cos-order} 代回半径定义式~\eqref{eq:4-4-radii-def}，直接导出核物质几何半径的大小排序：
\begin{equation}\label{eq:4-4-radii-order}
R_2 < R_1 < R_3.
\end{equation}
式~\eqref{eq:4-4-radii-order} 表明：在标准的玻尔—莫特森与 Lund 约定下，空间电荷几何主轴与直角坐标轴的对应关系为：
\begin{equation}\label{eq:4-4-axes-identity}
\text{最短几何轴 (short, $s$ 轴)} \iff k = 2; \quad
\text{中间几何轴 (intermediate, $m$ 轴)} \iff k = 1; \quad
\text{最长几何轴 (long, $l$ 轴)} \iff k = 3.
\end{equation}
在轴对称长椭极限 $\gamma \to 0^\circ$ 处，$\cos(-120^\circ) = \cos(-240^\circ) = -1/2$，导出 $R_1 = R_2 = R_0(1 - a/2) < R_3 = R_0(1+a)$（3轴为长椭旋转对称轴）；而在轴对称扁椭极限 $\gamma \to 60^\circ$ 处，$\cos(-60^\circ) = \cos(60^\circ) = 1/2$，$\cos(-180^\circ) = -1$，导出 $R_2 = R_0(1-a) < R_1 = R_3 = R_0(1+a/2)$（2轴为扁椭旋转对称轴）。这一逐式推导确立了主轴尺度几何关系，与第\ref{chap:2}章及第\ref{sec:3-2}节的主轴体系保持严格统一。

电荷几何半轴的大小排序，并不等同于核转动惯量张量的主轴排序。在核多体动力学中，转动惯量深刻受制于质量传输机制：
\begin{enumerate}
\item \textbf{经典刚体转动惯量}：绕第 $k$ 主轴的刚体惯量由垂直于该轴的物质密度二阶矩决定，即 $\mathcal{J}_k^{\text{rig}} = \int \rho(\mathbf{r}) (r^2 - x_k^2) d^3r \propto R_i^2 + R_j^2$（$i \ne j \ne k$）。根据几何半径不等式~\eqref{eq:4-4-radii-order}，由两较大半轴决定的惯量最大，因此刚体模型预言：绕最短几何轴 $s$（$k=2$）的转动惯量最大，绕最长几何轴 $l$（$k=3$）的转动惯量最小：
\begin{equation}\label{eq:4-4-rigid-order}
\mathcal{J}_2^{\text{rig}} > \mathcal{J}_1^{\text{rig}} > \mathcal{J}_3^{\text{rig}} \iff \mathcal{J}_s^{\text{rig}} > \mathcal{J}_m^{\text{rig}} > \mathcal{J}_l^{\text{rig}}.
\end{equation}
\item \textbf{无旋流体转动惯量}：在玻尔无旋流体模型中，惯量表达式为 $\mathcal{J}_k^{\text{irr}} = 4 B \beta^2 \sin^2\left(\gamma - \frac{2\pi}{3} k\right)$。在 $\gamma = 30^\circ$ 处，$\sin^2(-90^\circ) = 1$（$k=1$），而 $\sin^2(150^\circ) = \sin^2(30^\circ) = 1/4$（$k=2, 3$）。无旋流模型预言：绕中间几何轴 $m$（$k=1$）的转动惯量最大：
\begin{equation}\label{eq:4-4-irrot-order}
\mathcal{J}_1^{\text{irr}} > \mathcal{J}_2^{\text{irr}}, \mathcal{J}_3^{\text{irr}} \iff \mathcal{J}_m^{\text{irr}} > \mathcal{J}_s^{\text{irr}}, \mathcal{J}_l^{\text{irr}}.
\end{equation}
当 $0^\circ < \gamma < 30^\circ$ 时，$\mathcal{J}_1 > \mathcal{J}_2 > \mathcal{J}_3$；在 $\gamma = 30^\circ$ 处 $\mathcal{J}_2 = \mathcal{J}_3$；当 $30^\circ < \gamma < 60^\circ$ 时则演化为 $\mathcal{J}_1 > \mathcal{J}_3 > \mathcal{J}_2$。
\item \textbf{微观动态惯量响应}：在真实原子核中，由于费米子单粒子结构与残余配对关联，有效惯量张量并不必然处于刚体与无旋流的静态包络内，而是可以表现出显著的自洽转动角频率依赖性 $\mathcal{J}_k(\omega)$（如第\ref{sec:2-6}节与第\ref{sec:3-3}节所述，Matsuzaki 等人 2004）~\cite{matsuzaki-2004-nuclear-inertia-and-wobbling}。
\end{enumerate}

\subsubsection{准粒子取向趋势、局部动力学坐标置换与横向/纵向摆动模型边界}

奇 $A$ 核与多准粒子激发态的取向运动，由未配对价准粒子的内禀角动量 $\mathbf{j}$ 与变形核芯集体角动量 $\mathbf{R}$ 的矢量相加 $\mathbf{I} = \mathbf{R} + \mathbf{j}$ 决定。在变形平均场中，单粒子轨道受到各向异性四极驱动势的作用：
\begin{itemize}
\item \textbf{粒子型准粒子（处于子壳层底部）}：
费米面位于子壳层底部时，低 $\Omega$ 轨道优先被占据。核子波函数密度呈现沿内禀对称轴拉长的形态，为最大化与核芯三轴物质的重叠以降低体系能量，准粒子角动量 $\mathbf{j}$ 在模型势能面极小处倾向于\textbf{对准最短几何轴（$s$ 轴，即 $k=2$ 轴）}（如 $^{163}\mathrm{Lu}$ 的 $\pi i_{13/2}$ 壳底态以及 $^{187}\mathrm{Au}$ 的 $\pi h_{9/2}$ 态）。
\item \textbf{空穴型准粒子（处于子壳层顶端）}：
费米面靠近子壳层顶端时，高 $\Omega$ 轨道被占据，核子波函数呈现扁椭形态。为最小化与核芯物质的排斥势能，有效空穴角动量优先\textbf{对准最长几何轴（$l$ 轴，即 $k=3$ 轴）}。
\item \textbf{半满壳准粒子}：
费米面处于壳层中段时，准粒子倾向于在中间几何轴（$m$ 轴，即 $k=1$ 轴）方向形成主要的对准分量。
\end{itemize}

在 Frauendorf 与 Dönau（2014）的粒子--转子模型（PRM）框架下，横向摆动（TW）与纵向摆动（LW）具有严格的几何定义~\cite{frauendorf-2014-transverse-wobbling}：
\begin{enumerate}
\item \textbf{横向摆动（TW）}：准粒子角动量 $\mathbf{j}$ 的优势取向垂直于核芯所具有的最大转动惯量轴。在典型的类无旋流排序下，核芯最大惯量轴为中间轴 $m$（$k=1$），而壳底粒子型准粒子对准最短轴 $s$（$k=2$）。由于 $s \perp m$，准粒子与最大转动惯量轴在空间相互垂直，核芯绕中轴高速旋转，总角动量矢量偏离中轴发生微扰进动，构成横向摆动。
\item \textbf{纵向摆动（LW）}：准粒子角动量 $\mathbf{j}$ 与核芯最大转动惯量轴共线平行。若模型中核芯最大转动惯量依然沿中轴 $m$，则 LW 要求奇核子亦对准中轴。
\end{enumerate}

\textbf{坐标置换与第\ref{sec:3-3}节冻结顺排（FA）公式的精确映射}：
必须注意，式~\eqref{eq:4-4-axes-identity} 给出的电荷几何主轴指标为 $k_1 = m, k_2 = s, k_3 = l$；而第\ref{sec:3-3}节在推导冻结顺排（FA）小振幅频率时，采用的局部动力学指标约定为：局部轴 1 沿冻结顺排准粒子方向，局部轴 2 沿核芯最大转动惯量轴，局部轴 3 沿剩余横向轴。在所讨论的横向摆动（TW）情形中，准粒子对准几何短轴 $s$（$k=2$），核芯最大惯量在中轴 $m$（$k=1$）。为了避免数字下标混淆，我们显式采用几何主轴指标 $(s, m, l)$ 重写相应的动力学恢复力曲率与能谱参数。相应的转动常数定义为 $A_s = \frac{\hbar^2}{2\mathcal{J}_s}, A_m = \frac{\hbar^2}{2\mathcal{J}_m}, A_l = \frac{\hbar^2}{2\mathcal{J}_l}$。有效转动常数表示为：
\begin{equation}\label{eq:4-4-A-s-bar}
\bar{A}_s \equiv A_s \left( 1 - \frac{j}{I} \right).
\end{equation}
两个横向恢复力曲率分别沿中轴 $m$ 与长轴 $l$ 展开：
\begin{equation}\label{eq:4-4-curvatures-sml}
C_m = (A_m - A_s) + A_s \frac{j}{I}, \qquad C_l = (A_l - A_s) + A_s \frac{j}{I}.
\end{equation}
定义曲率差参数 $a_m \equiv A_m - A_s$ 与 $a_l \equiv A_l - A_s$。在类无旋流排序下，$\mathcal{J}_m > \mathcal{J}_s \ge \mathcal{J}_l \implies A_m < A_s \le A_l$，因此 $a_m < 0$ 而 $a_l \ge 0$。小振幅简谐摆动激发频率表示为：
\begin{equation}\label{eq:4-4-wob-freq-sml}
\hbar\omega_{\text{wob}} = 2I\sqrt{C_m C_l} = 2\sqrt{\left( a_m I + A_s j \right) \left( a_l I + A_s j \right)}.
\end{equation}
相应的临界分叉自旋为中轴曲率 $C_m(I_c) = 0$ 处：
\begin{equation}\label{eq:4-4-critical-spin-sml}
I_c = \frac{j}{1 - A_m / A_s} = \frac{j}{1 - \mathcal{J}_s / \mathcal{J}_m}.
\end{equation}

\textbf{微观机制与理论边界辨析}：必须强调第\ref{sec:3-2}、\ref{sec:3-3}与\ref{sec:3-6}节建立的物理约束：
\begin{itemize}
\item \textbf{摆动能量的非单调性演化}：在式~\eqref{eq:4-4-wob-freq-sml} 中，由于 $a_m < 0$ 而 $a_l \ge 0$，因子 $(a_m I + A_s j)$ 随自旋线性下降，而因子 $(a_l I + A_s j)$ 随自旋线性上升。在低自旋区间，两因子的乘积完全可能呈现\textbf{先上升后下降}的非单调演化。因此，实验上测得有效摆动能量随自旋下降，仅能作为支持横向对准模型的条件性线索，绝对不能作为判定 TW 成立的排他性充要条件；反之，若在特定自旋段观察到能量轻微上升，亦不能据此单方面否定摆动机制。
\item \textbf{能量极小与线性动力学稳定性的区别}：在转动坐标系哈密顿体系中，若两个横向二次系数同时为正（$C_m > 0$ 且 $C_l > 0$），参考态处于定域能量曲面的严格极小值点，小振幅微扰构成良定义的正能声子激发基态。若 $C_m < 0$ 且 $C_l < 0$，乘积 $C_m C_l > 0$ 虽在形式上给出实数频率特征值，且该处作为能量极大值点在陀螺科里奥利力作用下可具备线性动力学稳定性（类似于经典刚体绕最小惯量轴转动在能量极大处依然保持线性稳定，见本知识库 `a130-rewrite-wobbling-local-limits-20261113.md`），但在物理上它对应能量曲面的极大，不能作为低能集体声子激发的稳定真空。
\item \textbf{临界分叉自旋 $I_c$ 的适用范围}：式~\eqref{eq:4-4-critical-spin-sml} 导出的 $I_c$ 严格依赖于准粒子角动量刚性冻结为 $j$ 的强定域近似以及特定的常数惯量排序。在真实原子核中，随着转动频率增加，科里奥利力迫使准粒子偏离短轴向旋转轴倾斜，有效对准投影发生动态演化，不能把常数 $I_c$ 当作全微观体系的严格相变点。
\item \textbf{倾斜转动（Tilt）不自动蕴含空间手征性破缺}：角动量矢量偏离主惯量转轴并发生倾斜（Tilted Axis Rotation），并不等价于手征对称性破缺。若总角动量矢量的倾斜轨迹完全局限在三个几何主平面之一（例如 $s-m$ 平面或 $l-m$ 平面内的平面倾斜），系统对特定主轴反演与时间反演的复合操作 $\mathcal{T}\mathcal{R}_k(\pi)$ 依然保持对称，体系不具备手征性；只有当角动量在三个主轴上同时具备非零分量、破坏全部离散反转对称性时，才构成手征双重带物理条件（详见第\ref{sec:3-5}节与第\ref{sec:4-5}节）。
\end{itemize}

\subsection{经典三轴超形变摆动基准：$^{163}\mathrm{Lu}$ 的实测数据分析}\label{sec:4-4-2}

稀土区奇 $A$ 核素 $^{163}\mathrm{Lu}$（以及同位素 $^{165,167}\mathrm{Lu}$）的三轴超形变带（Triaxial Superdeformed, TSD），是核物理实验中多角度符合测量数据较为完备的摆动运动参照基准~\cite{odegard-2001-evidence-wobbling-163lu,jensen-2002-second-phonon-wobbling-163lu,campaign-g07-gorgen-2004-163lu-quadrupole-moments}。

\subsubsection{Görgen 2004 实验原表与跃迁强度数据}

Görgen 等人（2004）在劳伦斯伯克利国家实验室利用 Gammasphere 探测阵列，通过多普勒频移衰减法（DSAM）测量了 $^{163}\mathrm{Lu}$ TSD1 与 TSD2 能带的高自旋能级寿命与跃迁四极矩~\cite{campaign-g07-gorgen-2004-163lu-quadrupole-moments}。表~\ref{tab:4-4-lu163-sample}汇总了其论文 Table I 与 Table II 中所报告的代表性能级测量值、带内跃迁四极矩 $Q_t$ 以及带间连接跃迁的约化跃迁几率。

\begin{table}[!htbp]
\centering
\small
\caption{$^{163}\mathrm{Lu}$ 三轴超形变带能级寿命、带内 $Q_t$ 与带间连接跃迁强度（依据 Görgen et al. 2004 Table I 与 Table II 实测原表整理）。}\label{tab:4-4-lu163-sample}
\begin{tabularx}{\textwidth}{llcccc}
\hline\hline
能带与跃迁通道 & 初态自旋 $I_i^\pi$ & 光子能量 $E_\gamma$ [keV] & 平均寿命 $\tau$ [ps] & 跃迁四极矩 $Q_t$ [b] & 跃迁几率 / 强度 \\
\hline
\textbf{TSD1} ($n_w=0$ 指派) & $41/2^+$ & 578.6 & $0.364_{-0.085}^{+0.073}$ & $9.93_{-0.99}^{+1.14}$ & $B(E2) = 3.45_{-0.69}^{+0.80}\ e^2\mathrm{b}^2$ \\
带内 $\Delta I = 2$ & $45/2^+$ & 639.0 & $0.250_{-0.039}^{+0.035}$ & $9.34_{-0.65}^{+0.72}$ & $B(E2) = 3.07_{-0.43}^{+0.48}\ e^2\mathrm{b}^2$ \\
跃迁序列 & $49/2^+$ & 697.0 & $0.202_{-0.023}^{+0.021}$ & $8.32_{-0.42}^{+0.47}$ & $B(E2) = 2.45_{-0.25}^{+0.28}\ e^2\mathrm{b}^2$ \\
& $53/2^+$ & 752.6 & $0.119_{-0.010}^{+0.009}$ & $8.93_{-0.35}^{+0.38}$ & $B(E2) = 2.84_{-0.22}^{+0.24}\ e^2\mathrm{b}^2$ \\
& $57/2^+$ & 805.6 & $0.096_{-0.012}^{+0.011}$ & $8.37_{-0.49}^{+0.54}$ & $B(E2) = 2.50_{-0.29}^{+0.32}\ e^2\mathrm{b}^2$ \\
& $61/2^+$ & 857.7 & $0.088_{-0.011}^{+0.010}$ & $7.45_{-0.43}^{+0.49}$ & $B(E2) = 1.99_{-0.23}^{+0.26}\ e^2\mathrm{b}^2$ \\
& $65/2^+$ & 909.7 & $0.067_{-0.015}^{+0.010}$ & $7.37_{-0.57}^{+0.82}$ & $B(E2) = 1.95_{-0.30}^{+0.44}\ e^2\mathrm{b}^2$ \\
& $69/2^+$ & 962.5 & $0.047_{-0.011}^{+0.017}$ & $7.63_{-0.88}^{+1.46}$ & $B(E2) = 2.10_{-0.48}^{+0.80}\ e^2\mathrm{b}^2$ \\
\hline
\textbf{TSD2} ($n_w=1$ 指派) & $47/2^+$ & 654.6 & $0.215_{-0.048}^{+0.037}$ & $8.51_{-0.73}^{+0.95}$ & $B(E2) = 2.56_{-0.44}^{+0.57}\ e^2\mathrm{b}^2$ \\
带内 $\Delta I = 2$ & $51/2^+$ & 711.2 & $0.144_{-0.022}^{+0.017}$ & $8.67_{-0.53}^{+0.66}$ & $B(E2) = 2.67_{-0.33}^{+0.41}\ e^2\mathrm{b}^2$ \\
跃迁序列 & $55/2^+$ & 766.2 & $0.095_{-0.018}^{+0.013}$ & $8.88_{-0.64}^{+0.83}$ & $B(E2) = 2.81_{-0.41}^{+0.53}\ e^2\mathrm{b}^2$ \\
& $59/2^+$ & 819.9 & $0.087_{-0.037}^{+0.026}$ & $7.82_{-1.15}^{+1.66}$ & $B(E2) = 2.19_{-0.65}^{+0.94}\ e^2\mathrm{b}^2$ \\
& $63/2^+$ & 872.9 & $0.064_{-0.021}^{+0.013}$ & $7.91_{-0.84}^{+1.32}$ & $B(E2) = 2.25_{-0.48}^{+0.75}\ e^2\mathrm{b}^2$ \\
& $67/2^+$ & 926.5 & $0.075_{-0.025}^{+0.017}$ & $6.66_{-0.76}^{+1.09}$ & $B(E2) = 1.60_{-0.37}^{+0.52}\ e^2\mathrm{b}^2$ \\
& $71/2^+$ & 980.2 & $0.056_{-0.029}^{+0.017}$ & $6.68_{-1.02}^{+1.70}$ & $B(E2) = 1.61_{-0.49}^{+0.82}\ e^2\mathrm{b}^2$ \\
\hline
\textbf{TSD2} $\to$ \textbf{TSD1} & $47/2^+ \to 45/2^+$ & 658.9 & — & — & $B(E2) = 0.54_{-0.11}^{+0.13}\ e^2\mathrm{b}^2$, $B(M1) = 0.017_{-0.005}^{+0.006}\ \mu_N^2$ \\
带间 $\Delta I = 1$ & $51/2^+ \to 49/2^+$ & 673.2 & — & — & $B(E2) = 0.54_{-0.08}^{+0.09}\ e^2\mathrm{b}^2$, $B(M1) = 0.017_{-0.005}^{+0.005}\ \mu_N^2$ \\
连接跃迁 & $55/2^+ \to 53/2^+$ & 686.8 & — & — & $B(E2) = 0.70_{-0.15}^{+0.18}\ e^2\mathrm{b}^2$, $B(M1) = 0.024_{-0.007}^{+0.008}\ \mu_N^2$ \\
& $59/2^+ \to 57/2^+$ & 701.1 & — & — & $B(E2) = 0.65_{-0.26}^{+0.34}\ e^2\mathrm{b}^2$, $B(M1) = 0.023_{-0.011}^{+0.013}\ \mu_N^2$ \\
& $63/2^+ \to 61/2^+$ & 716.3 & — & — & $B(E2) = 0.66_{-0.24}^{+0.29}\ e^2\mathrm{b}^2$, $B(M1) = 0.024_{-0.010}^{+0.012}\ \mu_N^2$ \\
\hline\hline
\end{tabularx}
\end{table}

\subsubsection{实验数据特征、集体增强判定与客观证据边界}

核查 Görgen 等人（2004）的实测数据，可以提炼出 $^{163}\mathrm{Lu}$ 摆动运动解释的关键物理特征与严格的证据边界：
\begin{enumerate}
\item \textbf{四极形变的稳定性与微观一致性}：
TSD1 的跃迁四极矩在全测量自旋区间分布于 $7.37$--$9.93\ \mathrm{b}$（加权平均约为 $8.5\ \mathrm{b}$）；TSD2 的跃迁四极矩分布于 $6.66$--$8.88\ \mathrm{b}$（加权平均约为 $8.2\ \mathrm{b}$）。两带的 $Q_t$ 数值高度接近且随自旋演化行为一致，完全符合两能带建立在相近超形变核芯（推转计算给出 $\varepsilon_2 \approx 0.38, \gamma \approx +20^\circ$）之上的理论图像。必须说明，$n_w = 0, 1$ 属于作者的模型指派；相近的 $Q_t$ 是摆动模型的必要条件，但本身不足以单独排他性证明三轴刚性或多体波函数完全一致。
\item \textbf{带间连接跃迁的强烈电四极集体增强}：
连接 TSD2 与 TSD1 的 $\Delta I = 1$ 跃迁实测值高达 $B(E2)_{\mathrm{out}} = 0.54$--$0.70\ e^2\mathrm{b}^2$。采用标准核半径常数 $R_0 = 1.2 A^{1/3}\ \mathrm{fm}$，对于质量数 $A=163$，单个核子的标准 Weisskopf 单粒子估计为：
\begin{equation}\label{eq:4-4-weisskopf-e2}
B_{\mathrm{W}}(E2) = \frac{1}{4\pi}\left(\frac{3}{5}\right)^2 R_0^4 = 0.05940\, A^{4/3}\ e^2\mathrm{fm}^4 \approx 53.0\ e^2\mathrm{fm}^4 = 0.00530\ e^2\mathrm{b}^2.
\end{equation}
据此换算，实测带间跃迁几率 $0.54$--$0.70\ e^2\mathrm{b}^2$ 相当于高达约：
\begin{equation}\label{eq:4-4-lu163-wu}
B(E2)_{\mathrm{out}} \approx 100\text{--}132\ \mathrm{W.u.}
\end{equation}
的集体增强；而磁偶极跃迁强度约为 $B(M1) \approx 0.017$--$0.024\ \mu_N^2$。强烈的 $E2$ 集体增强与被压低的 $M1$ 强度，构成了带间跃迁由核芯宏观四极振动进动主导的关键实验证据。
\item \textbf{实验采用量依赖性与模型惯量边界}：
必须客观测定其方法学局限：在 Görgen 等人的分析中，从实测寿命中解离出 Table II 中的 $B(E2)$ 与 $B(M1)$，\textbf{依赖于前人在薄靶实验中测定的平均混合比 $\delta = -3.10_{-0.44}^{+0.36}$（Ødegård 2001，Jensen 2002）}~\cite{odegard-2001-evidence-wobbling-163lu,jensen-2002-second-phonon-wobbling-163lu}。该混合比在实验中仅测至自旋 $51/2^+$，更高自旋态的数值系假定该混合比保持不变外推提取所得。此外，理论文献中用于拟合 $^{163}\mathrm{Lu}$ 摆动能量的三个主轴转动惯量参数（如 $\mathcal{J}_m, \mathcal{J}_s, \mathcal{J}_l$）属于唯象拟合或微观推转/QRPA 模型的输出，绝不能将其误称作无模型依赖的实验直接实测量。
\item \textbf{自旋相空间与转动离心势}：
$^{163}\mathrm{Lu}$ 的两能带建立在很高的自旋区间（$I = 41/2^+$ 至 $71/2^+$）。在准粒子完全顺排估算下，核芯角动量算符模长估计达到：
\begin{equation}\label{eq:4-4-lu163-core-spin}
R = |\mathbf{I} - \mathbf{j}| \sim 15\text{--}30\hbar \gg 1.
\end{equation}
高速旋转产生的强离心势阱保证了集体转动维度的有效刚度，使得微扰进动波函数在谐振子极小附近高度局域化，从而使得局域谐振摆动近似在此处具备较高的物理适用度。
\end{enumerate}

\subsection{$A\approx 130$ 区域的低自旋摆动争议与极化双根仲裁}\label{sec:4-4-3}

当核物理学家试图将 $^{163}\mathrm{Lu}$ 的摆动图像向中重核区（$A\approx 130$）的低自旋带推广时，引发了近年来核结构领域关于角分布反演与微观竞争解释的深入学术讨论。

\subsubsection{Matta 等人（2015）的横向摆动宣称}

在奇质子核 $^{135}\mathrm{Pr}$（$Z=59, N=76$）中，奇质子占据侵入性的 $\pi 1h_{11/2}$ 轨道；TRS 势能面计算表明其基态具有中等三轴形变（$\beta_2 \approx 0.16, \gamma \approx 26^\circ$）。Matta 等人（2015）在阿贡国家实验室与印度 TIFR 利用 Gammasphere 与 INGA 阵列开展了在束测量，报道在负宇称基带（Band 1，自旋序列 $11/2^-, 15/2^-, 19/2^-, \dots$）旁观测到一条由 $\Delta I = 1$ 连接线相连的伴随带（Band 3，自旋序列 $13/2^-, 17/2^-, 21/2^-, \dots$）~\cite{matta-2015-transverse-wobbling-135pr}。作者宣称 Band 3 为基带之上的“一声子横向摆动带”，其主要依据包括：
\begin{enumerate}
\item 唯象摆动能量 $E_{\text{wob}}(I) \equiv E(I) - [E(I-1) + E(I+1)]/2$ 在低自旋区随自旋增加呈现下降趋势，符合 TW 简谐模型的唯象预期；
\item 对连接 Band 3 与 Band 1 的 $747.0\ \mathrm{keV}$ 等跃迁进行角分布拟合，提取出绝对值大于 1 的多极混合比解（如 $\delta = -2.0(4)$），对应电四极成分占比约为 $80\%$；
\item 测得这些特征连接跃迁的线偏振度不对称度呈现正值，据此推断这些跃迁具有电四极（$E2$）主导特征。
\end{enumerate}
随后，Sensharma 等人（2019）在同源的高统计量数字 Gammasphere（DGS）实验中进一步宣称观测到了 $^{135}\mathrm{Pr}$ 的“二声子横向摆动能带”~\cite{sensharma-2019-two-phonon-wobbling-135pr}。

\subsubsection{Lv 等人（2022）的独立实验再核查与角分布双根多义性}

郭松（S.~Guo）等人（2021）首先从方法学上指出了在束角分布拟合中固有的双根多义性问题~\cite{guo-2021-comment-transverse-wobbling-135pr}；随后，Lv 等人（2022）在芬兰于韦斯屈莱实验室利用 JUROGAM II 高分辨锗阵列完成了独立的高统计量符合重测，其结果对低自旋摆动声子图像提出了根本性的挑战~\cite{lv-2022-evidence-against-wobbling-135pr}：
\begin{enumerate}
\item \textbf{在束角分布拟合的二次有理式代数双根}：
在在束 $\gamma$ 谱学中，定向退激角分布函数展开为 $W(\theta) = 1 + A_2(\delta) P_2(\cos\theta) + A_4(\delta) P_4(\cos\theta)$，方向角关联比值 $R_{\mathrm{ac}}$ 同样由展开系数 $A_k$ 决定。根据第\ref{sec:5-9}节推导，展开系数 $A_k(\delta) = \frac{B_k + 2\delta C_k + \delta^2 D_k}{1 + \delta^2}$ 是关于多极混合比 $\delta$ 的二次有理式。因此，实验方程 $R_{\mathrm{ac}}^{\text{exp}} = R_{\mathrm{ac}}(\delta)$ 在整理后构成关于 $\delta$ 的一元二次方程。取决于实验比值与误差范围，方程在实数域内可具有两个实根、一个退化根或无有限实根。当存在两个实根时，通常表现为：
\begin{itemize}
\item 一个绝对值较大（$|\delta_1| > 1$），对应电四极主导（$E2$-rich）；
\item 另一个绝对值较小（$|\delta_2| < 1$），对应磁偶极主导（$M1$-rich）。
\end{itemize}
\item \textbf{线偏振符号与小根的相容性}：
Guo 等人（2021）与 Lv 等人（2022）明确指出：康普顿线偏振度不对称度 $P(\theta)$ 的数值与符号敏感依赖于初态自旋取向的统计分布张量以及混合比大小。在特定取向宽度与几何设置下，磁偶极主导的小根解同样可以给出正的线偏振度。因此，仅凭线偏振度呈现正符号，在物理上不能作为排他性支持大根、排除小根的充分证据。
\item \textbf{JUROGAM II 实测原表与能级分支比检验}：
严格核对能级跃迁与实测原表（Lv 等人 2022 Table 1）：
\begin{itemize}
\item 连接 Band 3 与 Band 1 的跃迁能量为 $747.3\ \mathrm{keV}$（其能级归属为 $17/2^- \to 15/2^-$）；实测线偏振度为 $P = 0.04_{-0.13}^{+0.08}$，角关联比值为 $R_{\mathrm{ac}} = 0.37(4)$，拟合出的小根解为：
\begin{equation}\label{eq:4-4-pr135-small-delta-747}
\delta = -0.47_{-0.22}^{+0.09}.
\end{equation}
在此小根解下，条件换算出的磁偶极辐射成分占比约为 $82\%$，电四极成分仅约 $18\%$；
\item 另一条关键连接线 $813.2\ \mathrm{keV}$（$21/2^- \to 19/2^-$），实测 $P = -0.03_{-0.12}^{+0.05}$，$R_{\mathrm{ac}} = 0.48(6)$，拟合出的小根解为：
\begin{equation}\label{eq:4-4-pr135-small-delta-813}
\delta = -0.37_{-0.14}^{+0.10},
\end{equation}
对应条件磁偶极成分占比约为 $88\%$；
\item 连接线 $450.2\ \mathrm{keV}$（$15/2^- \to 13/2^-$），实测 $R_{\mathrm{ac}} = 0.49(4)$，拟合出的小根解为 $\delta = -0.31_{-0.13}^{+0.10}$，对应条件磁偶极占比约为 $91\%$；
\item \textbf{同母态竞争分支比的检验}：从 Band 3 上的初态 $17/2^-$ 出发，存在两条平行的退激通道：落入基带 Band 1 的 $15/2^-$ 态（$747.3\ \mathrm{keV}$），以及落入签名伙伴带 Band 2 的 $13/2^-$ 态（$526.2\ \mathrm{keV}$）。Lv 等人在采用已测 $526.2\ \mathrm{keV}$ 多极性与相对强度后，导出约化四极跃迁几率之比为：
\begin{equation}\label{eq:4-4-pr135-branch-ratio}
\frac{B(E2; 747.3\ \mathrm{keV}, 17/2^- \to 15/2^-)}{B(E2; 526.2\ \mathrm{keV}, 17/2^- \to 13/2^-)} = 0.7_{-0.5}^{+0.7}.
\end{equation}
在纯横向摆动声子图像中，向基带的四极跃迁具有集体增强，向签名伙伴带的跃迁受到禁戒，上述比值在理论模型中通常预期显著大于 1。实测比值约为 0.7 表明初态波函数向两带具有同等量级的重叠，有力支持了能带混合的物理图像，向纯横向摆动声子模型提出了严重质疑。
\end{itemize}
\end{enumerate}

\subsubsection{微观多体竞争解释：IBFM、单粒子重对准与倾斜进动}

针对 $^{135}\mathrm{Pr}$ 的低自旋带，国际核结构理论界给出了多元竞争模型描述：
\begin{enumerate}
\item \textbf{微观相互作用玻色子-费米子模型（IBFM）}：
野村（K.~Nomura）等人（2022）基于相对论能量密度泛函 DD-PC1 与可分离配对力自洽映射偶偶核芯 $^{134}\mathrm{Ce}$ 的势能面，并拟合费米子--玻色子耦合参数，对 $^{135}\mathrm{Pr}$ 开展了微观 IBFM 计算（区分于该文中用于 $^{132}\mathrm{Ba} / ^{128}\mathrm{Xe}$ 的非相对论 Gogny D1M 泛函）~\cite{nomura-2022-questioning-wobbling-ibfm}。计算表明，$^{134}\mathrm{Ce}$ 核芯处于三轴 $\gamma$ 软势阱中。当奇质子与这一 $\gamma$ 软核芯发生四极动力学耦合时，自然形成了包含 Band 1 与 Band 3 的能级序列；模型理论预言两带间的连接跃迁天然由 $M1$ 主导，完全无须引入横向摆动激发假定。
\item \textbf{准粒子--三轴转子（QTR）放开冻结下的平面转动}：
Lv 等人（2022）利用固定三轴形变（$\varepsilon_2 = 0.16, \gamma = 26^\circ$）但放开准粒子取向自由度的微观 QTR 计算阐明：在带头自旋 $I = 13/2^-$ 处，扣除单粒子自旋 $j = 11/2\hbar$ 后，估算的核芯集体角动量仅为 $R = |\mathbf{I} - \mathbf{j}| \sim 1\hbar$ 左右。在弱转动离心势下，真实的量子角动量波函数在三维空间具有宽广的角向弥散，不能直接套用大自旋局域简谐高斯波包。随着自旋增加，奇核子角动量并非刚性冻结在短轴上，而是在科里奥利力作用下向主转动轴倾斜，发生单粒子对准重整（Planar Rotation），从而构成平面转动带。
\item \textbf{倾斜进动（Tilted Precession, TiP）模型}：
Lawrie 等人（2020）指出，在低自旋奇 $A$ 核中，体系角动量可能处于非主轴的经典倾斜平衡极小，表现为绕某一固定倾斜方向的准经典进动（TiP）~\cite{lawrie-2020-tilted-precession}。这表明该核区实验数据存在多种相容的理论解读。
\end{enumerate}

\subsection{$A\approx 180$--$190$ 邻区：高 $K$ 进动极限与重区形状共存的取向演化}\label{sec:4-4-4}

迈向更重的超铪/钨（$A\approx 178$ 邻区）以及金/铂/汞（$A\approx 187$--$196$）过渡区时，非轴对称取向动力学展现出两类不同的物理边界：轴对称退化下的高 $K$ 进动几何，以及微观软势能面下的多重形状共存。

\subsubsection{高 $K$ 进动模式：三轴摆动的轴对称退化极限（Shimizu 2005）}

清水（Y.~R.~Shimizu）、松崎（M.~Matsuzaki）与松柳（K.~Matsuyanagi）（2005）利用微观随机相位近似（RPA）理论，探讨了高 $K$ 轴对称转动态与三轴摆动运动之间的几何联系~\cite{shimizu-2005-high-k-precession}。在 $^{178}\mathrm{W}$（如 $K^\pi = 25^+$）与 $^{178,179}\mathrm{Hf}$ 等长椭形变核中，多个破对费米子在轴对称变形场下发生取向叠加，在对称轴（取为 3 轴）上构筑起单粒子角动量无量纲投影 $K = \sum_i \Omega_i$。

考察三轴转子在 $\gamma \to 0^\circ$ 轴对称极限下的连续退化行为：
\begin{enumerate}
\item \textbf{参考系频率关系与无量纲量子数}：
在轴对称小振幅 RPA 展开下，对于物理 $\Delta K = +1$ 的进动激发模，实验室参考系进动角频率 $\omega_{\mathrm{prec}}$ 与均匀推转随体参考系转动角频率 $\omega_{\mathrm{rot}}$ 严格满足代数关系：
\begin{equation}\label{eq:4-4-shimizu-frame}
\omega_{\mathrm{wob}} = \omega_{\mathrm{prec}} - \omega_{\mathrm{rot}}, \qquad
\omega_{\mathrm{prec}} = \frac{\hbar K}{\mathcal{J}_\perp^{\text{eff}}(\omega_{\mathrm{prec}})}.
\end{equation}
式中无量纲量子数 $K \equiv \langle\Phi|J_3|\Phi\rangle/\hbar$ 为对称轴上的纯单粒子投影；垂直有效惯量 $\mathcal{J}_\perp^{\text{eff}}$ 一般依赖于进动模式频率，需自洽求解。
\item \textbf{对称轴冗余约束与能谱结构}：
对理想的轴对称形状转子，绕其对称轴（3 轴）的形状取向属于冗余坐标；模型以约束 $R_3 = 0$ 表达不存在独立的轴向集体形状转动。这并不意味着轴对称体系的微观推转响应在所有通道上恒为零。在保持固定内禀单粒子投影 $K$ 的绝热强耦合极限下，转动态仍具有垂直方向的集体转动，其能谱表达式为：
\begin{equation}\label{eq:4-4-high-k-energy-formula}
E_K(I) - E_{\text{intr}} = \frac{\hbar^2}{2\mathcal{J}_\perp} \left[ I(I+1) - K^2 \right], \qquad I = K, K+1, K+2, \dots
\end{equation}
\item \textbf{能级首间距与大 $K$ 进动领先项的区别}：
必须严格区分两个能标：
\begin{itemize}
\item 实验室参考系下带头\textbf{首个能级间距}（$I=K+1$ 与 $I=K$ 之间的跃迁能量）严格为：
\begin{equation}\label{eq:4-4-first-gap}
\Delta E_{\text{first}} = E_K(K+1) - E_K(K) = \frac{\hbar^2(K+1)}{\mathcal{J}_\perp};
\end{equation}
\item 而式~\eqref{eq:4-4-shimizu-frame} 给出的大 $K$ 极限（$K \gg 1$）下的经典领先阶进动角频率能量为：
\begin{equation}\label{eq:4-4-asymptotic-prec}
\hbar\omega_{\mathrm{prec}} \simeq \frac{\hbar^2 K}{\mathcal{J}_\perp}.
\end{equation}
\end{itemize}
二者之间相差严格的量度微商项 $\hbar^2/\mathcal{J}_\perp$，相对修正为 $1/K$。该代数关系反映了离散量子自旋与半经典进动之间的精确对应。
\end{enumerate}

\subsubsection{重区 $^{187}\mathrm{Au}$ 的实验检验与争议（Guo 2022）}

在奇 $A$ 重核过渡区核素 $^{187}\mathrm{Au}$（$Z=79$）中，围绕所谓的“纵向摆动（LW）”同样展开了学术论争。Sensharma 等人（2020）利用 Gammasphere 实验宣称在 $^{187}\mathrm{Au}$ 中基于奇质子 $1h_{9/2}$ 轨道观测到了纵向摆动能带（Band 2，带头自旋 $11/2^-$）~\cite{sensharma-2020-longitudinal-wobbling-187au}。

然而，郭松（S.~Guo）等人（2022）在兰州 HIRFL 加速器上开展了独立测量，结合微观分析指出该指派存在的物理争议~\cite{guo-2022-low-spin-wobbling-187au}：
\begin{enumerate}
\item \textbf{驱动势能与对准几何的倾向分歧}：
在 $^{187}\mathrm{Au}$ 中，质子数 $Z=79$，质子费米面靠近 $1h_{9/2}$ 子壳层的底部，属于粒子型准粒子。在微观势能面与四极场计算中，底壳粒子在能量上倾向于对准最短几何轴（$s$ 轴，即 $k=2$ 轴）。然而，Sensharma 等人的纵向摆动模型为了符合纵向摆动假定，将该准粒子角动量设定为对准中间几何轴（$m$ 轴，即 $k=1$ 轴），由此产生了对准几何的模型设定分歧。
\item \textbf{低自旋下的核芯转动动量估计}：
在 Band 2 带头 $I = 11/2^-$ 处，按顺排近似估计核芯集体角动量仅为 $R \sim 1\hbar$ 左右。在弱离心转动环境下，简谐微扰势阱的适用性受到挑战。
\item \textbf{角分布小根与采用强度的模型依赖性}：
Guo 等人通过电子内转换系数 $\alpha_K$ 测量以及角关联数据表明，连接 Band 2 与 Band 1 的特征跃迁 $376\ \mathrm{keV}$（$11/2^- \to 9/2^-$）与 $462\ \mathrm{keV}$（$15/2^- \to 13/2^-$）支持小混合比解（实验拟合给出 $\delta \approx -0.26$ 与 $-0.28$）。由于 $^{187}\mathrm{Au}$ 的 Band 2 能级寿命在比较数据集中缺乏直接测量，Guo 等人通过采用邻近偶偶核芯 $^{186}\mathrm{Pt}$ 的带内跃迁强度 $B(E2)_{\mathrm{in}} \sim 100$--$200\ \mathrm{W.u.}$ 进行折算，导出其实际带间跃迁强度较低：
\begin{equation}\label{eq:4-4-au187-be2-ratio}
\frac{B(E2)_{\mathrm{out}}}{B(E2)_{\mathrm{in}}} < 0.1, \qquad B(E2)_{\mathrm{out}} \sim \text{数个}\ \mathrm{W.u.}
\end{equation}
较低的带间电四极跃迁强度表明 Band 2 更自然地被解释为包含形状共存与单粒子态激发的多构型混合带。
\end{enumerate}

\subsubsection{重区 Os/Pt/Hg 的 $\gamma$ 软度与多重形状共存界限}

在重核过渡区（$^{186,188,190}\mathrm{Os}$、$^{188,190,192}\mathrm{Pt}$ 与 $^{190,192}\mathrm{Hg}$）的微观结构中，微观约束密度泛函（CDFT）与推转玻尔哈密顿量计算表明：部分核态势能面在 $\gamma$ 方向较为平缓，存在明显的 $\gamma$ 软振动与形状涨落，且普遍伴随能量相近的长椭与扁椭极小之间的多重形状共存（Shape Coexistence）~\cite{prochniak-rohozinski-2009-bohr-collective-hamiltonian}。

必须在此确立明确的物理分界：\textbf{绝对不能将该区域出现的弱四极形变或扁椭倾向，误认为是证实轴对称转子假设的依据；更不能将形状共存或软三轴核直接贴上刚性三轴摆动的排他性标签}。任何取向模式的判定，都必须结合能量曲面、微观轨道占据以及跃迁强度的综合测量。

\subsection{跨区迁移条件、物理不变量映射与失效反例}\label{sec:4-4-5}

通过对上述稀土区、中重区以及重核过渡区的系统对照，可以提炼出取向运动在原子核不同质量区发生迁移的物理条件，并明确微观不变量在实验表观量上的映射界限。

\subsubsection{取向运动跨区迁移的物理条件与失效机制}

一个具有三轴形变特征的原子核体系，若要在实验谱学中稳定呈现出宏观简谐摆动运动，通常需要满足以下综合物理条件：
\begin{enumerate}
\item \textbf{微观势能面刚度条件}：
核芯在内禀空间具备相对稳定的三轴形变势阱，避免被大振幅 $\gamma$ 软振动或多重形状共存所掩盖；
\item \textbf{集体转动离心势条件}：
体系总自旋显著超越未配对准粒子的内禀角动量，核芯分配到的集体转动动量较大（$R = |\mathbf{I} - \mathbf{j}| \gg 1$），从而构筑起简谐恢复力势阱；
\item \textbf{准粒子内禀对准稳定性}：
价核子费米面稳定处于高 $j$ 子壳层底部或顶端，且准粒子角动量在所研究的转动频率窗口内能够抵御科里奥利力引起的向转轴动态重对准；
\item \textbf{声子激发能隙解耦}：
摆动激发能量与局域两准粒子破对能、签名伙伴带交叉能级差以及核芯本身的 $\gamma$ 振动态保持足够的解耦间隙，以避免发生破坏声子特征的剧烈能带混合。
\end{enumerate}

低自旋候选核（如 $^{135}\mathrm{Pr}$ 与 $^{187}\mathrm{Au}$ 的低激发带）之所以难以呈现出典型摆动特征，其关键原因之一在于其违背了上述强转动假设：在带头处核芯转动极弱（$R \sim 1\hbar$ 左右），单粒子角动量极易受到推转诱导向主转轴发生重对准，导致体系在低自旋下更容易表现为由单粒子自旋翻转主导的平面转动或粒子--振动强耦合态。

\subsubsection{物理不变量与微观模型参数的映射边界}

在跨核区比较中，必须严格区分不同的微观或唯象物理量：
\begin{enumerate}
\item \textbf{跃迁四极矩 $Q_t$ 与光谱四极矩 $Q_s$}：$Q_t$ 由带内 $\Delta I = 2$ 跃迁寿命反演，反映的是电四极跃迁张量的非对角矩阵元大小；$Q_s$ 是核态本身的静态对角电四极矩。在非轴对称或形状涨落核中，相同的 $Q_t$ 不等价于两能带具有完全相同的微观多体波函数，更不能直接推导得出相同的转动惯量张量。
\item \textbf{克莱因不变量二次矩 $q_2$ 与三次矩 $q_3$}：在第\ref{sec:2-4}节中已经严格证明，通过库仑激发求和规则提取的形状不变量无量纲比值 $R \equiv q_3 / q_2^{3/2} \propto \langle Q^3 \cos 3\delta \rangle / \langle Q^2 \rangle^{3/2}$，包含了体系在全部内禀形变空间中的大振幅积分权重。当核内存在强烈的 $\gamma$ 软振动时，$R$ 与刚体模型假定下的 $\cos 3\gamma$ 存在动力学偏差，不能简单建立一对一的代数换算。
\item \textbf{转动惯量的多重性}：由带内能级间距提取的运动学惯量 $\mathcal{J}^{(1)}$ 与动力学惯量 $\mathcal{J}^{(2)}$ 反映的是沿带的纵向转动响应；而决定摆动模式稳定性的是横向恢复力惯量 $\mathcal{J}_k(\omega)$。两者受控于截然不同的微观费米面与配对微商，不能用沿带间距直接推断横向动力学特征。
\item \textbf{电磁多极单位规范}：在磁偶极跃迁中，实验文献常用的传统原子核磁子单位 $\mu_N^2$ 与电荷型微观算符表述中的 $(\mu_N/c)^2$ 在标准定义下数值严格相同（如第\ref{sec:5-9}节式~\eqref{eq:5-9-delta-def} 所示），在任何换算中均不可人为施加多余的除以 $c^2$ 操作。
\end{enumerate}

\subsubsection{跨核区典型取向动力学对照总结}

表~\ref{tab:4-4-cross-region-comparison}汇总了跨越四大典型质量区的核态配置、形变机制、关键实测电磁可观测量以及当前理论界的主要竞争解释。

\begin{table}[!htbp]
\centering
\small
\caption{跨核区非轴对称取向动力学核心案例比较矩阵（严格基于已核原件数据与物理模型条件整理）。}\label{tab:4-4-cross-region-comparison}
\begin{tabularx}{\textwidth}{lXXXXX}
\hline\hline
核素与能带标识 & 准粒子构型与费米面位置 & 形变与微观惯量模型条件 & 自旋窗口与带头核芯转动动量 & 实测关键电磁特征 & 原作者解释 vs 主要竞争理论解释 \\
\hline
$^{163}\mathrm{Lu}$ & 奇质子 $\pi i_{13/2}$ & $\varepsilon_2 \approx 0.38, \gamma \approx +20^\circ$; & $I = 41/2^+$--$71/2^+$; & $Q_t \approx 6.7$--$9.9\ \mathrm{b}$; & 原作者：经典横向摆动 (TW); \\
TSD1 / TSD2 & 壳底粒子型对准短轴 $s=2$ & 满足无旋流惯量主轴排序 & 模型估算 $R \sim 15$--$30\hbar \gg 1$ & 带间 $B(E2)_{\mathrm{out}} \approx 0.54$--$0.70\ e^2\mathrm{b}^2$ & 理论评述：具备极强超形变势 \\
& (模型假设 $\mathbf{j} \perp \mathcal{J}_m$) & $\mathcal{J}_m > \mathcal{J}_s > \mathcal{J}_l$ & (强转动离心势) & (约 $100$--$132\ \mathrm{W.u.}$); 采用 $\delta \approx -3.10$ & 阱与高核芯离心转动的典型基准 \\
\hline
$^{135}\mathrm{Pr}$ & 奇质子 $\pi 1h_{11/2}$ & $\beta_2 \approx 0.16, \gamma \approx 26^\circ$; & $I = 11/2^-$--$25/2^-$; & $747.3\ \mathrm{keV}$ 跃迁小根解 & 原作者 (Matta 2015)：低自旋 TW; \\
Band 1 / Band 3 & 壳底粒子型 & 势能面具有中等三轴性， & 带头自旋 $13/2^-$, & $\delta \approx -0.47$, $M1$ 成分占 $\sim 82\%$; & 竞争解释 (Lv 2022)：双根多义性， \\
& 准粒子易受推转重对准 & 但微观配对导致惯量软化 & 模型估算 $R \sim 1\hbar$ 极微弱 & $B(E2; 747)/B(E2; 526) \approx 0.7$ & 单粒子重对准平面转动 / IBFM / 能带混合 \\
\hline
$^{178}\mathrm{W}$ & 多准粒子破对高 $K$ 态 & 轴对称长椭极限 $\gamma \to 0^\circ$; & $I \ge K = 25^+$; & 带内强烈回转 $\Delta I = 1, 2$; & 原作者 (Shimizu 2005)：高 $K$ 进动; \\
$K^\pi = 25^+$ & 费米子沿对称轴 $z=3$ 顺排 & 形状冗余约束 $R_3 = 0$， & 绕轴对称长轴进动， & 首跃迁间距 $\frac{\hbar^2(K+1)}{\mathcal{J}_\perp}$; & 物理联系：三轴摆动在轴对称下 \\
& 形成宏观投影 $K = 25$ & 垂直有效惯量 $\mathcal{J}_\perp^{\text{eff}}$ & 满足强耦合谱代数 & 大 $K$ 渐近频率 $\hbar\omega_{\mathrm{prec}} \simeq \frac{\hbar^2 K}{\mathcal{J}_\perp}$ & 的连续几何演化极限 \\
\hline
$^{187}\mathrm{Au}$ & 奇质子 $\pi 1h_{9/2}$ & $\beta_2 \approx 0.15, \gamma \approx 18^\circ$; & $I = 9/2^-$--$21/2^-$; & $376, 462\ \mathrm{keV}$ 跃迁小根解 & 原作者 (Sensharma 2020)：纵向摆动; \\
Band 1 / Band 2 & 壳底粒子型倾向短轴 $s=2$ & 处于微观长椭--扁椭形状共存 & 带头自旋 $11/2^-$, & $\delta \approx -0.26, -0.28$; 采用 & 竞争解释 (Guo 2022)：对准几何分歧， \\
& (与 LW 中轴对准模型分歧) & 与 $\gamma$ 软振动区间 & 模型估算 $R \sim 1\hbar$ 极微弱 & $^{186}\mathrm{Pt}$ 估计 $B(E2)_{\mathrm{out}}$ 仅数 W.u. & 带头缺乏离心恢复力，多重形状共存 \\
\hline\hline
\end{tabularx}
\end{table}

综上所述，原子核在三轴形变空间中的动力学取向，绝非由单一的标量形变参数 $\gamma$ 所能片面确定，而是由核芯势能面曲率、微观费米面单粒子代数结构、集体转动惯量的自洽动力学响应以及自旋相空间所共同决定的复杂多体过程。在跨核区谱学研究中，唯有坚持将实验二次有理双根的多义性检验、高精度绝对寿命测量以及放开冻结近似的微观多体模型紧密结合，才能在纷繁复杂的实验谱线与深层核结构机制之间建立起可证伪、可复现的科学联系。
'''

staging_path = 'outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G90/sec-4-4.tex'
with open(staging_path, 'w', encoding='utf-8') as f:
    f.write(content)

canonical_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-4-4.tex'
with open(canonical_path, 'w', encoding='utf-8') as f:
    f.write(content)

sha = hashlib.sha256(content.encode('utf-8')).hexdigest()
print(f'Done! sec-4-4.tex R2 written successfully. SHA-256: {sha}')
