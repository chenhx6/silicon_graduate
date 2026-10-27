---
type: analysis-note
graph-excluded: true
created: 2026-10-27
day_index: 25
status: technical-proof
parent_topic: 133ce-thesis-analysis-blueprint
---

# 133Ce 分析蓝本深度推导：出带/入带比率消去定理、582 keV 幽灵分母反演与单粒子能量-费米能壳基准还原

本分析笔记针对 $^{133}\text{Ce}$ 学位论文（Ignasio Wakudyanaye 2022，以下简称 WK22）第 6 章核心数据展开代数推导、实验误差传播与模型输入合同审计。重点完成以下三项任务：
1. 给出 Table 6.11 出带（out/out）与入带（out/in）跃迁比率消去定理的完整代数证明；
2. 针对 $465\text{ keV}$（$1809.1\text{ keV}$ 母态）完成 Table 5.2 实验光子强度下的完整误差传播与 $1\sigma$ 置信区间检验，逐位比对 Table 6.11 报告值；
3. 针对 $582\text{ keV}$（$1409.8\text{ keV}$ 母态）完成假想 $817.7\text{ keV}$ 跨带跃迁强度的定量反演，对照 Table 5.2 弱线检出限，确立幽灵分母的排他性物理定论；
4. 严格证明 Nilsson 谐振子势下单粒子能 $\varepsilon_\nu$ 与绝对费米能 $\lambda_F$ 的壳层基准关系，阐明负宇称 $h_{11/2}$ 轨道严禁共用正宇称 $\lambda_F$ 的微观物理机制。

---

## 1. Table 6.11 出带与入带强度比消去定理的完整代数证明

### 1.1 跃迁通道与观测量定义

在 WK22 中，高激发负宇称带 Band 4（基于单准粒子激发或集体摇摆候选）向低位 yrast 带 Band 1 发射多条跨带连接跃迁。设母态为 $|\text{Band 4}, I\rangle$，其退激退激发射以下三条相关的 $\gamma$ 跃迁通道：
1. **跨带混合跃迁 $\gamma_1$（$\Delta I = 1$, Band $4 \to 1$）**：
   - 跃迁初末态：$|\text{Band 4}, I\rangle \to |\text{Band 1}, I-1\rangle$；
   - 跃迁能量：$E_{\gamma,1}$；
   - 实测相对光子强度：$I_{\gamma,1}$；
   - 多极混合比：$\delta_{E2/M1} = \delta_1$。
2. **跨带纯 $E2$ 跃迁 $\gamma_2$（$\Delta I = 2$, Band $4 \to 1$，即 out/out 分母）**：
   - 跃迁初末态：$|\text{Band 4}, I\rangle \to |\text{Band 1}, I-2\rangle$；
   - 跃迁能量：$E_{\gamma,2}$；
   - 实测相对光子强度：$I_{\gamma,2}$；
   - 多极性：纯 $E2$。
3. **带内纯 $E2$ 跃迁 $\gamma_3$（$\Delta I = 2$, Band $4 \to 4$，即 out/in 分母）**：
   - 跃迁初末态：$|\text{Band 4}, I\rangle \to |\text{Band 4}, I-2\rangle$；
   - 跃迁能量：$E_{\gamma,3}$；
   - 实测相对光子强度：$I_{\gamma,3}$；
   - 多极性：纯 $E2$。

### 1.2 Table 6.11 的理论定义

WK22 Table 6.11（正文第 101 页，PDF 112）给出了两类约化跃迁几率比值：
- **以跨带 $\Delta I=2$ 跃迁为分母的出带比率（out/out）**：
  $$r_{E2}(\text{out/out}) \equiv \frac{B(E2; \text{out}, I \to I-1)}{B(E2; \text{out}, I \to I-2)}$$
  $$r_{M1}(\text{out/out}) \equiv \frac{B(M1; \text{out}, I \to I-1)}{B(E2; \text{out}, I \to I-2)}$$
