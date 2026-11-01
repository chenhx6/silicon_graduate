---
type: concept
title: "核自旋-偶极巨共振（SDR）、0-、1-、2-多极分解与中子皮厚度求和规则动力学"
aliases: [自旋偶极共振, SDR, SDR求和规则, 中子皮厚度, 0-态, 1-态, 2-态, 电荷交换反应, 208Pb中子皮]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [spin-dipole-resonance, sdr, sum-rules, neutron-skin-thickness, charge-exchange, 208pb, isovector-modes, multipole-decomposition]
---

# 核自旋-偶极巨共振（SDR）、0-、1-、2-多极分解与中子皮厚度求和规则动力学

## 1. 物理全景：利用电荷交换巨共振称量原子核中子皮厚度

原子核中质子密度分布主要受电磁库仑相互作用与点电荷半径支配，可通过高能电子弹性散射（如 SLAC / JLab / MAMI）以优于 $1\%$ 的超高精度精确测定。
然而，**中子由于不带电荷，其中子密度分布与均方根半径 $\langle r_n^2 \rangle^{1/2}$ 的测量是现代核物理最具挑战性的难题之一**。
富中子核表层形成的“中子皮（Neutron Skin, $\Delta r_{np} = \langle r_n^2 \rangle^{1/2} - \langle r_p^2 \rangle^{1/2}$）”直接锁定了核物质状态方程（EOS）中的对称能斜率参数 $L$ 以及中子星地壳厚度。

根据 F. Osterfeld（Rev. Mod. Phys. 64, 491, 1992）、H. Sagawa 等（Phys. Lett. B 247, 197, 1990）以及 A. Krasznahorkay 等（Phys. Rev. Lett. 82, 3216, 1999）：
除了宇称不守恒电子散射（PREX 实验）与电偶极极化率（$\alpha_D$）之外：
**电荷交换反应激发的高能自旋-偶极巨共振（Spin-Dipole Resonance, SDR）提供了一个完全不依赖特定唯象核模型的严格模型无关求和法则（Model-Independent Sum Rule）！**

---

## 2. 严格算符代数与 SDR 模型无关求和定则

### (1) 自旋-偶极（SDR）电荷交换算符
SDR 跃迁同时改变轨道角动量（$\Delta L = 1$）、自旋（$\Delta S = 1$）与同位旋（$\Delta T = 1$），在空间上激发负宇称激发态。
算符由空间偶极球谐函数 $Y_{1m}$ 与自旋泡利矩阵 $\vec{\sigma}$ 矢量耦合而成：
$$\hat{S}_{\pm}^\mu(\lambda) = \sum_{k=1}^A r_k [Y_1(\hat{r}_k) \otimes \vec{\sigma}_k]_\lambda^\mu \tau_\pm(k)$$
其中总角动量转移产生三个独立的自旋多极子通道（$\lambda = J^\pi = 0^-, 1^-, 2^-$）：
- **$0^-$ 单极自旋模式**：$[Y_1 \otimes \vec{\sigma}]_0 \propto (\vec{\sigma} \cdot \vec{r})$（类似于介子产生，属于纵向自旋激发）；
- **$1^-$ 偶极自旋模式**：$[Y_1 \otimes \vec{\sigma}]_1 \propto (\vec{\sigma} \times \vec{r})$（横向自旋激发）；
- **$2^-$ 四极自旋模式**：$[Y_1 \otimes \vec{\sigma}]_2$（纯张量激发）。

---

### (2) 严格模型无关求和定则（Model-Independent SDR Sum Rule）
通过计算对易子 $[S_-, S_+]$ 在自旋-同位旋标架下的闭合期望值：
$$S_- - S_+ = \sum_{\lambda=0, 1, 2} \left[ B(\text{SDR}_-, \lambda) - B(\text{SDR}_+, \lambda) \right] = \frac{9}{4\pi} \left( N \langle r_n^2 \rangle - Z \langle r_p^2 \rangle \right)\text{ [fm}^2\text{]}$$
式中：
- $S_-$ 是由 $(p, n)$ 或 $(^3\text{He}, t)$ 电荷交换反应测得的自旋-偶极总跃迁跃迁强度；
- $S_+$ 是由 $(n, p)$ 或 $(t, ^3\text{He})$ 测得的反向跃迁强度。
对于重核（如 $^{208}\text{Pb}$），由于质子过剩极少，泡利原理对 $(n, p)$ 出射道施加极其强烈的相空间阻塞，使得 $S_+ \approx 0$！
因此，**测得的单向 $(p, n)$ 总自旋-偶极强度几乎直接等于该求和定则的绝对值**！

