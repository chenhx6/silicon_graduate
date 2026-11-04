---
type: method
title: "Li & Chen：铯同位素手征对称性演化、3DTAC-CDFT 临界频率与 MχD 能面合同"
aliases: [Li Chen Cs chirality, 3DTAC-CDFT Cs chiral evolution, MchiD in odd-A Cs isotopes, critical chiral frequency, 119Cs pure proton chirality]
method_type: "chiral-symmetry-evolution-and-mchid-contract"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Chirality and Wobbling in Atomic Nuclei Ch.16, PDF pp.311-322, full chapter reading"
confidence: "high for formalisms, calculated curves, and reported data; conditional for model parameter choices"
tags: [nuclear-chirality, mchid, 3dtac-cdft, cs-isotopes, critical-frequency, aplanarity-angle, triaxial-pes, 119cs, odd-a-chirality]
sources: [book-petrache-chirality-and-wobbling]
---

# Li & Chen：铯同位素手征对称性演化、3DTAC-CDFT 临界频率与 MχD 能面合同

## Purpose

本方法合同基于李剑与陈铎在专著《Chirality and Wobbling in Atomic Nuclei》第 16 章的系统论述，
针对 A≈130 质量区手征核岛中候选核最密集的铯同位素链（\(Z=55, A=120\)–134），
解决核手征几何从奇奇核向奇 \(A\) 核拓展、手征对称性沿同位素链演化边界以及同核内多重手征双重带（M\(\chi\)D）微观机制的判据问题：

1. **3DTAC-CDFT 自洽手征演化与方位角 \(\phi\) 分岔**：在相对论点耦合泛函（PC-PK1）框架下自洽确定转动轴取向角 \((\theta, \phi)\)，以方位角从平面（\(\phi=0^\circ\)）向非共面（\(\phi > 0^\circ\)）的分岔定义手征转变的临界转动频率 \(\omega_{\rm crit}\)；
2. **临界频率随中子数下降的角动量几何机制（图 16.4）**：阐明中子填充 \((gd)\) 与 \((sd)\) 轨道导致其沿短轴与长轴分量减小、沿中间轴集体分量增大，从而使手征旋转在更低转速下即可启动的微观物理机制；
3. **手征岛同位素边界的微观判定**：证明边界核 \(^{120}\mathrm{Cs}\) 与 \(^{134}\mathrm{Cs}\) 在实验可及自旋范围内始终保持 \(\phi=0^\circ\) 共面旋转，在理论上严格确立了 Cs 同位素链手征存在的自然同位素边界；
4. **奇 \(A\) 核两种 3 准粒子手征构型的微观分类**：区分低 \(j\) 中子耦合奇奇芯构型（\(\pi h_{11/2} \otimes \nu h_{11/2}^{-1} \otimes \nu(gd/sd)^1\)）与高 \(j\) 质子结合两对齐中子孔构型（\(\pi h_{11/2} \otimes \nu(h_{11/2})^{-2}\)）；
5. **组态固定约束 CDFT 势能面与 M\(\chi\)D 排他性预言（表 16.1 与图 16.5）**：利用平行输运技术消除绝热能面跃变，微观导出 \(^{125,127,129,131}\mathrm{Cs}\) 局部形变极小，严格证明 \(^{125,129,131}\mathrm{Cs}\) 两个 3 准粒子态均具备稳定三轴度（\(\gamma \sim 13^\circ\)–\(26^\circ\)）从而支持 M\(\chi\)D，而 \(^{127}\mathrm{Cs}\) 因第二构型退化为近轴对称长椭（\(\gamma=0.8^\circ\)）而排除基于该两构型的 M\(\chi\)D；
6. **手征前沿新范式**：记录 \(^{119}\mathrm{Cs}\) 首个全质子 3 准粒子手征带（\(\pi g_{9/2}^{-1} \otimes \pi h_{11/2}^2\)）以及 \(^{126}\mathrm{Cs}\) 奇奇核首例同构型 M\(\chi\)D 的实验与理论前沿。