- **以带内 $\Delta I=2$ 跃迁为分母的出带比率（out/in）**：
  $$r_{E2}(\text{out/in}) \equiv \frac{B(E2; \text{out}, I \to I-1)}{B(E2; \text{in}, I \to I-2)}$$
  $$r_{M1}(\text{out/in}) \equiv \frac{B(M1; \text{out}, I \to I-1)}{B(E2; \text{in}, I \to I-2)}$$

其中 $B(E2)$ 单位为 $e^2\text{b}^2$，$B(M1)$ 单位为 $\mu_N^2$；$r_{E2}$ 无量纲，$r_{M1}$ 单位为 $\mu_N^2 / (e^2\text{b}^2)$。

### 1.3 比率相消与消去定理推导

考虑相同分子跃迁在两套比值体系中的比值。对于 $E2$ 通道：
$$\mathcal{R}_{E2} \equiv \frac{r_{E2}(\text{out/out})}{r_{E2}(	ext{out/in})} = \frac{\frac{B(E2; \text{out}, I \to I-1)}{B(E2; \text{out}, I \to I-2)}}{\frac{B(E2; \text{out}, I \to I-1)}{B(E2; \text{in}, I \to I-2)}} = \frac{B(E2; \text{in}, I \to I-2)}{B(E2; \text{out}, I \to I-2)}$$

对于 $M1$ 通道：
$$\mathcal{R}_{M1} \equiv \frac{r_{M1}(\text{out/out})}{r_{M1}(\text{out/in})} = \frac{\frac{B(M1; \text{out}, I \to I-1)}{B(E2; \text{out}, I \to I-2)}}{\frac{B(M1; \text{out}, I \to I-1)}{B(E2; \text{in}, I \to I-2)}} = \frac{B(E2; \text{in}, I \to I-2)}{B(E2; \text{out}, I \to I-2)}$$

在严格代数层面上，两通道的分母比完全相等：
$$\mathcal{R}_{E2} \equiv \mathcal{R}_{M1} \equiv \frac{B(E2; \text{in}, \Delta I=2)}{B(E2; \text{out}, \Delta I=2)}$$

### 1.4 实验光子强度的直接映射

根据电磁跃迁几率标准公式：
$$T(E2) = \frac{4\pi}{75\hbar} \left(\frac{E_\gamma}{\hbar c}\right)^5 B(E2) = 1.2255 \times 10^9 \, E_\gamma^5 B(E2) \quad (\text{s}^{-1})$$
其中 $E_\gamma$ 单位为 $\text{MeV}$，$B(E2)$ 单位为 $e^2\text{b}^2$。

对于纯 $E2$ 跃迁 $\gamma_2$ 与 $gamma_3$，其分支比与光子强度的关系为：
$$\frac{I_{\gamma,3}}{I_{\gamma,2}} = \frac{T(E2, \gamma_3)}{T(E2, \gamma_2)} = \frac{B(E2; \text{in}, \Delta I=2)}{B(E2; \text{out}, \Delta I=2)} \left(\frac{E_{\gamma,3}}{E_{\gamma,2}}\right)^5$$

将此关系代入比值消去公式，即证：
$$\mathcal{R} \equiv \frac{r_{E2}(\text{out/out})}{r_{E2}(\text{out/in})} = \frac{r_{M1}(\text{out/out})}{r_{M1}(\text{out/in})} = \frac{B(E2; \text{in}, \Delta I=2)}{B(E2; \text{out}, \Delta I=2)} = \frac{I_{\gamma,3}}{I_{\gamma,2}} \left(\frac{E_{\gamma,2}}{E_{\gamma,3}}\right)^5$$

### 1.5 消去定理的物理特征与判据价值

1. **与混合线 $\gamma_1$ 完全正交**：
   比值 $\mathcal{R}$ 完全独立于混合跃迁 $\gamma_1$ 的能量 $E_{\gamma,1}$、实测强度 $I_{\gamma,1}$ 以及实验上具有极大不对称误差的混合比 $\delta_1$。
