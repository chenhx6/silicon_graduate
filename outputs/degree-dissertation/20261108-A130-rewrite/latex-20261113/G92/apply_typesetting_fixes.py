# -*- coding: utf-8 -*-
import os

proj_root = "tmp/a130-release-29-20261113/project"

def patch_file(rel_path, replacements):
    full_path = os.path.join(proj_root, rel_path)
    with open(full_path, "r", encoding="utf-8") as f:
        text = f.read()
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
        else:
            print(f"Notice: pattern already patched or not found in {rel_path}: {old[:50]}...")
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Patched {rel_path}")

# 1. Frontinfo.tex: ensure schoollogo is empty
patch_file("Tex/Frontinfo.tex", [
    (r"\schoollogo{ucas_logo}", r"\schoollogo{}% 未提供所属学校；研究稿不显示模板学校的校徽或校名")
])

# 2. sec-3-7.tex
patch_file("Tex/Sections/sec-3-7.tex", [
    (r"极矢量（$\hat{\Pi} \mathbf{r} \hat{\Pi}^{-1} = -\mathbf{r}, \hat{\Pi} \mathbf{p} \hat{\Pi}^{-1} = -\mathbf{p}$）。然而",
     r"极矢量（满足 $\hat{\Pi} \mathbf{r} \hat{\Pi}^{-1} = -\mathbf{r}$ 与 $\hat{\Pi} \mathbf{p} \hat{\Pi}^{-1} = -\mathbf{p}$）。然而"),
    (r"\item 空间反射对称性破缺：由正负八极形变核态 $|\Phi(+\beta_3)\rangle$ 以及反演态 $|\Phi(-\beta_3)\rangle = \hat{\Pi} |\Phi(+\beta_3)\rangle$ 关联；" + "\n" +
     r"\item 手征转动对称性破缺：由左手三面角取向态 $|L\rangle$ 与右手三面角取向态 $|R\rangle = \mathcal{C} |L\rangle$ 关联，其中标准手征反转算符定义为 $\mathcal{C} \equiv \mathcal{T} \mathcal{R}_y(\pi)$。",
     r"\item 空间反射对称性破缺：由正负八极形变态 $|\Phi(+\beta_3)\rangle$ 与反演态 $|\Phi(-\beta_3)\rangle = \hat{\Pi} |\Phi(+\beta_3)\rangle$ 关联；" + "\n" +
     r"\item 手征转动对称性破缺：由左手三面角态 $|L\rangle$ 与右手态 $|R\rangle = \mathcal{C} |L\rangle$ 关联，标准手征算符为 $\mathcal{C} \equiv \mathcal{T} \mathcal{R}_y(\pi)$。")
])

# 3. sec-4-4.tex
patch_file("Tex/Sections/sec-4-4.tex", [
    # Eq 4-4-axes-identity: 215pt overfull
    (r"\begin{equation}\label{eq:4-4-axes-identity}" + "\n" +
     r"\text{最短几何轴 (short, $s$ 轴)} \iff k = 2; \quad" + "\n" +
     r"\text{中间几何轴 (intermediate, $m$ 轴)} \iff k = 1; \quad" + "\n" +
     r"\text{最长几何轴 (long, $l$ 轴)} \iff k = 3." + "\n" +
     r"\end{equation}",
     r"\begin{equation}\label{eq:4-4-axes-identity}" + "\n" +
     r"\begin{aligned}" + "\n" +
     r"\text{最短几何轴 (short, $s$ 轴)} &\iff k = 2; \\" + "\n" +
     r"\text{中间几何轴 (intermediate, $m$ 轴)} &\iff k = 1; \\" + "\n" +
     r"\text{最长几何轴 (long, $l$ 轴)} &\iff k = 3." + "\n" +
     r"\end{aligned}" + "\n" +
     r"\end{equation}"),
    # Table 4.1: 277pt overfull
    (r"\begin{tabularx}{\textwidth}{llcccc}",
     r"\begin{tabularx}{\textwidth}{p{2.6cm}p{1.8cm}ccc>{\raggedright\arraybackslash}X}"),
    # Inline overfulls in 4-4
    (r"由于 $^{187}\mathrm{Au}$ 的 Band 2 能级寿命在比较数据集中缺乏直接测量，Guo 等人通过采用邻近偶偶核芯 $^{186}\mathrm{Pt}$ 的带内跃迁强度 $B(E2)_{\mathrm{in}} \sim 100$--$200\ \mathrm{W.u.}$ 进行折算，导出其实际带间跃迁强度较低：",
     r"由于 $^{187}\mathrm{Au}$ 的 Band 2 寿命在比较数据集中缺乏直接测量，Guo 等人采用邻近核芯 $^{186}\mathrm{Pt}$ 的带内强度 $B(E2)_{\mathrm{in}} \sim 100$--$200\ \mathrm{W.u.}$ 折算，导出其实际带间跃迁强度较低："),
    (r"形状不变量无量纲比值 $R \equiv q_3 / q_2^{3/2} \propto \langle Q^3 \cos 3\delta \rangle / \langle Q^2 \rangle^{3/2}$，包含了体系",
     r"形状不变量无量纲比值 $R \equiv q_3 / q_2^{3/2}$（正比于 $\langle Q^3 \cos 3\delta \rangle / \langle Q^2 \rangle^{3/2}$），包含了体系"),
    # Table 4.2: 63pt overfull
    (r"\begin{table}[!htbp]" + "\n" + r"\centering" + "\n" + r"\small" + "\n" + r"\caption{跨核区非轴对称取向动力学核心案例比较矩阵（严格基于已核原件数据与物理模型条件整理）。}\label{tab:4-4-cross-region-comparison}" + "\n" + r"\begin{tabularx}{\textwidth}{lXXXXX}",
     r"\begin{table}[!htbp]" + "\n" + r"\centering" + "\n" + r"\footnotesize" + "\n" + r"\caption{跨核区非轴对称取向动力学核心案例比较矩阵（严格基于已核原件数据与物理模型条件整理）。}\label{tab:4-4-cross-region-comparison}" + "\n" + r"\begin{tabularx}{\textwidth}{p{2.0cm}Xp{2.3cm}p{2.3cm}p{2.5cm}X}")
])

