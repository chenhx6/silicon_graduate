# T10｜G67-v1 冻结稿 BCS 数学与原件定向核查

范围：只审 `raw/writing/gpt/A130/review-inputs/G67-v1/section-2-3.md` 及相邻 `section-2-3.json`，并针对七项问题读指定原件；不审活动稿、不写论文。下面的替换式是本任务建议或独立推导，只有明确标为原书式号者才归属于原文。结论不构成论文或整节科学通过。

## 1. 正束缚能的三点与四点差分：**三点错误，四点可用但需固定中心**

令 \(B>0\)，偶数核因配对通常比平滑背景多束缚，设 \(B(N)=B_{\rm sm}(N)+p(-1)^N\)，\(p>0\)。稿中的三点式对交错项给 \(-2p\)，四点式给 \(+2p\)：两者对同一纯奇偶交错符号相反。稿中随后把 \((-1)^N\Delta^{(3)}\) 称为正峰/深谷又混合了**带符号的原始曲率**和**乘奇偶因子的正能隙指标**。平滑背景和壳效应仍可改变局部符号，不应保证全部核素正值。

保持正束缚能约定的最小修正为
\[
\Delta_B^{(3)}(N)={(-1)^{N+1}\over2}[B(N-1)-2B(N)+B(N+1)],\quad
\Delta_B^{(4)}(N)={(-1)^N\over4}[B(N-2)-3B(N-1)+3B(N)-B(N+1)]
={\Delta_B^{(3)}(N-1)+\Delta_B^{(3)}(N)\over2}.
\]
后一式是以 \(N-1,N\) 两个三点指标取平均的四点约定；其他文献可能采用另一中心/符号，必须写出定义。若采用总能 \(E=-B\)，三点式改用 \((-1)^N\)；不要同时保留正 \(B\) 和那个符号。偶峰奇谷指原始 \(B\) 相对平滑背景，不是上述经过奇偶因子处理的 \(\Delta_B^{(3)}\) 本身。数值控制取 \(p=0.7\)：稿内三、四点分别为 −1.4、+1.4；此例是算术反例，不是实验数据。

## 2. 时间反演对与 \(J=0\)：**单固定 pair 等同于零角动量错误，归一有误**

在球形单 \(j\) 壳层、\(\bar m\) 含 \((-1)^{j-m}\) 相位、真空归一的约定下，归一化的 **集体** \(J=0\) 两粒子态可写成
\[
|j^2;00\rangle={1\over\sqrt{2(2j+1)}}\sum_{m=-j}^{j}(-1)^{j-m}c_{jm}^{\dagger}c_{j,-m}^{\dagger}|0\rangle
={1\over\sqrt{\Omega}}\sum_{m>0}(-1)^{j-m}c_{jm}^{\dagger}c_{j,-m}^{\dagger}|0\rangle,\quad \Omega={2j+1\over2}.
\]
若采用已归一化的反对称双粒子基，应相应重写系数，不能把有序张量积与归一 Slater 态的 \(\sqrt2\) 混用。\(c_k^\dagger c_{\bar k}^\dagger|0\rangle\) 只固定 \(M=0\)；一般是多个允许 \(J\) 的叠加。例外如 \(j=1/2\) 的同壳层对不能推广。轴对称变形轨道通常没有好 \(J\)，仅有投影与时间反演配对的相应意义。Suhonen 印刷 401／PDF414，式(13.59)及相邻段落支持时间反演配对的约定；它没有证明每个固定 \(m\) 对即为 \(J=0\)。

## 3. BCS 真空、\(H_{20}\) 与矩阵：**变换和正 \(uv\) 相容，稿的本征矩阵符号不相容**

