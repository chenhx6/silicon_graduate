# Selected analytic projection control：执行前合同

唯一写入目录：`tmp/day23-theses/ce133-projection-control/`。不改canonical、raw、课程/学分、review或Git；不运行Day22或父代理producer，不派生agent。

问题：量子算符先平方再投影，与先投影再平方有何差别？固定内禀态空间，能否解释为严格经典矢量且无横向涨落？

来源动机仅限133Ce论文：Eq3.14（PDF45/印34）Hcoll=Σ(Ik−jk)²/(2Jk)，Eq3.22（PDF48/印37）磁算符；Table6.6（PDF99/印88）|18>主分量0.981|5h11/2,+9/2>并含f7/2,+5/2及h11/2,+5/2；Ch6.3.3（PDF107–108/印96–97）单轨道|18> FA与重取向的作者解释。原PDF SHA256 48556dbfe5284efebdb901cd949f534ac5552c6504e2c744603afca386660080。

控制对象：实验室固定轴的不可约单j=11/2空间，ħ=1，标准有限矩阵j±；P仅张成|m=+9/2>、|m=−9/2> Kramers对子，Q=1−P。选它只因接近源主要分量，**不是133Ce真实|18>，不是把top3归一得到的态，不是作者FA输入或本征态复现。** 把z轴选作该控制的量子化轴，不据此重定原文全部轴/形变。

解析预期：PjxP=PjyP=0，PjzP=diag(9/2,−9/2)；Pjx²P=Pjy²P=31/4 I2，Pjz²P=81/4 I2。由Pjk²P−(PjkP)²=PjkQjkP得到正半定漏出项。对最高权重m=j，横向二阶矩仍j/2=11/4，而非零。

实现依赖探测：本环境没有SymPy；不安装新依赖，精确路径用标准库Fraction和平方自由根式运算，浮点矩阵路径用NumPy。

验证：标准库有理数-根式精确矩阵路径、独立ladder action路径与解析j(j+1)式交叉核；时间反演T=U K，T²=−1、P保持、j为T-odd、二阶矩为T-even。另做m=±1/2等反例与全空间极限，避免把选定高m子空间性质推广到任意Kramers对子。

投影H控制：用一个独立整数spin-L=2有限空间上的外部Xk，构造H=ΣAk(Xk⊗1−1⊗jk)²，Ak>0。这里只演示与投影可交换的外部算符的compression identity，**不是精确body-fixed QTR的总I表示或核能谱**。Ak采用人为有理数，与133Ce实测惯量/模型Harris参数无关。比较P H P与先代入PjkP再平方，记录被漏掉的recoil项及其是否只是常数；不得称新转动谱、模式指认或wobbling否证。

Rayleigh–Ritz：只在固定同一Hermitian H、同参数/算符/能量零点、真正嵌套变分空间中比较有序本征值；不同I block、不同模型参数、不同零点、不同状态映射/重新定标的excitation energies不能自动用变分不等式排序。控制中同时展示可适用例及改变零点使excitation比较失败的反例。

验收不含实验CI、寿命、g、Q、δ的新估计。报告误差仅为精确恒等式或数值线性代数残差；不把有限矩阵误差写成实验不确定度。
