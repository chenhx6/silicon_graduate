import hashlib

content = r'''\section{探测器与光子响应}\label{sec:5-2}

在在束 $\gamma$ 谱学与核结构衰变实验中，实验人员从能谱直方图上提取的核心观测指标是特征跃迁峰的净峰面积计数 $A_{\mathrm{peak}}$ 与峰位中心能量。然而，核谱学分析的一个基本事实是：\emph{测得的谱峰面积并不等于该激发态退激发射的特征光子数}。一个能量为 $E_\gamma$ 的真实发射光子，从离开靶核、穿过实验靶室与探测器死层，到与半导体晶体发生微观电磁相互作用并被数字化系统记录，经历了一系列具有能量依赖性、几何选择性与统计涨落的物理响应过程。

第~5.1~节讨论了核反应对目标态的输入布居，而探测器系统则是将微观跃迁光子转化为可测电子学信号的转换环节。高纯锗（HPGe）及由多晶体组合构成的 Clover 探测器因其卓越的能量分辨能力，构成了低能核结构谱仪的主力核心。若对光子相互作用截面、仪器响应函数的归一化条件、能量分辨率的物理来源、符合相加效应以及反散射屏蔽机制缺乏精确把握，容易在谱分析中引入系统性偏差：例如混淆内禀效率与绝对探测效率导致跃迁强度被严重低估，或者在近距离几何下忽略真符合相加（True Coincidence Summing）导致分支比与寿命反演失真。本节系统阐明光子与探测介质的相互作用机理，构建仪器响应函数与探测效率的严格定义体系，推导能量分辨率的微观物理贡献，深入剖析 Clover 探测器的 Add-back 模式与符合相加机制，并介绍反康普顿屏蔽与现代 $\gamma$ 射线径迹重构技术的物理边界。

\subsection{光子与物质相互作用与谱响应机制}\label{subsec:5-2-1}

在低能与中高能核结构能区（几十 keV 至十几 MeV），光子在锗晶体介质中的能量沉积由三类主导的微观量子电动力学过程控制（吴治华 2005 专著第 2 章第 4 节，印刷第 54–65 页，PDF 第 62–73 页~\cite{book-wu-nuclear-experiment-methods}）：
\begin{enumerate}
\item 光电效应（Photoelectric Effect）：
光子与锗原子的束缚内壳层电子（主要为 $K$ 壳层，结合能约 $11.1\,\text{keV}$）发生完全非弹性碰撞，光子被吸收并释放动能为 $E_e = E_\gamma - B_e$ 的光电子。伴随内壳层空穴退激发射的特征 X 射线（Ge $K_\alpha \approx 9.9\,\text{keV}$）或 Auger 电子在条件性完全再吸收后，光子的初始能量 $E_\gamma$ 全部转化为次级电离电荷。若光电吸收发生在晶体外表面或电极死层附近，出射的特征 X 射线可能逃逸出活性体积，导致特征锗逃逸峰（$E_{\mathrm{obs}} \approx E_\gamma - 9.9\,\text{keV}$）或混入连续谱。在远离吸收边的能区，光电截面遵循经验标度 $\sigma_{\mathrm{pe}} \propto Z^n / E_\gamma^{3.5}$（在锗晶体 $Z=32$ 中 $n \approx 4$–$5$），因而在低能区（$E_\gamma \lesssim 150\,\text{keV}$）占主导。光电吸收是直接形成全能吸收峰（Full-Energy Peak, FEP）的最有效单步机制。
\item 康普顿散射（Compton Scattering）：
光子与晶体内原子外层的弱束缚价电子发生非弹性散射，出射光子保留部分能量 $E_\gamma'$，反冲电子获得剩余动能 $E_e = E_\gamma - E_\gamma'$。根据相对论能量与动量守恒，当入射光子能量为 $E_\gamma$、散射角为 $\theta$ 时，反冲电子的动能由经典的康普顿公式给出：
\begin{equation}\label{eq:5-2-compton-electron}
E_e(\theta) = E_\gamma \frac{\frac{E_\gamma}{m_e c^2}(1 - \cos\theta)}{1 + \frac{E_\gamma}{m_e c^2}(1 - \cos\theta)},
\end{equation}
其中 $m_e c^2 \approx 511.0\,\text{keV}$ 为电子静质量能量。反冲电子能量随散射角 $\theta$ 单调增加，在完全对心后向散射（$\theta = 180^\circ$）时达到最大动能，在能谱中形成特征性的康普顿边缘（Compton Edge）：
\begin{equation}\label{eq:5-2-compton-edge}
E_{\mathrm{edge}} = E_\gamma \frac{2 E_\gamma / m_e c^2}{1 + 2 E_\gamma / m_e c^2}.
\end{equation}
若散射后的低能光子从探测器表面逸出，反冲电子在晶体内沉积其动能，产生能量在 $0 \le E_{\mathrm{obs}} \le E_{\mathrm{edge}}$ 之间的连续能谱分布；而在靶室或探测器周围材料中发生 $180^\circ$ 后向散射的光子若重新入射进入探测器，则会在低能侧形成后向散射峰（Backscatter Peak），其峰位约为 $E_{\mathrm{bs}} = E_\gamma - E_{\mathrm{edge}} \approx \frac{m_e c^2}{2 + m_e c^2 / E_\gamma}$。大量未被完全吸收的康普顿散射事件构成了全能峰下方的连续康普顿本底，制约了弱 $\gamma$ 谱线的信噪比。
\item 电子对生成（Pair Production）：
当光子能量超过两倍电子静质量阈能（$E_\gamma \ge 2 m_e c^2 \approx 1022.0\,\text{keV}$）时，在核库仑场的参与下，光子可转化为一对正负电子。正负电子对在介质中电离沉积动能 $(E_\gamma - 2 m_e c^2)$；随后热化的正电子与介质中的负电子发生湮灭，释放出两个背对背出射的 $511.0\,\text{keV}$ 湮灭光子。根据湮灭光子的逸出几率，在能谱中形成特征结构：
\begin{itemize}
\item 若两个 $511\,\text{keV}$ 光子均从探测晶体中逃逸，仅记录正负电子动能，在谱图中形成双逃逸峰（Double Escape Peak, DEP），峰位位于 $E_{\mathrm{obs}} = E_\gamma - 1022\,\text{keV}$；
\item 若一个 $511\,\text{keV}$ 光子被晶体吸收、另一个光子逃逸，在谱图中形成单逃逸峰（Single Escape Peak, SEP），峰位位于 $E_{\mathrm{obs}} = E_\gamma - 511\,\text{keV}$；
\item 逃逸出的 $511\,\text{keV}$ 光子进入相邻探测器时，在 $511\,\text{keV}$ 处形成孤立的湮灭吸收峰。
\end{itemize}
\end{enumerate}

\subsection{仪器响应函数与探测效率体系}\label{subsec:5-2-2}

为了从数学上严格描述单色光子入射后在探测系统输出端产生的复杂谱分布，引入仪器响应函数（Detector Response Function）$R(E_{\mathrm{obs}} \mid E_\gamma, \text{geom}, \text{gates})$。

讨论仪器响应函数时，首要的前提是澄清其归一化条件：
若将响应函数 $R(E_{\mathrm{obs}} \mid E_\gamma)$ 严格定义为\emph{条件于该光子已被探测器产生有效电离事件}的观测能量概率密度函数，则在整个测量能量区间上的积分恒等于 1：
\begin{equation}\label{eq:5-2-norm-cond}
\int_0^\infty R(E_{\mathrm{obs}} \mid E_\gamma) \, \mathrm{d}E_{\mathrm{obs}} = 1.
\end{equation}
响应函数总谱可严格分解为净全能吸收峰分量与其余不完全能量沉积（康普顿连续谱及逃逸峰）分量之和：$R(E_{\mathrm{obs}} \mid E_\gamma) = R_{\mathrm{FEP}}(E_{\mathrm{obs}} \mid E_\gamma) + R_{\mathrm{other}}(E_{\mathrm{obs}} \mid E_\gamma)$。在此条件归一化下，全能峰所占的净能量积分份额定义为探测器的峰总比（Peak-to-Total Ratio, P/T，吴治华 2005 专著第 10 章第 1 节，印刷第 257–260 页，PDF 第 265–268 页规范~\cite{book-wu-nuclear-experiment-methods}）：
\begin{equation}\label{eq:5-2-peak-to-total}
(P/T)(E_\gamma) \equiv \frac{\int_0^\infty R_{\mathrm{FEP}}(E_{\mathrm{obs}} \mid E_\gamma) \, \mathrm{d}E_{\mathrm{obs}}}{\int_0^\infty R(E_{\mathrm{obs}} \mid E_\gamma) \, \mathrm{d}E_{\mathrm{obs}}} = \int_0^\infty R_{\mathrm{FEP}}(E_{\mathrm{obs}} \mid E_\gamma) \, \mathrm{d}E_{\mathrm{obs}}.
\end{equation}
必须指出：在未经本底扣除的有限能量积分窗（如 $[E_\gamma - 3\sigma, E_\gamma + 3\sigma]$）内直接积分不仅会截断高斯峰尾，还会混入窗口下方的连续康普顿本底；因此在实验数据处理中，峰面积必须通过高斯拟合加局部本底扣除提取净全能峰分量 $A_{\mathrm{peak}}$，避免将未扣本底的窗口原始总计数等同于真全能吸收概率。
因此，探测器的绝对全能峰探测效率 $\varepsilon_{\mathrm{p}}(E_\gamma)$ 表达为总探测效率 $\varepsilon_{\mathrm{tot}}(E_\gamma)$ 与峰总比的乘积：
\begin{equation}\label{eq:5-2-eff-decomp}
\varepsilon_{\mathrm{p}}(E_\gamma) = \varepsilon_{\mathrm{tot}}(E_\gamma) \times (P/T)(E_\gamma).
\end{equation}
在物理表述中，绝不能在不加条件声明的前提下，既写 $\int R \, \mathrm{d}E_{\mathrm{obs}} = 1$ 又写 $\int_{\mathrm{peak}} R \, \mathrm{d}E_{\mathrm{obs}} = \varepsilon_{\mathrm{abs}}$，必须对条件概率测度予以明确界定。

在几何与传输层面，绝对探测效率与内禀探测效率（Intrinsic Efficiency）满足：
式~\eqref{eq:5-2-eff-decomp} 中的绝对峰效率在有限空间立体角上通常表达为角积分：
\begin{equation}\label{eq:5-2-eff-integral}
\varepsilon_{\mathrm{p}}(E_\gamma) = \frac{1}{4\pi} \int_{\Omega} W(\mathbf{n}) T_{\mathrm{abs}}(\mathbf{n}) \varepsilon_{\mathrm{int}}(E_\gamma, \mathbf{n}) \, \mathrm{d}\Omega,
\end{equation}
其中 $\mathbf{n}$ 为出射方向单位矢量，$W(\mathbf{n})$ 为该跃迁的相对空间角分布，满足全空间角归一条件 $\int_{4\pi} W(\mathbf{n})\,\mathrm{d}\Omega = 4\pi$（在各向同性极限下 $W(\mathbf{n}) \equiv 1$），$T_{\mathrm{abs}}(\mathbf{n})$ 为光子沿路径穿过靶室壁、冷指端窗与晶体死层（Dead Layer）的能量吸收透射率，$\varepsilon_{\mathrm{int}}(E_\gamma, \mathbf{n})$ 为进入晶体活性区后完全沉积能量的内禀探测概率。在弱各向异性或探测器张角较小的近似下，式~\eqref{eq:5-2-eff-integral} 常用因式分解形式近似表示为：
\begin{equation}\label{eq:5-2-eff-geom}
\varepsilon_{\mathrm{p}}(E_\gamma) \approx \frac{\Omega}{4\pi} \bar{\varepsilon}_{\mathrm{int}}(E_\gamma) \bar{T}_{\mathrm{abs}} \bar{F},
\end{equation}
其中 $\Omega = \int_{\mathrm{det}} \mathrm{d}\Omega$ 为几何立体角，各带上划线量代表立体角内的平均因数。

单标量效率曲线 $\varepsilon_{\mathrm{p}}(E_\gamma)$ 并不仅限于完全各向同性的理想点源，在实际在束实验中常定义为固定几何、特定能量及声明实验条件下的有效峰效率（Effective Peak Efficiency）。但当引入多道时间符合门（Coincidence Gate）或事件多重性筛选时，若多通道间存在死时间阻塞或几何相关，联合接受几率不能简单与各道独立边缘效率直接连乘，而应作为多维联合仪器响应统一处理（参见第~5.5~节）。

为直观展示上述相互作用机制在单色高能光子入射下的典型谱形特征，图~\ref{fig:5-2-detector-response} 给出了基于标准教学响应模型在 $E_\gamma = 1500\,\text{keV}$ 下合成的探测器响应谱图（计算参数、脚本与图工件见附录~F 与 \texttt{detector-response-simulation}）。

\begin{figure}[!htbp]
\centering
\IfFileExists{Img/detector-response-simulation.pdf}{%
  \includegraphics[width=0.88\textwidth]{Img/detector-response-simulation.pdf}%
}{%
  \fbox{\parbox{0.88\textwidth}{\centering\vspace{2.5cm}（图 5.1 探测器响应谱模拟图：\texttt{Img/detector-response-simulation.pdf}；展示 $1500\text{ keV}$ 光子在单晶 HPGe、Clover Add-back 及 BGO 反康普顿屏蔽下的合成谱形）\vspace{2.5cm}}}%
}
\caption{理想 $\gamma$ 射线探测器响应谱模拟对比（教学模型，基于参数化教学合成模型生成，明确区分晶体本征逃逸谱与靶室/屏蔽等周围材料引入的后向散射及湮灭吸收峰，入射能量取 $E_\gamma = 1500\,\text{keV}$。图中清晰标定了全能峰 FEP、$E_{\mathrm{edge}} \approx 1281.7\,\text{keV}$ 的康普顿边缘、单逃逸峰 SEP、双逃逸峰 DEP、$511\,\text{keV}$ 湮灭峰以及反向散射峰 $E_{\mathrm{bs}} \approx 218.3\,\text{keV}$。黑色实线代表单晶裸锗响应，蓝色曲线展示了 Clover 四晶体 Add-back 能量合并对全能峰的回收增强（图中展示的 Add-back 增益因子为选取的教学合成参数，非未知探测器实测值），红色曲线展示了 BGO 反康普顿屏蔽门控对连续本底与逃逸峰的主动抑制；注意此处为规范教学模型输出，纵轴为任意单位对数计数，非特定未知用户硬件实测拟合）。}
\label{fig:5-2-detector-response}
\end{figure}

\subsection{能量分辨率的微观物理贡献与独立性假定}\label{subsec:5-2-3}

探测器的能量分辨率表征其区分相近跃迁谱线的能力，通常以全能峰在半高全宽（Full Width at Half Maximum, FWHM）处的能量展宽 $\Delta E$ 表示。

HPGe 探测器的总能量分辨率由三类物理来源截然不同的涨落机制共同决定（吴治华 2005 专著第 5 章第 3 节，印刷第 146–151 页，PDF 第 154–159 页~\cite{book-wu-nuclear-experiment-methods}）：
\begin{enumerate}
\item 载流子产生的统计涨落（$\mathrm{FWHM}_{\mathrm{stat}}$）：
沉积能量 $E_\gamma$ 产生电子-空穴对的平均数目为 $N = E_\gamma / \epsilon$（在 77 K 锗半导体典型评价与参考参数中，产生一个电子-空穴对的平均有效能量常取参考标称值 $\epsilon \approx 2.96\,\text{eV}$）。由于部分能量耗散于不可逆的晶格声子激发，产生电子-空穴对数的涨落方差偏离纯泊松分布，由无量纲 Fano 因子 $F$ 修正（锗半导体中通常取经验参考值 $F \sim 0.1$）：对数涨落方差为无量纲数 $\sigma_N^2 = F N = F E_\gamma / \epsilon$。转换到观测能量尺度的等效能量方差为 $\sigma_{E, \mathrm{stat}}^2 = \epsilon^2 \sigma_N^2 = F \epsilon E_\gamma$（具有能量平方量纲 $\mathrm{MeV}^2$），对应的半高全宽能量展宽为：
\begin{equation}\label{eq:5-2-fwhm-stat}
\mathrm{FWHM}_{\mathrm{stat}} = 2\sqrt{2\ln 2} \sigma_{E, \mathrm{stat}} = 2\sqrt{2\ln 2} \sqrt{F \epsilon E_\gamma} \approx 2.355 \sqrt{F \epsilon E_\gamma}.
\end{equation}
统计展宽随能量平方根 $\sqrt{E_\gamma}$ 增长，构成了半导体探测器物理分辨率的理论极限。
\item 电荷收集不完全与空间弥散（$\mathrm{FWHM}_{\mathrm{cc}}$）：
由于晶体内深能级杂质引起的载流子俘获（Trapping）、晶体缺陷导致的寿命缩短，以及不同电离位置的空穴漂移路径与收集时间起伏，产生电荷收集效率分散。此外，第~5.3~节讨论的弹道亏损（Ballistic Deficit）亦会展宽收集不完全项。该项近似正比于沉积能量 $E_\gamma$。
\item 电子学热噪声与基线晃动（$\mathrm{FWHM}_{\mathrm{el}}$）：
前置放大器输入端 FET 的并联热噪声、串联电阻白噪声、探测器反向漏电流散粒噪声，以及第~5.3~节式~\eqref{eq:5-3-var-net} 所述的基线滑动平均涨落 $\sigma_{BL}$。该项在微观上完全由读出电路特性决定，与入射光子能量 $E_\gamma$ 基本无关。
\end{enumerate}

在各分量近似服从高斯分布或具有等效高斯二阶矩、且相互统计独立的假定下，总能量分辨率满足等效方差叠加律：
需要说明：不完全电荷收集项（$\mathrm{FWHM}_{\mathrm{cc}}$）通常引入低能侧指数拖尾，具有非对称非高斯特征；式~\eqref{eq:5-2-fwhm-quad} 属于等效二阶矩方差近似。
\begin{equation}\label{eq:5-2-fwhm-quad}
\mathrm{FWHM}_{\mathrm{tot}} = \sqrt{\mathrm{FWHM}_{\mathrm{stat}}^2 + \mathrm{FWHM}_{\mathrm{cc}}^2 + \mathrm{FWHM}_{\mathrm{el}}^2} = \sqrt{a + b E_\gamma + c E_\gamma^2}.
\end{equation}
必须强调：总分辨率是由电荷电离统计、晶体载流子输运与电子学模拟噪声共同主导的物理响应，绝不能依据 ADC 采样速率或数字量化位数单方面推断能量分辨率，亦不能脱离实测校准向未知探测器套用虚构性能指标。

\subsection{复合探测器、Add-back模式与符合相加效应}\label{subsec:5-2-4}

为了克服单晶 HPGe 探测器在兆电子伏以上能区光电吸收几率低下、且大体积单晶电荷收集时间过长的物理限制，核物理实验广泛采用了复合探测器结构，其中最典型的是四叶草型 Clover 探测器。在特定复合探测器设计（如典型的 Clover 探测器）中，常将 4 块相互独立读出但紧密排列的同轴高纯锗晶体（部分典型实现采用 $n$ 型同轴晶体）集成在同一个低温杜瓦内；不同阵列的具体晶体类型、电极分段与几何尺寸依研制规范而异，不应作单一普遍化假定。

对于一个入射光子，若其在某单一晶体内经单步光电效应完全沉积，由该晶体独立输出全能信号；若光子在晶体 A 发生初级康普顿散射，散射光子进入相邻的晶体 B 并在其中被完全光电吸收，在符合时间窗口 $\Delta T_{\mathrm{add}}$ 内，通过将两晶体的测得能量直接相加（$E_{\mathrm{add}} = E_A + E_B$），即可将原本属于康普顿本底的散射事件重新挽回为全能峰事件。这种数据重构机制称为 Add-back 模式。

在应用 Add-back 模式时，必须建立客观的得失权衡认知：
\begin{itemize}
\item 优势：显著增大了高能光子的全能峰绝对探测效率（在 $1.3\,\text{MeV}$ 处典型 Add-back 因子可达 $1.4$–$1.5$ 左右），并有效提升了谱图的峰总比 $(P/T)$；
\item 代价：由于能量是由两路物理晶叶信号相加重构（$E_{\mathrm{add}} = E_A + E_B$），总能量方差不仅包含两晶叶的固有噪声，还受晶体间能量分配涨落与电子学相关的调控：$\sigma_{\mathrm{add}}^2 = \sigma_A^2 + \sigma_B^2 + 2\mathrm{Cov}(E_A, E_B)$。若两通道模拟前放电子学噪声相互独立，纯电子学噪声方差线性相加（$\sigma_{\mathrm{add, el}}^2 = \sigma_{A, \mathrm{el}}^2 + \sigma_{B, \mathrm{el}}^2$）；但在完整的物理能量求和中，实际能量分辨率还受晶体间能量分配起伏、接触层电容串扰协方差以及各晶叶电荷收集时间不一致性的影响，导致 Add-back 全能峰的半高全宽相比单个孤立晶叶略有展宽；此外，多道求和改变了事件的多重性分布，增大了探测偶然符合以及相邻晶体间的相加污染，并非所有谱学指标均无条件得到改善。
\end{itemize}

在紧凑阵列几何下，必须严格区分两类机制截然不同的脉冲相加现象：
\begin{enumerate}
\item 偶然堆积相加（Accidental Pile-up）：
源于不相干核反应事件发射的光子在极高计数率下由于时间重叠进入同一成形窗（见第~5.3~节与第~5.5~节）。该相加几率强烈正比于实验总计数率 $R_{\mathrm{tot}}$，通过降低束流强度或减小成形时间可以压制。
\item 真符合相加（True Coincidence Summing, TCS）：
发生在同核级联退激的微观过程中。当某激发能级相继发射符合光子 $\gamma_1$ 与 $\gamma_2$ 时，若两光子在收集时间窗口内同时击中同一个物理晶体（或处于同一 Clover 的不同晶叶），探测器直接记录其能量总和。在理想线性响应、固定立体角几何与无死时间阻塞的前提下，真符合相加的单事件相对发生概率严格与源的活度或宏观计数率无关（因为两光子源于同一次微观核退激），而是由初末态跃迁分支比、级联角关联函数 $W(\theta_{12})$ 以及探测器对源张开的绝对几何立体角 $\Omega$ 共同决定；但在实际高计数率在束反应中，宏观脉冲堆积与死时间门控会非线性改变观测到的相加损失与有效峰面积，导致观测到的相加修正呈现复杂的计数率依赖偏离：
\begin{itemize}
\item 相加滑出（Summing-Out）：本应归属于能量 $E_1$ 全能峰的事件，因伴随的 $\gamma_2$ 同时沉积能量而滑出 $E_1$ 峰位，导致 $E_1$ 处的表观峰面积减小：
\begin{equation}\label{eq:5-2-summing-out}
A_{\gamma 1}^{\mathrm{obs}} \approx A_{\gamma 1} \left[ 1 - \sum_j b_{1j} \varepsilon_{\mathrm{tot}}(E_j) \bar{W}_{1j} \right];
\end{equation}
式中 $b_{1j}$ 为伴随级联支路的分支比，$\varepsilon_{\mathrm{tot}}$ 为伴随光子的总探测效率，$\bar{W}_{1j}$ 为包含探测器有限张角平均的级联角关联因子；该式为弱相加几率下的一阶近似，多级串联退激须结合衰变纲图进行完整矩阵积分以避免多重通道重复计数；
\item 相加滑入（Summing-In）：若两级联光子均在同一探测单元内发生完全能量沉积，在 $E_1 + E_2$ 处形成非本征跃迁的假复合相加峰。
\end{itemize}
\end{enumerate}
在紧凑的近距离靶--探测器几何下，真符合相加会显著改变表观峰面积。在反演分支比与跃迁几率时，不能简单假定各光子独立探测，必须通过已知放射源标定或数值模拟进行几何相关的相加修正。

\subsection{反康普顿屏蔽、极化灵敏度与径迹重构前沿}\label{subsec:5-2-5}

为了净化 HPGe 谱图并提取电磁辐射的内禀几何取向，现代 $\gamma$ 阵列引入了主动屏蔽与高级成像技术：
\begin{enumerate}
\item BGO 反康普顿主动屏蔽（Anti-Compton Veto）：
在 HPGe 晶体周围包裹高密度、高原子序数的锗酸铋（$\mathrm{Bi}_4\mathrm{Ge}_3\mathrm{O}_{12}$, BGO）闪烁体探测器（吴治华 2005 专著第 10 章第 3 节，印刷第 278–281 页，PDF 第 286–289 页~\cite{book-wu-nuclear-experiment-methods}）。当入射光子在 HPGe 内发生康普顿散射并将散射光子甩出晶体外时，逃逸光子极易被外围的 BGO 捕获并发光。通过将 HPGe 与 BGO 输出施加符合禁止门控（Veto Gate），系统自动舍弃发生逃逸的变形脉冲，从而将连续康普顿本底与单双逃逸峰强烈压低，使谱图的峰总比提高数倍。
需要说明：BGO 屏蔽无法做到完全消除本底，且伴随有假否决（False Veto）风险——从靶室散射的低能粒子、核反应中微子伴生快中子或级联发射的另一个不相关光子若误入 BGO，会将合法的 HPGe 全能峰事件错误否决。因此，BGO 阈值与否决门宽必须精细标定。
\item Clover 康普顿散射偏振计（Compton Polarimeter）：
根据相对论量子电动力学 Klein-Nishina 微分截面，线偏振光子的康普顿散射强烈偏向于垂直于电矢量 $\mathbf{E}$ 的方位角平面（Hamilton 1975 专著第 15 章第 5 节，PDF 第 727–728 页，印刷第 716–717 页~\cite{book-hamilton-electromagnetic-interaction}）：
\begin{equation}\label{eq:5-2-klein-nishina-pol}
\frac{\mathrm{d}\sigma}{\mathrm{d}\Omega} = \frac{r_0^2}{2} \left(\frac{E'}{E}\right)^2 \left[ \frac{E'}{E} + \frac{E}{E'} - 2\sin^2\theta \cos^2\phi \right],
\end{equation}
其中 $\phi$ 为散射平面与电矢量偏振平面的夹角。在 Clover 探测器中，相互正交排列的 4 块晶体自然构成了康普顿散射计与吸收计。通过测定光子在平行于反应平面与垂直于反应平面内的散射计数不对称度：
\begin{equation}\label{eq:5-2-asymmetry}
A = \frac{N_\perp - a N_\parallel}{N_\perp + a N_\parallel} = Q P,
\end{equation}
其中 $Q$ 为偏振灵敏度因数，$P$ 为入射光子的线偏振度，参数 $a \equiv N_\perp^0 / N_\parallel^0$ 为利用无偏振放射源（$P=0$）标定的探测器几何不对称校正因子（与第~5.7~节式~\eqref{eq:5-7-asym-exp} 约定一致；若采用倒数定义则公式须相应变换）。通过偏振度 $P$ 的正负符号，可以实验判定特征 $\gamma$ 射线属于电性辐射还是磁性辐射（如鉴别 $E1$ 与 $M1$）。必须指出：偏振度符号与电磁性质的对应关系依赖于核态自旋跃迁序列与探测器几何放置角，不能采用“$P$ 为正必为电性辐射”的机械简化，具体极化反演将在第~5.7~节详细展开。
\item 现代 $\gamma$ 射线跟踪技术（$\gamma$-Ray Tracking, AGATA 与 GRETINA）~\cite{akkoyun-2012-agata-instrument-response}：
传统加装 BGO 屏蔽的阵列面临着几何立体角受限（大量的立体角被被动材料或大体积辅助闪烁体屏蔽体占据）的根本瓶颈。以 AGATA（欧洲）与 GRETINA（美国）为代表的新一代阵列采用了高纯锗晶体电极高度电分段技术（如单晶分段为 36 个独立电极），结合脉冲形状分析（Pulse Shape Analysis, PSA）技术，能够在离线或具备专用硬件流水线的系统中反演相互作用点的三维空间坐标 $(x, y, z)$ 与能量沉积（位置分辨可达毫米量级；Akkoyun 等 2012 手稿 arXiv:1111.5731v1 41页手稿 PDF 第 1–10 页概述了其总体架构与技术规范，区分于最终期刊排版页码）。
进而，基于康普顿散射运动学角守恒进行正向径迹重构（Forward Tracking），在算法层面识别单光子的散射径迹序列，从而摆脱了厚重 BGO 辅助屏蔽体的几何限制；新一代阵列设计以追求接近 $4\pi$ 的高立体角覆盖为目标（模拟中设想的完整 $4\pi$ 阵列由 180 块六角分段晶体组成，实际在束实验均按分阶段安装的子阵列如 AGATA Demonstrator 等构型运行，其覆盖立体角依安装几何与辅助探测器配置而异）。组合脉冲形状分析与径迹重构技术能够显著提升全能峰重建效率并压制康普顿散射本底，反映了在束核谱学探测技术的重要发展。
\end{enumerate}
'''

staging_path = 'outputs/degree-dissertation/20261108-A130-rewrite/latex-20261113/G99/sec-5-2.tex'
with open(staging_path, 'w', encoding='utf-8') as f:
    f.write(content)

canonical_path = 'raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-5-2.tex'
with open(canonical_path, 'w', encoding='utf-8') as f:
    f.write(content)

sha = hashlib.sha256(content.encode('utf-8')).hexdigest()
print(f'Done! sec-5-2.tex written successfully. SHA-256: {sha}')
