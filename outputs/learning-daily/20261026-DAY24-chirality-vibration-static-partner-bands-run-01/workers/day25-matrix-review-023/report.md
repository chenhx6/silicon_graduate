# 三核companion矩阵独立审查023

结论：矩阵的逐核/逐pair科学分层与受检原件相符。发现的两项措辞风险已传root并在当前project内修正；定向复读未发现需否定原逐核支持的新P0/P1问题。没有为review补造新问题。

本轮只审已有source/project与本地raw关键定位；无联网/下载新body、无旧producer/114运行。仍为Day24中恰好下一卡Day25的无学分preview；未创建新卡/session/credit。本worker只写指定worker/tmp，无canonical/raw/PLAN/Bib/Git变更。以下self-audit不升级human-review状态。

## 已发现并由root修复的两项

| 原措辞与位置 | 风险 | root当前修订及复读结果 |
|---|---|---|
| project原line33“2019独立谱学扩展” | 未限定独立于谁，可能被读成LV19与PE18也是不同采集、可给独立实验票 | 当前line33改为“独立于MU07的另次采集”；line39另列与PE18共同campaign的支撑及selected-event/producer/Cov未知边界。受检层次正确 |
| project原line62“双方…独立clock”；“没有τ只得relativeEM” | 统计独立不是两带寿命可用的普适必要条件；jointfit/sharedCov也能提供逐态clock。后半若脱离当前相对γ方法，会错误排除其它absoluteEM约束 | 当前line64明确允许jointfit/共享Cov，并把无clock降级限定为“仅有相对γ资料且没有其它absoluteEM约束”。符合本页问题设计定位，不是普适模式否决门 |

root是实际修改者；本worker没有写canonical。复读的行号对应本报告保存的project snapshot，后续编辑可能移动。

## 同campaign：实际证据、推断强度和未得项

1. **LV19 arXiv PDF2/printed2 §II**直接报告152MeV 40Ar、K130/Jyväskylä、0.5mg/cm² enriched self-supporting100Mo、JUROGAM-II 39个suppressedGe；setup/data-analysis转引Ref38，RDCO/Rac定义也称与Ref38相同。**PDF7/printed7 Ref38**明确是B.F.Lv et al.,PRC98,044304(2018)。仅同定义不证明同producer或同事件选择。
2. **PE18 canonical PDF2/printed041304-1末段**给同152MeV/0.5Mo/Jyväskylä装置条件；**PDF3/printed041304-2左栏**不仅列5.1×10¹⁰共同fold≥3 prompt events，还明确**135Nd与136Nd是本次反应同时最强布居的两个核，各约100mb**，TDR记录、GRAIN排序、RADWARE分析。故不是仅凭相同事件数作依赖判断。
3. **已有吕冰峰thesis raw PDF66/printed65 §4.1–4.2**把两核合在一个实验叙述中：同一experiment用100Mo(40Ar,xn)布居135,136Nd，随后同页记共同的5.1×10¹⁰/TDR pool。该证据已在Wiki atomic claim里，无需新增source或只留outputs。精确入口见下一节。
4. PE18 PDF2称完整纲图将见Ref34；**PDF7/printed041304-6 Ref34只写B.F.Lv et al.(unpublished)**。它与LV19 Ref38为后续完整分析的书目路线一致，但**本worker未找到并读取PRC98,044304的独立body**，不以一个未命名的unpublished条目单独完成版本一一认领。

综合：**同campaign/同母采集pool的谱系支持足够**，因此不能仅凭不同核、2018/2019出版年给两次独立采集票。仍未取得具体run编号/active detector mask/selected-event intersection、两核各自gating/calibration producer及jointCov；既不能宣称两个channel使用完全相同histograms，也不能假定它们完全统计独立。两核的具体物理观测仍各有自己的内容，不因共享采集一并失效。

LV19相对MU07的另次采集与相对PE18的共同campaign是不同关系，不能用一个“独立”标签跨这两条边。

## 可直接复用的thesis知识入口，不新增未回写事实

- 现有source：`knowledge/sources/lv-bingfeng-2019-chirality-136nd-135nd-thesis.md`。
- **DD-20260910-136ND-01**（当前source line80）已记152MeV反应、135/136Nd、5.1×10¹⁰、single dependent campaign；**DD-02**（line81）已记与PE18依赖。
- source line115 limitations明确本thesis与两核期刊存在campaign/data lineage依赖；**AR-LV-1**（line121）也将两核归同Jyväskylä campaign。
- 实际raw：`raw/papers/degree dissertation/吕冰峰.pdf`；SHA256 **84e8b934fda9a97ea79527a8b1456f40e534bc67be847d61b1a1219002d85749**，164页。
- 本轮只fresh读**PDF66/printed65**的§4.1、§4.2及校准段开头，视觉核同页；另文本读**PDF67/printed66**的校准续段。未重读164页，也未恢复真实calibration constants。
- 短原字面定位：PDF66 §4.1开头“High-spin states in135,136Nd were populated…”位于同一“The experiment”段；§4.2开头“In this experiment…”后直接给common event pool/TDR。完整原段的定向text/render在本worker tmp，不取代原件。

