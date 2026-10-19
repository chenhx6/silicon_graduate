# Day17下一有界问题：detector合并权重，分析前冻结

既有priming：已读ST99 Fig2/18台及SG98 Eq13/12台；旧研究页有common-a的未分峰convex mixture，但尚未覆盖逐detector不同a/Q与不同样本权重。前一shared-calibration设计及其28/31数学检查不作本问题新证据。

问题：一个合并null a≈1或η，能否保证不同target/gate具有相同零点与单一线性Q？

预计合同：clover原始Nperp_j=L_j eperp_j(1+Q_j P_j)，Nparallel_j=L_j eparallel_j(1−Q_j P_j)，a_j=eparallel_j/eperp_j。先限同P_j=P，明确L在U/r/t中是否相同；推合并A的常数/线性/分母项，检查a与Q相关时的非线性，不能把corrected yield权重当裸counts权重。

SG98每台总photopeak均值n_j对P不变（Eq13前提），C_j=n_j(1+sqrtη_j Q_jP)/(1+η_j)，S_j=n_j−C_j。推合并η_U与target/r不同weights时的截距/斜率，不能平均η或靠一个Q修复offset。

反证与负控制：匹配权重且相同a或Q的clover应退化线性；SG98相同null baseline应无offset；P=0与同reference roundtrip都不足以验证全部迁移；perdetector correction/explicit forward model应恢复design P。所有新数字均declared expectations，不推断原490/197Pb有偏。

有界收益：若能从原ST99 .95–1.05单台a及.99–1.01合并a给只依赖明示前提的上界，记录为条件设计；无actual perdetector illumination/Q/Σ时不得当原实验系统误差。完成精确代数、直接求和/独立Rational核验和必要input后，此代数局部应收敛，不用更大MC填时段。
