# -*- coding: utf-8 -*-
path = "knowledge/research-notes/a130-rewrite-parity-chirality-and-e1-limits-20261113.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

start_marker = "### 4. 内禀电偶极矩 $|D_0|$ 提取的模型假定\n"
end_marker = "\n## Assumptions\n"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

assert start_idx != -1 and end_idx != -1

new_sec4 = r"""### 4. 内禀电偶极矩 $|D_0|$ 提取的模型假定与 $12/5$ 与 $8/5$ 因子来源

在强耦合轴对称单 $K$ 转子模型下：
$$
B(E1; I \to I-1) = \frac{3}{4\pi} D_0^2 \, \langle I \, K \, 1 \, 0 | I-1 \, K \rangle^2,
$$
$$
B(E2; I \to I-2) = \frac{5}{16\pi} Q_0^2 \, \langle I \, K \, 2 \, 0 | I-2 \, K \rangle^2.
$$
两式相除时，未化简 Clebsch--Gordan 符号比值前的严格有理常数前因子为：
$$
\frac{B(E1; I \to I-1)}{B(E2; I \to I-2)} = \frac{\frac{3}{4\pi}}{\frac{5}{16\pi}} \frac{D_0^2}{Q_0^2} \frac{\langle I \, K \, 1 \, 0 | I-1 \, K \rangle^2}{\langle I \, K \, 2 \, 0 | I-2 \, K \rangle^2} = \frac{12}{5} \frac{D_0^2}{Q_0^2} \frac{\langle I \, K \, 1 \, 0 | I-1 \, K \rangle^2}{\langle I \, K \, 2 \, 0 | I-2 \, K \rangle^2}.
$$
**文献中常见的 $8/5$ 形式的代数渊源**：
在偶偶核交替宇称能带等 $K=0$ 体系中，Clebsch--Gordan 系数模平方满足显式解析式：
$$
\langle I \, 0 \, 1 \, 0 | I-1 \, 0 \rangle^2 = \frac{I}{2I+1}, \qquad \langle I \, 0 \, 2 \, 0 | I-2 \, 0 \rangle^2 = \frac{3I(I-1)}{2(2I+1)(2I-1)}.
$$
其比值为：
$$
\frac{\langle I \, 0 \, 1 \, 0 | I-1 \, 0 \rangle^2}{\langle I \, 0 \, 2 \, 0 | I-2 \, 0 \rangle^2} = \frac{2(2I-1)}{3(I-1)}.
$$
将此代入总比值式，分母中的 3 与 $12/5$ 中的分子 12 相约得到 $4 \times 2 / 5 = 8/5$：
$$
\frac{B(E1; I \to I-1)}{B(E2; I \to I-2)} = \frac{8}{5} \left( \frac{2I-1}{I-1} \right) \frac{D_0^2}{Q_0^2} \quad (K=0, I \ge 2).
$$
例如：$I=2$ 时比值为 $\frac{24}{5} \frac{D_0^2}{Q_0^2}$；$I=3$ 时比值为 $4 \frac{D_0^2}{Q_0^2}$。这一推导完全澄清了物理文献中两类写法的代数关系：保留未化简 CG 比时前因子必为 $12/5$；只有将 $K=0$ 的 CG 代数解析化简后，方才出现 $8/5 \times \frac{2I-1}{I-1}$。若将化简后的 $8/5$ 再次乘上未化简的 CG 比，则属于重复代数缩并的硬性失误。

局限与物理边界：
1. 实验测得退激发分枝比 $B(E1)/B(E2)$ 在缺乏能级寿命测量且无 Coulomb 激发等绝对跃迁矩阵元数据时，只能提取比值 $|D_0 / Q_0|$，不能提取绝对 $|D_0|$；可结合同核独立测定的 $Q_0$（由同核带内 $B(E2)$ 或跃迁四极矩 $Q_t$ 导出）进行换算，不必须依赖未标定理论；
2. 比值公式含平方项，无法确定 $D_0$ 的物理正负符号；
3. 在三轴非轴对称核中，偶极矩在主轴系有多个分量（$D_0, D_1$），单一分支反演非唯一；
4. 唯象宏观液滴电荷位移与微观单粒子极化偶极的相消效应（如 $^{146}\mathrm{Ba}$）导致 $|D_0|$ 异常微弱不能作为排除八极形变的依据；
5. 在连接相反宇称能级之间的一条物理跃迁内部允许发生 $E1 + M2$ 多极混合，须与实验谱线双峰重叠（如 $E1$ 与同宇称 $M1/E2$ 重叠）严格区分。"""

text = text[:start_idx] + new_sec4 + text[end_idx:]

# Update promotion history
old_hist = "- 2026-11-13（G88续修）：整合 Butler-Nazarewicz 1996（PDF p. 5）与 Bucher 2017（PDF pp. 2–5 Table I）权威原件与哈希，确立 Ra 与 Ba 轨道对隔离，明确 146Ba 直接 E3 强集体性与 E1 相消机制边界，声明宏观与微观偶极不必然处处反号。"
new_hist = """- 2026-11-13（G88续修）：整合 Butler-Nazarewicz 1996（PDF p. 5）与 Bucher 2017（PDF pp. 2–5 Table I）权威原件与哈希，确立 Ra 与 Ba 轨道对隔离，明确 146Ba 直接 E3 强集体性与 E1 相消机制边界，声明宏观与微观偶极不必然处处反号。
- 2026-11-13（G88二审返修）：纠正未约分 CG 式前因子为 12/5 并给出 K=0 化简为 8/5[(2I-1)/(I-1)] 的完全代数推导；严密表述 C^2=(-1)^(4I)=+1 在整自旋与半整自旋下的代数；区分标量积不变与整个态空间反射变换；规范 q3 算符身份与四极/八极动力学耦合界限。"""

assert old_hist in text, "old_hist not found"
text = text.replace(old_hist, new_hist)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated research note for 3.7 round 2")
