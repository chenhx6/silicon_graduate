"""Build a paragraph-aligned Chapter3 reader from the user-provided PDF.
All source bboxes are explicit; display equations use source crops without repair.
"""
from pathlib import Path
import json,re,unicodedata
import fitz

OUT=Path(__file__).parent
SRC=Path('raw/papers/degree dissertation/Triaxiality and Rotational bands in 133Ce.pdf')
DOC=fitz.open(SRC)
RAW=json.loads((OUT/'extracted_blocks.json').read_text())
BY={(b['pdf_page'],b['block']):b for b in RAW}
spec=[]
def add(p,lo,hi,zh,kind='paragraph',number=None,original=None):
    spec.append(dict(page=p,source_blocks=list(range(lo,hi+1)),translation=zh,type=kind,
                     equation_number=number,original_override=original))
def h(p,lo,hi,zh):add(p,lo,hi,zh,'heading')
def e(p,lo,hi,num):add(p,lo,hi,'原式见上图；保留原符号、系数和单位写法，不在译文重写公式。','equation',num)

h(36,0,1,'第3章　原子核三轴性')
h(36,2,2,'3.1　引言')
add(36,3,9,'上一章讨论了轴对称转子，以及这类核转动产生的能带结构；其中，总核自旋 $I$ 的投影 $K$ 是好量子数。当原子核呈三轴形变时，不存在对称轴，$K$ 也不再是好量子数。三轴原子核可以同时绕其体固连轴转动。三轴核的能谱可能呈现复杂图样。本章综述目前对非轴对称形变核中转动态的认识。')
h(36,10,10,'3.2　非对称粒子加转子模型')
add(36,11,11,'三轴形变偶偶核芯的转动由下式支配：')
e(36,12,23,'3.1')
add(37,1,3,r'其中，$k=1,2,3$ 是内禀（体固连）轴，分别代表中轴、短轴和长轴。转动惯量（MoI）$\mathcal{J}_k$ 通常由无旋流模型描述，定义如下[20,21]：')
e(37,4,5,'3.2')
add(37,6,11,r'其中 $\mathcal{J}_1$ 最大。在 $0^\circ<\gamma<30^\circ$ 时，$\mathcal{J}_1>\mathcal{J}_2>\mathcal{J}_3$；在 $30^\circ<\gamma<60^\circ$ 时，$\mathcal{J}_1>\mathcal{J}_3>\mathcal{J}_2$。本研究假定无旋流型转动惯量，因为这一选择得到实验证据支持[2]。转动主要绕有利的中轴进行：该轴转动惯量最大，因此绕该轴转动所需能量最低。哈密顿量（式3.1）变为：')
e(37,12,13,'3.3')
add(37,14,21,r'其中 $A_k=\hbar^2/(2\mathcal{J}_k)$。式3.3所示哈密顿量的解是一系列转动态，包括基态带和若干激发转动带。激发带常被称为 $\gamma$ 带[74]。为将这些激发的低能转动态与 Bohr 哈密顿量[15]中由转动、振动集体模式耦合产生的 $K=2$、$K=4$ 等 $\gamma$ 带区分开，三轴核中的这些转动带被称为倾斜进动带[42]，因为它们表征原子核同时绕三条核轴的进动，见3.2.1节。')
add(37,22,23,r'图3.1：若干原子核的经验测定转动惯量随 $\gamma$ 形变的变化。改编自文献[2]。','caption','3.1')
add(38,1,11,r'激发带来自三维哈密顿量的解。$I=0$ 恰有一个态，$I=1$ 没有态，$I=2$ 有两个态，$I=3$ 有一个态，$I=4$ 有三个态，$I=5$ 有两个态，$I=6$ 有四个态，依此类推。模型预言的自旋序列因而为 $I=\{0,2,2,3,4,4,4,5,5,6,6,6,6,\ldots\}$。这些态可以按如下方式组织成转动带：自旋 $I=0,2,4,6,\ldots$ 的最低能态构成基态带；第一激发带由 $I=2,3,4,5,6,\ldots$ 构成；下一激发带由 $I=4,5,6,7,8,\ldots$ 构成；第三激发带的自旋序列为 $I=6,7,8,\ldots$，$K=6$，等等。图3.2给出了三轴转子转动态的排列，下一节进一步讨论。')
h(38,12,12,'3.2.1　倾斜进动带')
add(38,13,20,r'描述偶偶三轴核转动产生的激发转动带，一种也许更合适的方法，是把它们视为总角动量矢量 $\vec I$ 偏离中轴并绕中轴进动的结果。如前所述，中轴的转动惯量最大，绕它转动更有利。在 $\gamma=30^\circ$ 时，哈密顿量（式3.3）具有一种对称性：短轴和长轴（分别为2轴、3轴）的转动惯量相等，即 $\mathcal{J}_2=\mathcal{J}_3$。因此可以将哈密顿量写为[42]：')
e(38,21,23,'3.4')
add(38,24,24,'相应的能量本征值为：')
e(38,25,26,'3.5')
add(38,27,31,r'其中 $i$ 为 $\vec I$ 在中轴上的投影。当 $i=|I|$ 时，$\vec I$ 完全沿中轴排列，见图3.2(d)；所得 $\Delta I=2$ 态序列构成图3.2(a)所示基态带。激发带通过使 $I$ 偏离中轴而形成，见图3.2(e)、(f)。当 $i=I-1$ 和 $i=I-2$ 时，所得……〔原段下接PDF40〕')
add(39,36,37,'图3.2：三轴偶偶转子的能谱。(a)为基态带，$i=I$（红色）。(b)为第一激发带：蓝色态 $i=I-2$，浅蓝色态 $i=I-1$。(c)为第二激发带：绿色态 $i=I-4$，浅绿色态 $i=I-3$。黑色箭头表示E2跃迁，黄色箭头表示混合M1+E2跃迁。(d)至(f)为相应的角动量矢量倾斜。','caption','3.2')
add(40,1,5,r'〔续PDF38原段〕……态序列分别为第一激发带的 $\Delta I=2$ 奇自旋和偶自旋序列（图3.2(b)中以黑色显示）。如果 $i=I-3$ 和 $i=I-4$，对应转动态分别构成第二激发带的奇自旋和偶自旋序列（图3.2(c)中以黑色显示）。实际上，激发带出现在 $i<|I|$ 时，也就是 $\vec I$ 偏离中轴时。')
add(40,6,13,r'在奇质量核中，核芯的转动角动量 $\vec R$ 与核子（空穴）的单粒子角动量 $\vec j$ 耦合。中轴是三轴转子优先选择的转动轴，因此 $\vec R$ 一般指向该方向。在极限情况下，单粒子角动量 $\vec j$ 可与 $\vec R$ 纵向（平行）或横向（垂直）耦合[23]。一个转动态的总角动量为两者之和，$\vec I=\vec R+\vec j$。纵向和横向耦合系统的哈密顿量可写成：')
e(40,14,15,'3.6')
add(40,16,16,'以及')
e(40,17,18,'3.7')
add(40,19,26,r'当单粒子角动量 $\vec j$ 沿中轴排列时，形成纵向耦合。这出现在价核子占据给定子壳中部附近轨道的情形。它产生一系列 $\Delta I=2$ 态，构成从 $I=j$ 开始、随后为 $I=j+2,j+4,j+6,\ldots$ 的晕转动带。激发带由 $\vec I$ 偏离中轴形成。可以通过两种不同方式实现：(i)使集体角动量 $\vec R$ 偏离中轴，或(ii)使单粒子角动量 $\vec j$ 偏离中轴。')
add(40,27,34,r'当单粒子角动量与偶偶三轴核芯横向耦合时，$\vec R$ 主要沿中轴，$\vec j$ 指向垂直于中轴的方向，即短轴或长轴。在此情形，价核子占据给定子壳底部（顶部）附近的轨道，作为粒子（空穴）而沿短（长）核轴取向。横向耦合转动带可通过两种方式产生角动量：(i)增大 $R_{\parallel}$，即沿中轴的转动角动量分量，这会……〔续下页〕')
add(41,1,2,r'〔续上页原段〕……产生 $\Delta I=1$ 类型的能带；或(ii)增大 $R_{\perp}$，即沿垂直轴的转动角动量，产生 $\Delta I=2$ 类型的能带。')
add(41,3,13,r'对于 $\Delta I=1$ 类型的能带，当核形状轴对称时，总角动量及单粒子角动量在对称轴上的投影 $K$、$\Omega$ 都是好量子数。能带建立在 $I=\Omega=K$ 态上，随后为 $K+1,K+2,K+3,\ldots$，形成图3.3(a)中黑色的晕带。晕带中的高自旋态通过增大沿中轴的转动角动量 $R_{\parallel}$ 形成。三轴性使额外转动带的能量降低，图3.3(a)用蓝色和红色表示。在三轴情况下 $K$、$\Omega$ 不是好量子数；但已有研究表明，对处于 $i_{13/2}$ 或 $h_{11/2}$ 子壳、且 $\gamma\approx30^\circ$ 的核子而言，特别是在带头附近，$K$、$\Omega$ 近似为好量子数[51]。')
add(41,14,24,r'要产生 $\Delta I=1$ 类型的激发带，原子核沿垂直轴（长轴或短轴，取决于 $\vec j$ 的方向）的转动增加约 $R_{\perp}\approx2\hbar$。因此第一激发带的带头应约为 $I\approx\Omega+2$。例如，建立在 $\Omega=9/2$ 的 $h_{11/2}$ 轨道上的第一激发带，其带头为 $I=13/2$；它包含 $I=13/2,15/2,17/2,19/2,\ldots$ 态，如图3.3(a)蓝色所示。$R_{\perp}$ 再增加约 $2\hbar$ 便形成第二激发带，如图3.3(a)红色所示。图3.3(b)给出了晕带（黑色）、第一激发带（蓝色）和第二激发带（红色）的角动量产生机制。符号 $\parallel$、$\perp$ 分别表示沿中轴和垂直于中轴方向的分量。')
add(41,25,31,r'可按单粒子角动量、总角动量及转动角动量在垂直轴上的投影 $\Omega_{\perp}$、$K_{\perp}$、$R_{\perp}$ 对转动带分类，记为 $(\Omega_{\perp},K_{\perp},R_{\perp})$。晕带由 $(9/2,9/2,0)$ 态构成；第一激发带由 $(9/2,13/2,2)$ 态构成；第二激发带由 $(9/2,17/2,4)$ 态构成。')
add(41,32,34,r'当 Coriolis 相互作用较强时，可形成 $\Delta I=2$ 类型的能带[44]。在某些核中，同一自旋 $I$、$R_{\perp}\approx2$ 的态可能低于 $R_{\perp}\approx0$ 的态。例如在 $^{135}\mathrm{Pr}$ 中……〔续下页〕')
add(42,1,2,r'图3.3：基于 $\Omega=9/2$ 的 $h_{11/2}$ 轨道，示意奇质量三轴核中横向耦合的能带。(a)为 $\Delta I=1$ 带；(b)示意角动量产生机制。(c)为 $\Delta I=2$ 类型的带；图注接着仍写(c)，表示相应角动量产生机制。改编自文献[44]。','caption','3.3')
add(42,3,17,r'〔续上页原段〕……组态 $(\Omega_{\perp},K_{\perp},R_{\perp})=(9/2,13/2,2)$ 的13/2态，低于组态同样写成 $(9/2,13/2,2)$ 的13/2态[45]。在此情况下，晕转动带由最低能态构成，它们不具有同一组 $(\Omega_{\perp},K_{\perp},R_{\perp})$。实际上，在 $I>\Omega_{\perp}$ 的转动带中，每个态相对紧邻的前一态多 $2\hbar$ 角动量，形成 $\Delta I=2$ 的转动态；因此这类能带沿垂直轴转动，如图3.3(c)所示。增大沿中轴的转动角动量会形成激发转动带。第一激发带带头自旋为 $I_{\mathrm{bandhead}}=\Omega+1$，随后为 $I=I_{\mathrm{bandhead}}+2,I_{\mathrm{bandhead}}+4,I_{\mathrm{bandhead}}+6,\ldots$。下一激发带建立在比前一带带头多 $1\hbar$ 的态上。图3.3(c)示意 $\Delta I=2$ 类型的转动带；(d)表示角动量产生机制。')
h(43,1,1,'3.2.2　原子核摆动运动')
add(43,2,7,'Bohr 和 Mottelson 在文献[15]中为偶偶核提出了核摆动运动：当核密度分布沿三条核主轴不相同时，产生这种集体激发模式。对偶偶三轴转子，摆动近似以简单一维转动耦合摆动声子激发，替代三维转动哈密顿量（式3.3）：')
e(43,8,9,'3.8')
add(43,10,17,r'摆动哈密顿量的解描述一组称为摆动带的转动带。其中 $\omega$ 为摆动频率，$n=0,1,2,\ldots$ 为被激发的摆动声子数；$n=0$ 对应基态带，$n=1$ 和 $n=2$ 分别对应第一激发（$\gamma$）带的奇自旋和偶自旋序列，依此类推。实际上，每一个声子激发对应一个激发转动带。在摆动近似内，每次声子激发都会使转动角动量偏离中轴。')
add(43,18,18,r'摆动频率 $\omega$ 由下式定义：')
e(43,19,19,'3.9')
add(43,20,21,'摆动带的激发能和跃迁概率表现出特征性的量子化行为。具体而言：')
add(43,22,22,'(i)转动带的能量线性依赖于 $n$：')
e(43,23,24,'3.10')
add(43,25,28,'这种关系表现为相邻两条摆动带的激发能等间隔。例如，$n=0$ 与 $n=1$ 摆动带激发能曲线之间的间距，与 $n=1$ 和 $n=2$ 摆动带之间的间距相同。')
add(44,1,3,'(ii)所有摆动带内的 $B(E2)$ 跃迁概率相同，因为它们都对应绕同一轴——中轴——的转动：')
e(44,4,4,'3.11')
add(44,5,6,'(iii)带间 $B(E2)$ 跃迁概率线性依赖于 $n$，因为它们连接不同声子激发的能带：')
e(44,7,9,'3.12')
add(44,10,16,r'其中 $Q_0$、$Q_2$ 分别表示内禀四极矩和谱学四极矩。三维转动哈密顿量的摆动近似仅在高自旋处有效[15]。这也许正是迄今尚未在偶偶核低自旋处观察到摆动的原因。在 $A\approx160$ 质量区的奇质量 $^{161\text{–}167}\mathrm{Lu}$ 和 $^{167}\mathrm{Ta}$ 中，已从实验观察到摆动运动；这些转动带对应三轴超形变核形状[4,16,31,34,55,63]。')
add(44,17,24,r'近期 Frauendorf 和 Dönau 研究了奇质量核中的摆动[23]，按单粒子角动量分别垂直或平行于中轴的情况，提出横向和纵向摆动的概念。预期纵向（横向）摆动带具有：(i)摆动频率随自旋增大而升高（降低）；(ii)约化跃迁概率 $B(E2;n,I\to n-1,I-1)$ 和 $B(M1;n,I\to n-1,I-1)$ 应正比于 $n$。')
add(44,25,32,r'此外，两条建立在同一单准粒子组态上、相差一个摆动声子 $\Delta n=1$ 的摆动带，应由以E2成分为主的 $\Delta I=1$ 混合M1+E2跃迁连接，即混合比 $|\delta|>1$。因此，测得模大于1的混合比，是支持摆动解释所必需的实验证据。已有报道在 $^{135}\mathrm{Pr}$、$^{105}\mathrm{Pd}$、$^{183}\mathrm{Au}$、$^{133}\mathrm{La}$、$^{187}\mathrm{Au}$、$^{130}\mathrm{Ba}$ 和 $^{127}\mathrm{Xe}$ 的若干连接跃迁中得到模大于1的混合比，引用依次为[49,65]、[73]、[53]、[14]、[64]、[18,58]、[17]。但近期这些结果受到质疑[27,29,45]……〔续下页〕')
add(45,1,2,r'〔续上页原段〕……并且 $^{135}\mathrm{Pr}$ 的新实验数据提示混合比实际上小于1[44]。')
h(45,3,4,'3.3　准粒子加三轴转子（QTR）模型形式体系')
add(45,5,7,'准粒子加三轴转子（QTR）模型已被广泛用于研究奇质量原子核的三轴性[44,52,61]。模型哈密顿量采用下列形式：')
e(45,8,8,'3.13')
add(45,9,11,'哈密顿量的集体部分已在2.4.2和3.2节讨论。在存在一个价核子的情况下，哈密顿量可写为：')
e(45,12,22,'3.14')
add(45,23,26,r'其中 $\vec I$、$\vec R$、$\vec j$ 分别按通常含义表示总角动量、集体核芯角动量及单粒子角动量，并有 $\vec R=\vec I-\vec j$。$\mathcal{J}_k$ 是沿 $k$ 轴的转动惯量，$k=1,2,3$。这里假定无旋流型转动惯量。')
h(45,27,27,'3.3.1　QTR能量和波函数')
add(45,28,28,'哈密顿量的内禀部分可写为：')
e(46,1,13,'3.15')
add(46,14,18,r'其中 $\lambda_F$ 为费米能，$\Delta$ 为配对能隙参数，按粒子数守恒条件计算[51]；$|\bar\nu\rangle$ 为 $|\nu\rangle$ 的时间反演态。单粒子态 $|\nu\rangle$ 及相应能量通过对角化 $H_{\mathrm{sp}}$ 得到。与文献[39,62]类似，这里采用 Nilsson 型哈密顿量：',original=r'where $\lambda_F$ denotes the Fermi energy, $\Delta$ is the pairing gap parameter and is calculated following particle conservation [51] and $|\bar\nu\rangle$ is the time-reversal state of $|\nu\rangle$. The single-particle states $|\nu\rangle$ and the corresponding energies are obtained by diagonalizing the Hamiltonian $H_{sp}$. Similar to Refs. [39, 62], a Nilsson type Hamiltonian is employed,')
e(46,19,25,'3.16')
add(46,26,30,r'其中 $\rho$ 为拉伸坐标系中的半径，$\varepsilon_2$、$\gamma$ 是通常的 Nilsson 形变参数，$Y_2^{\pm2}$、$Y_2^0$ 为二阶球谐函数，$\kappa$、$\mu$ 为标准 Nilsson 参数。')
add(46,31,31,'单粒子态写为：')
e(46,32,45,None)
add(46,46,48,r'其中 $\Omega$ 为单粒子角动量算符 $j$ 在3轴上的投影；由于时间反演简并，它被限制为 $\ldots,-7/2,-3/2,+1/2,+5/2,\ldots$ [51]。')
add(46,49,52,'将惰性核芯与价核子的内禀波函数耦合，在完整基空间中对角化哈密顿量（式3.13），可得到QTR模型的解。忽略配对相互作用时，可构造强耦合基：')
e(47,1,8,'3.17')
add(47,9,18,r'其中 $D^I_{M,K}$ 表示转动D函数，描述不同取向坐标系之间的变换。上式中 $K$ 取 $\ldots,-7/2,-3/2,+1/2,+5/2,\ldots$。对 $K$ 的限制源自基态在点群 $D_2$ 下的对称化：该条件要求波函数绕体固连 $\hat1$ 轴转动180°后不变，由此得到 $K-\Omega$ 为偶整数[40]。可在这一基（式3.17）中计算 $H_{\mathrm{coll}}$、$H_{\mathrm{int}}$ 的矩阵元；对角化给出QTR模型哈密顿量的本征能和本征态。',original=r'where $D^I_{M,K}$ denote the rotational $D$ functions, which describe transformations between differently oriented coordinate systems. In the equation above, $K$ assumes the values of ..., $-7/2,-3/2,+1/2,+5/2$, ... and the restriction on $K$ is due to the fact that the basis states are symmetrized under the point group $D_2$, which requires the wave function to be invariant under a rotation of $180^\circ$ around the body-fixed $\hat1$-axis, this leads to $K-\Omega$ being an even integer [40]. The matrix elements of $H_{coll}$ and $H_{int}$ can be evaluated in this basis (equation 3.17), and the diagonalization yields the eigenenergies and eigenstates of the QTR model Hamiltonian.')
add(47,19,31,r'在QTR模型中，可以直接纳入配对效应：把基态（式3.17）中的单粒子态 $a_\nu^+|0\rangle$ 替换成BCS准粒子态（本段原文写成 $a_\nu^+|\tilde0\rangle$），得到新的展开基，其中 $|\tilde0\rangle$ 是BCS真空态。准粒子算符 $\alpha_\nu^+$ 给为：',original=r'Pairing effects can be included in a straightforward manner in the QTR model by replacing the single-particle state $a_\nu^+|0\rangle$ in the basis state (equation 3.17) with BCS quasiparticle state $a_\nu^+|\tilde0\rangle$ to get a new expansion basis, where $|\tilde0\rangle$ is the BCS vacuum state. The quasiparticle operators $\alpha_\nu^+$ are given by;')
e(47,32,43,'3.18')
add(47,44,47,r'其中 $u_\nu^2+v_\nu^2=1$。在新基中，QTR哈密顿量的波函数可写为：',original=r'where $u_\nu^2+v_\nu^2=1$. In this new basis, the wavefunctions of the QTR Hamiltonian can be written as;')
e(47,48,52,'3.19')
add(47,53,63,r'这里 $\nu$ 表示准粒子态 $\alpha_\nu^+|\tilde0\rangle$，而非单粒子态 $a_\nu^+$。单粒子能量 $\varepsilon_\nu$ 必须换成准粒子能量 $\varepsilon_\nu^{\prime}=\sqrt{(\varepsilon_\nu-\lambda_F)^2+\Delta^2}$。总哈密顿量写为：',original=r'here $\nu$ represents the quasiparticle states $\alpha_\nu^+|\tilde0\rangle$ instead of the single-particle states $a_\nu^+$. The single-particle energies $\varepsilon_\nu$ must be replaced by the quasiparticle energies $\varepsilon_\nu^{\prime}=\sqrt{(\varepsilon_\nu-\lambda_F)^2+\Delta^2}$. The total Hamiltonian is expressed as;')
e(47,64,70,'3.20')
add(48,1,5,r'式3.14中的哈密顿量具有源自核内禀轴置换的粒子—空穴对称性[51]。一个结果是：与参数 $(\varepsilon_2,\gamma,\lambda_F)$ 核芯耦合的粒子，与参数 $(\varepsilon_2,60^\circ-\gamma,-\lambda_F)$ 核芯耦合的准粒子（空穴），具有完全相同的能谱。')
h(48,6,6,'3.3.2　QTR跃迁概率')
add(48,7,8,'电磁跃迁概率按文献[15]给出，一般形式为：')
e(48,9,9,'3.21')
add(48,10,14,r'其中 $\Gamma(O\lambda)$ 是电磁算符，$O$ 代表算符类型（磁/电），$\lambda$ 为跃迁阶数，$B$ 为约化跃迁概率；$|I_i\rangle$ 和 $\langle I_f|$ 分别表示跃迁前的初态及跃迁后末态的厄米共轭。磁偶极（$\lambda=1$）矩算符定义为：')
e(48,15,17,'3.22')
add(48,18,21,r'求和遍历奇粒子；$g_R=Z/A$ 为核芯g因子，$g_l$、$g_s$ 分别为单粒子轨道角动量及自旋g因子[36]。$\vec R$、$\vec l$、$\vec s$ 取通常含义。电四极（$\lambda=2$）算符定义为：')
e(48,22,25,'3.23')
add(48,26,27,r'它可分为占主导的核芯部分和奇粒子部分。混合比 $\delta_{E2/M1}$ 定义为：')
e(48,28,30,'3.24')
add(49,1,2,r'其中 $\Gamma(E2)$、$\Gamma(M1)$ 分别为电四极和磁偶极算符，$E_\gamma$ 为γ射线能量。这与通常的下列定义对应：')
e(49,3,5,'3.25')
add(49,6,7,'其中 $T(E2)$、$T(M1)$ 分别为相应的电跃迁和磁跃迁概率。')
h(49,8,8,'3.4　QTR模型计算')
add(49,9,15,'本研究采用 Ragnarson 和 Semmes 的QTR模型代码[39,40]，依 GAMPN、ASYMO、PROBMO 的次序逐一运行三个程序。GAMPN计算单粒子本征态和矩阵元；ASYMO计算三轴转子态，并将其与GAMPN生成的单粒子态耦合；最后，PROBMO利用前两个程序的输出计算核电磁跃迁性质[66]。')
h(49,16,16,'3.4.1　GAMPN')
add(49,17,27,r'如前所述，GAMPN计算QTR模型哈密顿量的单粒子态。对质子数为 $Z$、质量数为 $A$ 的特定核进行计算时，程序需要四极形变参数 $\varepsilon_2$、轴不对称形变 $\gamma$、十六极形变参数 $\varepsilon_4$、价核子组态，以及标准 Nilsson 参数 $\kappa$、$\mu$。本计算采用文献[11]中的标准 Nilsson 参数。通常可由势能面（PES）计算或实验数据推得 $\varepsilon_2$、$\gamma$。此外还必须指定感兴趣的单粒子组态空间，即指定计算中纳入哪些费米面附近轨道。')
add(49,28,29,r'程序输出单粒子能量 $\varepsilon_\nu$、单粒子矩阵元，以及在 $|NLJ\Omega\rangle$ 基中展开的单粒子本征态 $|\nu\rangle$。对……〔续下页〕')
add(50,1,4,'〔续上页原段〕……轴对称核形状，程序输出为纯 Nilsson 态；对非对称核形状，输出则是宇称相同、占据概率不同的基态混合。该信息传给下一程序ASYMO。')
h(50,5,5,'3.4.2　ASYMO')
add(50,6,14,r'ASYMO把核芯转动与从GAMPN传来的所选单粒子矩阵元和本征态 $|\nu\rangle$ 耦合，构造准粒子加三轴转子态。计算最多可使用15个单粒子态，通常只纳入靠近费米面的单粒子态子集。ASYMO输入包含这些单粒子态的信息（与GAMPN所用的态相同，或更少）。核芯转动惯量可以从第一 $2^+$ 态的实验能量提取[51]，也可用考虑转动惯量自旋依赖的Harris参数表示[30,48]。')
h(50,15,15,'3.4.3　PROBMO')
add(50,16,20,r'GAMPN和ASYMO的结果传给PROBMO，用于计算所有已算核态之间全部连接跃迁的电磁性质，包括 $B(E2)$、$B(M1)$ 跃迁概率、M1+E2跃迁的混合比 $\delta_{E2/M1}$，以及每个态的四极矩。')