对稿中的实数约定，\(P_k^\dagger=c_k^\dagger c_{\bar k}^\dagger\)，\(|\Phi\rangle=\prod_k(u_k+v_kP_k^\dagger)|0\rangle\)：所给两个 \(\alpha\) 的确湮灭该真空，且 \(\kappa_k=\langle c_{\bar k}c_k\rangle=u_kv_k\)。当 \(G\) 实对称且 \(\Delta_k=\sum_lG_{kl}u_lv_l\)，对稿列出的 pair-only Hamiltonian 直接 Wick 收缩得到
\[
\mu_k=G_{kk}v_k^2,\quad \xi_k=\epsilon_k-\lambda-G_{kk}v_k^2,\quad
H'_{20,k}=2\xi_k u_kv_k-\Delta_k(u_k^2-v_k^2).
\]
令其零并取正能分支、\(\Delta_k>0\)：\(u_kv_k=\Delta_k/(2E_k)\)，\(E_k=\sqrt{\xi_k^2+\Delta_k^2}\)。与该 **同一相位约定**相容的替换为
\[
\begin{pmatrix}\xi_k&+\Delta_k\\+\Delta_k&-\xi_k\end{pmatrix}\binom{u_k}{v_k}=E_k\binom{u_k}{v_k}.
\]
也可以保留稿的负非对角，改本征矢为 \((u_k,-v_k)^T\)；但须明示所用 Nambu 基底和相位，不可只改一个式子。原稿 \((-\Delta,-\Delta)\) 对 \((u,v)\) 的正能本征矢要求 \(uv=-\Delta/(2E)\)。控制输入 \((\xi,\Delta)=(0.6,0.8)\)，原矩阵正 \(uv\) 残差 1.6，修正矩阵残差 \(1.24\times10^{-16}\)。

Suhonen 印刷 399–402／PDF412–415：式(13.40)–(13.41)、(13.45)–(13.48)、(13.54)–(13.65)给变分与 \(H_{20}\) 的对应；书用耦合算符和自己的相位，以上 \(\mu_k\) 是本任务对**稿内哈密顿量**的推导，不是照抄书的通式。自能不是普遍“通常较小”；若近似忽略或吸收到预先定义的单粒子谱，需显式声明并在所有相关方程一致处理。稿中的常 \(G\) 方程分母丢掉 \(\mu\) 而两能级段又保留另一种 \(\mu\)，构成不一致。\(\Delta=0\) 分支不可通过除以 \(\Delta\) 的 gap 方程推出。单独的 \(\delta\langle H-\lambda N\rangle=0\) 与 \(H_{20}=0\) 是驻点条件；极小值还要检查受约束二阶变分及竞争分支。乘积归一为1本身也不足以逻辑推出每因子归一；应将每对 \(u_k^2+v_k^2=1\) 设为逐对规范化约定。

## 4. 粒子数、相角与定数态：**\(\hbar\) 错误，配对关联与反常密度混淆**

\(\theta\) 是无量纲的单粒子规范角，\(\hat N\) 是无量纲粒子数：角表示中 \(\hat N=-i\partial_\theta\)，而 \(-i\hbar\partial_\theta\) 对应 \(\hbar\hat N\)。若改用 pair 相角，因成对算符带两倍相位，必须同时调整共轭变量和周期，不能悄然更换约定。QRPA 局域共轭对是态附近的线性化描述；并非在有限核完整 Hilbert 空间构造出满足严格全局正则对易关系的自伴角算符。Hinohara APS 版 p.5 式(49)–(53)；R2 canonical crosswalk 的“配对规范角”段落。

若 \(\hat N|\Psi_N\rangle=N|\Psi_N\rangle\)，则 \(\langle\Psi_N|c_{\bar k}c_k|\Psi_N\rangle=0\) 严格成立，因为该算符改变粒子数2。即使如此，\(\langle P_k^\dagger P_l\rangle\)、两粒子转移矩阵元 \(\langle\Psi_{N-2}|P_k|\Psi_N\rangle\) 或合适的关联能仍可非零：配对关联不以态内 \(\kappa\ne0\) 为必要条件。稿末“固定数配对张量绝不会断裂”应删除或改为相应的数守恒两体关联随具体模型演化。投影 \(P_N|\Phi\rangle\) 若非零是好粒子数试探态，并非自动为给定哈密顿量的精确能量本征态。

## 5. Hinohara 粒子数曲率：**稿的正 \(B\) 正曲率式与自身 \(H-\lambda N\) 约定矛盾；原作存在符号记法边界**

Hinohara APS 发表版 p.8 Eq.(66) 字面称 \(B\) 为 binding energy 并写 \(+\lambda\Delta N+(\Delta N)^2/(2\mathcal J)\)；Eq.(67) 写 \(\mathcal J=-S(\hat N,0)\)。但 p.9 Fig.4 图注比较的实验曲线使用 \(-B_{\rm exp}\)，并给出负的中子化学势，提示其 \(B\) 与正束缚能的记号在原文中不能直接无歧义移植。不要把“原文写成正 \(B\)”隐去，也不要未经作者程序核查断言产生歧义的具体原因。

