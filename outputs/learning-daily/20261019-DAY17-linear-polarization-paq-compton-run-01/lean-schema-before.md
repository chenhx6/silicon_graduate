# 默认Lean消费端：原样body的schema与失败控制

本问题先前已读source，非盲测。CMake固定版本默认构建LeanAnalyzeComptonMatrices；newhelper输出xiThetaDet/Cry/Mixed/Count，Lean却读取XiHist2D_DetDetCoincidenceTheta等六个不同key。仅同仓库/同Compton名称不保证可串联。

执行前合同：完整原Lean source通过include改名main和batch-entry wrapper执行，唯一runtime附加为gROOT->SetBatch，禁止GUI；启用现有ROOT MathMore宏。fixture generator用真实ROOT写两套六TH2D key，固定180×180 bins、0–180.000001角范围，prompt均值1000(1−.2cos2ξ)、mixed1000、geometry1。这是设计期望直方图，不是data、Poisson抽样或原fits/Σ。

case1只有newhelper命名，预期暴露缺schema输入；case2为Lean所需legacy命名，作为原program正控制。保存actualreturn/signal/error/outputkeys/fitparameters，不能将exit0当物理P/Q认证。代码default62Ga template/Mixing1=.5不代表实际reference，不能以该template生新实验偏振。

所有input/binary/output在repo tmp，本run保存manifest/hash/result。原producer源/原SDK/globalconfig不修改；原程序失败属于局部证据，不抹去、不自动patch第三方；如timeout只记录本handle状态，先确认运行再决定，不重启其它session/daemon。