# Map every original extraction block before emitting the bilingual artifact.
def clean(s):
    s=unicodedata.normalize('NFC',s)
    for a,b in [('ﬁ','fi'),('ﬀ','ff'),('ﬂ','fl'),('ﬃ','ffi'),('ﬄ','ffl')]:s=s.replace(a,b)
    s=re.sub(r'(?<=[A-Za-z])-\s*\n\s*(?=[A-Za-z])','',s)
    s=' '.join(s.split())
    for a,b in [('eveneven','even-even'),('oddA','odd-A'),('on equasiparticle','one-quasiparticle'),('onequasiparticle','one-quasiparticle'),('bodyfixed','body-fixed')]:s=s.replace(a,b)
    return s
def union(boxes):return [min(b[0] for b in boxes),min(b[1] for b in boxes),max(b[2] for b in boxes),max(b[3] for b in boxes)]
counts={'S':0,'C':0,'E':0};blocks=[];equations=[];used={};figures=[]
for i,s in enumerate(spec):
    prefix='E' if s['type']=='equation' else 'C' if s['type']=='caption' else 'S'
    counts[prefix]+=1;bid=f'{prefix}{counts[prefix]:03d}'
    originals=[BY[(s['page'],j)] for j in s['source_blocks']]
    box=union([b['bbox'] for b in originals]);raw=''.join(b['text'] for b in originals)
    for j in s['source_blocks']:
        key=(s['page'],j);assert key not in used,key;used[key]=bid
    entry=dict(id=bid,page=s['page'],printed_page=s['page']-11,type=s['type'],order=i+1,
               original_text=s['original_override'] or clean(raw),raw_extraction=raw,
               translation=s['translation'],bbox=box,source_block_indices=s['source_blocks'],
               confidence='medium',refs=[],needs_review=True)
    if s['type']=='equation':
        if s['equation_number']=='3.6':entry['translation']='原式见上图；图中“for longitudinal coupling”意为“用于纵向耦合”。保留原符号与单位写法。'
        if s['equation_number']=='3.7':entry['translation']='原式见上图；图中“for transverse coupling”意为“用于横向耦合”。保留原符号与单位写法。'
        path=f'assets/equations/{bid}.png';(OUT/'assets/equations').mkdir(parents=True,exist_ok=True)
        rect=fitz.Rect(box)+(-7,-5,7,5)
        DOC[s['page']-1].get_pixmap(matrix=fitz.Matrix(2.5,2.5),clip=rect).save(OUT/path)
        entry.update(equation_number=s['equation_number'],latex=None,image_path=path,
                     representation='original-equation-image',confidence='low',
                     transcription_status='LaTeX transcription unavailable; original formula retained intentionally')
        equations.append({k:entry[k] for k in ['id','page','equation_number','latex','image_path','bbox','confidence']})
    blocks.append(entry)