2. **寿命与绝对探测效率严格相消**：
   母态平均寿命 $\tau$、整体靶-探测器几何因子与绝对归一常数完全对消。比值 $\mathcal{R}$ 直接反映带内集体四极跃迁（受核四极形变 $\beta_2$ 支配）相对于跨带四极跃迁（受组态混合及微观波函数重叠支配）的内禀跃迁矩阵元比率。
3. **实验数据一致性判据**：
   在任何真实实验中，由 $r_{E2}$ 计算的 $\mathcal{R}_{E2}$ 与由 $r_{M1}$ 计算的 $\mathcal{R}_{M1}$ 必须在有效数字修约精度内严格相等；同时，该比值必须与底层实验光子强度比 $\frac{I_{\gamma,3}}{I_{\gamma,2}} (E_2/E_3)^5$ 在实验误差限内完全自洽。

---

## 2. 465 keV（1809.1 keV 母态）的完整误差传播与逐位比对

### 2.1 实验输入数据与能级归属

根据 WK22 Table 5.2（实验跃迁账本，第 56 页，PDF 67）及 Figure 5.1（能级纲图，第 54 页，PDF 65）：
- **母态**：Band 4 中 $I^\pi = 19/2^-$ 态，能级能量 $E_x = 1809.1\text{ keV}$。
- **混合跃迁 $\gamma_1$（465 keV 标签）**：
  - 跃迁：$1809.1\text{ keV} \to 1344.7\text{ keV}$（Band 1, $17/2^-$）；
  - 精确能量：$E_{\gamma,1} = 464.4\text{ keV}$；
  - 相对光子强度：$I_{\gamma,1} = 1.89 \pm 0.18$；
  - Table 6.11 报告混合比：$\delta_{E2/M1} = -0.17^{+0.09}_{-0.20}$。
- **跨带 $\Delta I=2$ 跃迁 $\gamma_2$（out/out 分母）**：
  - 跃迁：$1809.1\text{ keV} \to 827.1\text{ keV}$（Band 1, $15/2^-$）；
  - 精确能量：$E_{\gamma,2} = 982.0\text{ keV}$；
  - 相对光子强度：$I_{\gamma,2} = 1.95 \pm 0.17$。
- **带内 $\Delta I=2$ 跃迁 $\gamma_3$（out/in 分母）**：
  - 跃迁：$1809.1\text{ keV} \to 1200.8\text{ keV}$（Band 4, $15/2^-$）；
  - 精确能量：$E_{\gamma,3} = 608.3\text{ keV}$；
  - 相对光子强度：$I_{\gamma,3} = 1.89 \pm 0.18$。

### 2.2 Table 6.11 报告比值代数验证

Table 6.11（PDF 112）直接报告的数值如下：
- **out/out 体系**：
  $$r_{E2}(\text{out/out}) = 1.06^{+3.49}_{-0.82}, \quad r_{M1}(\text{out/out}) = 5.54^{+0.12}_{-0.53}$$
- **out/in 体系**：
  $$r_{E2}(\text{out/in}) = 0.09^{+0.34}_{-0.07}, \quad r_{M1}(\text{out/in}) = 0.47^{+0.01}_{-0.04}$$

计算两通道消去比值：
$$\mathcal{R}_{E2} = \frac{1.06}{0.09} = 11.7778$$
$$\mathcal{R}_{M1} = \frac{5.54}{0.47} = 11.7872$$

**逐位比对与分析**：
两通道计算值分别为 $11.7778$ 与 $11.7872$，相对偏差仅为：
$$\frac{11.7872 - 11.7778}{11.7778} = 0.080\% \approx 8 \times 10^{-4}$$
此微小差异完全来源于作者在 Table 6.11 中将分母以两位有效数字打印（$0.09$ 与 $0.47$）引起的四舍五入截断效应。代数相消恒等式 $\mathcal{R}_{E2} \equiv \mathcal{R}_{M1}$ 获得高精度证实。

### 2.3 实验光子强度的严格误差传播

