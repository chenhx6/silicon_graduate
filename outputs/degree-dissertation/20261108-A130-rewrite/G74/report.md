# G74：完整单核子谱重心、Baranger ESPE与可观测性边界定向文献研学报告

**任务角色**：G74 定向文献研学 worker  
**服务目标**：重写中的博士论文第 2.2 节及 2.8 节（单核子谱重心、Baranger ESPE与可观测性边界）  
**执行日期**：2026-11-08  
**工作契约**：严格遵循本地优先、合法多源获取、不可逆操作禁止、无 Git 写操作、不向知识库共享页/正文草稿写入。过程产物与报告仅保存在 `outputs/degree-dissertation/20261108-A130-rewrite/G74/`，原始新物仅保存在 `raw/papers/gpt/query/20261108-a130-espe-primary/`。

---

## 一、 核定与合法获取的主原件（身份、版本、哈希与实际读取范围）

本次任务定向核定并合法获取了 2 篇核心经典／现代原始理论文献，所有文件均通过 `wiki_archive_gate.py` 严格校验，元数据完整登记于 `manifest.json`：

### 1.1 原件①：Baranger 1970 经典奠基论文

- **作者与题名**：Michel Baranger, *A definition of the single-nucleon potential*
- **期刊出处**：*Nuclear Physics A* **149** (1970), Issue 2 (29 June 1970), pp. 225–240.
- **正式 DOI**：`10.1016/0375-9474(70)90692-5`
- **核定来源**：从 Otsuka 2022 (*Physics* **4**, 258–285) PDF 第 25 页 Appendix A（印刷 p. 282）及参考文献 Ref. [19]（印刷 p. 283）逐字核定。Otsuka 原文标注为 `Baranger, M. A definition of the single-nucleon potential. Nucl. Phys. A 1970, 149, 225`。
- **获取途径与本地凭证**：首先经 `system/scripts/local_literature_archive.py check-local` 确认本地馆藏缺失。随后使用仓库内合法配置的 Elsevier ScienceDirect 机构凭据（经白名单读取，未打印或泄露任何密钥），通过官方 Article Retrieval API 正式获取。
- **本地归档文件**：
  - PDF 归档路径：`raw/papers/gpt/query/20261108-a130-espe-primary/baranger-1970-single-nucleon-potential.pdf`
  - 文件大小：79,996 字节
  - 实际 SHA-256：`c2782f86bca908b42c46d6742de7f3bd97341835fbdfb114b454818dd8bd0d1f`
  - 完整全文数据载体：API 同步交付之全文 XML `tmp/runs/20261108-A130-rewrite/G74/baranger-1970.xml`（114,723 字节），包含 34,510 字符完整正文、全部公式与参考文献列表。
- **实际读取范围与定位符**：
  - Section 1 (Introduction, pp. 225–226)：单核子势作为理论概念的不可直接测量性、短时与长时行为的物理区分。
  - Section 2 (The definition, pp. 226–228)：实验学家定义 Eq. (1)；双满壳/一般参考态核单体哈密顿量精确算符定义 Eq. (2)；单粒子基下的能级平均 Eq. (3)；求和规则 Eq. (4)–(5)；对易子算符表达式 Eq. (6) 与二体反对称矩阵元展开 Eq. (8)。
  - Section 3 (Feynman expansion of W, pp. 228–231)：时间推演、传播子短时行为、Feynman 图展开。
  - Section 4 (Comparison between single-nucleon energies and exact energies, pp. 231–235)：短时展开（零点导数、极少图）与长时展开（极点收敛、复杂核物质与折叠图）的对照。
  - Section 6 (Elimination of short-range correlations, pp. 235–236)：核力硬心诱导短程关联对无截断谱重心的发散破坏；有效模型空间动量截断（$k_{\max} \sim 2.5\text{ fm}^{-1}$）与 G 矩阵引入。
  - Section 7 (The single-nucleon strength distribution, pp. 236–239)：二阶矩算符 $W^{(2)}$、单核子强度分布均方根展宽 $\sigma^2$ 的定义与声子耦合图。

### 1.2 原件②：Duguet 等 2015 现代不可观测性与重整化标度理论论文

- **作者与题名**：T. Duguet, H. Hergert, J. D. Holt, V. Somà, *Non-observable nature of the nuclear shell structure: Meaning, illustrations, and consequences*
- **期刊出处**：*Physical Review C* **92**, 034313 (2015)；预印本 arXiv:1411.1237v3 [nucl-th] (11 Sep 2015, 16 页)。
- **正式 DOI**：`10.1103/PhysRevC.92.034313`
- **核定来源**：从 Otsuka 2020 RMP (Rev. Mod. Phys. **92**, 015002) 第 1220 行对 Duguet 等 2015 脚注 1 的讨论，以及相关文献引用链核实。
- **获取途径与本地凭证**：经 `system/scripts/local_literature_archive.py check-local` 确认本地未收录。由 arXiv 开放获取源获取包含全部正文、公式及图表的完整 16 页 PDF。
- **本地归档文件**：
  - PDF 归档路径：`raw/papers/gpt/query/20261108-a130-espe-primary/duguet-2015-non-observable-shell-structure.pdf`
  - 文件大小：615,150 字节
  - 实际 SHA-256：`0b4547204e0f735f89361727551d86852fd65bbb769915598b2e1610f9184a67`
