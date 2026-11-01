---
type: source
title: "Petrache 2024 - Chirality and Wobbling in Atomic Nuclei"
aliases: [Petrache2024, Chirality and Wobbling Book, 核手征与摆动专著]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "Chirality and Wobbling in Atomic Nuclei"
authors: [Costel Marian Petrache (editor), Stefan Frauendorf, Jie Meng, Elena A. Lawrie, Song Guo, Bingfeng Lv, Kosuke Nomura, J. A. Sheikh, Pengwei Zhao, Qibo Chen, et al.]
publisher: "CRC Press / Taylor & Francis Group"
year: 2024
pages: "339"
isbn: "9781032483863"
canonical_source: "C. M. Petrache (ed.), Chirality and Wobbling in Atomic Nuclei, CRC Press (2024)"
library_file: "raw/books/Chirality and Wobbling in Atomic Nuclei.pdf"
raw_file: "raw/books/Chirality and Wobbling in Atomic Nuclei.pdf"
raw_sha256: "787c7ae68836d95f4a9022f2c1e07177fefcebc11d752a62919b4b547e3fe7d2"
nuclei: [135Pr, 136Nd, 135Nd, 133La, 133Ce, 131Ce, 187Au, 105Pd, 126Cs, 128Cs, 130Ba, 133Ba, 163Lu, 165Lu]
reactions: [fusion-evaporation, in-beam-gamma]
experiments: [JUROGAM, Gammasphere, INGA, AFRODITE, AGATA, GRETINA]
models: [particle-rotor-model, tilted-axis-cranking, covariant-density-functional-theory, triaxial-projected-shell-model, ibfm]
topics: [nuclear-chirality, wobbling-motion, transverse-wobbling, longitudinal-wobbling, triaxiality, dual-root-degeneracy]
---

# Petrache 2024 - Chirality and Wobbling in Atomic Nuclei

## 专著全貌与划时代意义

本书是低能核结构领域第一部全面系统总结**原子核手征性（Chirality）与摆动运动（Wobbling Motion）**二十余年发展史与最新学术争议的权威巨著（339 页，2024 年出版）。由国际三轴核结构大师 Costel Marian Petrache 领衔主编，汇聚了包括手征性与摆动运动奠基人 Stefan Frauendorf、孟杰、Elena Lawrie，以及中国核物理前沿团队（郭松、吕冰锋、赵鹏巍、陈启博、亓斌等）在内的全球顶级学者。

该书全面覆盖了从经典三轴刚体转动、粒子-转子耦合模型（PRM/PTR）、微观协变密度泛函理论（CDFT）、含时协变密度泛函（TD-CDFT）、三轴投影壳模型（TPSM）、相互作用玻色子-费米子模型（IBFM），到大阵列束内 $\gamma$ 谱学实验证据、多重手征带（M$\chi$D）、横向/纵向摆动判定、以及近期在 $^{135}\text{Pr}$、$^{187}\text{Au}$ 等核中引发全球广泛争鸣的低自旋摆动反思。

---

## 17 个核心章节精解与理论图景

### Chapter 1: History and Future Perspectives (C. M. Petrache, pp. 20–42)
- **历史梳理**：系统回顾 1997 年 Frauendorf 与孟杰预言核手征性；2001 年 Ødegård 等在 $^{163}\text{Lu}$ 中首次观测高自旋摆动声子激发；2014 年 Frauendorf 与 Dönau 提出横向摆动（TW）机制；2015 年 Matta 等在 $^{135}\text{Pr}$ 报道首个奇 $A$ 核横向摆动；以及 2022 年后吕冰锋、郭松等在 $^{135}\text{Pr}$ 中指出混淆双根退化、推翻摆动解释的科学反转。
- **两大模式本质界定**：
  - **手征性**：三个非共面不相等的角动量矢量（价质子、价中子、三轴核芯转动）打破手征对称性；
  - **摆动运动**：非轴对称三轴椭球转子绕主转动惯量轴的微幅进动（低能激发本质为转动自由度的量子进动谐振子）。

### Chapter 2: Wobbling Motion in Triaxial Nuclei (S. Frauendorf, pp. 43–80)
- **三轴转子（Triaxial Rotor）基石**：
  $$H_{\text{rot}} = \frac{R_1^2}{2\mathcal{J}_1} + \frac{R_2^2}{2\mathcal{J}_2} + \frac{R_3^2}{2\mathcal{J}_3}$$
  若 $\mathcal{J}_1 > \mathcal{J}_2, \mathcal{J}_3$，能量最低的稳定转动绕 1 轴进行。摆动频率在简谐振子近似下为：
  $$\hbar\omega_w = \hbar\omega_{\text{rot}} \sqrt{\frac{(\mathcal{J}_1 - \mathcal{J}_2)(\mathcal{J}_1 - \mathcal{J}_3)}{\mathcal{J}_2 \mathcal{J}_3}}$$
