---
type: source
title: "Diddens et al. 1958 - Oriented 56Co decay to 56Fe"
title_original: "Angular Distribution and Linear Polarization of the Gamma Rays from Oriented 56Co Nuclei"
aliases: []
created: 2026-11-21
updated: 2026-11-21
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
authors: ["A. N. Diddens", "W. J. Huiskamp", "J. C. Severiens", "A. R. Miedema", "M. J. Steenland"]
year: 1958
doi: "10.1016/0029-5582(58)90009-9"
canonical_source: "Nuclear Physics 5 (1958), 58-88, published edition"
raw_file: raw/papers/gpt/query/20261119-polarization-delta-collection/10.1016_0029-5582_58_90009-9.pdf
raw_sha256: cd34e9cddf5423c6c6a5445abac3eea3e1a2244f7738baf655502ae0fcd67446
raw_storage_status: archived-local
archive_required: true
archive_manifest: raw/papers/gpt/query/20261119-polarization-delta-collection/manifest.json
nuclei: ["56Co", "56Fe", "56Mn"]
tags: ["linear-polarization", "angular-distribution", "mixing-ratio", "nuclear-orientation"]
---

# Diddens 等 1958：⁵⁶Co 核取向、⁵⁶Fe 线偏振与混合比

## Bibliographic Record

A. N. Diddens、W. J. Huiskamp、J. C. Severiens、A. R. Miedema、M. J. Steenland，*Nuclear Physics* **5**, 58–88（1958）。PDF 1–31 对应印刷页 58–88。一页题页摘录与出版版同源。

## Scope and Reading Depth

覆盖 31 页的仪器、采集、方向分布、极化、指认、结构讨论和书目。目视核对表 2–5、图 10 与主要解支。

## Summary

室温符合用于确定 ⁵⁶Co 衰变进入 ⁵⁶Fe 的主要级联，低温取向的角分布与极化则用来判断这些跃迁的多极性。1.75 MeV 与 2.02 MeV 的混合比证据不同。前者有单线的极化条目，后者仅有合窗比较，并用 Sakai 的方向关联限制主分支。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator |
| --- | --- | --- | --- | --- |
| D58-DECAY | 700–900 keV 正电子门关联 0.845 和 1.238 MeV 主 γ。β 谱仪对约 0.9 MeV 的正电子分支给 1% 上限。两条主 γ 的符合谱检验时，1.75 MeV 峰至少 80% 与 1.238 MeV 线符合，弱线的近邻分量未能排除。区分 ⁵⁶Co 的 1.75/2.02 MeV 与 ⁵⁶Mn 的 1.81/2.13 MeV。 | spectroscopy-and-line-assignment | direct-original-pages | PDF 4–14，表 1、图 2–6、§4 |
| D58-P | Ce–Mg 硝酸盐内的 Co²⁺ 在约 300 Oe 极化场中测量。角分布使用 \(\varepsilon=1-W(0^\circ)/W(90^\circ)\)，温态 1 K 用于归一。极化用塑料散射体和 NaI(Tl) 侧探测器，\(\chi\simeq75^\circ\) 且接受范围约 ±15°。式 3 给 \(N_\perp/N_\parallel=(1+\bar QP_1)/(1-\bar QP_1)\)，实际对低温比值再作 1 K 归一。 | setup-and-observable | direct-original-pages | PDF 2–4、14–20，§§2、5、6、图 7–8、表 2–3 |
| D58-175 | 1.75 MeV 的 \(P_1=+0.0754\pm0.027\)、\(\varepsilon=-0.09\pm0.04\)（\(1/T^*\simeq125\)）。作者偏好 3.84 MeV 态 \(3^+\)，以 1.75 MeV 支路到 2.08 MeV 的 \(4^+\) 态，\(\lvert\delta\rvert\lesssim0.05\)、代表值 −0.03。\(5^+\) 对应的 +0.04 仍可在误差边缘；2.99 MeV 弱线归属和 1.75 MeV 可能双线影响排序。 | mixed-transition-and-alternative | direct-original-pages | PDF 20、26–28，表 3、5，图 10、§§7.2、8 |
| D58-202 | 2.02 MeV 的 4.10→2.08 MeV \(4^+\to4^+\) 线是主 E2 的 M1/E2 混合。角分布有多支。当时既有角关联支持 \(+5\lesssim\delta\lesssim+15\)，表 5 用约 +10。正文保留更大的正支和约 −30 的负支。2.02 MeV 与 1.75 MeV 合窗只提示 \(P_1,\varepsilon\) 的相对符号，表 3 无 2.02 MeV 单线 \(P_1\)。 | conditional-mixing-ratio | direct-original-pages | PDF 20、25–28，§§6.2、7.2、8，图 10、表 4–5 |
| D58-ORIENT | 用 \(f_k(I_1,\beta_0)=V_k^{0-1}f_k(I_0,\beta_0)\) 传播母态取向，\(V_k\) 依赖先行 β、γ 链。利用 3.25 MeV 的方向各向异性，在 \(1/T^*=250\) 估 \(\beta_0=0.62\pm0.07\)。表 4 用 0.60 做说明性回算，同一方案在 \(1/T^*=125\) 用约 0.40。母态等距磁子级是有范围的参考近似。 | source-specific-orientation-model | direct-original-pages | PDF 20–27，式 4–5、图 9、表 4 |

## Competing Interpretations and Limitations

- \(\beta_0\) 参考量和母态到子态的级联传播属于低温核取向。原文也指出实际 Co²⁺ 晶体的磁子态非等距，此近似用来估计小的四阶项。用表 4 回算符合只能说明所选 \(\lambda_1,\lambda_2\) 可用，不能据此确定衰变矩阵元或在束 \(\sigma/I\)。
- 极化标定采用接受度平均的计算 \(Q\)，用 ⁵⁶Mn 谱作控制。表 3 的 3.25 MeV 给 \(P_1=-0.065\pm0.045\) 与 \(\varepsilon=+0.20\pm0.025\)，正文保留它与纯 E2 理想关系的量级不符。温度误差和有限能量分辨的校正边界见 PDF 20。
- 2.61 MeV 在作者偏好的 \(3^+\to2^+\) 解释下 \(\lvert\delta\rvert<0.04\)。负宇称备选要求不同类型 E1/M2，故和 1.75/2.02 MeV 的 E2/M1 记录分开。表 5 的 1.81/2.13 MeV \(\delta\) 引自 ⁵⁶Mn 测量。模型讨论的振动解释依赖当时的能级和强度，保留为作者解释。

## Extracted Pages

- PDF 1–7：身份、冷源、电子学、谱分解和早期结果。
- PDF 8–14：β–γ 和 γ–γ 符合、上下限和衰变纲图比较。
- PDF 15–20：温度归一、几何和 \(Q\)、直接偏振及误差。
- PDF 21–31：按阶传播、混合比分支、能级图、振动模型与书目。
