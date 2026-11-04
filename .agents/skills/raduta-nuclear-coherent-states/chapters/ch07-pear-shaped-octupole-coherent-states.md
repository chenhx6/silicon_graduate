# 第 7 章：梨形八极相干态、空间反演对称性破缺与宇称四重带

**来源专著**：A. A. Raduta《Nuclear Structure with Coherent States》（Springer 2016）第 7 章
**对应页码**：印刷 pp. 236–254 / 物理 PDF pp. 243–261

---

## 1. 核心理论推导与八极相干态构建

### 1.1 梨形反射不对称核 (Pear-Shaped Nuclei)
当原子核同时具备宏观四极长椭形变 $\beta_2$ 与八极梨形形变 $\beta_3$ 时，空间反演对称性（$\vec{r} \to -\vec{r}$）在核内禀系中自发破缺。
- **混合玻色相干基态**：
  引入七维八极玻色子创生算符 $b_{3\mu}^\dagger$（$\mu = -3, \dots, +3$）：
  $$|\psi_{\text{oct}}(d_2, d_3)\rangle = \exp\left[ d_2 (b_{20}^\dagger - b_{20}) + d_3 (b_{30}^\dagger - b_{30}) \right] |0\rangle,$$
  其中 $d_2 \propto \beta_2$ 对应四极伸长，$d_3 \propto \beta_3$ 对应八极梨形不对称度。

---

## 2. 双重投影：三维角动量与正负宇称投影

由于相干态不仅破坏全空间转动不变性，更破坏了宇称不变性（$\hat{\mathcal{P}} b_{3\mu}^\dagger \hat{\mathcal{P}}^{-1} = - b_{3\mu}^\dagger$），必须施加双重投影：
1. **正负宇称投影算符**：
   $$\hat{P}^\pm = \frac{1}{2} (1 \pm \hat{\mathcal{P}});$$
2. **正交物理态解构**：
   - **正宇称交替分支（$\pi=+$）**：
     $$|\phi_{IM}^+\rangle \propto \hat{P}_{M0}^I \hat{P}^+ |\psi_{\text{oct}}\rangle \implies I^\pi = 0^+, 2^+, 4^+, 6^+, \dots;$$
   - **负宇称交替分支（$\pi=-$）**：
     $$|\phi_{IM}^-\rangle \propto \hat{P}_{M0}^I \hat{P}^- |\psi_{\text{oct}}\rangle \implies I^\pi = 1^-, 3^-, 5^-, 7^-, \dots$$
3. **交替宇称交错带（Alternating-Parity Bands）**：
   随自旋角动量上升，离心势垒促使正宇称态与负宇称态之间的能量位移差（Energy Staggering）迅速衰减趋近于零：
   $$\Delta E(I) = E(I^-) - \frac{1}{2} [E((I+1)^+) + E((I-1)^+)] \xrightarrow{I \gg 1} 0,$$
   两分支能级交织融合成单一条等间距交错的连续四极转动带序列：$0^+, 1^-, 2^+, 3^-, 4^+, 5^-, \dots$。

---

## 3. 集体增强电偶极 $E1$ 跃迁与手征-八极四重带

### 3.1 梨形电荷-质心分离与宏观内禀偶极矩 $D_0$
由于质子流体与中子流体表面电荷分布与质心发生相对错位，梨形核具有宏观静态内禀电偶极矩：
$$D_0 \approx C_{\text{dip}} Z e A^{-1/3} \beta_2 \beta_3.$$
交替宇称带之间通过极强的集体增强电偶极跃迁相连：$B(E1; I \to I \pm 1) \sim 10^{-2} - 10^{-3}\text{ W.u.}$，比普通稳定核单粒子阻碍跃迁强数千倍！

### 3.2 手征-八极宇称四重带 (Chiral-Parity Quartets)
当三轴非轴对称形变与反射不对称八极形变在同一核素中同时发生时：
- 系统自发破缺时间反演对称性（左/右手征双重态）与空间反演对称性（正/负宇称对偶）；
- 四重简并极小经连续群投影分裂为**四条平行的转动能带**：包含两对具有相同自旋序列、相反宇称的手征双重带（Band $1^+$, Band $2^+$, Band $1^-$, Band $2^-$）；
- 为基础物理中检验时间反演破缺与原子电偶极矩（EDM）提供了最高灵敏度的核结构载体。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/raduta-gcsm-chiral-and-triaxial-rotor-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`chiral-octupole-quartet` 子命令)
- **上游来源**：`knowledge/sources/book-raduta-coherent-states.md`