figspec=[('F001',37,'3.1',[219,540,413,716],[],None),
         ('F002',39,'3.2',[153,163,455,600],list(range(1,36)),None),
         ('F003',42,'3.3',[103,79,533,381],[],None)]
for fid,page,no,box,indices,_ in figspec:
    path=f'assets/figures/{fid}.png';(OUT/'assets/figures').mkdir(parents=True,exist_ok=True)
    DOC[page-1].get_pixmap(matrix=fitz.Matrix(2.3,2.3),clip=fitz.Rect(box)).save(OUT/path)
    cap=next(b for b in blocks if b['type']=='caption' and b['page']==page)
    cap['refs']=[fid]
    figures.append(dict(id=fid,page=page,printed_number=no,caption_id=cap['id'],image_path=path,bbox=box,
                        placement_hint='near_first_substantive_discussion_in_source_order',placed_after=cap['id'],
                        alt_text=f'Original Figure{no}',confidence='medium'))
    for j in indices:assert (page,j) not in used;used[(page,j)]=fid

excluded=[];unmapped=[]
for b in RAW:
    key=(b['pdf_page'],b['block'])
    if key in used:continue
    if b['bbox'][3]<70 or (b['pdf_page']==36 and b['block']==24):
        excluded.append(dict(pdf_page=b['pdf_page'],block=b['block'],reason='running header or page number',text=b['text']))
    else:unmapped.append(b)
