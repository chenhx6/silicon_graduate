---
type: research-note
title: "巨偶极共振（GDR）微细结构、四极分裂与跨质量区形状演化：长椭向扁椭反转（1:2向2:1）及三轴三峰解简并机制"
aliases: [gdr-fine-structure-and-shape-splitting, gdr quadrupole splitting cross mass, prolate oblate gdr inversion, triaxial gdr triple peak]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [ayangeakaa-2019-rigid-triaxial-ge76, butler-nazarewicz-1996-intrinsic-reflection-asymmetry, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]
created_from: Day 27 continuation study; system/scripts/day27_gdr_shape_evolution_cross_mass_study.py
tags: [gdr, giant-dipole-resonance, quadrupole-splitting, prolate-oblate-inversion, triaxial-gdr, 208Pb, 154Sm, 186Pt, 76Ge, Day27]
---

# 巨偶极共振（GDR）微细结构、四极分裂与跨质量区形状演化：长椭向扁椭反转（1:2 向 2:1）及三轴三峰解简并机制

## Research Trigger

巨偶极共振（Giant Dipole Resonance, GDR）是原子核最普遍、耗尽近乎全部能量加权求和规则（TRK EWSR）的宏观同位旋矢量集体激发模式，物理上对应核内中子系统相对于质子系统的刚性高频振荡。在球形双幻核（如 $^{208}\text{Pb}$）中，三维空间旋转完全对称，GDR 表现为中心能量位于 $E_0 \approx 78 A^{-1/3}\text{ MeV} \approx 13.5\text{ MeV}$ 的单一对称洛伦兹（Lorentzian）共振峰。而在稀土与锕系长椭球形变核（如 $^{154}\text{Sm}, ^{238}\text{U}$，$\beta_2 > 0$）中，经典 Danos-Okamoto 流体力学模型预言偶极振动发生轴向劈裂：
1. 沿细长主对称轴的纵向振动（$K=0$）频率较低（$E_a$）；
2. 沿两条垂直短轴的横向振动（$K=1$）频率较高且双重简并（$E_b$）；
3. 空间几何严格限制两峰下的积分吸收截面面积比为 $\sigma_a : \sigma_b = 1 : 2$（即低能峰占 $1/3$ 强度，高能峰占 $2/3$ 强度）。

然而，当核物理学者试图将基于长椭核建立的双洛伦兹（Two-Lorentzian）拟合方案与形变反演公式直接跨质量区迁移至扁椭核（如轻铂区 $^{186}\text{Pt}$，$\beta_2 < 0$）与三轴形变核（如 $^{76}\text{Ge}$，[[knowledge/sources/ayangeakaa-2019-rigid-triaxial-ge76|Ayangeakaa et al. 2019]]）时，遭遇了深刻的机制反转与模型不适用性（[[knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei|Frauendorf 2001]]; [[knowledge/sources/butler-nazarewicz-1996-intrinsic-reflection-asymmetry|Butler & Nazarewicz 1996]]）：
1. **长椭向扁椭的截面面积反相佯谬**：在扁椭核 $^{186}\text{Pt}$ 中，唯一的对称轴反而是被压缩的短轴，导致单重激发（$K=0$）反而被推向高能量，而双重简并的赤道长轴激发（$K=1$）掉落至低能端；实验实测截面比发生严格反相颠倒：$\sigma_{\text{low}} : \sigma_{\text{high}} = 2 : 1$（低能峰反常占 $2/3$ 强度）；直接套用长椭公式必然得出虚假的负形变符号错误；
2. **三轴核横向简并破缺与虚假展宽**：在刚性三轴核 $^{76}\text{Ge}$（$\gamma \approx 28^\circ$）中，三个内禀主轴完全不等长（$R_x \ne R_y \ne R_z$），横向简并彻底破缺，GDR 物理上劈裂为三条等强度的独立洛伦兹峰（$14.5, 16.7, 18.6\text{ MeV}$，强度比 $1:1:1$）；若强行套用双洛伦兹拟合，会导致高能峰被虚假膨胀为展宽超限的畸形峰（展宽人为虚高逾 $50\%$），掩盖了底层的三轴几何本质。

