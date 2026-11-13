# -*- coding: utf-8 -*-
import subprocess

path = "raw/writing/gpt/A130/these_2023_template/these_template/Tex/Sections/sec-5-9.tex"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Anchor after line 110
anchor_1 = r"""相配使得 $\delta$ 为无量纲纯数。若在常规采用磁矩型算符 $\mathcal{M}_\mu(M1)$（量纲 $\mu_N$）的约定下，分母相应补入 $1/c$ 因子（或等价地将光速 $c$ 移至分子与 $E_\gamma/\hbar$ 搭配），数值比值与相位约定保持完全自洽。$\delta$ 不能视作初末态裸约化矩阵元的简单无量纲相除。"""

replacement_1 = r"""相配使得 $\delta$ 为无量纲纯数。若在常规采用磁矩型算符 $\mathcal{M}_\mu(M1)$（量纲 $\mu_N$）的约定下，分母相应补入 $1/c$ 因子（或等价地将光速 $c$ 移至分子与 $E_\gamma/\hbar$ 搭配），数值比值与相位约定保持完全自洽。$\delta$ 不能视作初末态裸约化矩阵元的简单无量纲相除。本书在发射过程选用 Krane--Steffen 混合比约定：式\eqref{eq:5-9-delta-def}中的矩阵元、算符相位和几何系数按同一约定配套。对于 Hamilton 的 $F_k$ 和其定义的 $\delta$，角分布混合项写为 $+2\delta F_k(LL')$；这与上述矩阵元比的约定一致。Lange 等给出的发射约定中 $\delta_{\rm KS}=-\delta_{\rm RB}$，转换文献时还必须同步转换几何干涉系数并区分发射与吸收。已发表数据保留来源原有符号及其约定；只有核实来源约定并需要统一比较时才显式换算，$\delta^2$ 与由其确定的多极份额不受此符号变换影响。"""

assert anchor_1 in text, "anchor_1 not found"
text = text.replace(anchor_1, replacement_1)

# 2. Anchor for toy example C_M1 and B_mu
anchor_2 = r"""采用 Suhonen 教材印出常数精确重建的前因子：
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

replacement_2 = r"""采用 Suhonen 教材印出常数精确重建的前因子，对于式\eqref{eq:5-9-ce2}为 $C_{E2} \approx 1.2250333078 \times 10^9\,\text{s}^{-1}\,\text{MeV}^{-5}\,(e^2\,\text{fm}^4)^{-1}$；对于能量和强度均先按各自单位归一的式\eqref{eq:5-9-cm1}，$C_{M1} = 1.7583758801 \times 10^{13}\,\text{s}^{-1}$。教学算例写为
对通道 1（$4^+ \to 3^+$），$E_{\gamma, 1}^5 = (0.800)^5 = 0.32768\,\text{MeV}^5$：
\begin{equation}\label{eq:5-9-ped-be2-1}
B(E2; 4^+ \to 3^+) = \frac{1.10485 \times 10^{11}}{C_{E2} \times 0.32768} \approx 275.24\,e^2\,\text{fm}^4,
\end{equation}
计算值为 $275.2371\,e^2\,\text{fm}^4$，折合 $0.0275\,e^2\,\text{b}^2$。
磁偶极成分在 $E_{\gamma, 1}^3 = (0.800)^3 = 0.512\,\text{MeV}^3$ 下显式写为：
\begin{equation}\label{eq:5-9-ped-bm1-1}
B_\mu(M1; 4^+ \to 3^+) = \mu_N^2 \frac{4.91046 \times 10^{10}\,\text{s}^{-1}}{C_{M1} (0.800)^3} \approx 0.005454\,\mu_N^2,
\end{equation}
计算值为 $0.00545432\,\mu_N^2$。"""

assert anchor_2 in text, "anchor_2 not found"
text = text.replace(anchor_2, replacement_2)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully written updated sec-5-9.tex")