# 4. sec-4-5.tex
patch_file("Tex/Sections/sec-4-5.tex", [
    # Table 4.3 overfulls
    (r"\begin{table}[!htbp]" + "\n" + r"\centering" + "\n" + r"\small" + "\n" + r"\caption{$^{78}\mathrm{Br}$ 与 $^{74}\mathrm{As}$ 中相关能带的观测自旋范围、组态指派与实验测量载荷汇总（严格依据刘晨 2016 博士论文与 PRL 2016、肖骁 2019 硕士论文与 PRC 2022 原件核对）。}\label{tab:4-5-bands-summary}" + "\n" + r"\begin{tabularx}{\textwidth}{llp{2.6cm}p{3.2cm}X}",
     r"\begin{table}[!htbp]" + "\n" + r"\centering" + "\n" + r"\footnotesize" + "\n" + r"\caption{$^{78}\mathrm{Br}$ 与 $^{74}\mathrm{As}$ 中相关能带的观测自旋范围、组态指派与实验测量载荷汇总（严格依据刘晨 2016 博士论文与 PRL 2016、肖骁 2019 硕士论文与 PRC 2022 原件核对）。}\label{tab:4-5-bands-summary}" + "\n" + r"\begin{tabularx}{\textwidth}{p{2.1cm}p{1.7cm}p{2.3cm}p{2.6cm}X}"),
    # Eq 4-5-cg-formula: 49.5pt overfull
    (r"\begin{equation}\label{eq:4-5-cg-formula}" + "\n" +
     r"B(E1; I \to I-1) = \frac{3}{4\pi}\,D_0^2\,\langle I K 1 0 | I-1 K \rangle^2 , \qquad" + "\n" +
     r"B(E2; I \to I-2) = \frac{5}{16\pi}\,Q_0^2\,\langle I K 2 0 | I-2 K \rangle^2 ." + "\n" +
     r"\end{equation}",
     r"\begin{equation}\label{eq:4-5-cg-formula}" + "\n" +
     r"\begin{aligned}" + "\n" +
     r"B(E1; I \to I-1) &= \frac{3}{4\pi}\,D_0^2\,\langle I K 1 0 | I-1 K \rangle^2 , \\" + "\n" +
     r"B(E2; I \to I-2) &= \frac{5}{16\pi}\,Q_0^2\,\langle I K 2 0 | I-2 K \rangle^2 ." + "\n" +
     r"\end{aligned}" + "\n" +
     r"\end{equation}")
])

