# 汇报证据索引

这是汇报索引。长期物理知识由下列 knowledge 页面维护，计算回执不替代原件。
没有使用或发布 iThemba 私有实验数据。

| ID | 确定的证据对象 | 原件／计算定位 | 长期知识入口 |
|---|---|---|---|
| E01 | 129–137Ba最低11/2模型矩与五态通道份额 | `raw/writing/gpt/odd-ba-quadrupole-closure/data/results/calibrated-chain.json`，`cases[*].primary`；Nomura2017 Eqs12–15 | `knowledge/research-notes/odd-ba-quadrupole-closure-and-spin-channel-redistribution.md` |
| E02 | 固定其它相互作用的135Ba Gamma五点路径 | 同稿件`data/results/quadrupole-path.json`，`points`及`adjacent_overlaps` | 同E01 |
| E03 | 固定γ=20°无配对粒子—转子控制 | `../rigid-core-control/{protocol.json,results.json,proof.md,checks.json}`；5个C、全部48个15/2态 | `knowledge/research-notes/fixed-shape-particle-rotor-quadrupole-proxy-control.md` |
| E04 | 135/137Ba原理论谱对照 | `../source-chain-replay/{source-points-frozen.json,comparison.csv}`；原arXiv v2 PDF p7 Fig5(c) | `knowledge/research-notes/ba135-ba137-source-energy-replay-boundary.md` |
| E05 | Vogt2017的能级、寿命、E2及依赖 | `raw/papers/gpt/query/20261106-vogt2017-ba137-rstat/manifest.json`；accepted PDF Fig6/7、TablesII/III | `knowledge/sources/vogt-2017-135xe-137ba-isomers-high-spin.md` |
| E06 | 有符号完整q2/q3、有限自旋闭合 | 稿件`data/code/quadrupole_scalar_invariants.py`；E03的独立几何／Euler积分检验 | E01与E03知识页；`knowledge/sources/quadrupole-invariant-spin-channel-precedents.md` |
| E07 | 固定Hamiltonian的E2中央值分支 | 稿件`data/results/calibrated-operator-predictions.csv`，5个标定分支加主参考；静态矩评价原文 | E01知识页；`knowledge/sources/nndc-ba135-ba137-static-e2-constraints.md` |
| E08 | 137Ba 28个预定强度比较及14个衰变图上界 | `../isomer-benchmark/{results.json,decay-width-results.json}`；模型能量、全部开放E2通路 | `knowledge/research-notes/ba137-isomer-e2-network-validity.md` |
| E09 | 独立单位与算术／解释复核 | `../isomer-source-review/{unit-audit.json,checks.json}`；`../isomer-review/{review.md,arithmetic-checks.json}` | `knowledge/sources/nndc-e2-weisskopf-direction-and-lifetime-ratio.md`，BM-I printed382 Eqs3C-16–18 |
| E10 | 四书阅读证据对账、实际六页单元 | `../book-coverage/{coverage-reconciliation.json,reading-unit.json,closeout.json}`；BM-II PDF66–71/printed44–49 | `knowledge/research-notes/book-reading-coverage-reconciliation-20261106.md` |
| E11 | 上一阶段10页候选稿、本阶段收束状态 | 稿件`main.pdf`、`README.md`；本目录`brief.md`、`layout-check.json` | E01、E03、E08知识页和本轮handoff |

Nomura原件为arXiv:1704.07101v2，对应PRC96,014304(2017)；这里的
“原谱”指本地该版本图中数据，未另行认证期刊最终排版版本。Vogt原件为
PRC95,024316(2017)的accepted稿，PDF页码比稿件印刷页码多1。

图件由 `make_figures.py` 从已冻结JSON/CSV生成；输入SHA-256和实际绘图
子集写入 `figure-inputs.json`。线段仅连接已计算点，不代表补算中间点。
柱／曲线是模型结果；Vogt观测的报价误差与模型误差没有合并。