与稿前面 \(H-\lambda N\)、正束缚能 \(B_+=-E\) 一致的替换为
\[
E(N)=E(N_0)+\lambda\,\delta N+{(\delta N)^2\over2\mathcal J}+\cdots,\quad
B_+(N)=B_+(N_0)-\lambda\,\delta N-{(\delta N)^2\over2\mathcal J}+\cdots,
\quad \lambda={\partial E\over\partial N},\quad \mathcal J={\partial N\over\partial\lambda}=-S(\hat N,0).
\]
\(\mathcal J^{-1}=\partial^2E/\partial N^2=-\partial^2B_+/\partial N^2\)，仅适用于指定的平滑、局部自洽约束态族、所选固定其他粒子数路径和响应约定，且响应须非奇异。\(\mathcal J\) 正负应由具体受约束曲率决定，不能仅由书写形式保证；远离参考态或穿过结构变化时局域展开可能失效。此处不扩展原件内其他系数争议。

## 6. Suhonen 两能级模型与稿内 pair-only 模型：**原书公式确实如此，但不能与稿给定哈密顿量混用**

原件精确定位：印刷 408／PDF421 §13.5.2 定义两壳、\(\epsilon_{1,2}=\mp\varepsilon/2\)、每壳 \(2\Omega\) 个单粒子态、平均数 \(2\Omega\)；印刷 409／PDF422 式(13.103)设 *任意* 壳标签 \(a,b,c,d\in\{1,2\}\) 的归一化耦合 \(J=0\) 两体矩阵元均为 \(-\Omega G\)，式(13.104)–(13.105)给
\[
\Delta=\Omega G(u_1v_1+u_2v_2),\quad
\mu_1=G(v_1^2+\tfrac12v_2^2),\quad\mu_2=G(\tfrac12v_1^2+v_2^2).
\]
这包含跨壳粒子—空穴自能贡献；不只是稿内 \(-G\sum_{kl}P_k^\dagger P_l\) 那种仅同一壳内时间反演 pair 散射。书在配对非零的对称支 \(v_1^2+v_2^2=1\) 上得 \(E_1=E_2=\Omega G\)、\(\lambda=-3G/4\)（式(13.110)–(13.112)）；印刷 410／PDF423 式(13.114)、(13.117)、(13.120) 分别给 \(\eta=2\Omega\varepsilon/(4\Omega-1)\)、\(\Delta^2=(\Omega G)^2-\eta^2\)、\(G_{\rm crit}=2\varepsilon/(4\Omega-1)\)。印刷 411／PDF424 式(13.121)–(13.124)给稿中 \(x\) 和占据式。原文采用特定壳、相位和矩阵元设定（包括式(13.108)所述偶 \(l\) 的正振幅），不是一般常 \(G\) Hamiltonian 的定理。

**本任务对冻结稿哈密顿量的独立推导**：同样 \(\Omega\)、两壳、半填充，保留稿内完整 \(k=l\) 对角项与其 Wick 自能 \(\mu_i=Gv_i^2\)。设 \(t=v_1^2-v_2^2\)，\(v_1^2+v_2^2=1\)，则
\[
\langle H\rangle=-\Omega\varepsilon t-G\left[\Omega+{(4\Omega^2-2\Omega)(1-t^2)\over4}\right],
\quad t_*={\varepsilon\over G(2\Omega-1)},\quad
G_{c,\rm pair}={\varepsilon\over2\Omega-1},\quad\lambda=-{G\over2},
\]
\[
E_1=E_2=\Omega G,\quad |\xi_1|=|\xi_2|={\Omega\varepsilon\over2\Omega-1},\quad
\Delta=\Omega G\sqrt{1-t_*^2}\quad(G>G_{c,\rm pair}).
\]
这里 \(\lambda\) 的值指非零配对、镜像对称的驻点；塌缩区的粒子数平台上 \(\lambda\) 一般不唯一。控制脚本直接在 16 维 pair 占据基构造期望，与上式四个 \(t\) 点相符；该空间只覆盖 seniority-zero 试探态，并非对任意态或实核的精确谱结论。Suhonen 的 \(\mu\) 多出的交叉项在上述镜像试探态上使能量相对 pair-only 再减 \(\Omega G(1-t^2)/4\)，从而把 \(4\Omega-2\) 改成 \(4\Omega-1\)；这是根据其自能推导出的差异，不把它伪装成原文另给的公式。