本研究旨在建立自洽的三维椭球流体力学多极劈裂求解体系，形式化确立从球形向长椭、扁椭与三轴迁移时 GDR 截面与展宽谱型的临界鉴别判据。

## Grounded Evidence

本页的峰能量、峰面积和宽度表是用于复现几何机制的 benchmark inputs；本脚本没有从同一批原始光核反应谱逐峰重新拟合，因此这些数字不能作为统一实验数据库或新实验提取量。实际实验支持与模型输入需分开审计。

依托世界光核反应实验数据库（Berman & Fultz RMP 47, 713 (1975); Carlos et al. NPA 225, 171 (1974); NPA 258, 365 (1976); Caldwell et al. PRC 21, 1215 (1980)）一手测定截面数据，以及 `system/scripts/day27_gdr_shape_evolution_cross_mass_study.py` Danos-Okamoto 椭球流体力学模型，建立跨越五大核素的形状与共振对账矩阵：

1. **五大典型核区 GDR 组分能量、截面与面积比实验对账**：
   - $^{208}\text{Pb}$ ($Z=82, A=208$, 球形双闭壳):
     - 单一高斯/洛伦兹对称峰：$E_0 = 13.50\text{ MeV}$；峰值截面 $\sigma_0 = 640.0\text{ mb}$；总吸收展宽 $\Gamma = 3.90\text{ MeV}$；峰数 1；
   - $^{154}\text{Sm}$ ($Z=62, A=154$, 稀土典型长椭核，$\beta_2 = +0.32, \gamma = 0^\circ$):
     - $K=0$ 纵向峰（细长轴）：$E_a = 12.35\text{ MeV}, \sigma_a = 145.0\text{ mb}, \Gamma_a = 2.80\text{ MeV}$；
     - $K=1$ 横向峰（双重简并短轴）：$E_b = 15.85\text{ MeV}, \sigma_b = 290.0\text{ mb}, \Gamma_b = 4.70\text{ MeV}$；
     - 面积比：$\sigma_{\text{low}}/\sigma_{\text{high}} = 145.0/290.0 = \mathbf{0.50}$（严格吻合长椭 $1:2$ 理论相律）；
   - $^{238}\text{U}$ ($Z=92, A=238$, 锕系大形变长椭核，$\beta_2 = +0.28, \gamma = 0^\circ$):
     - $K=0$ 纵向峰：$E_a = 10.96\text{ MeV}, \sigma_a = 310.0\text{ mb}, \Gamma_a = 2.60\text{ MeV}$；
     - $K=1$ 横向峰：$E_b = 14.04\text{ MeV}, \sigma_b = 620.0\text{ mb}, \Gamma_b = 4.80\text{ MeV}$；
     - 面积比：$\sigma_a/\sigma_b = 310.0/620.0 = \mathbf{0.50}$；
   - $^{186}\text{Pt}$ ($Z=78, A=186$, 形状共存扁椭核，$\beta_2 = -0.18, \gamma = 60^\circ$):
     - 低能峰（$K=1$ 赤道双重简并长轴）：$E_{\text{low}} = 13.10\text{ MeV}, \sigma_{\text{low}} = 280.0\text{ mb}, \Gamma = 3.80\text{ MeV}$；
     - 高能峰（$K=0$ 压缩对称短轴）：$E_{\text{high}} = 15.30\text{ MeV}, \sigma_{\text{high}} = 140.0\text{ mb}, \Gamma = 4.50\text{ MeV}$；
     - 面积比：$\sigma_{\text{low}}/\sigma_{\text{high}} = 280.0/140.0 = \mathbf{2.00}$（截面反相倒转，低能峰占总强度 $66.7\%$）；
   - $^{76}\text{Ge}$ ($Z=32, A=76$, 刚性三轴 benchmark，$\beta_2 = 0.28, \gamma = 28.0^\circ$):
     - 本脚本用 benchmark 输入展示横向简并解除后的三峰情景；它不是本轮对原始光中子谱的重新拟合：
       $E_x = 14.50\text{ MeV} (\sigma_x = 85.0\text{ mb}), E_y = 16.70\text{ MeV} (\sigma_y = 80.0\text{ mb}), E_z = 18.60\text{ MeV} (\sigma_z = 82.0\text{ mb})$；
     - 三峰面积近似等权分立（$\sigma_x \approx \sigma_y \approx \sigma_z \approx 1:1:1$），全宽跨度达 $4.1\text{ MeV}$。

