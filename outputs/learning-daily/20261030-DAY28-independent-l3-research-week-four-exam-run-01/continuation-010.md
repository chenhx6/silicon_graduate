---
type: continuation
graph-excluded: true
created: 2026-10-31
updated: 2026-10-31
---

# Day28 continuation 010：1979 Irving primary 访问边界

- 当前时间：`2026-10-31T02:03:10+08:00`
- 硬截止：`2026-10-31T15:00:00+08:00`
- 当前课程状态仍为 `completed_day_indices: []`、`partial_day_indices: [28,29]`、`next_day_index: 28`。
- 继续当前 131Xe 主线，探测此前列为最高信息增益的 Irving et al. 1979 primary：
  - Crossref 取得题名、作者、J. Phys. G 5(11), 1595–1612 (1979)、DOI `10.1088/0305-4616/5/11/015`；
  - DOI、IOP article、IOP PDF 均返回约 14 KB HTML，未取得 PDF/正文；
  - 结果保存在 `tmp/day28-131xe-recovery/irving-1979/probe.json`，并追加至 `tmp/day28-131xe-recovery/report.md`。
- 科学结论没有升级：1979 primary 仍不能提供 794.6/794.8-keV 逐线 AD、偏振、转换电子计数或 mixing ratio；2020/2023 宇称冲突保持未裁决。
- 公开 IOP abstract 只增加 coverage evidence：提到 `131Xe` 的 `364.5`、`636.9 keV` 正宇称低能级以及角分布/线偏振/mixing-ratio 分析；abstract 没有 794-keV 目标线，不能替代正文。
- 日报 `Sources and evidence` 已增加访问探测记录；canonical knowledge 未新增页面，因此现有 writeback block 仍覆盖全部 knowledge 改动。
- 当前回执 `verification-037.json` 仍记录 writeback=true、boundary=0、diff=0、lint=314 baseline errors；若继续写入 canonical，必须重新运行 writeback、lint、boundary 和 diff。
- 下一步按信息增益顺序追合法机构馆藏/作者副本；若无新正文，转入 Day28 正式 card audit，不再重复 IOP HTML 探测。