# 5. sec-4-8.tex
patch_file("Tex/Sections/sec-4-8.tex", [
    (r"若引入按各自基准单位归一化的无量纲数值 $b_{M1} \equiv B_S(M1) / (\mu_N/c)^2 = B_\mu(M1) / \mu_N^2$，则实用跃迁率常数表示为：",
     r"若引入按各自基准单位归一化的无量纲数值 $b_{M1} \equiv B_S(M1) / (\mu_N/c)^2$（等价于 $B_\mu(M1) / \mu_N^2$），则实用跃迁率常数表示为："),
    (r"\begin{equation}\label{eq:4-8-isomer-feeding-ensemble}" + "\n" +
     r"\sigma_{\mathrm{isomer}}(E) = \sum_{J_0} \sigma_{\mathrm{cap}}(E, J_0) P_{\mathrm{CN}}(E, J_0) W_{\mathrm{sur}}(E^*, J_0) \bar{b}_{\mathrm{feed}}(E, J_0) = \sum_{J_0} \sigma_{\mathrm{ER}}(E, J_0) \bar{b}_{\mathrm{feed}}(E, J_0)." + "\n" +
     r"\end{equation}",
     r"\begin{equation}\label{eq:4-8-isomer-feeding-ensemble}" + "\n" +
     r"\begin{aligned}" + "\n" +
     r"\sigma_{\mathrm{isomer}}(E) &= \sum_{J_0} \sigma_{\mathrm{cap}}(E, J_0) P_{\mathrm{CN}}(E, J_0) W_{\mathrm{sur}}(E^*, J_0) \bar{b}_{\mathrm{feed}}(E, J_0) \\" + "\n" +
     r"&= \sum_{J_0} \sigma_{\mathrm{ER}}(E, J_0) \bar{b}_{\mathrm{feed}}(E, J_0)." + "\n" +
     r"\end{aligned}" + "\n" +
     r"\end{equation}")
])

