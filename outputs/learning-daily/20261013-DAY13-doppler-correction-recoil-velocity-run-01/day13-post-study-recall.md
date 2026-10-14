# DAY13 来源后复述与判定边界

原 run/session 继续；这次是学习后的 self-audit，不是来源前盲测、human review 或正式 Day14周考。答案的长期 owner 均在 knowledge；本页只保存题目、回忆要点和核对结果，不作为论文事实源。

| 问题 | 本次复述要点 | Canonical 核对位置 | Self-audit |
|---|---|---|---|
| E0=E_labγ(1−βcosθ)里的β是谁？ | 对应选定reference的vector/epoch。直接解释为母系restE需要emissionparent；exitreference可以保留history，但模板须同observable。 | doppler-correction：精确式、photonrecoil及校准适用性 | pass |
| 为什么较窄correctedpeak不能单独证明速度正确？ | 位置/方向、response、gate和meanvector优化可给相同局部结果；需要producer、独立控制、fullshape和sharedΣ。 | Doppler诊断表、widthrank2、validationcontract | pass |
| scalarβ很精确，vector就唯一吗？ | full localrank也可有global镜像；PID/RF另有离散branches。 | vectoridentifiability、RFalias已有例题 | pass |
| 为什么最终重分bin不能加成独立统计量？ | 使用同events，crosscovariance由eventmarks决定；不同粗分区联合可以取回summary分辨信息，仍无新raw事件。 | 共享事件、总计数设计与重放的信息 | pass |
| 中点×bin宽再归一化够不够？ | 未必；exactbin积分、ROI分母和edges影响shape。自设粗bin拟合偏移不是sourcebias。 | 有限能量bin、BC84-2 | pass |
| 每bin≥10能担保统计无偏吗？ | 不担保；countstatistic、data-dependentedges、background和modelcorrectness需各自检查。 | 均匀rate与adaptivebin反例 | pass |
| 共用background或MC可以当独立bins吗？ | 共享off产生交叉项；normalizedweightedtemplates有零方向和共同event跨参数cov。差分误差有时抵消，不是统一方向。 | 共享background、finiteMC与sum/differencecontrols | pass |
| 联合68.3%区域、τprofile和τ投影是不是同一件事？ | interest维数/threshold不同；必须按指定observable和nuisanceprofile解释，边界/不可识别也改变asymptoticlaw。 | 非线性region与semantic replay | pass |
| profile速度nuisance的模拟closure能否验证实际βtag？ | 只验证独立无偏tag/已知family前提；真实tagstage、sharedcalibration、bias或differenthistory仍须数据证据。 | 速度nuisance：forwardmodel边界 | pass |
| 长lineτ≫Tcross是否意味着完全没有history问题？ | 不；finitefraction、estimator/window、vertex和referenceframe仍需界定。mode不能普遍消除geometry误差。 | 长控制线、CM21-15/16/22、applicabilityaudit | pass |
| CM21图9的0.4%/0.7%能否作为σβ？ | 是aftertargetvelocity/T的tuning幅度，非σ或entryvelocityresolution。 | CM21-22 publishedp7/Fig9 | pass |
| 能否据这些toys解释20O150/70fs或给新absoluteB？ | 不能；真实events/response/Σ/feeding/code缺失，两采集与模型依赖需分层，τ/branch/δ契约仍缺。 | validationcontract、a130thesismatrix、sourceCI20/ZA23 | pass |

十二项复述能回链到canonical owner；没有新的Day卡学分。科学未知仍留在actualpacket/readiness，不把self-score写成人工审查或实验验证。