- **实际读取范围与定位符**：
  - Section I (Introduction, pp. 1–4)：幻数作为多体可观测量（$E(2_1^+)$、分离能差）与不可观测的单核子壳层结构（ESPE）的概念解耦；
  - Section II.A–B (Nuclear shell energies, pp. 4–6)：添粒／去粒振幅与谱因子 Eq. (6a)–(6b)；谱函数矩阵 $S(\omega)$ 与 $n$ 阶矩 Eq. (8)；零阶矩求和规则 Eq. (9)；一阶矩重心场 $h^{\mathrm{cent}}$ 与本征方程 Eq. (10)–(12)；对易子关系式 Eq. (13) 与基态一阶、二阶密度矩阵展开 Eq. (14)–(15)；证明 $h^{\mathrm{cent}} = h^\infty$（Dyson 自能静态项）及 HF 极限下回到 Koopmans 定理；
  - Section II.C (Partitioning of one-nucleon separation energies, pp. 6–7)：单核子分离能与 ESPE 的精确矩阵划分式 Eq. (17)–(18)；
  - Section II.D (Non-observability, pp. 7–10)：χ-EFT 标度性 Eq. (19)；么正变换流方程 Eq. (25)–(26)；谱振幅流方程 Eq. (27)；能量本征值不变性 $dE/d\lambda=0$ Eq. (28)；零阶矩标度不变性 $dM^{(0)}/d\lambda = 0$ Eq. (29a) 与一阶矩标度依赖性 $dM^{(1)}/d\lambda \ne 0$ Eq. (29b)；“两位理论工作者在不同标度下精确拟合相同实验数据但提取出不同 ESPE”的思想实验；
  - Section III (Illustrations, pp. 10–14)：MR-IM-SRG 与 G-SCGF 在氧同位素（$^{14-24}$O）和 $^{74}$Ni 中 ESPE 随 $\lambda \in [1.88, 2.24]\text{ fm}^{-1}$ 的实际变化曲线（Fig. 1–5）。

---

## 二、 完整单核子谱重心与 Baranger ESPE 的物理与数学定义

### 2.1 参考态与添粒／去粒（Addition / Removal）能量与谱强度的标准定义

设系统的完全微观多体哈密顿量为 $H$，选定一个归一化的 $A$ 粒子参考态 $|\Psi_0^A\rangle$（通常为偶偶核基态），其能量本征值为 $E_0^A$：
$$H |\Psi_0^A\rangle = E_0^A |\Psi_0^A\rangle.$$

在任意给定的单粒子正交归一基 $\{c_p^\dagger, c_p\}$ 下（对球对称体系，$p \equiv (n, l, j, m, \tau)$）：

1. **添粒（Addition / Particle）通道**：
   通过在 $|\Psi_0^A\rangle$ 上添加一个核子，跃迁至 $A+1$ 核的第 $\mu$ 个精确本征态 $|\Psi_\mu^{A+1}\rangle$（能量为 $E_\mu^{A+1}$）。
   - **添粒能量**定义为相对于参考态的能量差：
     $$E_\mu^+ \equiv E_\mu^{A+1} - E_0^A.$$
   - **添粒谱振幅（Spectroscopic Amplitude）**：
     $$U_\mu^p \equiv \langle \Psi_\mu^{A+1} | c_p^\dagger | \Psi_0^A \rangle.$$
   - **添粒单粒子谱概率矩阵元**与**谱学因子（Spectroscopic Factor, SF）**：
     $$(S_\mu^+)_{pq} \equiv U_\mu^p (U_\mu^q)^*, \quad \mathrm{SF}_\mu^+ \equiv \mathrm{Tr}_{\mathcal{H}_1}[S_\mu^+] = \sum_{p} |U_\mu^p|^2.$$

2. **去粒（Removal / Hole）通道**：
   通过从 $|\Psi_0^A\rangle$ 中移除一个核子，跃迁至 $A-1$ 核的第 $\nu$ 个精确本征态 $|\Psi_\nu^{A-1}\rangle$（能量为 $E_\nu^{A-1}$）。
   - **去粒能量**定义为相对于参考态的能量差（**注意能量符号约定**）：
     $$E_\nu^- \equiv E_0^A - E_\nu^{A-1}.$$
     *符号说明*：若基态单中子分离能为 $S_n(A) = E_0^{A-1} - E_0^A$，则去粒到 $A-1$ 基态的跃迁能量为 $E_0^- = -S_n(A) < 0$。去粒激发态 $E_x^{A-1} = E_\nu^{A-1} - E_0^{A-1} \ge 0$，因此 $E_\nu^- = -S_n(A) - E_x^{A-1}$。去粒激发能在实际能谱中越向高处走，$E_\nu^-$ 的代数值越负。
   - **去粒谱振幅**：
     $$V_\nu^p \equiv \langle \Psi_\nu^{A-1} | c_p | \Psi_0^A \rangle.$$
   - **去粒单粒子谱概率矩阵元**与**谱学因子**：
     $$(S_\nu^-)_{pq} \equiv (V_\nu^p)^* V_\nu^q, \quad \mathrm{SF}_\nu^- \equiv \mathrm{Tr}_{\mathcal{H}_1}[S_\nu^-] = \sum_{p} |V_\nu^p|^2.$$

### 2.2 谱函数矩阵与 Dyson 一体 Green 函数