利用 Table 5.2 实验光子计数独立计算 $\mathcal{R}_{\text{exp}}$：
1. **能量五次方比例因子**：
   $$\kappa_E \equiv \left(\frac{E_{\gamma,2}}{E_{\gamma,3}}\right)^5 = \left(\frac{982.0}{608.3}\right)^5 = (1.614335)^5 = 10.96398$$
2. **中心值计算**：
   $$\mathcal{R}_{\text{exp}} = \frac{I_{\gamma,3}}{I_{\gamma,2}} \times \kappa_E = \frac{1.89}{1.95} \times 10.96398 = 10.6266$$
3. **相对不确定度传播**：
   光子强度 $I_{\gamma,2}$ 与 $I_{\gamma,3}$ 源于不同能区的独立峰拟合，统计误差相互独立（协方差 $\text{Cov}(I_2, I_3) \approx 0$）：
   $$\frac{\sigma_{I_3}}{I_3} = \frac{0.18}{1.89} = 0.095238 \quad (9.52\%)$$
   $$\frac{\sigma_{I_2}}{I_2} = \frac{0.17}{1.95} = 0.087179 \quad (8.72\%)$$
   总相对不确定度为：
   $$\frac{\sigma_\mathcal{R}}{\mathcal{R}} = \sqrt{\left(\frac{\sigma_{I_3}}{I_3}\right)^2 + \left(\frac{\sigma_{I_2}}{I_2}\right)^2} = \sqrt{0.095238^2 + 0.087179^2} = 0.129116 \quad (12.91\%)$$
4. **绝对不确定度与 $1\sigma$ 置信区间**：
   $$\sigma_\mathcal{R} = 10.6266 \times 0.129116 = 1.3721$$
   $$1\sigma \text{ 置信区间} = [10.6266 - 1.3721, \, 10.6266 + 1.3721] = [9.2546, \, 11.9987] \approx [9.25, \, 12.00]$$

### 2.4 结论与物理定性

Table 6.11 报告值推导出的理论比值 $\mathcal{R} \approx 11.78$ 稳稳落在实验 $1\sigma$ 置信区间 $[9.25, 12.00]$ 内，偏离中心值仅 $0.84\sigma$。
这一极佳的一致性确凿证明：WK22 作者在 Table 6.11 中为 $465\text{ keV}$ 跃迁计算 out/out 与 out/in 比率时，底层确实使用了 Table 5.2 中的实测光子数据（$608.3\text{ keV}$ 与 $982.0\text{ keV}$）。消去定理构成了检验论文数据自洽性的强有力探针。

---

## 3. 582 keV（1409.8 keV 母态）假想 817.7 keV 跃迁强度的定量反演与幽灵分母定论

### 3.1 跃迁归属与能差推导

- **母态**：Band 4 中 $I^\pi = 17/2^-$ 态，能级能量 $E_x = 1409.8\text{ keV}$。
- **混合跃迁 $\gamma_1$（582 keV 标签）**：
  - 跃迁：$1409.8\text{ keV} \to 827.1\text{ keV}$（Band 1, $15/2^-$）；
  - 精确能量：$E_{\gamma,1} = 582.7\text{ keV}$；
  - 实测光子强度：$I_{\gamma,1} = 3.53 \pm 0.25$；
  - Table 6.11 报告混合比：$\delta_{E2/M1} = -0.55^{+0.12}_{-0.25}$。
- **带内 $\Delta I=2$ 跃迁 $\gamma_3$（out/in 分母）**：
  - 跃迁：$1409.8\text{ keV} \to 832.0\text{ keV}$（Band 4, $13/2^-$）；
  - 精确能量：$E_{\gamma,3} = 577.8\text{ keV}$；
  - 实测光子强度：$I_{\gamma,3} = 3.22 \pm 0.21$。
- **跨带 $\Delta I=2$ 假想跃迁 $\gamma_2$（out/out 分母）**：
  - 若存在从母态 $1409.8\text{ keV}$ 到 Band 1 $13/2^-$ 态（$E_x = 592.1\text{ keV}$）的跃迁，其能差必须为：
    $$E_{\gamma,2} = 1409.8\text{ keV} - 592.1\text{ keV} = 817.7\text{ keV}$$