- **粒子-转子耦合（Particle-Triaxial Rotor, PTR）分类**：
  - **横向摆动（TW）**：高 $j$ 准粒子角动量 $\vec{j}$ 垂直于最大转动惯量轴（如绕 3 轴对齐，而 $\mathcal{J}_1$ 最大）。随自旋 $I$ 增加，Coriolis 力使总角动量向 1 轴倾斜，导致**摆动能量 $E_w(I) = E(I, n_w=1) - [E(I-1, n_w=0) + E(I+1, n_w=0)]/2$ 随自旋 $I$ 下降**！
  - **纵向摆动（LW）**：准粒子角动量 $\vec{j}$ 与最大转动惯量轴平行（均沿 1 轴）。随着自旋 $I$ 增加，摆动频率随自旋增加而上升。

### Chapter 3: 25th Anniversary of Nuclear Chirality (J. Meng & Y. P. Wang, pp. 81–93)
- **手征双重带物理判据（“孟杰判据”）**：
  1. 能级能量近简并：$\Delta E(I) = E_2(I) - E_1(I)$ 较小且随自旋呈现平缓或微小能隙；
  2. 相同的自旋宇称序列：$I^\pi, (I+1)^\pi, (I+2)^\pi, \dots$ 具有相同的转动惯量与回弯行为；
  3. 跃迁分支比与强度极度对称：带间/带内 $B(M1)/B(E2)$ 呈现奇偶交替交织并随自旋收敛；
  4. 手征恢复机制：在静态手征区，左右手系发生量子隧道穿透形成正负宇称伙伴（手征振动向静态手征演化）。

### Chapter 5: Recent Experimental Results on Chirality and Wobbling (S. Guo & B. F. Lv, pp. 110–126)
- **$^{135}\text{Pr}$ 摆动争议的关键破局**：
  详细展示 2022 年在芬兰 JYFL 采用 JUROGAM II 阵列测量的线偏振数据。原先宣称的横向摆动带连接线（$\Delta I=1$ 跃迁）的角分布系数 $a_2 \approx -0.42$ 存在绝对数学双根退化（$\delta_1 = -1.83$ 摆动解 vs $\delta_2 = -0.47$ 伙伴带解）。偏振度测量以 $>11\sigma$ 的显著性彻底排除了大 $|\delta|$ 的摆动解，证实连接线为 $81.9\%\ M1$ 占优，实为常规的旋称伙伴带（signature partner band）！
- **$^{136}\text{Nd}$ 偶偶核横向摆动的确立**：展示两准中子组态横向摆动的直接微观证据。

### Chapter 6: Tilted Precession and Wobbling (E. A. Lawrie, pp. 127–155)
- **倾斜进动（Tilted Precession, TP）动力学**：
  从庞加莱截面和非线性经典轨道出发，证明当势能面关于角动量方向具有倾斜极小值时，体系优先发生倾斜进动。若恢复力常数不对称，进动谱与摆动谱极其相似，必须通过绝对电磁跃迁几率 $B(E2)_{\text{out}}/B(E2)_{\text{in}}$ 加以裁决。

### Chapter 11: Interacting Boson-Fermion Model Perspectives (K. Nomura, pp. 239–255)
- **$\gamma$ 软核对摆动运动的挑战**：
  Nomura 指出在 $A\approx 130$ 质量区（如 $^{131}\text{Xe}, {}^{133}\text{La}, {}^{135}\text{Pr}$），微观自洽平均场表明核芯具有强烈的 $\gamma$ 柔软度（$\gamma$-softness），有效三轴势能面极浅。在 IBFM 框架下，原本被指认为“摆动激发”的能带，本质上是准粒子与大振幅 $\gamma$ 振动声子耦合的产物，摆动能量随自旋下降是 $\gamma$ 自由度软化的自然表现。

---

## 对本 Wiki 与博士课题的核心价值

1. **确立研究体系顶层认知**：彻底建立手征性与摆动运动在 $A\approx 130$ 质量区（包括 $^{131,133}\text{Ce}$）的分类谱系与适用边界。
2. **筑牢实验反误判防线**：坚决贯彻“五道门”证据裁判标准，绝不因单一度规（如角分布或能谱靠近）轻易宣布新模式，必须提供偏振、多极混合比、绝对寿命和理论势能刚性的完备链条！
