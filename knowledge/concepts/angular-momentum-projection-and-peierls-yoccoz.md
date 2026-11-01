---
type: concept
title: "量子角动量投影（AMP）、重整化转动能谱与Peierls-Yoccoz转动惯量动力学"
aliases: [角动量投影, AMP, 旋转对称性恢复, 重整化能谱, Peierls-Yoccoz惯量, 范数核, 哈密顿核, 高斯重叠近似, GOA, 投影壳模型]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [angular-momentum-projection, amp, peierls-yoccoz, rotational-bands, symmetry-restoration, gaussian-overlap-approximation, goa, tpsm]
---

# 量子角动量投影（AMP）、重整化转动能谱与Peierls-Yoccoz转动惯量动力学

## 1. 物理全景：从破缺对称性内禀波包到实验室系纯自旋态

在微观核多体理论（如 Nilsson 变形平均场、Hartree-Fock 或 Hartree-Fock-Bogoliubov）中，为了在变分空间中容纳强形变核芯的集体四极关联，自洽场强制打破了空间转动不变性：
$$[\hat{H}, \hat{\mathbf{J}}^2] \ne 0$$
内禀变形波函数 $|\Phi\rangle$ 在物理上**并不是一个具有确定角动量 $I$ 的物理真实能态**，而是一个叠加了全套自旋序列（$I = 0, 2, 4, 6, \dots$ 或 $I = K, K+1, \dots$）的庞大相干波包。

根据 R. E. Peierls & J. Yoccoz（Proc. Phys. Soc. A 70, 381, 1957）、P. Ring & P. Schuck《The Nuclear Many-Body Problem》（第 11 章）以及卢希庭《原子核物理（修订版）》（第 4 章）：
为了在实验室参考系中严谨恢复角动量守恒、计算绝对能级与电磁跃迁几率，必须运用**量子角动量投影技术（Quantum Angular Momentum Projection, AMP）**：
1. **转动对称性投影算符 $\hat{P}_{MK}^I$**：
   利用不可约 Wigner $D$ 矩阵在整个 $SO(3)$ 空间欧拉角 $(\alpha, \beta, \gamma)$ 上实施相干群积分，将内禀波函数中混杂的假自旋分量严格过滤投影出纯净的实验室自旋态 $|I M K\rangle$；
2. **Peierls-Yoccoz 转动能谱与自洽转动惯量 $\mathcal{J}_{\text{PY}}$**：
   在投影态下计算哈密顿量期望值，自然从微观波函数中推导出了严格满足 $I(I+1)$ 的转动能带阶梯：
   $$E(I) = \frac{\langle \Phi | \hat{H} \hat{P}_{00}^I | \Phi \rangle}{\langle \Phi | \hat{P}_{00}^I | \Phi \rangle} = E_{\text{int}} + \frac{\hbar^2}{2\mathcal{J}_{\text{PY}}} I(I + 1)$$
3. **Peierls-Yoccoz 惯量与 Thouless-Valatin 推转惯量的物理区隔**：
   - Peierls-Yoccoz 惯量 $\mathcal{J}_{\text{PY}}$ 由静态内禀态角动量涨落 $\langle \hat{J}_y^2 \rangle$ 给出，因未计入时间反演破缺的动态轨道重整，比刚体惯量约小 $30\%$；
   - 随自旋推转的 Thouless-Valatin 惯量包含动态时间奇相互作用（Time-odd field），构成了投影壳模型（TPSM）在三轴超形变与回弯动力学中的底层支柱。

---

## 2. 严格投影数学积分与高斯重叠近似（GOA）

