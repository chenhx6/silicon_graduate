# Tonev 2006：¹³⁴Pr 跃迁几率与手征检验原实验（090）

本单元取得并完整阅读 APS 正式 5 页 PRL 原文，逐页核看全部图表（Figs. 1–3）及 Table I。Tonev 等的实验直接测定了 ¹³⁴Pr 双带的寿命和跃迁几率，其结论明确为：**不支持静态手征（static chirality）**，而**动态手征（dynamic chirality）**或准粒子与核形状自由度的耦合仍然是兼容的解释。不能把该工作简述为“完全否定了手征”。

## 来源、获取与范围

D. Tonev et al., *Transition Probabilities in ¹³⁴Pr: A Test for Chirality in Nuclear Systems*, Physical Review Letters **96**, 052501 (2006)，DOI [10.1103/PhysRevLett.96.052501](https://doi.org/10.1103/PhysRevLett.96.052501)。Crossref、APS 落地页和 PDF 首页元数据完全匹配。PDF 5 页、347,475 bytes，SHA256 `eac94a5ff8402144aa66b003fbafada85e180126941063eb5bfc62be5b20d134`。原文及中间文件在 `tmp/day24-tonev134pr-primary-090/`。开读前记录在 `primed-recall.md`（非盲测、不计分）。

从 APS 官方链接直接取得正式 PDF；未声明为开放许可证。落地页无补充材料链接，SI 在文章入口和正文范围内记为未识别，不做全网不存在声明。路由记录见 `access-manifest.json`。

## 实验设置与 DDCM 方法

实验在斯特拉斯堡 IReS 的 Vivitron 加速器上进行，使用 **¹¹⁹Sn(¹⁹F,4n)¹³⁴Pr** 反应。采用 Euroball IV 探测器阵列和 BGO 内球。事件触发要求 Ge cluster/clover 至少 3 击发且内球至少 3 击发，使用了标准 Compton add-back。

寿命测量结合了两种方法：

1. **RDDS**：束能 87 MeV，靶为 0.5 mg/cm² ¹¹⁹Sn 蒸发在 1.8 mg/cm² ¹⁸¹Ta 箔上面向束流；反冲核速度 \(v=0.98(2)\%c\)，在 6.0 mg/cm² Au 箔中停止。测量了 20 个靶-阻停体距离（从电接触到 2500 μm）。数据分析使用标准微分衰变曲线法（DDCM），对所考察能级下方的跃迁设置移动（S）和未移动（U）成分门。
2. **DSAM**：束能 83 MeV，靶为 0.7 mg/cm² ¹¹⁹Sn 蒸发在 9.5 mg/cm² ¹⁸¹Ta 背衬上用于阻停反冲核。反冲核减速历史使用修改版 DESASTOP 进行 Monte Carlo 模拟，线形分析按 DSAM 的 DDCM 方法处理。

Euroball clover 环同时用作 Compton 偏振计。确认了 306 keV 双峰的延迟成分为 E1（与 Roberts 2003 一致）；结合方向关联（DCO）与线偏振分析，为 \(\Delta I=1\) 带内跃迁指认了以 M1 为主且 E2 极小的多极性，\(\Delta I=2\) 带内和带间跃迁表现为 E2 特征。

**数据完整性边界**：正文第 3 页明确说明：“Details of the lifetime analysis, branching ratios and linear polarizations coefficients will be reported in a forthcoming publication [15] (Tonev et al., to be published)”。因此，本篇 PRL 正文并没有给出逐线的完整数值分支比表、偏振系数数值表、内转换系数处理或协方差矩阵；这些量留待后续长文。

## Table I：两带寿命测定结果

Table I 给出的物理量均为 **平均寿命 \(	au\)（ps）**，而非半衰期 \(T_{1/2}\)：

| 带 | 态 \(I^\pi\)| \(	au\) (ps) | 方法 |
|---|---|---:|---|
| Band 1 | \(10^+_1\) | 4.93(15) | RDDS（与 Klemme 1999 相符） |
| Band 1 | \(11^+_1\) | 1.614(326) | RDDS |
| Band 1 | \(12^+_1\) | 1.425(130) | RDDS |
| Band 1 | \(13^+_1\) | 0.904(50) | RDDS |
| Band 1 | \(14^+_1\) | 0.882(147) | DSAM（表注：RDDS与DSAM均测定且吻合，列统计更高的DSAM） |
| Band 1 | \(15^+_1\) | 0.608(68) | DSAM |
| Band 1 | \(16^+_1\) | 0.562(47) | DSAM |
| Band 1 | \(17^+_1\) | 0.422(30) | DSAM |
| Band 1 | \(18^+_1\) | 0.249(10) | DSAM |
| Band 2 | \(13^+_2\) | 1.443(50) | RDDS/DSAM 范围 |
| Band 2 | \(14^+_2\) | 1.280(50) | RDDS/DSAM 范围 |
| Band 2 | \(15^+_2\) | 0.887(47) | DSAM（表注：同上，两方法吻合，列DSAM） |
| Band 2 | \(16^+_2\) | 0.824(52) | DSAM |
| Band 2 | \(17^+_2\) | 0.353(49) | DSAM |

除 \(10^+_1\) 外，其余能级寿命均为首次测定。

## 跃迁几率与模型比较（Fig. 3）

从寿命与分支比提取的跃迁几率呈现以下关键特征：

1. **\(B(E2)\) 的显著差异**：在能级近简并区域（\(I=14^+ - 19^+\)），Band 1 的带内 \(B(E2)\) 实验值比 Band 2 大 **2 到 3 倍**。这直接排除了静态手征模型（要求两带带内 \(B(E2)\) 几乎相等）。
2. **\(B(M1)\) 的平滑行为**：两带的 \(B(M1, I	o I-1)\) 在实验误差内表现相似且相对较强，**没有观察到任何明显的奇偶交错（staggering）**。
3. **TQPTR 模型的失败**：假定刚性三轴核芯（转动惯量比 \(1.52:3.55:1\)）的双准粒子+三轴转子模型预言两带 \(B(E2)\) 趋于相等、\(B(E2)\) 随自旋上升、且在 \(I>12^+\) 出现强烈的 \(B(M1)\) 交错，这三点均与实验严重不符。
4. **IBFFM 模型的成功**：引入三轴核芯三阶项并计入形状涨落（由邻核 ¹³⁴Ce 确定涨落幅度）的相互作用玻色子-费米子-费米子模型，成功再现了带内 \(B(E2)\) 的 2–3 倍差异、消除了 \(B(M1)\) 交错，并解释了近乎平坦的 \(B(E2)\) 随自旋走势。

作者据此指出：¹³⁴Pr 如果存在手征性，它主要具有**动力学手征（dynamical chirality）**特征，原子核在手征与非手征构型之间涨落；或者表明准粒子与核形状自由度的耦合才是支配机制。

## 谱系：与 Petrache 2006 (PE06) 的关系及下游维护

1. **PE06 的文献引用核验**：
   - Petrache et al. 2006 (PRL 96, 112502) 的 **Ref. [9]** 明确包含：*D. Tonev et al., AIP Conf. Proc. 764, 93 (2005); Phys. Rev. Lett. 96, 052501 (2006)*，即本篇论文。PE06 的寿命和带内 \(B\) 对比来自本篇。
   - PE06 用于两带解混合提取 \(Q_{0,1}/Q_{0,2}=2.0(4)\) 的实验分支比来自其 **Ref. [11]**：*K. Starosta et al. (to be published)*。
   - Tonev 本文文末提到的待发表论文是其自身的 **Ref. [15]**：*D. Tonev et al. (to be published)*。
   - 因此，PE06 是基于本篇寿命数据和 Starosta 等人分支比的批判性理论分析，并非一次新的独立实验测量。
2. **对 Wiki 下游的指示**：
   - `knowledge/sources/starosta-2001-n75-chiral-vibrations.md:201` 历史行中“随后被Tonev 2006与Petrache 2006严格否定”的措辞过于绝对。Tonev 原文只是否定了静态手征（static chirality），对动态手征和形状涨落保持开放；建议父级任务在后续维护中将该表述精准化为“否定了理想/静态手征图像”。

所有原子化证据见 `claim-ledger.json`（23 条主张）；寿命数据见 `table1-lifetime-ledger.json`；获取回执见 `access-manifest.json`。未修改任何 canonical 文件或 Git 状态。来源自审不是 human-reviewed。
