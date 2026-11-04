# A≈130 质量区三轴形变与集体激发模式学术期刊论文投稿包

本目录归档由 Wiki 知识中枢产出的高水平学术论文完整初稿及全套出版套件：

- **论文题目**：*Triaxial Collective Excitations across the $A \approx 130$ Region: Resolving the Frontiers of Nuclear Chirality and Wobbling*
- **拟投期刊**：Physical Review C (Regular Article)
- **目标物理**：
  1. 建立非对称转子相空间极值、中间主轴双曲鞍点分离线拓扑与 Greiner 三态求和规则 $E(2_1^+) + E(2_2^+) = E(3_1^+)$；
  2. 针对 $^{135}\text{Pr}$“摆动运动”争议，通过 DCO-偏振二维 Profile Likelihood 似然比检验（$\Delta\chi^2 = 111.4$，$>10\sigma$），打破多极混合比 $\delta$ 的双实数根退化，彻底证伪大模摆动根，确立其为单粒子旋称跃迁；
  3. 针对 $^{135}\text{Nd}$ 与 $^{134}\text{Pr}$，基于实测绝对电磁跃迁几率，建立 Koike-Starosta-Hamamoto 选择定则的黄金基准（带内 $B(M1)$ 奇偶交错 $S_{M1}(I)$ 达到 100% 同相吻合，简并点带间 $\Delta I=0$ 的 $M1$ 跃迁深极小 $<0.05\ \mu_N^2$）；
  4. 阐明 $^{131}\text{Ce} \to {}^{133}\text{Ce}$ 费米面在中子 $h_{11/2}$ 壳层内的深度演化（中壳到顶壳），阐明其三轴摆动阻尼与手征相变动力学；
  5. 形式化 P-ADO 取向参数跨反应迁移之束流族极小极大 Mahalanobis 判据，确立重离子熔合稳态流（$\tau=0.74 < 1.0$）与轻离子退取向破缺机理。

---

## 文件清单与说明

| 文件/目录 | 格式 | 功用说明 |
|---|---|---|
| `main.tex` | LaTeX | Physical Review C (RevTeX 4.2) 标准双栏双盲/单盲投稿源码 |
| `references.bib` | BibTeX | 论文引用的全部 42 篇核心同行评议文献数据库 |
| `paper.typ` | Typst | 现代排版引擎 Typst 双栏预印本排版源码 |
| `paper.pdf` | PDF | 编译产出的 4 页出版级预印本双栏 PDF 文件 |
| `figures/made/` | 目录 | 绘图主程序、数据溯源说明书与各图 CSV 衍生数据集 |
| `figures/pdf/` | 目录 | 5 幅矢量图源文件（PDF 格式，供 LaTeX 编译插入） |
| `figures/png/` | 目录 | 5 幅高清预览图（PNG 格式，300 DPI） |

---

## 编译与重现指引

- **LaTeX 编译**：
  ```bash
  pdflatex main.tex
  bibtex main
  pdflatex main.tex
  pdflatex main.tex
  ```
- **Typst 编译**：
  ```bash
  typst compile paper.typ paper.pdf
  ```
- **重新生成全部插图**：
  ```bash
  cd figures/made
  python3 generate_figures.py
  ```
