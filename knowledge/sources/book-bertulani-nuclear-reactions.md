---
type: source
title: "Carlos A. Bertulani & P. Danielewicz 2021 - Introduction to Nuclear Reactions (2nd Edition)"
aliases: [Bertulani2021, Introduction to Nuclear Reactions, 反应论基础]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: book
reading_depth: deep-read
title_original: "Introduction to Nuclear Reactions"
authors: [Carlos A. Bertulani, Pawel Danielewicz]
publisher: "CRC Press / Taylor & Francis Group"
year: 2021
pages: "421"
isbn: "9780367353629"
canonical_source: "C. A. Bertulani and P. Danielewicz, Introduction to Nuclear Reactions (2nd Ed.), CRC Press (2021)"
library_file: "raw/books/Introduction to Nuclear Reactions (C.A. Bertulani P. Danielewicz) (Z-Library).pdf"
raw_file: "raw/books/Introduction to Nuclear Reactions (C.A. Bertulani P. Danielewicz) (Z-Library).pdf"
raw_sha256: "ad1391abd781e2277433283b6635679cfc45efc9d9d5472d4aabcd172509cb71"
nuclei: []
reactions: [compound-nucleus, direct-reactions, optical-model, hauser-feshbach]
experiments: []
models: [optical-model, hauser-feshbach, coupled-channels, semiclassical-scattering]
topics: [nuclear-reactions, transmission-coefficients, level-density, scattering-matrix]
---

# Carlos A. Bertulani & P. Danielewicz 2021 - Introduction to Nuclear Reactions (2nd Edition)

## 专著全貌与学术定位

本书是国际通行的现代核反应理论进阶教材（421 页，第二版）。系统阐述经典与量子散射理论、分波相移与光学模型势（Optical Model Potential）、DWBA 扭曲波玻恩近似直接反应、以及统计复合核反应的 Hauser-Feshbach 理论与能级密度公式，为评估熔合蒸发反应中不同出射通道（$xn, yp, z\alpha$）的角分布与分支比提供了严格的微观微分截面计算基础。

## 核心章节精要与理论内容

### Chapter 6: Compound Nucleus Reactions & Hauser-Feshbach Theory (pp. 175–218)
- **Hauser-Feshbach 统计截面公式**：
  考虑角动量与宇称守恒，从入射通道 $\alpha$ 经过复合核状态 $J^\pi$ 衰变到出射通道 $\beta$ 的微分截面为：
  $$\sigma_{\alpha \beta}(E) = \frac{\pi}{k_\alpha^2} \sum_{J^\pi} \frac{2J + 1}{(2I_p + 1)(2I_t + 1)} \frac{\sum_{l, s} T_l^\alpha(E) \cdot \sum_{l', s'} T_{l'}^\beta(E')}{\sum_{\gamma} \sum_{l'', s''} T_{l''}^\gamma(E'')}$$
  其中 $T_l(E)$ 为出射/入射分波穿透系数（Transmission coefficient），由光学模型势在通道边界严格求解径向薛定谔方程获得。
- **分波透射系数与势垒穿透**：低能带电粒子（质子、$\alpha$ 粒子）受到强烈库仑势垒阻挡，穿透系数 $T_l(E) \ll 1$，因而在低能重离子熔合反应中，中子蒸发（$xn$ 反应道，库仑势垒为零）占据压倒性的主导地位！