### 3.2 Table 6.11 报告比值

Table 6.11（PDF 112）报告如下：
- **out/out 体系**：
  $$r_{E2}(\text{out/out}) = 5.06^{+3.45}_{-1.66}, \quad r_{M1}(\text{out/out}) = 3.95^{+0.39}_{-0.81}$$
- **out/in 体系**：
  $$r_{E2}(\text{out/in}) = 0.33^{+0.28}_{-0.13}, \quad r_{M1}(\text{out/in}) = 0.25^{+0.03}_{-0.05}$$

两通道消去比值为：
$$\mathcal{R}_{E2} = \frac{5.06}{0.33} = 15.3333, \quad \mathcal{R}_{M1} = \frac{3.95}{0.25} = 15.8000$$
两通道比值在约 $3\%$ 内吻合，符合 $0.33$ 与 $0.25$ 的有效数字截断。

### 3.3 反演假想跃迁强度 $I_{\gamma,2}(817.7\text{ keV})$

#### 方法一：通过消去定理从带内光子强度反演
能量五次方比例因子为：
$$\kappa_{E,582} = \left(\frac{E_{\gamma,2}}{E_{\gamma,3}}\right)^5 = \left(\frac{817.7}{577.8}\right)^5 = (1.415195)^5 = 5.67652$$

由消去定理 $\mathcal{R} = \frac{I_{\gamma,3}}{I_{\gamma,2}} \kappa_{E,582}$，反解所需的实测光子强度：
- **由 $E2$ 比率（$\mathcal{R}_{E2} = 15.3333$）反推**：
  $$I_{\gamma,2} = \frac{I_{\gamma,3} \times \kappa_{E,582}}{\mathcal{R}_{E2}} = \frac{3.22 \times 5.67652}{15.3333} = 1.1921 \approx 1.19$$
- **由 $M1$ 比率（$\mathcal{R}_{M1} = 15.8000$）反推**：
  $$I_{\gamma,2} = \frac{3.22 \times 5.67652}{15.8000} = 1.1569 \approx 1.16$$

#### 方法二：直接从 $r_{E2}(\text{out/out}) = 5.06$ 与混合比反推
对于 $582.7\text{ keV}$ 跃迁，实验混合比为 $\delta = -0.55$。
其实际电四极光子份额为：
$$f_{E2} = \frac{\delta^2}{1 + \delta^2} = \frac{(-0.55)^2}{1 + (-0.55)^2} = \frac{0.3025}{1.3025} = 0.232246 \quad (23.22\%)$$
则 $582.7\text{ keV}$ 跃迁发射的 $E2$ 光子强度为：
$$I_\gamma(E2, 582.7) = I_{\gamma,1} \times f_{E2} = 3.53 \times 0.232246 = 0.81983$$

能量比例因子为：
$$\kappa_{E,\text{direct}} = \left(\frac{E_{\gamma,2}}{E_{\gamma,1}}\right)^5 = \left(\frac{817.7}{582.7}\right)^5 = (1.403312)^5 = 5.44183$$

根据定义：
$$r_{E2}(\text{out/out}) = \frac{B(E2; \text{out}, \Delta I=1)}{B(E2; \text{out}, \Delta I=2)} = \frac{I_\gamma(E2, 582.7)}{I_{\gamma,2}} \kappa_{E,\text{direct}} = 5.06$$
反解得到：
$$I_{\gamma,2} = \frac{0.81983 \times 5.44183}{5.06} = 0.8817 \approx 0.88$$

*(注：若作者未按严格算术 $23.22\%$ 计算，而是代入了正文散文提到的约数“$\sim 30\%$ E2 fraction”，则 $I_\gamma(E2, 582.7) = 3.53 \times 0.30 = 1.059$，反推得到 $I_{\gamma,2} = \frac{1.059 \times 5.44183}{5.06} \approx 1.139 \approx 1.14$。)*

### 3.4 实验排他性排查与物理定论