若**有意识忽略全部自能**，则 \(\xi_i=\epsilon_i-\lambda\)、\(\lambda=0\)，非零配对支有 \(G_c=\varepsilon/(2\Omega)\)、\(\Delta=\sqrt{(\Omega G)^2-(\varepsilon/2)^2}\)。这又是另一近似，不能与原书 \(4\Omega-1\) 混用。建议 writer 选择一种 Hamiltonian、计数和自能方案贯穿全文；要引用原书系数就须明确扩大相互作用定义，而不是直接接在稿内 pair-only 哈密顿量之后。

## 7. 极限、极小值与非解析：**稿的若干绝对断言错误**

- \(\Delta\to0\) 可以发生于有限 \(G=G_c\)，不等于 \(G\to0\)。在有有限壳隙的上述例子中，\(G\downarrow G_c\) 时 \(\Delta\sim\text{const}\sqrt{G-G_c}\) 连续趋零而非必然阶跃；下降到 \(G=0\) 才是无相互作用极限。\(G\le G_c\) 的 \(\Delta=0\) 自洽态在 \(G>0\) 仍有相互作用对角能量及可能的定数关联，不能称为无相互作用 Hamiltonian。强耦合时饱和的是 \(\Delta/G\to\Omega\)，不是绝对 \(\Delta\) 随 \(G\to\infty\) 饱和。
- BCS 非零支的消失可以是连续塌缩；其他条件下的分支交叉、自洽转动或约束问题可能出现跳变，不能统一断言必阶跃。\(H_{20}=0\) 只是驻点：需在固定平均粒子数的允许变分中比较能量并检查 Hessian。本模型的 \(t\) 方向曲率 \(G\Omega(2\Omega-1)>0\) 只证明这个受限对称路径上的极小，不证明全变分空间全局极小。
- 有限维、解析参数依赖的 Hamiltonian 中，孤立非简并本征支在局部通常解析；不同对称性或未耦合本征支可以精确交叉，使基态选支或导数出现非解析。不要把“有限核没有热力学极限下的严格相变”扩大为“任何有限核、任何参数均无非解析”。PBCS、VAP 和精确解并不自动保证全部观测量对全部路径平滑；弱耦合也不能一概断言必是“强烈”配对振动。固定 \(N\) 的态内反常密度恒为零，不能用它判断配对是否断裂。
- 稿把 \(2\Delta\) 写成精确阈值过强：对共同正 \(\Delta\) 的冻结独立准粒子近似，\(E_k+E_l\ge2\Delta\) 是下界，实际最低允许组态需考虑离散谱、阻塞、量子数与残余作用；\(2\Delta\) 不必可达，更不是实核所有低能激发的精确阈值。Suhonen 印刷 403／PDF416 式(13.68)–(13.69)本身是带具体模型条件的下界。

## 原件、范围与独立控制记录

- Suhonen：`raw/books/From nucleons to nucleus concepts of microscopic .pdf`，SHA-256 `4d4b799b8d91784638bac29e0749fe08ba9720f067fd76317f7e256d6f8cd27c`。定向回读印刷 399–404、408–411（PDF412–417、421–424）；对应 408–411 也在 PDF396–399 重复出现。PDF402–403 实为印刷414–415，不能套用固定偏移。本次未以全书阅读声称代替原式核查。
- Hinohara：`raw/papers/gpt/query/20261108-r2-t05-response-definitions/aps-publication.pdf`，SHA-256 `764d644a2349235027e15c320d78f15fcd7d8fd264ebe6412fd2b80e1a625f86`；定向回读 APS 5 页式(49)–(53)、8–9 页式(66)–(67)和 Fig.4 图注，结合 `knowledge/research-notes/doctoral-r2-collective-inertia-response-crosswalk-20261108.md` 局域相角及响应定义。原 APS 文献身份另通过出版商摘要查询，未下载新原件。Jain 原页本次未使用，故没有用其支持额外断言。
- `control.py` 为 producer，`control-input.json` 为输入，`control-output.json` 为实际输出；SHA-256 与真实 UTC 执行信息见同目录 `receipt.json`。这是有限数学控制，非实核拟合、非独立实验或论文验收。
