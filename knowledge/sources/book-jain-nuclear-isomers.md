---
type: source
title: "Ashok Kumar Jain 等 2021 - Nuclear Isomers: A Primer"
aliases: [Jain2021, Nuclear Isomers Primer, 同核异能态入门与前沿]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "Nuclear Isomers: A Primer"
authors: [Ashok Kumar Jain, Bhoomika Maheshwari, Alpana Goel]
publisher: "Springer Nature Switzerland"
year: 2021
pages: "151"
isbn: "9783030767228"
canonical_source: "A. K. Jain, B. Maheshwari, and A. Goel, Nuclear Isomers: A Primer, Springer (2021)"
library_file: "raw/books/nuclear isomer - A Prime.pdf"
raw_file: "raw/books/nuclear isomer - A Prime.pdf"
raw_sha256: "20f88b84240637e10a6086eca6b9f6e80a28813ad1ecf14a795144a4d5c2ac34"
nuclei: []
reactions: [in-beam-gamma, delayed-gamma, isomers]
experiments: []
models: [spin-trap, seniority-isomers, k-isomers, shape-isomers]
topics: [nuclear-isomers, transition-hindrance, k-quantum-number, gamma-ray-half-life]
---

# Ashok Kumar Jain 等 2021 - Nuclear Isomers: A Primer

## 专著全貌与学术定位

全书 151 页，系统总结了原子核长寿命激发态——**同核异能态（Nuclear Isomers，通常定义为 $T_{1/2} \ge 1\text{ ns}$）**的四种基本微观机制：
1. **自旋陷阱（Spin Traps）**：大角动量跃迁导致辐射相空间极度压缩；
2. **Seniority 异能态与广义 Seniority**：在近球形核价核子壳层中，对偶相互作用守恒引起的 $E2$ 跃迁矩阵元对消；
3. **$K$-同核异能态（$K$-Isomers）**：轴对称形变核中角动量在对称轴上的投影量子数 $K$ 发生大跨度跳跃（$\Delta K > \lambda$）；
4. **形状异能态（Shape Isomers）**：双峰裂变势垒或形状共存导致的宏观势垒阻碍。

对于高自旋在束谱学而言，异能态是截断级联退激、决定探测器延迟符合窗口的关键物理边界。

## 核心章节精要与理论内容

### Chapter 5: $K$-Isomers and Hindrance Factors (pp. 71–98)
- **$K$ 量子数守恒与破缺度 $\nu$**：
  在轴对称变形核中，能态具有良好的角动量投影量子数 $K$。对于多极数为 $\lambda$ 的电磁跃迁，选择定则要求：
  $$|\Delta K| = |K_i - K_f| \le \lambda$$
  当 $|\Delta K| > \lambda$ 时，跃迁被称为 **$K$-禁戒跃迁（$K$-forbidden transition）**。定义禁戒度（Degree of forbiddenness）为：
  $$\nu = |\Delta K| - \lambda$$
- **Weisskopf 阻碍因子 $F_W$ 与折合阻碍度 $f_\nu$**：
  $$F_W = \frac{T_{1/2}^{\text{exp}}}{T_{1/2}^{\text{sp(Weisskopf)}}}$$
  由于每增加一级 $K$-禁戒，核波函数都需要通过微小的 Coriolis 相互作用或三轴形变杂化产生一次微扰混合，因此实验上经验阻碍度遵循指数幂律：
  $$f_\nu = (F_W)^{1/\nu} \approx 100 \quad (\text{通常每级禁戒使跃迁几率降低约 } 100 \text{ 倍})$$
- **$K$-阻碍破缺与三轴性（Triaxiality）的深刻关联**：
  在三轴形变核中（如 $A\approx 130$ 质量区的奇奇核与偶偶核），由于轴对称性被打破，$K$ 不再是严格守恒的量子数，出现剧烈的 $K$-混合（$K$-mixing）。**若一个理论上看似高禁戒的 $K$-isomer 表现出异常小的 $f_\nu$（如 $f_\nu < 10$），往往直接泄露了原子核具有显著三轴非对称形变的微观指纹！**
