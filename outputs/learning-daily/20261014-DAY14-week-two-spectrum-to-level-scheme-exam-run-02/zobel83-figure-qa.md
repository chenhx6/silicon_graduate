# Zobel1983单图QA

Backend为本run既有Python/matplotlib，配置仅保存Wiki/tmp。目标为Wiki学习/方法附图；最终PDF尺寸140.00×110.00mm。

- 数据：原Table1共40个nonempty transition-setting rows，选958.0keV同一parent全部10行（alpha5/C5），其余30行属于不同parent，未用于本matched-parent问题。alpha9MeV这一列原文空白，未补零；raw表保持。CSV/fixture可回查每个beam energy与quotedstaterror。
- 图：单panel，数据为published LS fit means与marginalstaterrors，灰线为task-definedGaussian模型；不画jointCI或显著性。叠近的C点保留真实位置，未jitter或删点；两个beam family用circle/square区分。
- 源码validator exit0、0FAIL/3WARN：PNG400dpi/未导TIFF适合本Wiki预览，最终线图用SVG/PDF；140mm为本figurecontract尺寸，不采用期刊89/183mm默认。均已核实际输出，未标称期刊生产合同。
- Alignment：单plotarea，JSON记录NOT APPLICABLE；不称多panel对齐通过。PDFglyph audit exit0，最小字8pt，无小于5pt；最终collisionaudit exit0、0fail/0warn。
- PNG完整视觉检查：10个data points及误差可追溯，重叠C点与model/data颜色/形状区分正确；legend/citation/轴/脚注不裁切、不碰撞；这不认证统计模型正确或补出缺失Cov。
- 源表误差仅按quotedstatisticalerrors使用；诊断variance把其当std并选择rho±.8/0，属于任务敏感性而非作者矩阵或实验概率。

原Jul08 source人审范围不扩展，本run新增图/数值/模型是Codex自审。