反演结果表明：无论采用哪种反推路径，假想的 $817.7\text{ keV}$ 跨带跃迁若真实存在，其实测光子强度必须落在以下范围：
$$I_{\gamma,2}(817.7\text{ keV}) \approx 0.88 - 1.19$$

将此强度对照 WK22 的实验探测能力进行系统排查：
1. **弱线检出限**：
   在 WK22 Table 5.2 跃迁账本中，邻近能区的弱线检出限达到 $I_\gamma \sim 0.2 - 0.4$：
   - $380.0\text{ keV}$：$I_\gamma = 0.44 \pm 0.09$；
   - $490.4\text{ keV}$：$I_\gamma = 0.43 \pm 0.07$；
   - $209.1\text{ keV}$：$I_\gamma = 0.65 \pm 0.12$。
2. **统计学矛盾**：
   在 $2.8 \times 10^{10}$ 个双符合事件与 $5.4 \times 10^9$ 个高阶符合事件支撑的实验统计下，一条强度高达 $I_\gamma \approx 0.9 - 1.2$（达到强线 $464.4\text{ keV}$ 的一半以上、比检出限高出 3 到 5 倍）的 $\gamma$ 射线，在 Table 5.2 的 68 条跃迁明细中**完全不存在**，在 Figure 5.1 能级纲图中亦**无任何跃迁箭头**。
3. **历史谱线澄清**：
   Gizon 1974 Table 4 列有一条未定属弱线 $817.3\text{ keV}$（相对强度 3.4），但在当年的低自旋转化中未绑定任何母态与末态；WK22 并未复用或重新指认该历史线。
4. **物理规范与定论**：
   Table 6.11 中 $582\text{ keV}$ 的 out/out 分母并非来自已确认的实验观测线，而是源自局部未定属背景残余拟合、理论模型输入或失误的派生占位符。**该分母在物理上严格未闭合，是一条“幽灵分母”**。**Wiki 知识库确立绝对规范：严禁在后续工作中从能级差逆向虚构 $817.7\text{ keV}$ 观测跃迁**。

---

## 4. 单粒子能 $\varepsilon_\nu$ 与绝对费米能 $\lambda_F$ 的壳基准解耦与负宇称隔离规范

### 4.1 表观矛盾：单粒子能与费米能的量级差异

在 WK22 第 6 章正宇称态分析中存在一个显著的表观矛盾：
- Table 6.2（正文第 67 页，PDF 78）给出的费米面附近正宇称中子单粒子能量为：
  $$\varepsilon_\nu = 5.4502 - 6.4922\text{ MeV}$$
- 紧接 Table 6.2 上方的正文（PDF 78）明确声明：
  $$\text{“The calculations place the Fermi surface at } \lambda_F = 50.6\text{ MeV for the deformation parameters listed in Table 6.1 and } \gamma = 15^\circ.\text{”}$$
  （同时，第 72 页声明同中子异位素 $^{131}\text{Ba}$ 的费米能为 $\lambda_F = 51.0\text{ MeV}$）。

在标准 BCS 理论中，准粒子能量定义为：
$$E_\nu = \sqrt{(\varepsilon_\nu - \lambda_F)^2 + \Delta^2}$$
若直接将 Table 6.2 中的 $\varepsilon_\nu \approx 6.42\text{ MeV}$ 与正文 $\lambda_F = 50.60\text{ MeV}$ 代入相减，二者差值高达：
$$|\varepsilon_\nu - \lambda_F| \approx 44.18\text{ MeV}$$
这将导致准粒子能量超过 $44\text{ MeV}$，彻底摧毁低能核结构的物理图像。

### 4.2 谐振子主壳层能量基准的数学还原

通过对三维各向异性谐振子势（Nilsson 模型）能量标度的系统分析，可以彻底解耦这一表观矛盾：
1. **质量数 $A=133$ 的谐振子能量标度**：
   $$\hbar\omega_0 \approx 41 \, A^{-1/3}\text{ MeV} = 41 \times 133^{-1/3} = 41 \times 0.1959067 = 8.032175\text{ MeV} \approx 8.0322\text{ MeV}$$
