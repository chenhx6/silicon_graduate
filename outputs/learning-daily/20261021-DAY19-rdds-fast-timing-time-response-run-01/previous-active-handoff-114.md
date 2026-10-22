## Active handoff — Day19 checkpoint113，阵列合并权重与对齐平移消去条件

原run/session/15:00上海研究截止，goal active，completed[]/partial[19,20]/next19/count18；未收束/授分/发布。108撤回095–107保持；109–111声明模型/校准设计、110TDPAD原读scope及112GCD公开发表稿阅读保持。

基于 day19_gcd_pooled_weighting113.py 与 gcd-pooled-weighting-result-113.json（1200次MC与解析方差比1.009），建立多探测器合并GCD（Régis 2015 Eq. 11/Sec. 3）的数据处理合同边界：
1. 对齐平移消去条件：对每对探测器施加的常数时移 s_i 在单对差 DeltaC_i 中自然消去；但在合并质心差 DeltaC_pool 中，平移严格消去的充要条件是 start 与 stop 分支具有严格对称的对权重（w+_i = w-_i）。角色不对称权重（如 [0.8, 0.2] vs [0.2, 0.8]）在两对模型中造成 36 ps 残留偏差，平移不变性被破坏。
2. 校准 mean PRD 样本匹配条件：若校准级联与目标级联在各对间的产额分布不同，mean PRD 必须使用目标级联的匹配权重加权；若误用标量无权均值，在两对模型中引入 9 ps 系统偏差。简单原始计数相加仅在各对事件数相等时等价于无权理论式。
3. 证据状态：新 RG15-9 记录于 regis-2015-generalized-centroid-difference.md，同步写回 recoil-distance-doppler-shift.md 与 lifetime-method-selection-response-contract.md。此控制定义数据处理边界，不断言原 EXILL&FATIMA 实验存在违约。

三页writeback valid/unmapped空、lint 0 error 251 warning（两项预留raw/citation_key警告已隔离）、boundary/preflight/protected hash与diffcheck全部通过，receipt 113。距15:00截止约120分钟，按计划进入综合收敛与收束前准备，不开新源，不开Day21。