# 6. AppendixA.tex
patch_file("Tex/Appendices/AppendixA.tex", [
    (r"约化矩阵元的归一化必须连同其具体定义式一起使用。核物理文献中，A.~Bohr 与 B.~R.~Mottelson 在其经典专著《Nuclear Structure》卷一式~(1A-60) 中给出的定义为：",
     r"约化矩阵元的归一化须连同其具体定义式一起使用。核物理文献中，A.~Bohr 与 B.~R.~Mottelson 在其专著《Nuclear Structure》卷一式~(1A-60) 中定义为："),
    (r"则其与本附录采用的标准约化矩阵元之间的数值比例因子为 $\langle j_f \| T^{(k)} \| j_i \rangle = \sqrt{2j_f + 1}\,\mathcal{R}_C$。比较不同专著或计算程序包（如壳模型代码与转动模型代码）时，必须首先核实其原始公式中是否包含该统计因数，避免在跃迁几率或有效电荷提取中引入偏差。表\ref{tab:appA-convention-comparison}汇总了经原件严格核对的定义约定。",
     r"则其与本附录标准约化矩阵元的数值比例因子为 $\langle j_f \| T^{(k)} \| j_i \rangle = \sqrt{2j_f + 1}\,\mathcal{R}_C$。比较不同专著或程序包时，须先核实公式中是否包含该统计因数，避免在跃迁几率或有效电荷中引入偏差。表\ref{tab:appA-convention-comparison}汇总了经原件核对的约定。"),
    # Table A.1
    (r"\begin{tabularx}{\textwidth}{p{3.8cm} p{5.0cm} p{2.8cm} >{\raggedright\arraybackslash}X}",
     r"\begin{tabularx}{\textwidth}{p{2.8cm} p{4.4cm} p{2.5cm} >{\raggedright\arraybackslash}X}"),
    # Line 91
    (r"若已在所用基底下将相应约化矩阵元选为实数，式\eqref{eq:appA-rme-exchange}表现为符号反转关系 $\langle j_f \| T^{(k)} \| j_i \rangle = (-1)^{j_f - j_i} \langle j_i \| T^{(k)} \| j_f \rangle$。",
     r"若已在所用基底下将相应约化矩阵元选为实数，式\eqref{eq:appA-rme-exchange}表现为符号反转关系：" + "\n" +
     r"\begin{equation}\label{eq:appA-rme-real-exchange}" + "\n" +
     r"\langle j_f \| T^{(k)} \| j_i \rangle = (-1)^{j_f - j_i} \langle j_i \| T^{(k)} \| j_f \rangle ." + "\n" +
     r"\end{equation}"),
    # Eq appA-9j-rme: 12pt overfull
    (r"\begin{equation}\label{eq:appA-9j-rme}" + "\n" +
     r"\langle (j_1' j_2') J' \| [\mathbf{T}^{(k_1)} \otimes \mathbf{U}^{(k_2)}]^{(K)} \| (j_1 j_2) J \rangle = \hat{J} \hat{J}' \hat{K} \begin{Bmatrix} j_1' & j_1 & k_1 \\ j_2' & j_2 & k_2 \\ J' & J & K \end{Bmatrix} \langle j_1' \| \mathbf{T}^{(k_1)} \| j_1 \rangle \langle j_2' \| \mathbf{U}^{(k_2)} \| j_2 \rangle ," + "\n" +
     r"\end{equation}",
     r"\begin{equation}\label{eq:appA-9j-rme}" + "\n" +
     r"\begin{aligned}" + "\n" +
     r"&\langle (j_1' j_2') J' \| [\mathbf{T}^{(k_1)} \otimes \mathbf{U}^{(k_2)}]^{(K)} \| (j_1 j_2) J \rangle \\" + "\n" +
     r"&\quad = \hat{J} \hat{J}' \hat{K} \begin{Bmatrix} j_1' & j_1 & k_1 \\ j_2' & j_2 & k_2 \\ J' & J & K \end{Bmatrix} \langle j_1' \| \mathbf{T}^{(k_1)} \| j_1 \rangle \langle j_2' \| \mathbf{U}^{(k_2)} \| j_2 \rangle ," + "\n" +
     r"\end{aligned}" + "\n" +
     r"\end{equation}"),
    # Eq appA-racah-formula: 44pt overfull
    (r"\begin{equation}\label{eq:appA-racah-formula}" + "\n" +
     r"\begin{Bmatrix} a & b & c \\ d & e & f \end{Bmatrix} = \Delta_R(a,b,c) \Delta_R(a,e,f) \Delta_R(d,b,f) \Delta_R(d,e,c) \sum_z \frac{(-1)^z (z+1)!}{\prod_{i=1}^4 (z - v_i)! \prod_{k=1}^3 (w_k - z)!} ," + "\n" +
     r"\end{equation}",
     r"\begin{equation}\label{eq:appA-racah-formula}" + "\n" +
     r"\begin{aligned}" + "\n" +
     r"\begin{Bmatrix} a & b & c \\ d & e & f \end{Bmatrix} &= \Delta_R(a,b,c) \Delta_R(a,e,f) \Delta_R(d,b,f) \Delta_R(d,e,c) \\" + "\n" +
     r"&\quad \times \sum_z \frac{(-1)^z (z+1)!}{\prod_{i=1}^4 (z - v_i)! \prod_{k=1}^3 (w_k - z)!} ," + "\n" +
     r"\end{aligned}" + "\n" +
     r"\end{equation}"),
    # Eq appA-ortho-sum-example: 39pt overfull
    (r"\begin{align}\label{eq:appA-ortho-sum-example}" + "\n" +
     r"\sum_{x=1}^3 (2x + 1) \begin{Bmatrix} 1 & 2 & x \\ 1 & 2 & 2 \end{Bmatrix}^2 &= (2\times 1 + 1) \left(-\frac{1}{10}\right)^2 + (2\times 2 + 1) \left(\frac{1}{6}\right)^2 + (2\times 3 + 1) \left(\frac{1}{15}\right)^2 \notag \\" + "\n" +
     r"&= 3 \times \frac{1}{100} + 5 \times \frac{1}{36} + 7 \times \frac{1}{225} \notag \\" + "\n" +
     r"&= \frac{3}{100} + \frac{5}{36} + \frac{7}{225} ." + "\n" +
     r"\end{align}",
     r"\begin{align}\label{eq:appA-ortho-sum-example}" + "\n" +
     r"\sum_{x=1}^3 (2x + 1) \begin{Bmatrix} 1 & 2 & x \\ 1 & 2 & 2 \end{Bmatrix}^2" + "\n" +
     r"&= (2\times 1 + 1) \left(-\frac{1}{10}\right)^2 + (2\times 2 + 1) \left(\frac{1}{6}\right)^2 \notag \\" + "\n" +
     r"&\quad + (2\times 3 + 1) \left(\frac{1}{15}\right)^2 \notag \\" + "\n" +
     r"&= 3 \times \frac{1}{100} + 5 \times \frac{1}{36} + 7 \times \frac{1}{225} \notag \\" + "\n" +
     r"&= \frac{3}{100} + \frac{5}{36} + \frac{7}{225} ." + "\n" +
     r"\end{align}"),
    # Line 197
    (r"根据式\eqref{eq:appA-rme-exchange}导出的约化矩阵元伴随关系，自伴随电磁算符满足 $|\langle i I_i \| \mathcal{M}(\sigma\lambda) \| f I_f \rangle|^2 = |\langle f I_f \| \mathcal{M}(\sigma\lambda) \| i I_i \rangle|^2$。对比式\eqref{eq:appA-b-standard-down}与式\eqref{eq:appA-b-standard-up}，得到正逆方向约化强度的统计权互易关系：",
     r"根据式\eqref{eq:appA-rme-exchange}导出的约化矩阵元伴随关系，自伴随电磁算符满足：" + "\n" +
     r"\begin{equation}\label{eq:appA-adjoint-rme-sq}" + "\n" +
     r"|\langle i I_i \| \mathcal{M}(\sigma\lambda) \| f I_f \rangle|^2 = |\langle f I_f \| \mathcal{M}(\sigma\lambda) \| i I_i \rangle|^2 ." + "\n" +
     r"\end{equation}" + "\n" +
     r"对比式\eqref{eq:appA-b-standard-down}与式\eqref{eq:appA-b-standard-up}，得到正逆方向约化强度的统计权互易关系：")
])

print("All typesetting fixes successfully applied!")