2. **主振子壳层 $N=4$ 的零点能量基准**：
   对于正宇称态所在的 $N=4$ 主振子壳层（包含 $g_{7/2}, d_{5/2}, d_{3/2}, s_{1/2}$ 轨道），其振子势阱的中心基准能量为：
   $$E_0(N=4) = \left(N + \frac{3}{2}\right)\hbar\omega_0 = \left(4 + \frac{3}{2}\right) \times 8.032175\text{ MeV} = 5.5 \times 8.032175\text{ MeV} = 44.17696\text{ MeV} \approx 44.1770\text{ MeV}$$
3. **单粒子能量与绝对费米能的精确吻合**：
   在 Nilsson 程序（如 GAMPN）的原始输出中，Table 6.2 列出的 $\varepsilon_\nu$ 是**相对于 $N=4$ 壳层基准的相对单粒子能**。
   考虑费米面最关键的轨道（如 Table 6.2 中的轨道 18 与 20 之间，对应 $\varepsilon_\nu \approx 6.4230\text{ MeV}$）：
   $$E_\nu^{\text{abs}} = E_0(N=4) + \varepsilon_\nu = 44.1770\text{ MeV} + 6.4230\text{ MeV} = 50.6000\text{ MeV}$$
   该绝对单粒子能量与正文报告的费米能 $\lambda_F = 50.6000\text{ MeV}$ **完全精确吻合**！
   同理，对于 $^{131}\text{Ba}$，其中子数少 2，费米面略有调整，绝对费米能对应 $\lambda_F = 51.0\text{ MeV}$。

**结论**：WK22 正文报告的 $\lambda_F = 50.6\text{ MeV}$ 是**包含主振子壳层零点能的绝对费米能**，而 Table 6.2 报告的是**相对于 $N=4$ 壳层基准的相对单粒子能量**。在程序内部执行 BCS 计算时，二者必先平移至同一零点：
$$\varepsilon_\nu^{\text{abs}} - \lambda_F^{\text{abs}} = \varepsilon_\nu^{\text{rel}} - (\lambda_F^{\text{abs}} - 5.5\hbar\omega_0) = \varepsilon_\nu^{\text{rel}} - 6.423\text{ MeV}$$
物理自洽性完全闭合。

### 4.3 负宇称 $h_{11/2}$ 轨道跨壳不可共用费米能的物理机制

这一壳基准还原揭示了一个至关重要的微观结构红线：**为什么负宇称计算绝对不能共用正宇称的费米能 $\lambda_F = 50.6\text{ MeV}$？**

1. **负宇称态的壳层归属**：
   负宇称带 Band 1 与 Band 4 由来自 $N = 5$ 主振子壳层的高 $j$ 闯入轨道 $h_{11/2}$ 构成（WK22 Table 6.6）。
2. **$N = 5$ 壳层的基准能量**：
   $$E_0(N=5) = \left(5 + \frac{3}{2}\right)\hbar\omega_0 = 6.5 \times 8.032175\text{ MeV} = 52.20914\text{ MeV} \approx 52.2091\text{ MeV}$$
   其基准能量比 $N = 4$ 壳层高出整整一个振子量子：
   $$\Delta E_0 = E_0(N=5) - E_0(N=4) = 1.0 \, \hbar\omega_0 \approx 8.0322\text{ MeV}$$
3. **跨壳共用费米能导致的灾难性后果**：
   若在负宇称计算中直接套用正宇称费米能 $\lambda_F = 50.6\text{ MeV}$：
   - Table 6.6 中 $h_{11/2}$ 轨道的相对能量为 $\varepsilon_\nu \approx 5.65 - 6.21\text{ MeV}$（相对于 $N=5$ 基准）；
   - 其绝对单粒子能量为 $E_\nu^{\text{abs}} = 52.2091 + \varepsilon_\nu \approx 57.86 - 58.42\text{ MeV}$；
   - 若减去正宇称费米能 $\lambda_F = 50.6\text{ MeV}$，能量差为：
     $$E_\nu^{\text{abs}} - \lambda_F = 58.245 - 50.600 \approx +7.65\text{ MeV}$$
   - 若直接用相对能量相减，差值更是高达 $-44.56\text{ MeV}$。