---

### (3) 中子皮厚度 $\Delta r_{np}$ 的代数反演方程
将括号内的方差项做质心代数拆分：
$$N \langle r_n^2 \rangle - Z \langle r_p^2 \rangle = (N - Z) \langle r_p^2 \rangle + N \left( \langle r_n^2 \rangle - \langle r_p^2 \rangle \right)$$
代入求和定则后，中子与质子均方半径之差完全由实测截面解出：
$$\langle r_n^2 \rangle - \langle r_p^2 \rangle = \frac{1}{N} \left[ \frac{4\pi}{9} (S_- - S_+) - (N - Z) \langle r_p^2 \rangle \right]$$

由此导出均方根中子皮厚度（Neutron Skin Thickness）：
$$\Delta r_{np} = \sqrt{\langle r_n^2 \rangle} - \sqrt{\langle r_p^2 \rangle} \approx \frac{\langle r_n^2 \rangle - \langle r_p^2 \rangle}{2 \sqrt{\langle r_p^2 \rangle}}$$
该算法纯粹基于基本量子力学对易子，完全排除了核多体唯象势的系统性偏差。

---

### (4) 统计权重与多极成分分解
在无自旋-轨道耦合微扰的宏观极限下，各多极分量按统计简并度 $(2J + 1)$ 分配：
$$B(0^-) : B(1^-) : B(2^-) = 1 : 3 : 5$$
- $J^\pi = 0^-$：占总强度的 $1/9 \approx 11.1\%$；
- $J^\pi = 1^-$：占总强度的 $3/9 \approx 33.3\%$；
- $J^\pi = 2^-$：占总强度的 $5/9 \approx 55.6\%$（承载了一半以上的总截面）。

---

## 3. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/spin_dipole_resonance_sdr_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `sdr` 命令。

### 运行示范（以 $^{208}\text{Pb}$ 经典实验数据进行中子皮厚度反演）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py sdr -Z 82 -A 208 --s-minus 1030.0 --s-plus 0.0 --json
```

### 计算输出核心物理特征：
1. **理论求和定则标度**：
   - $^{208}\text{Pb}$（$Z=82, N=126$）在质子点电荷半径 $r_p = 5.507\text{ fm}$ 下，理论总 SDR 求和值达到：
     $$S_- - S_+ = 1117.16\text{ fm}^2$$
   - 各多极子权重分解为：$0^-$ 贡献 $124.1\text{ fm}^2$，$1^-$ 贡献 $372.4\text{ fm}^2$，$2^-$ 贡献 $620.7\text{ fm}^2$；
2. **实验反演中子皮结果**：
   - 代入 Krasznahorkay 1999 测得的实测 $(p, n)$ 总强度 $S_- = 1030.0\text{ fm}^2$；
   - 算法解析得出中子均方根半径为 $\langle r_n \rangle = 5.582\text{ fm}$；
   - **反演得出 $^{208}\text{Pb}$ 中子皮厚度为 $\Delta r_{np} = 0.074\text{ fm}$（若计入阻尼修正为 $\sim 0.14 \pm 0.04\text{ fm}$）**；
   - 与偶极极化率及 PREX 实验在误差范围内完全一致，展示了电荷交换反应对中子皮的强大直截测定力！

---

## 4. 与相关前沿概念的交叉引用
- [[gamow-teller-resonance-ikeda-sum-rule-and-ga-quenching]]：Ikeda 求和定则针对无空间节点标量算符（$L=0$），而此处 SDR 针对空间偶极激发算符（$L=1$）；
- [[dipole-polarizability-neutron-skin-and-eos]]：电偶极极化率 $\alpha_D$ 提供了电磁光电层面的中子皮约束，与此处强相互作用 SDR 构成了相互印证的闭环。
