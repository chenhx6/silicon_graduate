# 自由级联反冲推导与使用边界

本文件是计算回执配套，长期公式保存在knowledge/methods/level-scheme-reconstruction.md的新锚。基于同M和Mf而非把两种不共享endpoint的cascade拼在一起。Mi²−Mf²=2M(h+l)−2hl、mi²=M²−2Me1。由末态on-shell得 E2=(mi²−Mf²)/(2[M−e1(1−c)])。共同c0=0 reference下，high-first E2=l−hlc/(M−h(1−c))，low-first E2=h−hlc/(M−l(1−c))。

能量和S与contrastX在独立等σ的Gaussian响应下可分；这是条件于选定c的声明统计模型，标签权重也chosen，不是boost后的完整angular-amplitude density。Contrast是两个±a的高斯混合，J用半Jeffreys/nats，非power或实际count要求。F(a)=E[-a+X tanh(aX)]²，leading J=F(a)(hl/M)²c²/σ²。Sum-order差为−hlc(h−l)(1−c)/[(M−h(1−c))(M−l(1−c))]，O(M^-2)，不该用两个M²大数减法数值冒充零。

完全stopping需要环境转移动量/动能，不能把它当对自由p_final的Lorentz变换。保持原free c0 anchors和共同Mf时，second-rest E*=e_anchor (M−E1)/sqrt(M²−2ME1)，仍有O(M^-2)常数；去掉的是O(M^-1) opening-angle项。该边界修正先前“stopping可能全消失”的预测。

可选sympy symbolic probe因本环境未装sympy而失败（ModuleNotFoundError）；未安装新依赖，改用Fraction对5个opening cos×两种order精确验证4vector不变量，boost作为独立float控制。正式66checks通过，未借失败probe生成结论。

用户断网延期后执行，原15:37closeout只为历史。所有M/σ/isolated/free/共同response为设计，source只提供.6keV名义gap与order未定；不重测质量/τ/次序或给pvalue。
