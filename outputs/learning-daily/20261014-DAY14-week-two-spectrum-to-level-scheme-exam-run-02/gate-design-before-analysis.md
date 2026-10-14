# 当前问题的来源后、计算前预测

这是读完Herzáň后对同一Day14 continuity问题的设计预测，不是新的source-before盲测。尚未运行下面的gate toy，不改正式来源前冻结答卷。

1. 在单核单路径模型中，17/2+的299.2→323.4级联与622.4直接分支互斥；上方41/2+的299.8可先发射，再走任一下方分支。若gate/response已独立校准，622与323两个门应该给不同的299.2/299.8组分比例。
2. 两条谱线能量完全不可分时，一张门不能分两个强度参数；两个已知conditional gate系数可能补足rank。但branching、gate purity、效率若也未知，得到两张谱不自动解除全部nuisance。
3. 同一high-spin事件在323门下可贡献两条299-keV光子，因此逐bin/逐line计数不一定独立Poisson。需要区分固定parent N与Poisson parent flow，分析shared-event covariance。
4. 46/87-keV低能γ的非观测功效应包含α、效率、branch flow与统计。作者E2 conversion系数仅是本设计的有条件输入，不认证未观测路径或实际N。

自设模型将无IC、无额外feeding、无angular correlations、独立photon detection与纯门作为第一层极限；这些是可测试的toy假设，不能冒充JUROGAM实际response、branching或event selection。计算后必须检查b→0/1、门效率→0、相同response、未知branch和shared-count条件。