## Inputs and Assumptions

### 3DTAC-CDFT microscopic framework

三维倾斜轴推转协变密度泛函理论（3DTAC-CDFT）采用微观相对论拉格朗日量与点耦合相互作用泛函（PC-PK1）。
在内禀参考系中，推转拉格朗日量为 \(\hat H' = \hat H - \vec\omega \cdot \hat{\vec J}\)。
转动角速度矢量 \(\vec\omega\) 的方向由球坐标 \((\theta, \phi)\) 唯一定义：

\[
\vec\omega = \omega (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta) ,
\]

其中极角 \(\theta\) 为 \(\vec\omega\) 与长轴（\(l\) 轴）夹角，方位角 \(\phi\) 为 \(\vec\omega\) 在短–中间主平面（\(s-m\) 面）投影与短轴（\(s\) 轴）夹角。
转动方向通过最小化总 Routhian 或自洽要求 \(\vec\omega \parallel \langle\hat{\vec J}\rangle\) 确定。

### Configuration-fixed constrained CDFT

在研究多重手征双重带（M\(\chi\)D）时，传统的绝对能量极小（绝热约束）会因为能级交叉导致势能面（PES）不连续或跳跃。
本方法采用组态固定约束 CDFT（采用 PK1 泛函），利用波函数“平行输运（Parallel-transport）”锁定特定准粒子占据数，
在二维 \((\beta, \gamma)\) 空间追踪各组态在形变改变时的连续势能曲线，获取确定性的局部三轴形变极小 \((\beta_0, \gamma_0)\)。

## What It Can Establish

### 1. 手征临界频率 \(\omega_{\rm crit}\) 与同位素链演化（图 16.4）

通过追踪自洽角度 \((\theta, \phi)\) 随转速 \(\hbar\omega\) 的演化：

- **极角特征（\(\theta > 50^\circ\)）**：在所有 Cs 同位素中，极角始终大于 \(50^\circ\)，这是因为底部单质子占据 \(h_{11/2}\) 沿短轴（\(s\) 轴）产生的强对齐量（\(\approx 5.5\hbar\)）明显压倒顶壳中子孔沿长轴（\(l\) 轴）的反常对齐量（\(\approx 4\hbar\)）；
- **方位角分岔与超临界转变**：在低转速下，\(\phi = 0^\circ\)，系统处于 \((s, l)\) 主平面内的共面旋转相；一旦转速超过临界频率 \(\hbar\omega_{\rm crit}\)，\(\phi\) 发生自发破缺脱离零点（\(\phi > 0^\circ\)），出现明显的非共面手征旋转；
- **临界频率随中子数单调下降**：
  - 在 \(120-126\mathrm{Cs}\)、\(127-128\mathrm{Cs}\) 与 \(129-134\mathrm{Cs}\) 三类构型中，\(\hbar\omega_{\rm crit}\) 均随核质量数 \(A\) 增加而系统性降低；
  - 微观机理：随着中子数填充，中子在 \((gd)\) 或 \((sd)\) 轨道上的角动量在短轴与长轴投影减小，而在中间轴（\(m\) 轴）上的集体惯量投影增大，显著降低了建立三轴立体非共面参考系所需的核芯转速；
- **同位素手征边界确立**：在 \(^{120}\mathrm{Cs}\)（\(N=65\)）与 \(^{134}\mathrm{Cs}\)（\(N=79\)）中，即便计算转速推至 \(\hbar\omega = 0.55\text{ MeV}\) 与 \(0.45\text{ MeV}\)（对应自旋 \(I > 24\hbar\)，超出当前实验可及区），\(\phi\) 始终严格保持为 \(0^\circ\)，从微观理论层面确立了两端同位素的手征边界。

### 2. 电磁比率 \(B(M1)/B(E2)\) 的下落规律（图 16.3）

在半经典微观推转计算中，由于形变 \((\beta, \gamma)\) 沿带变化极小，\(B(E2)\) 近似恒定；
随着转动角频率上升，质子与中子角动量矢量在中间轴逐渐对齐靠拢（剪刀角关闭），导致磁偶极跃迁强度 \(B(M1)\) 呈现平滑单调衰减趋势。
计算给出的 \(B(M1)/B(E2)\) 下落趋势与 \(^{121,123,125-134}\mathrm{Cs}\) 实验高度吻合；而在中子数较少的 \(^{120,122,124}\mathrm{Cs}\) 中计算过高，揭示出轻同位素中超出平均场的动态配对起伏效应更为关键。

### 3. 奇 \(A\) 铯同位素 M\(\chi\)D 的三轴能面判据（表 16.1 与图 16.5）

在 \(^{125,127,129,131}\mathrm{Cs}\) 中，组态固定 CDFT 计算了两类具有手征潜力的 3 准粒子态：
- **构型 \(A1\)**：\(\pi h_{11/2} \otimes \nu h_{11/2}^{-1} \otimes \nu(sd)^1\)（低 \(j\) 中子耦合奇奇手征芯）；
- **构型 \(A2\)**：\(\pi h_{11/2} \otimes \nu (h_{11/2})^{-2}\)（质子粒子结合对齐中子孔）。

计算确立了高度分选性的物理判据：

1. **\(^{125}\mathrm{Cs}\)**：\(A1\) 极小位于 \((\beta=0.25, \gamma=26.3^\circ)\)，\(A2\) 极小位于 \((\beta=0.26, \gamma=24.3^\circ)\)，两构型均具备良好三轴度，**预言存在 M\(\chi\)D**；计算带头激发能（\(A1\) 为 2.75 MeV，实验为 2.322 MeV）与实验吻合；
2. **\(^{127}\mathrm{Cs}\)**：\(A1\) 具有三轴度（\(\beta=0.24, \gamma=14.4^\circ\)），但 \(A2\) 的非轴对称度极小（\(\beta=0.23, \gamma=0.8^\circ\)，退化为轴对称长椭球），**明确排除基于 \(A1/A2\) 构型的 M\(\chi\)D 机制**；
3. **\(^{129}\mathrm{Cs}\)**：\(A1\)（\(\beta=0.21, \gamma=13.4^\circ\)）与 \(A2\)（\(\beta=0.21, \gamma=22.7^\circ\)）均支持三轴性，**支持 M\(\chi\)D 存在**，\(A1\) 带头激发能 2.78 MeV 与实验 2.676 MeV 符合良好；
4. **\(^{131}\mathrm{Cs}\)**：\(A1\)（\(\beta=0.18, \gamma=22.0^\circ\)）与 \(A2\)（\(\beta=0.17, \gamma=24.8^\circ\)）同样表现出双三轴极小，**支持 M\(\chi\)D 存在**，计算带头 2.11 MeV 与实验 2.55 MeV 符合。

### 4. 手征研究前沿新突破

- **纯质子手征性（\(^{119}\mathrm{Cs}\)）**：突破传统必须“质子粒子 + 中子空穴”的限制，在 \(^{119}\mathrm{Cs}\) 中证实由纯质子构型（\(\pi g_{9/2}^{-1} \otimes \pi h_{11/2}^2\)）构造三轴非共面旋转，开创全质子手征体系；
- **奇奇核同构型 M\(\chi\)D（\(^{126}\mathrm{Cs}\)）**：首例报道在相同 2 准粒子构型 \(\pi h_{11/2} \otimes \nu h_{11/2}^{-1}\) 上形成两对手征双带，拓展了多重手征对称性的产生机制。

## Experimental and M\(\chi\)D Spectroscopic Analysis Contract

在分析 Cs 链及 A≈130 区域奇 \(A\) 与奇奇核多重手征候选带时，必须执行以下合同标准：

1. **微观能面三轴度作为 M\(\chi\)D 必要门槛**：宣称同一核内多对手征带，必须对每一个候选构型在自洽组态固定 CDFT/TRS 能面上核验是否具有显著三轴度（通常要求 \(\gamma \ge 12^\circ\)）；如 \(^{127}\mathrm{Cs}\) 的 \(A2\) 构型虽具备 3 准粒子特征，但因 \(\gamma \a0.8^\circ\) 退化为轴对称，禁止指认为手征带；
2. **临界频率自旋门**：手征双带的出现必须高于临界频率 \(\omega_{\rm crit}\)（即方位角分岔点），低自旋区出现的能级重叠应归为前手征共面相或手征振动，不能外推为全自旋静态手征；
3. **双带能级与 \(B(M1)/B(E2)\) 综合检验**：在束谱学实验必须同时测量主带与伴随带的绝对激发能、分支比与多极混合比 \(\delta\)，利用 \(B(M1)/B(E2)\) 单调平缓下降排除单粒子退激污染；
4. **同位素系统学一致性**：Cs 链中临界频率随中子数下降具有普适几何机制，若某一中间同位素反常出现 \(\omega_{\rm crit}\) 暴增，必须首先排查是否有核心形状相变或组态交叉。

## What It Cannot Establish Alone

- 3DTAC-CDFT 属于平均场近似，无法计算穿隧恢复对称性后产生的伴随带能级劈裂与双带量子本征态，需外接集体哈密顿量或 RPA；
- 半经典电磁跃迁公式给出平滑下降的 \(B(M1)/B(E2)\) 曲线，无法重现由于有限多体对称性（如 \(S\) 对称性）引起的带内 \(B(M1)\) 奇偶交错微观细节；
- 能面上的三轴极小是静态基底，若要确证为刚性手征转动，仍需核对势能面对 \(\gamma\) 形变的刚度与零点振动扩散度。

## Knowledge Impact and Learning Decision

李剑与陈铎的第 16 章系统整合了 A≈130 区域手征研究最成熟的同位素体系（Cs 链）：
它在相对论微观密度泛函高度厘清了同位素手征演化机制与临界频率 \(\omega_{\rm crit}\) 变化物理根源，
确立了两类 3 准粒子手征构型的微观能面判据，
成功预测了 \(^{125,129,131}\mathrm{Cs}\) 的 M\(\chi\)D 并排除了 \(^{127}\mathrm{Cs}\)，
为 Wiki 奠定了奇 \(A\) 与奇奇核多重手征态分析的权威微观标准。

本单元完成第 16 章全文、公式推导、表 16.1 及图 16.1–16.5 的全面精读与核验。

## Evidence and Locators

- Ch.16 pp.292–294 / physical PDF pp.311–313：核手征性背景、A≈130 手征岛图 16.1、奇奇核与奇 \(A\) 核构型分类；
- Ch.16 pp.294–298 / physical PDF pp.313–317：3DTAC-CDFT 自洽框架、能量谱对比（图 16.2）、\(B(M1)/B(E2)\) 比值（图 16.3）、转动轴取向角 \((\theta, \phi)\) 演化与临界频率 \(\omega_{\rm crit}\) 下降机制（图 16.4）、\(^{120,134}\mathrm{Cs}\) 边界确立；
- Ch.16 pp.298–301 / physical PDF pp.317–320：组态固定约束 CDFT、平行输运技术、势能面局部极小（图 16.5）、表 16.1（\(^{125,127,129,131}\mathrm{Cs}\) 形变参数与 M\(\chi\)D 判据）；
- Ch.16 pp.301–302 / physical PDF pp.320–321：\(^{119}\mathrm{Cs}\) 全质子手征前沿与 \(^{126}\mathrm{Cs}\) 同构型 M\(\chi\)D 总结；
- 已渲染核对 PDF pp.312、314、315、316、318、319。

## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[grodner-cs-chiral-transition-and-selection-rules-contract]]
- [[petrache-ch3-chiral-geometry-and-selection-boundary]]
- [[multiple-chiral-doublets-and-chiral-parity-quartets]]
- [[multiple-chiral-doublets-mchid-multiconfiguration]]
- [[chiral-geometry-tilted-axis-cranking-and-aplanarity]]
- [[chen-cdft-prm-wobbling-and-fermi-surface-contract]]
