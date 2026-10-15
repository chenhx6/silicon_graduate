# exploratory probe边界

2026-10-15T09:36:27.062152+08:00。首个scratch probe在输出时因numpy.bool JSON不可序列化exit1，且复核helper签名发现direction需rad而误传degree；没有保存或采用这些scratch数值/模型结论。现用显式deg2rad(40/90)及Pythonbool重新计算；正式witness/ranges须在单位与rotation/normalization检查后持久化。预冻结的geometry仍为40°/90°，没有更改以强求1.45。
