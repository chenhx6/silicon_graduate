# 候选解释比较入口

| 检查 | 能说明什么 | 不能直接说明什么 |
| --- | --- | --- |
| 能量差、对齐、惯量 | 建立可比较的带序列和模型约束 | 唯一的 TW/LW、手征指认 |
| 混合比 δ | 指定约定下的辐射振幅比 | 绝对 B(E2)、唯一根或唯一模式 |
| 偏振与角关联 | 在校准响应和统计模型内约束 δ 分支 | 仅凭正负号通用定性裁决 |
| 寿命、分支比与 ICC | 构建部分跃迁率 | 未计侧馈/未见分支时的无系统误差强度 |
| 势能面/波函数几何 | 给出模型条件下的形变和角动量信息 | 直接实验事实或无参数唯一模型 |

原书争议与反例见 `knowledge/sources/book-petrache-chirality-and-wobbling.md`。135Pr 不使用红绿灯终局标签；130Ba/136Nd 的两准粒子案例不套用所有连接线必须 E2 绝对占优的规则。实时进展回到原始论文，版本和时间范围明确标注。

## 摆动（Wobbling）vs 倾斜进动（TiP）严格判据（Elena Lawrie, CRC 2025 表 6.1）

| 物理性质 | 振动型摆动（Vibrational Wobbling, 声子 $n_w$） | 转动型倾斜进动（Rotational TiP, 倾斜量子数 $m$） |
| --- | --- | --- |
| 激发能对激发量子数标度 $E_{\text{exc}}(I = \text{const})$ | 正比于声子数：$E \propto n_w$（线性等间距） | 正比于倾角平方：$E \propto m^2$（二次方转动贡献） |
| 偶偶核能级求和定则 | $E(2_g^+) + E(2_\gamma^+) > E(3_\gamma^+)$（显著大于零） | $E(2_g^+) + E(2_\gamma^+) = E(3_\gamma^+)$（严格相等或残差 $\sim 0$） |
| 带间多极跃迁选择定则 | 严格满足 $\Delta n_w = 1$（$\Delta n_w > 1$ 跃迁如 $n_w=2 \to 0$ 严格禁戒，强度 $\approx 0$） | 允许 $\Delta m > 1$ 集体 $E2$ 交叉跃迁（如 $m=2 \to 0$ 测得强 $E2$，数十 W.u.） |
| 带间连接跃迁 $B(E2)$ 标度 | $B(E2; n_w, I \to n_w-1, I-1) \propto n_w / I$ | 不严格反比于 $1/I$ |
| 实验指认首要门禁 | 连接线必须以集体 $E2$ 主导（$|\delta| \gg 1$）；若 $M1$ 主导（$|\delta| \le 1$）则排除纯声子摆动 | $M1$ 可由于准粒子进动或 $\gamma$ 振动耦合主导（如 $^{135}\text{Pr}$） |

## 横向摆动（TW）频率与软化极限（Frauendorf & Dönau 2014, CRC 2025 式 2.20–2.21）

- 惯量序：$\mathcal{J}_m > \mathcal{J}_s > \mathcal{J}_l$（中轴惯量最大，主导集体转动）；
- 奇核子沿短轴（$s$ 轴）对齐（$j$ 轨道）：有效转动参数 $\bar{A}_s(I) = A_s(1 - j/I)$；
- 横向摆动频率：$\hbar\omega_{\text{TW}}(I) = 2I \sqrt{(A_m - \bar{A}_s(I))(A_l - \bar{A}_s(I))}$；
- 临界软化自旋：$I_c = j \frac{\mathcal{J}_m}{\mathcal{J}_m - \mathcal{J}_s}$，当 $I \to I_c$ 时 $\hbar\omega_{\text{TW}} \to 0$，谐近似破裂；
- TW 核心特征：$\frac{d(\hbar\omega_{\text{TW}})}{dI} < 0$（频率随自旋升高而下降）。

## 核手征性（Chirality）三维角动量几何与选择定则（Meng & Wang, CRC 2025 第 3 章）

- 手征三脚架：$\vec{I} = \vec{j}_p(s\text{-axis}) + \vec{j}_n(l\text{-axis}) + \vec{R}(m\text{-axis})$；
- 手征体积元（Aplanarity Volume）：$\mathcal{V}_{\text{chiral}} = \vec{j}_p \cdot (\vec{j}_n \times \vec{R}) = j_p j_n \sqrt{\max(0, I(I+1) - j_p^2 - j_n^2)} \ne 0$；
- 手征双带特征：
  1. 相同宇称与组态的 $\Delta I = 1$ 双能带；
  2. 能级简并度演化：低自旋手征振动（$\Delta E(I) > 100\text{ keV}$）$\to$ 高自旋手征恢复（$\Delta E(I) \to 0$）；
  3. 带内 $B(M1)/B(E2)$ 比值与带间 $B(M1)$ 随自旋呈现剧烈的特征**奇偶交错**（Odd-Even Staggering）。