assert not unmapped,unmapped
glossary=[
 ('triaxiality','三轴性','与γ形变和惯量合同一起解释'),('particle-plus-rotor','粒子加转子','本文模型框架'),
 ('quasiparticle-plus-triaxial rotor (QTR)','准粒子加三轴转子','保留QTR缩写'),
 ('intermediate / short / long axis','中轴／短轴／长轴','本章1/2/3轴依次对应'),
 ('irrotational-flow moments of inertia','无旋流型转动惯量','作者采用的模型假设'),
 ('tilted-precession bands','倾斜进动带','不自动等同摆动带'),('yrast band','晕带','给定自旋最低能态序列'),
 ('wobbling','摆动','声子近似须保留高自旋适用条件'),('longitudinal / transverse coupling','纵向／横向耦合','j相对中轴的理想取向'),
 ('pairing gap','配对能隙','Δ'),('time-reversal state','时间反演态','ν上横线按原图保留'),
 ('strong-coupling basis','强耦合基','D2对称化合同'),('BCS vacuum','BCS真空','不补解出的u/v数值'),
 ('mixing ratio','混合比','δE2/M1'),('quadrupole / hexadecapole deformation','四极／十六极形变','原文quadruple按物理含义译四极'),
 ('GAMPN / ASYMO / PROBMO','GAMPN／ASYMO／PROBMO','单粒子→耦合能级→电磁性质')]