建议root在project共同campaign段引用上述既有atomicID，以便这个依赖事实仍有knowledge落点；不需要把thesis算第三份独立实验。

## 其余科学层次核验：保留，不要求改写

**134Pr PE06：**PDF2/printed112502-2直接给15+/16+的36/44keV能差及明确的两带混合假设（忽略off-diagonal E2、短段V不随spin变）；PDF3/112502-3 Eqs3–5/TableI给odd/even V约14/17keV和Q0,1/Q0,2允许1.6–2.4。2.0(4)不是新直接形变测量或已定义Gaussian CI。PDF4/112502-4 Ref9为寿命来源，Ref11为branch数据且当年to-be-published；结论保留手征几何残余的问题。矩阵将其写成对simple ideal pair的实质限制，没有扩大到所有动态手征不存在，符合原件支持及边界。

**135Nd正/负families：**LV19 PDF4–5明确J0按能谱调，负pair γ22.2改20.2为再现39/2 ratio增长；正D3只有一项B比，D4未有配套absoluteEM，PDF6 Fig6为PRM RMS分量。负D5/D6的绝对B在PDF5明确引Ref36=MU07（PDF7）。矩阵没有把RMS写实测signed几何，没有把新relative比写MU07的absolute复测，亦没有用正pair缺τ否定负pair既有强支持。

**136Nd pair与模型分开：**PE18 PDF3/041304-2说D5/D5-chiral两成员B比误差内近同；PDF5/041304-4 TableI及正文将D5对应**C六qp候选**，D3对应D*。显式3D φ只在**PDF6/041304-5 Fig6的D3/D***；crossing/8、6、6qp扩展与configuration mixing在PDF5明确超当前TAC。矩阵保D5真实ratio支持，没有拿D3几何替D5代补，也没有把C/D* βγ/Ex称实测。

PE18本轮root对假SI/TableC的更正与本次TableI视觉相符：不恢复任何不存在的TableC/SI寿命/δ/absoluteB。该错误的撤回不影响原正文真实D5结果。本worker本轮没有重新核additional/published三份文件的全部字节身份，不重复冒称完成那项root审计。

**“最小companion”设计：**project明确是选定pair/spin段的可审查问题设计，不是缺某量便否定chirality的必要条件；也明完整组合不保证唯一。共享clock/Cov问题修订后，没有发现新强门限或强制每个ps态都做TDPAD/g的问题。

## 实际阅读与验证边界

- 完整读root project及三source的相关active/D25P段；未逐条重审其全部历史withdrawn脚本/claim。
- PE06原件：本轮定向text/visual **PDF2–4**（Eqs1–5、TableI、相关Fig1–4/Refs9/11）；不是worker新读4页全文。
- LV19 canonical arXiv原件：本轮主要text/visual **PDF2、4、5、7**，核setup/Ref38、模型参数、单ratio和MU07谱系。原589/649文字和Ei矛盾仅按已有D25P边界保留，没有替作者改表。
- PE18 canonical：text/visual **PDF2、3、5、6、7**，核setup、同时产额、D5比值、TableI C/D*、D3 Fig6、结论和refs。没有数字化曲线或新拟合。
- thesis：上述PDF66/67窄读。没有联网、没有新paper、没有PRC98,044304 body阅读认证。
- SHA重新匹配：PE06 **ec32a76efbeebf1a924a1c95eb9d404a99158fc9226605414b324e982cfe1d4f**；LV19 **97182e90125ce57ac2faa0feeef42b6bc12952b3287f82f277a04f8d32cf0303**；PE18 **d2615fc0d95428b06c056eb8946afa2f62940ce58d79c1fc1cc3f50e19c73ef3**。

工具：rg定位、本地PyMuPDF定向text/render、view_image关键原页、hashlib匹配、项目再次直接读取。无科学拟合/统计CI计算。结果是限定scope下的科学/谱系审查，不是整库认证。

## 交付

本目录含`review.json`（两项发现及root处理）、`project-reviewed-snapshot.md`（复读版本）、`artifact-manifest.json`；tmp含raw checks和受检原页text/render。可复用事实由现有knowledge atomicIDs承接，root负责最终canonical写回。
