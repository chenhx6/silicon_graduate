# source-to-beam响应合同：量化前冻结

2026-10-16T09:42上海附近。Priming已由day15-tracking-response-before-sources.md记录。当前直接读25页本地manuscript与24页publisher的Intro/Sec3/Figs6–10/Summary/AppB相关段；posterior发现不冒充盲预测。

已知来源：article76（publisher/Crossref/Bib同），原Wiki81待精确修正；publisherPDF Eq18定义thetaCM，Eq19字面theta无lab标；不未查code就宣称作者实际做错。数据/code为reasonable request，未向作者发消息。响应矩阵重归一/插值/外推、variance调整与Fig8/9系统波动均源明确。

本任务选一个source-to-beam输入合同练习：
- 由Eq18的u=(x-beta)/(1-beta*x)独立求du/dx及光子4vector energy。检查beta0、全域归一、反向boost、局部导数；把Eq19字面u/x两种读法分开。用sourcebeta=.027/Erest991/70–175deg条件生成所需labenergy表，非measuredresponse和源code诊断。
- 先明确measure dcos(theta)与dtheta。scalar source-response只在matchedmeasure/support/selection下相除；response实际依赖labenergy时要按每个angle取相应能量，原文未给本任务可重放的axis/sorter约定，不补做法。
- 以显式chosen two-source independent Poisson计数和归一/线性插值定义，解析Jacobian传播展示共享Cov。它不是作者variance算法，也不用插值图重造actualmatrix。
- 弱/zeroresponse、额外trigger/gate和config/threshold/multiplicity差异维持readiness；不以小beta Jacobian例解释Fig8原systematics或重拟sigma/delta。

停止条件：原literal/推导/模型点/实际观测严格分开，规范表/反证/可复算检查写canonical method和source；保留旧humanreview/needsflags。正式14成绩不变，15仅preview、不开16。