mapping=dict(paper=dict(title='Triaxiality and Rotational Bands in 133Ce — Chapter3 Nuclear Triaxiality',
                       author='Ignasio Wakudyanaye',source_type='pdf',source_format='pdf-text',source_path=str(SRC),language='en',scope_pdf_pages=list(range(36,51))),
             blocks=blocks,pages=[dict(page=p,printed_page=p-11,block_ids=[b['id'] for b in blocks if b['page']==p],figure_ids=[f['id'] for f in figures if f['page']==p]) for p in range(36,51)],
             equations=equations,figures=figures,glossary=[dict(term=a,translation=b,note=c) for a,b,c in glossary],
             extraction_coverage=dict(mapped_raw_block_count=len(used),excluded_running_items=excluded,unmapped=[]),
             source_identity=json.loads((OUT/'source_identity.json').read_text()))
(OUT/'source_map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')

paper=['# 第3章 Nuclear Triaxiality：逐段中英对照读本',
       '来源：用户提供的 Ignasio Wakudyanaye 学位论文。范围：PDF36–50／印刷页25–39。全部正文、标题、图注逐段对应；公式保留原图。本文译文不替代原文的科学证据审核。',
       '## 页索引', '\n'.join(f'- [PDF{p}／p.{p-11}](#page{p})' for p in range(36,51)),
       '## 公式索引','\n'.join(f'- [{q["id"]} · '+(f'Eq.({q["equation_number"]})' if q['equation_number'] else '未编号单粒子展开式')+f'](#{q["id"]}) — PDF{q["page"]}' for q in equations),
       '## 术语表','| Original | 中文 | 使用约定 |\n|---|---|---|\n'+'\n'.join(f'| {a} | {b} | {c} |' for a,b,c in glossary)]