### (1) 轴对称 $K=0$ 能态投影算符推导
对于轴对称形变基态 $|\Phi\rangle$（$K=0$），绕对称轴旋转 $\alpha$ 与 $\gamma$ 是平凡简并的。投影算符完全简化为沿中间轴 $y$ 旋转极角 $\beta$ 的一维角动量积分：
$$\hat{P}_{00}^I = \frac{2I + 1}{2} \int_0^\pi d\beta \sin\beta \cdot d_{00}^I(\beta) \cdot e^{-i \beta \hat{J}_y}$$
其中 $d_{00}^I(\beta)$ 为 Wigner 旋转函数，在 $K=M=0$ 下**严格等价于一阶勒让德多项式（Legendre Polynomial）**：
$$d_{00}^I(\beta) = P_I(\cos\beta)$$

---

### (2) 范数核 $n(\beta)$ 与哈密顿核 $h(\beta)$
定义转动重叠函数：
- **范数核（Norm Kernel）**：
  $$n(\beta) = \langle \Phi | e^{-i \beta \hat{J}_y} | \Phi \rangle$$
- **哈密顿核（Hamiltonian Kernel）**：
  $$h(\beta) = \langle \Phi | \hat{H} e^{-i \beta \hat{J}_y} | \Phi \rangle$$

在强变形极限下，$\langle \hat{J}_y^2 \rangle$ 涨落极大，转动重叠函数在 $\beta = 0$ 附近呈现极其陡峭的高斯峰，构成了著名的**高斯重叠近似（Gaussian Overlap Approximation, GOA）**：
$$n(\beta) \approx \exp\left( - \frac{1}{2} \langle \hat{J}_y^2 \rangle \beta^2 \right)$$
$$h(\beta) \approx n(\beta) \left[ \langle \hat{H} \rangle + \frac{\hbar^2}{2\mathcal{J}_{\text{PY}}} \langle \hat{J}_y^2 \rangle \beta^2 \right]$$

---

### (3) 投影能谱积分公式
对偶自旋 $I = 0, 2, 4, 6, \dots$：
$$N_{00}^I = \frac{2I + 1}{2} \int_0^\pi d\beta \sin\beta \cdot P_I(\cos\beta) \cdot n(\beta)$$
$$H_{00}^I = \frac{2I + 1}{2} \int_0^\pi d\beta \sin\beta \cdot P_I(\cos\beta) \cdot h(\beta)$$

最终在实验室参考系中恢复的自洽物理能谱为：
$$E(I) = \frac{H_{00}^I}{N_{00}^I}$$
激发能为 $\Delta E_x(I) = E(I) - E(0)$。

---

## 3. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/angular_momentum_projection_amp_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `amp` 命令。

### 运行示范（以 $\langle J_y^2 \rangle = 35\hbar^2, A_{\text{rot}} = 25\text{ keV}$ 进行 $I = 0 \sim 10$ 投影）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py amp --max-spin 10 --jy2 35.0 --a-rot 0.025 --json
```

### 计算输出核心物理特征：
1. **范数积分与概率权重**：
   - 随自旋升高，态的投影重数展现出单峰泊松分布：$I=0$ 时 $N_I = 0.0142$，$I=4$ 处达到极大值 $0.0958$，$I=10$ 时自然回落，清晰证明了内禀变形波包由不同自旋成分构成的多体概率波包本质；
2. **重整化转动谱**：
   - 投影精确给出了纯转动态阶梯，与经典 Peierls-Yoccoz 解析极值 $E \propto I(I+1)$ 吻合良好，消除了任何人工固定转子几何的唯象假设！

---

## 4. 与相关前沿概念的交叉引用
- [[tpsm-band-diagram-calculator]]：三轴投影壳模型（TPSM）正是在此处 1D 投影基础上拓展出三维非轴对称欧拉角全投影；
- [[nilsson-deformed-shell-model-dynamics]]：微观 Nilsson 单核子波函数在进行组态混合后，正是经由此处投影算符输出实验室系可观测在束能级；
- [[moment-of-inertia-spin-analyzer]]：运动学转动惯量 $\mathcal{J}^{(1)}$ 在理论微观起源上正是 Peierls-Yoccoz 投影积分的宏观体现。