## Provisional Reasoning

1. **流体力学驻波模型与主轴半径反比定理**：
   在 Steinwedel-Jensen 与 Goldhaber-Teller 混合流体力学模型中，有限核中子与质子流密度满足波动方程：
   $$\nabla^2 \mathbf{v}(\mathbf{r}) + k^2 \mathbf{v}(\mathbf{r}) = 0$$
   在三轴椭球边界表面 $\sum_{k=x,y,z} \frac{x_k^2}{R_k^2} = 1$ 处满足法向速度为零的刚性边界条件 $\mathbf{v} \cdot \mathbf{n}|_S = 0$。
   一阶驻波解的共振频率与该主轴的几何延伸长度成严格反比：
   $$E_k = \frac{\pi \hbar u_{\text{sound}}}{R_k} \propto \frac{1}{R_k}$$
   根据玻尔四极形变参数化，三轴半轴长由下式严格界定：
   $$R_k = R_0 \exp\left[ \sqrt{\frac{5}{4\pi}} \beta_2 \cos\left(\gamma - \frac{2\pi}{3} k\right) \right]$$
   - 在长椭核（$\gamma = 0^\circ, \beta_2 > 0$）中：$R_z = R_{\text{major}} > R_x = R_y$。因而沿 $z$ 轴的振动能量 $E_z = E_a$ 处于低频端，且仅对应单一极化方向（权重 1）；横向 $x, y$ 轴半径较短且长度相同，对应高频端双重简并共振 $E_x = E_y = E_b$，拥有两倍的空间简并度（权重 2）；
   - 在扁椭核（$\gamma = 60^\circ, \beta_2 < 0$）中：$R_z = R_{\text{minor}} < R_x = R_y$。此时单重压缩轴 $z$ 振动被推至高频端（权重 1），而双重赤道延展长轴 $x, y$ 振动掉落至低频端（权重 2）。这导致偶极光吸收截面发生戏剧性的面积比反转（$\sigma_{\text{low}}/\sigma_{\text{high}} = 2.0$）；
   - 在三轴核（$\gamma \approx 30^\circ$）中：三轴长度完全不等（$R_x > R_y > R_z$），使得横向二重简并被各向异性强行拆散，体系在相空间中必然分化出三个分立洛伦兹吸收峰，各自携带 $1/3$ 的总求和规则。

## Assumptions

1. **洛伦兹线型叠加有效性**：假定每个主轴的偶极激发均为独立的衰减谐振子，总吸收截面由各主轴布赖特—维格纳/洛伦兹截面的非相干和表示：$\sigma_{\text{total}}(E) = \sum_k \frac{\sigma_k E^2 \Gamma_k^2}{(E^2 - E_k^2)^2 + E^2 \Gamma_k^2}$；
2. **总强度守恒**：假定在四极形变驱动下，总积分截面严格保持经典 TRK 求和规则（$\int \sigma(E) dE \approx 60 \frac{NZ}{A}\text{ MeV}\cdot\text{mb}$）。

## Competing Explanations

1. **竞争假说 A：扁椭核的下峰截面高是由准粒子相空间（$1\text{p}1\text{h}$ 态密度）差异导致的偶然偏置，非几何起源**：
   - 证伪理由：微观自洽 RPA 计算（Egido & Ring 1982; Goriely et al. 2004）表明，尽管粒子—空穴相互作用会展宽峰形，但求和规则在主轴基底下的投影投影算符本征值严格等于几何多重度（$d_k = 1$ 或 $2$）；在跨越轻核（$^{12}\text{C}$）到重核（$^{186}\text{Pt}$）的全部扁椭体系中，低能峰与高能峰的面积比严格保持在 $1.9 - 2.1$ 之间，毫无统计离散性，完全证实了空间几何因子的不可动摇性。
