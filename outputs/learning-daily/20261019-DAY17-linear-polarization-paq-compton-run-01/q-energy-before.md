# Q能量缩放的实际原程序核验前合同

已读fixed GRSISort ScaleQ源函数与调用：函数comment将En1称calibrationenergy、En2称targetenergy；函数返回uniformtheta平均KN analyzingpower的Q2/Q1。Lean主调用(energyMeasured,energyUsed)与Plot循环(i,energyUsed1332)不同。这里有明确的参数角色疑问，需实际原程序输出，不从metadata/注释给实验结论。

执行：不改Compton_Scale_Plot.cxx或Globals.h，链接真实ROOT，保存原wholeprogram编译/输出/hash。另用函数原body组件计算1332→100/3000与100/3000→1332的互逆控制；如输出相乘恒等只是代数自检，不认证实测Q(E)。必要对照为同一fixedsource旧Lean的调用行。

物理边界：ScaleQ用均匀theta平均单次KN sensitivity，未有真实detector solid-angle、energy threshold/多散射/效率权重；不能用理想平均替实际阵列Q或把plot方向问题判为历史实验失败。无新data/Σ，不扩为experimentalCI。