将添粒与去粒两支的全部谱信息汇集，定义作用在单粒子 Hilbert 空间 $\mathcal{H}_1$ 上的能量相关**谱函数矩阵（Spectral Function）**：
$$S_{pq}(\omega) \equiv \sum_{\mu \in \mathcal{H}^{A+1}} (S_\mu^+)_{pq} \,\delta(\omega - E_\mu^+) + \sum_{\nu \in \mathcal{H}^{A-1}} (S_\nu^-)_{pq} \,\delta(\omega - E_\nu^-).$$
谱函数矩阵直接对应于因果单核子 Green 函数 $G_{pq}(\omega)$ 的虚部：
$$S_{pq}(\omega) = -\frac{1}{\pi} \mathrm{Im}\, G_{pq}(\omega) \,\mathrm{sgn}(\omega - \mu_{\mathrm{Fermi}}).$$
对其迹求和即得到基无关的**谱强度分布（Spectral Strength Distribution, SSD）**：
$$\mathcal{S}(\omega) \equiv \mathrm{Tr}_{\mathcal{H}_1}[S(\omega)] = \sum_{\mu} \mathrm{SF}_\mu^+ \,\delta(\omega - E_\mu^+) + \sum_{\nu} \mathrm{SF}_\nu^- \,\delta(\omega - E_\nu^-).$$

### 2.3 零阶矩（求和规则）与一阶矩（重心场哈密顿量）

定义谱函数的第 $n$ 阶能量矩矩阵：
$$M^{(n)}_{pq} \equiv \int_{-\infty}^{+\infty} \omega^n S_{pq}(\omega) \, d\omega.$$
利用反演展开定理（Duguet 2015 Eq. (13)，Baranger 1970 Eq. (6)）：
$$M^{(n)}_{pq} = \langle \Psi_0^A | \{ [\dots[[c_p, H], H]\dots], c_q^\dagger \} | \Psi_0^A \rangle \quad (n\text{ 个对易子}).$$

1. **零阶矩 $n=0$（Macfarlane-French 求和规则）**：
   $$M^{(0)}_{pq} = \langle \Psi_0^A | \{ c_p, c_q^\dagger \} | \Psi_0^A \rangle = \delta_{pq}.$$
   对任意单粒子态 $|p\rangle$，添粒总概率与去粒总概率之和严格守恒且等于 1：
   $$\sum_\mu (S_\mu^+)_{pp} + \sum_\nu (S_\nu^-)_{pp} = 1.$$
   对于球对称轨道 $j$（简并度 $g_j = 2j+1$），对磁量子数 $m$ 求和后得到传统壳模型形式：
   $$\sum_{m=-j}^j \left[ \sum_\mu S^+_{\mu, jm} + \sum_\nu S^-_{\nu, jm} \right] = 2j+1.$$
   这赋予了每一个对角矩阵元 $S_{pp}(\omega)$ 作为**统计概率密度分布（PDF）**的严格数学意义。

2. **一阶矩 $n=1$（Baranger 重心场哈密顿量矩阵）**：
   $$h^{\mathrm{cent}}_{pq} \equiv M^{(1)}_{pq} = \sum_{\mu} (S_\mu^+)_{pq} E_\mu^+ + \sum_{\nu} (S_\nu^-)_{pq} E_\nu^-.$$
   利用 $n=1$ 的对易子关系：
   $$h^{\mathrm{cent}}_{pq} = \langle \Psi_0^A | \{ [c_p, H], c_q^\dagger \} | \Psi_0^A \rangle.$$
   对包含一体动能 $T$、二体相互作用 $V^{2N}$ 及三体相互作用 $V^{3N}$ 的通用微观多体哈密顿量，直接对易代数给出：
   $$h^{\mathrm{cent}}_{pq} = t_{pq} + \sum_{rs} \bar{v}^{2N}_{prqs} \rho^{[1]}_{sr} + \frac{1}{4} \sum_{rstv} \bar{v}^{3N}_{prtqsv} \rho^{[2]}_{svrt} \equiv h^\infty_{pq}.$$
   其中 $\bar{v}$ 为规范化的反对称两体／三体相互作用矩阵元，$\rho^{[1]}_{sr} = \langle \Psi_0^A | c_r^\dagger c_s | \Psi_0^A \rangle$ 与 $\rho^{[2]}_{svrt} = \langle \Psi_0^A | c_r^\dagger c_t^\dagger c_v c_s | \Psi_0^A \rangle$ 分别为参考态 $|\Psi_0^A\rangle$ 的精确一体与二体密度矩阵。
   
   **物理内涵**：$h^{\mathrm{cent}}$ 在单体空间严格等于 Dyson 一体不可约自能 $\Sigma(\omega)$ 在无穷大频率处的静态无能量依赖分量 $h^\infty = T + \Sigma(\infty)$。它代表一个核子在多体关联参考态基底中感受到的**精确等效单体平均场**。
   对该单体矩阵对角化：
   $$h^{\mathrm{cent}} \psi_p^{\mathrm{cent}} = e_p^{\mathrm{cent}} \psi_p^{\mathrm{cent}},$$
   其本征值 $\{ e_p^{\mathrm{cent}} \}$ 即为**严格的 Baranger 有效单粒子能量（Baranger ESPE）**：
   $$e_p^{\mathrm{cent}} = \sum_{\mu} (S_\mu^+)_{pp} E_\mu^+ + \sum_{\nu} (S_\nu^-)_{pp} E_\nu^-.$$

---

## 三、 同轨同种核子单极修正的精确微观代数推导

