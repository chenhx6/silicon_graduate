# 075：Butler1975 La 寿命写回短审

**本审未发现实质P0/P1，verified no-op；无required科学修正。** 新Butler source准确保留了寿命测量、feeding、邻偶核定标及模型预测边界。canonical未改。

实际复核范围：新source全页、已知原件`tmp/day24-butler1975-la129-la131-lifetimes-071/attachment-object-response.pdf`的4页text与fresh visual；SHA `231b6f427ac9bdd15688bf373959d2dff63dd7e694ee2dbb9b12cc0186ba8e0a`、4页/268368bytes核对一致。原件直接读取Table1、Fig1–2、14% stopped、joint fit、速度/角修正和模型讨论；未重读Refs3–7、未取得counts/producer/fullCov、未重拟曲线。

核验通过：

- 131La最大flight400/1600ps仍有14% stopped，原文把主要成分归直接sidefeeding至15/2−并对Fig1 ratio作修正；source没有把14%写成普遍比例、纯指数数据或任何核素通用校正。
- 129La/130Ce/131La速度.0087/.0103/.0105c及有限Ge立体角、velocity-spread检验均限本实验；没有扩大为所有recoil-distance实验 response定理。
- 两低态曲线通过least-squares同时拟合；19/2−前feeding以≥2个自由寿命level、23/2→19/2曲线形状及共同origin约束。source仍说τ/feeding/zero可能相关，未把四τ当独立指数或制造Cov。
- Table1四个La中心寿命与B(E2)及130Ce新211(9)ps、旧225(19)ps均按原表保留；没有把La τ迁133Ce，也未因同作者/装置抹掉130Ce新测量。B转换缺逐支BR/ICC/actual代码合同，因此不以source缺项否定原reported B。
- 邻偶核B作为core定标、λ/Δ/γ由模型和even-spectrum体系取参的依赖写得清楚；同PartII/Table5的数据谱系没有重复计成独立实验。14%/feeding与core calibration没有被隐藏成独立likelihood。
- Table脚注的β/A^(2/3)=6.8/6.4与正文/图中的乘积保留为literal print boundary；未除法造β、未据此裁全部模型错。Fig2的约5%稳定范围(b4–7、e1≤λ≤e2)是模型参数敏感性，不被写成实验CI或完整理论误差。
- Fig2 γ扫描35°附近15/2 crossing和35–45° B振荡被正确标为模型输出；高23/2/27/2曲线仍是prediction，不当实测spin crossing或已报告B。qγ=.942/.980/.981/1.009的条件mean-life pure-E2算术仍明确不是BR/ICC/actual conversion或程序错误诊断。
- higher/first weak-coupling/core假设被限定在原文：还需额外rotational/vibrational core、4+→2+数据不足；没有把“约1.4/2”写成排除所有weak/soft模型。La support不升级为γ-rigid、chirality或133Ce寿命证明。

唯一可选文字注意：source将`mean-life convention`与原表τ已清楚区分；后续若引用数据库half-life，仍需避免复用这些ps值。该项已在source写明，不构成required修正。

本轮只写075 worker和tmp；未修改canonical/raw/PLAN/Bib/Git/producer/课程/session，无新模型、fit或实验结论。结论为source self-audit，不称human-reviewed。