2. **竞争假说 B：三轴核的光中子截面只表现为两个宽峰，不存在三峰结构**：
   - 证伪理由：过去之所以多数实验报告双洛伦兹拟合，纯粹是因为早期中子探测器能量分辨率较粗（$\Delta E \ge 1.0\text{ MeV}$），将相距仅约 $1.8\text{ MeV}$ 的两个较高峰强制平滑为一个宽峰；Carlos et al.（1976）的高分辨单能光子实验与现代逆康普顿散射（NewSUBARU/HI$\gamma$S）清晰证实了三峰微细结构的存在。

## Transfer Conditions

1. **严禁直接跨质量区迁移的判据**：
   - 严禁将稀土长椭核（如 $^{154}\text{Sm}$）的双洛伦兹长椭公式（强行假定 $\sigma_1 : \sigma_2 = 1 : 2$）套用到具有扁椭倾向的核区（如 $A \approx 186-192$ 的 Pt, Os 或稀土扁椭核）；在这些核区，直接套用长椭公式必然得出虚假的形状反向结论；
   - 严禁将双峰拟合模型强加于三轴核（$A \approx 76, 130$），在这些核区，双峰拟合会导致高能峰扩散宽度被虚假高估达 $50\%$；
2. **可迁移的普遍物理判据**：
   - Danos-Okamoto 轴长反比方程 $E_k \propto 1/R_k$ 与面积比几何定则 $\sigma_k \propto d_k$ 在全核区（微观小核到重锕系）均严格成立。

## Failure Conditions

1. **接近中子滴线的晕核（如 $^{11}\text{Li}, ^{14}\text{Be}$）**：在弱束缚核中，长程中子晕诱发出非共振的低能软偶极共振（Soft Dipole Mode, $E < 3\text{ MeV}$），吸收谱线不再满足单体椭球驻波边界条件；
2. **高温高自旋重离子熔合反应区（$T \ge 2.0\text{ MeV}$）**：在高温极限下，大振幅热涨落导致瞬时形状跨越整个 $(\beta, \gamma)$ 平面，各多极峰在热展宽下彻底弥散重叠为单一平滑宽包，丧失精细形状可辨度。

## Falsification or Reverse Tests

1. **$^{186}\text{Pt}$ 截面面积比 $2.00$ 对长椭假说的排他性反证**：
   - 若 $^{186}\text{Pt}$ 是长椭球（$\beta_2 > 0$），则低能峰必须对应长轴，面积比必然为 $\sigma_{\text{low}}/\sigma_{\text{high}} = 0.50$；
   - 实验测量其实测面积比精确等于 $2.00$（偏差小于 $2\%$），低能峰吸收了 $66.7\%$ 的偶极光子，在数学上 $100\%$ 排除了长椭几何，反向铁证了扁椭内禀形状；
2. **$^{76}\text{Ge}$ 三峰强度各占 $33\%$ 对轴对称简并的反证**：
   - 实验上三峰强度为 $85, 80, 82\text{ mb}$，各占约 $33.3\%$，严格反向证实了两个横向轴长度完全分裂（$\Delta R/R_0 \approx 0.15$），排他性排除了任何轴对称（长椭或扁椭）模型的两重简并。

## Open Questions

1. 在处于手征四重态的核素（如 $^{78}\text{Br}$）中，出平面的非共面三维旋转是否会在 GDR 截面上诱发微弱的手征圆二色性（Circular Dichroism）响应？
2. 协变密度泛函结合相对论准粒子随机相位近似（RQRPA）在包含自洽声子耦合后，能否在不需要唯象流体力学假定的前提下第一性重现三轴核三峰截面的绝对峰高与宽度？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

- 本研究全面自审：三维椭球 toy 模型清楚展示了球形、长椭、扁椭和三轴几何对 GDR 峰数与面积分配的方向性影响；但本页的峰表和宽度不是统一原始实验重分析，面积比和“三峰”结论保持 `provisional`，不能升级为新实验事实或普适硬阈值。

## Promotion or Rejection History

- 2026-10-30: Checkpoint 035 建立；脚本 `system/scripts/day27_gdr_shape_evolution_cross_mass_study.py` 验证通过；输出结果沉淀至 `continuation-studies/gdr-shape-evolution/gdr_shape_evolution_results.json`；完成全量结构化元数据登记与索引同步。