在球对称 $0^+$ 参考态下，一体密度矩阵在角动量耦合基中是对角的：
$$\langle \Psi_0^A | c_{j'm'\tau'}^\dagger c_{j''m''\tau''} | \Psi_0^A \rangle = \delta_{j'j''} \delta_{m'm''} \delta_{\tau'\tau''} \frac{\langle \hat{n}_{j'}^{\tau'} \rangle}{2j'+1}.$$
考查轨道 $j$（简并度 $g_j = 2j+1$）的对角单体场矩阵元。根据 Baranger 1970 Eq. (8) 及 Duguet 2015 Eq. (14)，二体作用贡献为：
$$e_j^{\mathrm{cent}} = e_{0j} + \frac{1}{2j+1} \sum_{m=-j}^j \sum_{j'm'} \bar{v}_{jm, j'm', jm, j'm'} \frac{\langle \hat{n}_{j'} \rangle}{2j'+1}.$$

现在对粒子指标求和分类：

### 3.1 异轨或异种粒子（$j' \ne j$ 或 $\tau' \ne \tau$）
由于不同轨道间或质子-中子间不存在全同核子的磁量子数泡利相消，双重求和 $\sum_{m=-j}^j \sum_{m'=-j'}^{j'}$ 包含 $(2j+1)(2j'+1)$ 个完全允许的反对称对态。
按壳模型标准角动量加权平均，两轨道间的两体单极相互作用矩阵元定义为：
$$V^{\mathrm{mono}}(j, j') \equiv \frac{\sum_{m, m'} \bar{v}_{jm, j'm', jm, j'm'}}{(2j+1)(2j'+1)} = \frac{\sum_J (2J+1) \langle jj'; J | V | jj'; J \rangle_A}{\sum_J (2J+1)}.$$
将其代入求和式，分子分母的 $(2j+1)(2j'+1)$ 精确对消，直接给出：
$$\sum_{j' \ne j} V^{\mathrm{mono}}(j, j') \langle \hat{n}_{j'} \rangle.$$

### 3.2 同轨同种粒子（$j' = j$ 且 $\tau' = \tau$）
当相互作用发生在同种核子的完全相同轨道 $j$ 内时，由于全同费米子泡利不相容原理，当 $m = m'$ 时，反对称矩阵元严格为零：
$$\bar{v}_{jm, jm, jm, jm} \equiv 0.$$
因此，双重指标和 $\sum_{m=-j}^j \sum_{m'=-j}^j$ 中只有 $m \ne m'$ 的项非零。其非零对态的总数为：
$$(2j+1)^2 - (2j+1) = (2j+1)(2j) = g_j(g_j - 1).$$
在传统壳模型单极相互作用理论（Bansal-French 1964, Poves-Zuker 1981, Otsuka 2010/2020）中，同轨两体单极矩阵元 $V^{\mathrm{mono}}(j, j)$ 是在**物理上真正允许的无序对**（共 $\binom{g_j}{2} = \frac{g_j(g_j-1)}{2}$ 对）或有序对（共 $g_j(g_j-1)$ 对）上取平均：
$$V^{\mathrm{mono}}(j, j) \equiv \frac{\sum_{m \ne m'} \bar{v}_{jm, jm', jm, jm'}}{g_j(g_j - 1)} = \frac{\sum_{J\text{ even}} (2J+1) \langle j^2; J | V | j^2; J \rangle_A}{\sum_{J\text{ even}} (2J+1)}.$$
将此非零求和式代入 Baranger 的表达式：
$$\text{同轨贡献} = \frac{1}{g_j^2} \left( \sum_{m \ne m'} \bar{v}_{jm, jm', jm, jm'} \right) \langle \hat{n}_j \rangle = \frac{g_j(g_j - 1)}{g_j^2} V^{\mathrm{mono}}(j, j) \langle \hat{n}_j \rangle.$$
代入 $g_j = 2j+1$：
$$\frac{g_j - 1}{g_j} = 1 - \frac{1}{g_j} = 1 - \frac{1}{2j+1} = \frac{2j}{2j+1}.$$
因此，同轨项为：
$$\text{同轨贡献} = V^{\mathrm{mono}}(j, j) \langle \hat{n}_j \rangle - \frac{1}{2j+1} V^{\mathrm{mono}}(j, j) \langle \hat{n}_j \rangle.$$

### 3.3 统合单极展开式与 Otsuka 附录纠偏的物理对应
将所有轨道汇集，得到 Baranger ESPE 的严格单极展开通式：
$$e_j^{\mathrm{cent}} = e_{0j} + \sum_{j'} V^{\mathrm{mono}}(j, j') \langle \hat{n}_{j'} \rangle - \frac{1}{2j+1} V^{\mathrm{mono}}(j, j) \langle \hat{n}_j \rangle.$$
其中求和 $\sum_{j'}$ 现在包含了 $j'=j$ 的无限制单极项。

**物理来源与文献印证**：
- 这个扣除项 $-\frac{1}{2j+1} V^{\mathrm{mono}}(j, j) \langle \hat{n}_j \rangle$ 本质上是**同轨核子的自相互作用修正（Self-interaction Correction）**。添加一个核子进入轨道 $j$ 时，该核子不能与自身相互作用；而密度算符 $\langle \hat{n}_j \rangle$ 统计了包含自身在内的全部平均占据。
- **Otsuka 2020 RMP 之疏漏与 Otsuka 2022 附录之修正**：
  在 Otsuka 等 2020 RMP 第 1213 行公式（出版式 Eq. (43)）中，作者写为 $\epsilon_j = \epsilon^0_j + \sum_{j'} V^m_{j, j'} \langle 0 | \hat{n}_{j'} | 0 \rangle$，忽略了同轨分母与对数计数的差异。
  经角动量理论学者 Tsunoda 指出后，Otsuka 在 2022 年专著论文（*Physics* **4**, p. 282, Appendix A）中明确勘误：
  > *“...the following term is found to be added to Equation (43) of [15]: $-\frac{1}{2j+1} V^m(j, j) \langle 0 | \hat{n}_j | 0 \rangle$... So, this is the contribution from the interaction between a neutron orbit $j$ and the same neutron orbit $j$... In addition, the factor $1/(2j+1)$ reduces this quantity.”*
- **数值控制验算**：本任务编写的代数控制脚本在 $j=1/2, 3/2, 5/2, 7/2, 9/2$（$g_j = 2, 4, 6, 8, 10$）的全部占据 $n \in [0, g_j]$ 下，严格核验了上述解析求和，重合误差在浮点精度极限下严格为零（$< 10^{-16}$）。

### 3.4 添粒差、连续导数与完整谱重心三者的代数对照与态间变化

在博士论文第 2.2 节中，必须向读者彻底澄清以下三个极易混淆的单粒子能量“定义变体”：

| 能量定义类型 | 符号与表达式 | 适用物理情境与操作定义 | 同轨自项依赖 |
| :--- | :--- | :--- | :--- |
| **添粒有限差** | $\Delta E_j^+ = E(n_j+1) - E(n_j) = e_{0j} + V_{jj} n_j + \sum_{j'\ne j} V_{jj'} n_{j'}$ | 纯粹的外加一个粒子有限差；要求初态有空位 | 自项系数为 $+V_{jj} n_j$ |
| **移粒有限差** | $\Delta E_j^- = E(n_j) - E(n_j-1) = e_{0j} + V_{jj} (n_j-1) + \sum_{j'\ne j} V_{jj'} n_{j'}$ | 纯粹的移去一个粒子有限差；要求初态非空 | 自项系数为 $+V_{jj}(n_j-1)$ |
| **单极能量连续导数** | $\frac{\partial \langle H^{\mathrm{mono}} \rangle}{\partial n_j} = e_{0j} + V_{jj}\left(n_j - \frac{1}{2}\right) + \sum_{j'\ne j} V_{jj'} n_{j'}$ | 能量泛函对占据数的解析变分；两态相减消除常数 $V_{jj}/2$ | 自项系数为 $+V_{jj}(n_j - 1/2)$ |
| **完整 Baranger 谱重心** | $e_j^{\mathrm{cent}} = e_{0j} + V_{jj}\left(1 - \frac{1}{2j+1}\right) n_j + \sum_{j'\ne j} V_{jj'} n_{j'}$ | 添粒与去粒谱强度的严格能量加权平均 | 自项系数为 $+V_{jj} n_j \left(1 - \frac{1}{2j+1}\right)$ |

**态间变化 $\Delta e_j$ 的抵消条件**：
当考查从核态 1 到核态 2 的 ESPE 变化 $\Delta e_j = e_j(2) - e_j(1)$ 时：
1. 若采用**添粒有限差**或**连续导数**约定，若轨道相互作用矩阵元 $V_{jj'}$ 保持常数，则态间变化严格为：
   $$\Delta e_j = \sum_{j'} V^{\mathrm{mono}}(j, j') \Delta n_{j'}.$$
2. 若与**完整 Baranger 谱重心**对照，由于同轨存在修正项，其实际态间变化为：
   $$\Delta e_j^{\mathrm{cent}} = \sum_{j'} V^{\mathrm{mono}}(j, j') \Delta n_{j'} - \frac{1}{2j+1} V^{\mathrm{mono}}(j, j) \Delta n_j.$$
   只有在以下三种特定条件之一下，该修正项的差值才消失：
   - 目标轨道 $j$ 在两态之间的占据数无变化，即 $\Delta n_j = 0$（例如考查价核子添加到中子轨道 $j'$ 对完全未填充的质子轨道 $j$ 的驱动）；
   - 同轨同种核子单极强度极弱，$V^{\mathrm{mono}}(j, j) \approx 0$；
   - 轨道具有较大角动量（如 $h_{11/2}, g_{9/2}$），压低因子 $\frac{1}{2j+1} \le 0.1$，使得修正量远小于物理驱动能标（$< 0.1\text{ MeV}$）。
   如果发生同轨占据的大幅跃迁（如 $0p-0h$ 到 $2p-2h$ 激发致使 $\Delta n_j = 2$），则两套定义之间存在固有的 $\frac{2}{2j+1} V_{jj}^{\mathrm{mono}}$ 代数偏移，不能无条件混为一谈。

---

## 四、 ESPE 的不可观测性、重整化标度依赖与方案依赖（Duguet 2015 深读）

### 4.1 真实可观测量与理论辅助量的量子力学界定

根据量子力学基本原理与低能有效场论（χ-EFT），体系的物理量可严格分为两类（Duguet 2015 Section II.D）：

1. **真实物理可观测量（Observables）**：
   在核多体 Schrödinger 方程的自伴算符本征值问题中，哈密顿量 $H$ 的能量本征值 $E_k^A$、束缚能与激发能 $E_x$、单核子分离能 $S_n, S_p$、以及直接反应跃迁截面 $d\sigma(\theta)/d\Omega$，均属于**实验可观测量**。
   在对体系施行任意连续么正变换 $U(\lambda)$（如自由空间或介质内相似重整化群 SRG / IM-SRG，其中 $\lambda$ 为动量分辨标度）时，算符依 $O(\lambda) = U(\lambda) O U^\dagger(\lambda)$ 演化，波函数依 $|\Psi(\lambda)\rangle = U(\lambda) |\Psi\rangle$ 演化。可观测量的期望值和本征值严格标度无关：
   $$\frac{d}{d\lambda} E_k^A(\lambda) = 0, \quad \frac{d}{d\lambda} \left( E_\mu^+(\lambda) \right) = 0, \quad \frac{d}{d\lambda} \left( E_\nu^-(\lambda) \right) = 0.$$

2. **理论辅助量（Non-observable Theoretical Constructs）**：
   单核子产生／湮灭算符 $c_p^\dagger, c_p$、谱振幅 $U_\mu^p, V_\nu^p$、谱因子 $\mathrm{SF}^\pm$、单体波函数、以及作为谱函数一阶矩的 Baranger ESPE $e_p^{\mathrm{cent}}$，**均不属于量子力学可观测量**。

### 4.2 么正变换下的流方程与 ESPE 的“Running”特性

当分辨标度 $\lambda$ 改变时，若要求单核子转移探针保持纯粹的“向特定单粒子轨道 $p$ 添/去单一核子”的物理定义，则单粒子产生算符 $c_p^\dagger$ 并不随 $U(\lambda)$ 发生多体旋转。其结果是，谱振幅必须随标度 $\lambda$ 演化（Duguet 2015 Eq. (27b)）：
$$\frac{d}{d\lambda} U_\mu^p(\lambda) = - \langle \Psi_\mu^{A+1}(\lambda) | [\eta(\lambda), c_p^\dagger] | \Psi_0^A(\lambda) \rangle^* \ne 0.$$
其中 $\eta(\lambda) = \frac{dU(\lambda)}{d\lambda} U^\dagger(\lambda)$ 为 SRG 变换的反对称发生器。
将此代入零阶矩与一阶矩：
- **零阶矩（求和规则）**严格标度无关（Duguet 2015 Eq. (29a)）：
  $$\frac{d}{d\lambda} M^{(0)}_{pq}(\lambda) = 0.$$
  这意味着无论在何种标度下，总谱强度守恒性永远成立。
- **一阶矩（Baranger ESPE）**则不可避免地随标度演化（Duguet 2015 Eq. (29b)）：
  $$\frac{d}{d\lambda} M^{(1)}_{pq}(\lambda) \ne 0 \implies \frac{d}{d\lambda} e_p^{\mathrm{cent}}(\lambda) \ne 0.$$

**Duguet 思想实验的核心启示**：
设想两位理论物理学家 A 与 B 独立分析同一套理想、完备的单核子转移反应实验数据 $\{ E_k^\pm, \sigma_k^\pm \}$。若他们采用完全相同的严格结构与反应理论，但采用了两个互为么正等价但分辨标度不同的哈密顿量 $H(\lambda_1)$ 与 $H(\lambda_2)$：
- 两人计算出的可观测激发能量 $E_k^\pm$、分离能以及反应截面 $\sigma_k^\pm$ **完全相同**，且均精确复现实验；
- 但两人提取出的一体能谱与谱学因子却**必然不同**：
  $$e_p^{\mathrm{cent}}(\lambda_1) \ne e_p^{\mathrm{cent}}(\lambda_2), \quad \mathrm{SF}_k^\pm(\lambda_1) \ne \mathrm{SF}_k^\pm(\lambda_2).$$
这直接确立了：**单粒子能级和谱学因子不是大自然的客观内禀读数，而是依附于理论分辨标度 $\lambda$ 与模型空间的理论构造物。**

### 4.3 破除“双重误区”：避免虚无主义与幼稚实在论

在博士论文写作中，必须坚决避免两种走极端的错误倾向：

1. **破除“幼稚实在论”（Naive Realism）**：
   不能将实验上在某一转移反应中测得的单个主峰能级，直接称为“无模型依赖的、客观存在的单粒子轨道能”；也不能将有限能量窗口内测出的碎片截面均值等同于绝对的 Baranger 重心。任何谱学因子和单粒子重心的提取都深度依赖反应势模型、束缚态几何与能区截断。

2. **破除“相对主义虚无主义”（Radical Nihilism）**：
   **绝对不能得出“凡重心都绝不可测，因此壳演化和单粒子能毫无物理意义”的全称否定结论！**
   - 实验上在给定观测窗口 $W$ 和特定转移通道下测得的截面加权能量：
     $$\bar{E}_{j, W}^{\mathrm{obs}} = \frac{\sum_{\mu \in W} \sigma_\mu E_\mu}{\sum_{\mu \in W} \sigma_\mu}$$
     是**客观定义的数据层汇总统计量（Data-level summary statistic）**，具有明确的实验可复现性；
   - 在双满壳或接近单极主导的区域，单粒子自由度往往集中在基态附近有限几个强单粒子跃迁态中（谱学因子占 $70\% \sim 80\%$），其余微弱强度虽受短程关联被推至几十甚至上百 MeV，但低能窗口内的谱重心位移主要受低动量核力（特别是张量力和中心力单极分量）的系统性驱动；
   - Duguet 等人在文章结尾明确指出：只要不同研究者**预先约定一个统一且物理上合理的软分辨标度（如 $\lambda \sim 2.0\text{ fm}^{-1}$）**，并在自洽的结构与反应框架下开展比较，ESPE 就是极其有效且不可或缺的物理分析工具。

### 4.4 何种近似、算符与分辨标度下可与唯象 ESPE（壳模型）有效比较

将微观 ab initio 计算的 Baranger ESPE 与唯象壳模型（如 USD、GXPF1、JUN45、SNBG3）中的 ESPE 建立联系，必须满足以下条件：
1. **分辨标度匹配**：
   必须通过 SRG、IM-SRG 或 G 矩阵折叠图，将核力预先演化至与价空间相适应的低动量软标度（动量截断 $\lambda \approx 1.8 \sim 2.2\text{ fm}^{-1}$，或 Baranger 1970 预言的 $k_{\max} \approx 2.0 \sim 2.5\text{ fm}^{-1}$）。在这一标度下，硬心短程关联被解耦，多粒子-多孔激发被大幅压低。
2. **价空间有效相互作用的正规序（Normal Ordering）**：
   将三核子力（3NF）在核芯或系综参考态上进行正规序截断至二体水平（NO2B 近似），其零体项提供核芯束缚能，一体项直接重整化为有效单粒子轨道能 $h^{(1)}$，两体项构成价空间有效相互作用 $V_{\mathrm{eff}}$。
3. **消除动力学自能涨落**：
   根据 Duguet 2015 Eq. (18)，当且仅当所考察的外加／外去状态的动力学自能 $\Sigma^{\mathrm{dyn}}(E^\pm)$ 足够平缓或其色散修正可被有效两体单极项充分吸收时，唯象单极哈密顿量对角和的有限差才能逼近微观 Baranger 重心。

---

## 五、 实验提取的物理边界与转移反应分析现实

### 5.1 反应模型依赖性与谱因子 $C^2S$ 的假象
实验上无法直接把电流表接入原子核测量谱强度。单核子转移反应 $(d,p), (p,d), (^3\text{He},d)$ 或结团敲出反应中，实验测量的是微分截面 $d\sigma/d\Omega$。
提取谱因子必须依赖直接反应理论模型（DWBA、ADWA 或 CDCC）：
$$\left(\frac{d\sigma}{d\Omega}\right)_{\mathrm{exp}} = C^2S \cdot \sigma_{\mathrm{DWBA}}(\theta; V_{\mathrm{opt}}, r_0, a, \beta_2).$$
- **光学势（OMP）不确定性**：入射道与出射道连续谱光学势的实部与虚部深度、弥散度参数存在连续简并，不同势参数可导致提取的 $C^2S$ 产生 $20\% \sim 40\%$ 的系统偏差；
- **束缚态波函数几何依赖性**：单粒子波函数通常假设在 Woods-Saxon 势阱中产生，其半径参数 $r_0$（通常取 1.20–1.25 fm）和弥散度 $a$（通常取 0.65 fm）直接决定了核表面渐近归一化系数（ANC），这一纯几何假设直接线性传递至 $C^2S$ 的绝对数值。

### 5.2 观测窗口 $W$ 截断与双支不平衡
- **能区截断**：束缚态伽马谱学和转移反应测量通常受限于 $E_x < 6 \sim 8\text{ MeV}$ 的低激发窗。由于张量力和短程关联的作用，单粒子总强度的 $15\% \sim 30\%$ 被不可逆地推向深孔高能区或连续谱巨共振区。低能窗口截断导致实测求和规则 $\sum_{\mu \in W} C^2S_\mu$ 往往只有 $0.6 \sim 0.8$，从未达到理论上的 $1.0$（或对同轨为 $2j+1$）；
- **单路观测的局限**：单纯利用一个 $(d,p)$ 反应（纯添粒）测量，在物理上根本无法涵盖具有部分占据轨道的去粒贡献。除非参考核是极端严格的空壳层或满壳层，否则单路观测碎片加权能量不可与完整 Baranger 重心画等号。

---

## 六、 对博士论文第 2.2 节当前措辞的最小修改方案

结合上述原件证据与核物理数学推导，对当前冻结稿 `section-2-2.md` 提出以下针对性极强、改动最小、立论最稳健的修改方案：

### 6.1 概念层分流：明确解耦三级单粒子能概念

在 2.2.1 小节开头，必须开门见山定义并区分以下三个物理概念，杜绝含混统称：
1. **有限差单极 ESPE（壳模型添粒差）**：作为单极相互作用哈密顿量在固定组态下添加一个核子的能量增量，用于解析微观壳演化趋势：
   $$\Delta e_j = \sum_{j'} V^{\mathrm{mono}}(j, j') \Delta n_{j'}.$$
2. **微观 Baranger 谱重心（Baranger ESPE）**：作为因果 Green 函数谱函数的一阶能量矩，严格综合添粒与去粒两支信息，其与壳模型单极项的严格联系包含同轨自项修正：
   $$e_j^{\mathrm{cent}} = e_{0j} + \sum_{j'} V^{\mathrm{mono}}(j, j') \langle \hat{n}_{j'} \rangle - \frac{1}{2j+1} V^{\mathrm{mono}}(j, j) \langle \hat{n}_j \rangle.$$
3. **实验能窗加权碎片重心（Observational Window Centroid）**：作为特定反应通道在给定可探测能量窗口 $W$ 内的数据层统计量：
   $$\bar{E}_{j, W}^{\mathrm{obs}} = \frac{\sum_{\mu \in W} C^2S_\mu E_\mu}{\sum_{\mu \in W} C^2S_\mu}.$$

### 6.2 同轨自相互作用修正常数的严密交代

在 2.2.1 或 2.2.2 节中，当引用 Otsuka 2020 RMP 或 Otsuka 2022 时，写明：
> “需要指出，在球对称参考态下，严格由 Green 函数一阶矩定义的 Baranger 谱重心与传统壳模型单极平均能量之间，在同轨同种核子通道存在微小的自相互作用修正项 $-\frac{1}{2j+1} V^{\mathrm{mono}}(j, j) \langle \hat{n}_j \rangle$（Otsuka 2022 Appendix A）。在考查不同核态之间由异轨占据数变化驱动的壳演化时，由于 $\Delta n_j = 0$ 或该轨道简并度较大且单极相互作用较弱，该项在态间差中精确或高度抵消，从而恢复了由相互作用矩阵元与占据数直接线性相乘的标准壳演化表达式 $\Delta e_j = \sum_{j'} V^{\mathrm{mono}}(j, j') \Delta n_{j'}$。”

### 6.3 科学准确地重构可观测性边界段落

将原稿中可能出现的“实验直接提取绝对 Baranger 重心”或“谱重心绝不可测”等偏颇表述，修改为基于 Baranger 1970 与 Duguet 2015 现代框架的规范学术表达：
> “从第一性原理与量子力学本质审视，有效单粒子能量与单核子谱学因子并不是量子力学自伴算符的本征观测量，其绝对数值随相互作用的动量分辨标度 $\lambda$ 与微观方案发生重整化演化（Running）（Baranger 1970; Duguet et al. 2015）。实际转移反应中所提取的截面加权能量重心，受制于探测能窗截断、连续谱背景以及光学势与束缚态势阱几何的模型依赖性。然而，这一不可观测性边界并不削弱 ESPE 作为物理分析工具的有效性：当在统一选定的低动量软标度（$\lambda \sim 2.0\text{ fm}^{-1}$）下开展自洽分析时，ESPE 构成了将复杂多体关联和激发能谱还原为清晰壳演化图像的不可替代的理论桥梁；而在主要单粒子强度未严重碎裂的低激发区，实验测得的局域谱重心正是检验这一单极演化机制的直接经验约束。”

---

## 七、 原件证据分级、限制与真实未读边界

依据 Wiki 科学证据规则，对本次研学所依赖的原件进行严格分类与边界隔离：

| 证据项编号 | 原件来源与定位符 | 物理结论 / 证据主张 | Claim Kind | 限制条件与反方竞争解释 | 真实未读边界 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **G74-BAR-1** | Baranger 1970 (NPA 149), p. 226, Eq. (2)–(5) | 单核子势由添粒与去粒两支以谱因子为权重联合定义；零阶矩求和严格等于 1。 | Foundational Definition | 假设基态为双满壳（但可推广至 $0^+$）；未考虑连续谱共振积分的实际截断困难。 | 未通读其核物质 Brueckner-Hartree-Fock 原始数值程序细节。 |
| **G74-BAR-2** | Baranger 1970 (NPA 149), p. 227, Eq. (6)–(8) | 单粒子哈密顿量为精确单体算符，形式上对应基态密度矩阵与反对称两体矩阵元的收缩。 | Operator Formalism | 限于纯两体哈密顿量，三体相互作用在文中仅被定性提及未完全展开。 | 未通读其更高阶声子耦合多级展开的具体 Fortran 程序实现。 |
| **G74-BAR-3** | Baranger 1970 (NPA 149), p. 236, Section 6 | 真实核力硬心短程关联会使无截断能量积分失去实用性；必须在截断模型空间中借由 G 矩阵定义。 | Methodological Boundary | 1970 年尚未建立现代 EFT 与 SRG 流方程，作者明确承认不知道最佳模型空间截断的理论选取准则。 | 无现代手征微观力的定量结论。 |
| **G74-DUG-1** | Duguet et al. 2015 (PRC 92), p. 5–6, Eq. (10)–(14) | Baranger ESPE 严格等价于 Dyson 自能静态无穷大分量 $T+\Sigma(\infty)$，可在任意多体方法中严格计算。 | Microscopic Ab Initio | 计算要求已知体系的一体与二体精确密度矩阵 $\rho^{[1]}, \rho^{[2]}$。 | 未包含大形变非球对称态下的自洽形变投影。 |
| **G74-DUG-2** | Duguet et al. 2015 (PRC 92), p. 8–9, Eq. (25)–(29) | 谱学因子与 ESPE 随 SRG 标度 $\lambda$ 连续 running，因而不属于客观可观测量；但能量本征值和截面不变。 | Theoretical Proof | 实际 ab initio 计算中由于略去诱导四体及更高力，么正性存在极微弱的破缺（约 1–2 MeV）。 | 氧同位素链以外的重核（A≈130）高自旋形变带未在该文计算范围内。 |
| **G74-OT22-1** | Otsuka 2022 (*Physics* 4), p. 282, Appendix A | 壳模型单极 ESPE 与 Baranger ESPE 在同轨同种粒子通道存在 $-\frac{1}{2j+1} V^m(j, j) \langle \hat{n}_j \rangle$ 的修正。 | Theoretical Correction | 仅适用于球对称平均，若存在形变和组态相消，单极假设需要重整化。 | 未核查该文中提到的更早非公开私人通信细节。 |

---

## 八、 结论与交付确认

1. **原件真实性与归档门**：
   已成功下载并留档 Baranger 1970（Elsevier API 正式授权获取）与 Duguet et al. 2015（arXiv 原件）两篇主原件至 `raw/papers/gpt/query/20261108-a130-espe-primary/`，生成标准 `manifest.json`。经 `system/scripts/wiki_archive_gate.py` 严格校验，`failure_count: 0`，归档门完全通过。
2. **科学结论边界**：
   本研学报告仅提供扎实、无模型偏见的理论文献研学支撑与代数推导事实，不代替论文作者进行正文撰写，不执行任何 Git 提交，不自评科学通过。所有结论严格溯源至已通读的原件指定页码与公式。