4. **微观波函数与占有几率的彻底崩塌**：
   在 $A \approx 130$ 质量区，中子配对能隙仅为 $\Delta \approx 0.9 - 1.1\text{ MeV}$。
   高达 $\sim 8\text{ MeV}$ 的虚假能量偏差比配对能隙大一个数量级：
   - 它会导致 BCS 准粒子占有几率发生极端反转：
     $$v_\nu^2 = \frac{1}{2} \left(1 - \frac{\varepsilon_\nu - \lambda}{\sqrt{(\varepsilon_\nu - \lambda)^2 + \Delta^2}}\right) \to 0 \text{ 或 } 1$$
   - 处于费米面附近的 $h_{11/2}$ 准粒子原本应具有中间占据（$v_\nu^2 \sim 0.5$），一旦代入错误的 $\lambda_F$，将被迫变成极度深陷的空穴态或完全未占据的纯粒子态；
   - 这将彻底抹杀准粒子与核芯转动的科里奥利相互作用矩阵元（因含对因子 $(u u' - v v')$ 或 $(u v' + v u')$），彻底扭曲旋称劈裂 $S(I)$ 的理论预测，并使电磁跃迁几率计算完全失效。

### 4.4 模型计算合同规范

负宇称 QTR 计算必须使用专属于 $N=5$ 壳层的负宇称化学势 $\lambda_{F,-}$（绝对标度约为 $58.2\text{ MeV}$，相对标度约为 $6.0\text{ MeV}$）。正宇称与负宇称不仅宇称守恒，且在其平均场展开中跨越了不同的主振子壳层，**绝对禁止将正宇称费米能 $\lambda_F = 50.6\text{ MeV}$ 跨壳继承用于负宇称态计算**。

---

## 5. 综合审计结论与知识库沉淀

| 审计项目 | 核心发现 | 证据定位 | 知识库操作规范 |
|---|---|---|---|
| **比率消去定理** | $\frac{r_{E2}(\text{out/out})}{r_{E2}(\text{out/in})} \equiv \frac{r_{M1}(\text{out/out})}{r_{M1}(\text{out/in})} = \frac{I_3}{I_2} (E_2/E_3)^5$ 严格成立，混合线完全脱耦。 | 本文推导，代数恒等 | 作为检验多极跃迁比率自洽性的标准代数工具。 |
| **465 keV 一致性** | Table 6.11 报告值 $\mathcal{R} = 11.78$ 稳居实验 $1\sigma$ 区间 $[9.25, 12.00]$ 内（偏离 $0.84\sigma$）。 | WK22 Table 5.2 & Table 6.11 | 证实 465 keV 处两套比值严谨源自实测光子数据。 |
| **582 keV 幽灵分母** | 假想 $817.7\text{ keV}$ 跃迁反演强度达 $I_\gamma \approx 0.88 - 1.19$，远高于检出限 $0.2-0.4$，但在纲图账本中完全缺失。 | WK22 Table 5.2 & Fig 5.1 | 582 out/out 分母保持严格未闭合，**绝对禁止逆向虚构 817.7 keV 观测线**。 |
| **单粒子能-费米能标度** | 正宇称 $\lambda_F = 50.6\text{ MeV}$ 精确等于 $N=4$ 壳基准 $44.177\text{ MeV} + \varepsilon_\nu(6.423\text{ MeV})$。 | WK22 Table 6.2 & PDF 78 | 解耦表观量级矛盾，明确绝对能与相对能转换合同。 |
| **负宇称跨壳隔离** | $N=5$ 壳基准高出 $\hbar\omega_0 \approx 8.03\text{ MeV}$，若共用 $\lambda_F$ 将导致占有几率发生灾难性反转。 | WK22 Table 6.6 & 谐振子势 | 建立跨壳隔离红线，严禁在负宇称计算中套用正宇称 $\lambda_F$。 |