for page in range(36,51):
    paper.append(f'<a id="page{page}"></a>\n## PDF{page}／印刷页{page-11}')
    paper.append(f'[原页视觉核验图](visual-pages/pdf{page:03d}.png)')
    for b in [x for x in blocks if x['page']==page]:
        paper.append(f'<a id="{b["id"]}"></a>\n**Source:** PDF{page}／p.{page-11} · {b["id"]}')
        if b['type']=='equation':
            label=f'Eq.({b["equation_number"]})' if b['equation_number'] else 'Unnumbered single-particle expansion'
            paper.append(f'**Original:** {label} · 原图回退\n\n![Original equation {b["id"]}]({b["image_path"]})\n\n**中文:** {b["translation"]}\n\nLaTeX transcription unavailable；公式以原图为准。')
        else:
            if b['type']=='caption':
                f=next(x for x in figures if x['caption_id']==b['id'])
                paper.append(f'<a id="{f["id"]}"></a>\n### Figure {f["printed_number"]}\n\n**Placed near:** PDF{page} · {b["id"]}\n\n![{f["alt_text"]}]({f["image_path"]})')
            paper.append(f'**Original:** {b["original_text"]}\n\n**中文:** {b["translation"]}')
paper.append('## 阅读提示与独立审计注记\n\n正文保留作者原话及其语气。单位、轴、近似适用域、δ阈值和程序合同的独立审计集中见 [translation_notes.md](translation_notes.md)，不得把这些注记倒写成作者原结论。')
(OUT/'paper.md').write_text('\n\n'.join(paper)+'\n')
coverage=dict(scope_pdf_pages=list(range(36,51)),printed_pages=list(range(25,40)),
              mapped_raw_block_count=len(used),excluded_running_items=len(excluded),unmapped_count=0,
              bilingual_blocks=len(blocks),paragraphs=sum(b['type']=='paragraph' for b in blocks),
              headings=sum(b['type']=='heading' for b in blocks),captions=len(figures),figures=len(figures),
              display_equations=len(equations),numbered_equations=25,unnumbered_equations=1,
              formula_representation='source image fallback',actually_viewed_source_pages=list(range(36,51)),
              pending_translation_blocks=[],scope_complete=True,whole_thesis_complete=False,
              no_canonical_raw_git_mutations=True)
(OUT/'coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(coverage,ensure_ascii=False,indent=2))
