# L26 Fig4 averaging前假设与边界

当前只延续原Day16/partial17，原2026-10-19 15:00上海截止不变；正式16一次，不正式17/18。已读完整L26与M22、知道Fig4作者Pbar约.35/.53与A0 .028/.044，明确strongpriming，不称盲重放。

本bounded问题使用**原公开Figure4 top的C(theta)曲线**，先按真实PDF vector/raster形态检查可否可靠digitize。曲线是1238-keV56Co的角覆盖，任意纵向scale归一后消去；它不是本run取得的rawgamma或2DComptonresponse。theta histogram若已是counts/bin，积分measure是dtheta，不能再乘一次sinθ；改用cosθ时要正确Jacobian。轴范围/zero baseline只能由原ticks固定，不能为目标.35调offset或曲线。

用原measured a2=.34/a4=-.12、beta=.044和Eq12/aberration计算physicalP(theta_lab)。先复算作者的coverage-weighted平均，再在**声明positive/factorized kernel**下比较含Wlab的event-weighted平均；实际producer是否先按theta归一、C是否同≥2/cut/multiplicityselection不明，两者差不能直接称作者错误或解释A0差异。jointtheta-psi响应下，平均Sigma*P一般不等于分别平均之积，需记录缺哪个jointkernel；这与统计fitCov是不同对象。

必须保留digitizationprecision/原图sha和失败控制：constantW时两平均同、unpolarizedP0同、overallCscale不影响；若图形可靠性不足就明确readiness，不重画想象response。无新counts/拟合/实验P或Q。当前helper/sourcehumanprefixoldflags不动，科学delta写knowledge再requiredchecks/pub。
