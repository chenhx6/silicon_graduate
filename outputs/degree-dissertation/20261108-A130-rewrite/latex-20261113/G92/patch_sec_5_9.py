# -*- coding: utf-8 -*-
path = "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-5-9.tex"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update text after eq:5-9-delta-def
old_delta_block = r"""\begin{equation}\label{eq:5-9-delta-def}
\delta(E2/M1) = \frac{\sqrt{3}}{10} \frac{E_\gamma}{\hbar c} \frac{\langle I_f \| \mathcal{M}(E2) \| I_i \rangle}{\langle I_f \| \mathcal{M}_S(M1) \| I_i \rangle}.
\end{equation}
此时电荷型磁算符满足 $\mathcal{M}_S(M1) = \mathcal{M}_\mu(M1)/c$，其矩阵元量纲为 $\mu_N/c$（具有电荷乘长度量纲 $e\cdot\text{fm}$），与电四极约化矩阵元除以长度量纲匹配。"""

new_delta_block = r"""\begin{equation}\label{eq:5-9-delta-def}
\delta(E2/M1) = \frac{\sqrt{3}}{10} \frac{E_\gamma}{\hbar c} \frac{\langle I_f \| \mathcal{M}(E2) \| I_i \rangle}{\langle I_f \| \mathcal{M}_S(M1) \| I_i \rangle}.
\end{equation}
此时电荷型磁算符满足 $\mathcal{M}_S(M1) = \mathcal{M}_\mu(M1)/c$，其矩阵元量纲为 $\mu_N/c$（具有电荷乘长度量纲 $e\cdot\text{fm}$），与电四极约化矩阵元除以长度量纲匹配。本书在发射过程选用 Krane--Steffen 混合比约定：式\eqref{eq:5-9-delta-def}中的矩阵元、算符相位和几何系数按同一约定配套。对于 Hamilton 的 $F_k$ 和其定义的 $\delta$，角分布混合项写为 $+2\delta F_k(LL')$；这与上述矩阵元比的约定一致。Lange 等给出的发射约定中 $\delta_{\rm KS}=-\delta_{\rm RB}$，转换文献时还必须同步转换几何干涉系数并区分发射与吸收。已发表数据保留来源原有符号及其约定；只有核实来源约定并需要统一比较时才显式换算，$\delta^2$ 与由其确定的多极份额不受此符号变换影响。"""

assert old_delta_block in text, "old_delta_block not found"
text = text.replace(old_delta_block, new_delta_block)

# 2. Update toy example C_M1 and B_mu
old_toy_block = r"""采用 Suhonen 教材印出常数精确重建的前因子：
\begin{align*}
C_{E2} &\approx 1.2250333078 \times 10^9\,\text{s}^{-1}\,\text{MeV}^{-5}\,(e^2\,\text{fm}^4)^{-1}, \\
C_{M1} &\approx 1.7583758801 \times 10^{13}\,\text{s}^{-1}\,\text{MeV}^{-3}\,[(\mu_N/c)^2]^{-1}.
\end{align*}
对通道 1（$4^+ \to 3^+$），$E_{\gamma, 1}^5 = (0.800)^5 = 0.32768\,\text{MeV}^5$：
\begin{equation}\label{eq:5-9-ped-be2-1}
B(E2; 4^+ \to 3^+) = \frac{1.10485 \times 10^{11}}{C_{E2} \times 0.32768} \approx 275.24\,e^2\,\text{fm}^4,
\end{equation}
计算值为 $275.2371\,e^2\,\text{fm}^4$，折合 $0.0275\,e^2\,\text{b}^2$。
磁偶极成分在 $E_{\gamma, 1}^3 = 0.512\,\text{MeV}^3$ 下反演：
\begin{equation}\label{eq:5-9-ped-bm1-1}
B_\mu(M1; 4^+ \to 3^+) = \frac{4.91046 \times 10^{10}}{C_{M1} \times 0.512} \approx 0.005454\,\mu_N^2,
\end{equation}
计算值为 $0.00545432\,\mu_N^2$。"""

new_toy_block = r"""采用 Suhonen 教材印出常数精确重建的前因子，对于式\eqref{eq:5-9-ce2}为 $C_{E2} \approx 1.2250333078 \times 10^9\,\text{s}^{-1}\,\text{MeV}^{-5}\,(e^2\,\text{fm}^4)^{-1}$；对于能量和强度均先按各自单位归一的式\eqref{eq:5-9-cm1}，实用率常数统一为 $C_{M1} = 1.7583758801 \times 10^{13}\,\text{s}^{-1}$。
对通道 1（$4^+ \to 3^+$），$E_{\gamma, 1}^5 = (0.800)^5 = 0.32768\,\text{MeV}^5$：
\begin{equation}\label{eq:5-9-ped-be2-1}
B(E2; 4^+ \to 3^+) = \frac{1.10485 \times 10^{11}}{C_{E2} \times 0.32768} \approx 275.24\,e^2\,\text{fm}^4,
\end{equation}
计算值为 $275.2371\,e^2\,\text{fm}^4$，折合 $0.0275\,e^2\,\text{b}^2$。
磁偶极成分在 $E_{\gamma, 1}^3 = (0.800)^3 = 0.512\,\text{MeV}^3$ 下显式反演为：
\begin{equation}\label{eq:5-9-ped-bm1-1}
B_\mu(M1; 4^+ \to 3^+) = \mu_N^2 \frac{4.91046 \times 10^{10}\,\text{s}^{-1}}{C_{M1} (0.800)^3} \approx 0.005454\,\mu_N^2,
\end{equation}
计算值为 $0.00545432\,\mu_N^2$。"""

assert old_toy_block in text, "old_toy_block not found"
text = text.replace(old_toy_block, new_toy_block)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully patched sec-5-9.tex per T20")
