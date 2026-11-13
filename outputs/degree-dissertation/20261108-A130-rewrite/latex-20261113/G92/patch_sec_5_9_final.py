# -*- coding: utf-8 -*-
path = "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-5-9.tex"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update line 106 to remove Rose-Brink collocation and state SI charge-type operator separately
old_106 = r"""多极混合比 $\delta$ 是出射光子场发射几率振幅之比，它不仅包含微观约化矩阵元，还内含了光子动量因子 $q = E_\gamma / (\hbar c)$ 与电磁耦合参数。当磁辐射算符采用国际单位制（SI）约定、显式包含 $\mu_N/c$ 因子时（如 Suhonen 专著与 Rose-Brink 体系），将分母明确写作电荷型磁算符 $\mathcal{M}_S(M1)$，混合比与约化矩阵元的关系表述为："""

new_106 = r"""多极混合比 $\delta$ 是出射光子场发射几率振幅之比，它不仅包含微观约化矩阵元，还内含了光子动量因子 $q = E_\gamma / (\hbar c)$ 与电磁耦合参数。当磁辐射算符采用国际单位制（SI）电荷型磁多极算符 $\mathcal{M}_S(M1) \equiv \mathcal{M}_\mu(M1)/c$（显式包含 $\mu_N/c$ 因子，矩阵元量纲为 $\mu_N/c$，即 $e\cdot\text{fm}$）单独定义时，混合比与约化矩阵元的关系表述为："""

assert old_106 in text, "old_106 not found"
text = text.replace(old_106, new_106)

# 2. Delete hanging "教学算例写为" before "对通道 1"
old_toy = r"""采用 Suhonen 教材印出常数精确重建的前因子，对于式\eqref{eq:5-9-ce2}为 $C_{E2} \approx 1.2250333078 \times 10^9\,\text{s}^{-1}\,\text{MeV}^{-5}\,(e^2\,\text{fm}^4)^{-1}$；对于能量和强度均先按各自单位归一的式\eqref{eq:5-9-cm1}，$C_{M1} = 1.7583758801 \times 10^{13}\,\text{s}^{-1}$。教学算例写为
对通道 1（$4^+ \to 3^+$），$E_{\gamma, 1}^5 = (0.800)^5 = 0.32768\,\text{MeV}^5$："""

new_toy = r"""采用 Suhonen 教材印出常数精确重建的前因子，对于式\eqref{eq:5-9-ce2}为 $C_{E2} \approx 1.2250333078 \times 10^9\,\text{s}^{-1}\,\text{MeV}^{-5}\,(e^2\,\text{fm}^4)^{-1}$；对于能量和强度均先按各自单位归一的式\eqref{eq:5-9-cm1}，实用率常数统一为 $C_{M1} = 1.7583758801 \times 10^{13}\,\text{s}^{-1}$。
对通道 1（$4^+ \to 3^+$），$E_{\gamma, 1}^5 = (0.800)^5 = 0.32768\,\text{MeV}^5$："""

assert old_toy in text, "old_toy not found"
text = text.replace(old_toy, new_toy)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully applied final patch to sec-5-9.tex")
