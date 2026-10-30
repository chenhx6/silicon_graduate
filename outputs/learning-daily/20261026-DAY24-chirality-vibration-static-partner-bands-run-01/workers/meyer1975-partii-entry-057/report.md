# 057：WK22 Ref52 PartII 完整获取，确认直接133Ce入口，尚未全读

入口结论：**不是仅metadata；完整25页已获取并核身份/首末/hash，存在直接133Ce专节和Fig9，值得继续完整原件阅读。** 本单元仅entry+定向locator上下文，不称全文已读、不认证科学参数表或将metadata填入experimental matrix。保持同Day24/133Ce方法链，无新课或信用变化。

## Ref52 身份和重叠

WK22原bibliography **physicalPDF126 / printed115**（本轮文字与整页视觉核）明确：Ref51为PartI,NPA249(1)111–140,PII0375947475900950；**Ref52为PartII,NPA249(1)141–165,PII0375947475900962**。两篇邻接但不同body，PartI旧读不能代替PartII应用证据。

Crossref exact DOI `10.1016/0375-9474(75)90096-2` 返回200，J.Meyer-Ter-Vehn、NuclearPhysicsA249(1),141–165,1975匹配。Crossref只给主标题“Collective model description of transitional odd-A nuclei”，没有PartII subtitle；PDF首页视觉给全名 **“(II). Comparison with unique parity states of nuclei in the A=135 and A=190 mass regions”**，与WK22对应。received17February1975/revised22April1975不替代出版年。

定向Wiki source/blueprint及raw文件名搜索未见该PartII原件已读记录。另有Meyer1978的61Ni/67Zn为不同文献，不能当重叠。tmp既有054/055是PartI本轮任务，非PartII；本次宽tmp文件名搜索遇个别无关目录permissiondenied后改限raw/papers与knowledge，未反复扫描。这不是全库全部PDF正文穷尽。

## 获取、完整性和SI

- 正文：`tmp/day24-meyer1975-partii-entry-057/attachment-object-response.pdf`。
- **25页，1,368,683B，SHA256 `fd1ba7f9280e8bafd86bbec06ec18e8a7089f93e84306829a4be897d9dd8439d`**；%PDF/pdfinfo有效、非加密。PDF1 printed141与PDF25 printed165均视觉核，141–165含首尾25页匹配。
- 已配置Elsevier API：ArticleFULL XML实际给`1-s2.0-0375947475900962-main.pdf`，再Object API取得body，两个HTTP200、无失败/重复端点/OA或browserfallback。XML190304B，SHA`640cb5a15490ec025bae72c534dc8b66b42b1d739ca38d801f9efad3617bf031`；请求来源/响应metadata见tmp`access-manifest.json`。
- 按既有授权`--si`执行；FULL XML只列mainPDF/main_1png和si1/si2gif。两gif的metadata为**ALTIMG、abstract-attachment=true、18pixel高**，是inline抽象公式图，不把文件名si误判Supplementary。未识别真实SI只限此inventory，不作绝无SI的全局声明。
- providerCredentials仅通过既有私有配置module读入并用于HTTPheaders；没有输出secret、改凭据/外部skill。下载仅tmp，raw未归档；无producer/未知附件/114执行。

## 实际已读范围

1. WK22 physical126/printed115的Ref51/52原页（文字+视觉）。
2. PartII **PDF1/printed141**：标题/abstract/§1首页；明确rigidtriaxialfixedβ/γ是假设近似，不能取摘要的stable-shape语言为已独立测rigidity。
3. **PDF14/154、16/156、18/158、19/159**全文文字作为A135/133Ce入口上下文；PDF18/19整页视觉核（包含Fig8/9）；未把读取一个表的OCR当整表数值核。
4. **PDF25/165**references文字+视觉。其余全部PDF仅机器抽文/heading/核素定位，不计全文阅读；尤其PDF2–13、15、17、20–24尚未完成本单元直接阅读。没有把整source标deep-read。

## 确认的直接相关对象与下一read区

**最重要的新entry：§3.2.4“The nucleus133Ce”，physicalPDF18末–19 / printed158–159，Fig9在PDF19。** 它直接把N75的135Nd、133Ce、131Ba负宇称谱并列，引用Ref26/27；不是131Ce。PDF16的整体A135 evidence list还含133/135La、135Pr、129Cs h11/2protons；135/137Nd、133/135Ce、131Ba h11/2neutron-holeyrast families；129/131La favoredyrast E2寿命比较。它有实质blueprint价值，不只是题名A135相近；这些是本文引用实验/模型比较对象，尚未逐篇primary复核。

已视觉核Fig9的任务用途只限定为**定位和需要深核的原义**：图把experimentalnegative-parity133Ce与triaxial/axialmodel列并排，实验列以11/2−为0、9/2−标−170（相对图自身reference），不是可直接套WK22绝对Ex。图注没有说明全1974→2022 nodecrosswalk；本单元不把−170当现代ground/isomer值，不从同spin自动合并两个时代的bandlabels。后续需读邻页/PartI定义和Ref26primary再比能量零点/assignment。

§3.2.4字面说triaxial比γ0solution更好，同时**保lowest9/2state仍过高**，穿入Fermienergy未充分下移；提到常见adhocCoriolisattenuation却说明本文没有用，self-consistentcoreinertia怎样纳入三轴rotor仍open。PDF19§4开头还明确“naive to take rigid shape literally”，需讨论soft/fluctuating程度。这个原文反例/限制是后续必须保的读区，不能只摘fig的agreement或摘要的stabletriaxial。

此外PDF18前半137Nd额外negativeparity组比较保branching不符、h11/2解释不convincing，并提出f7/2/可能h9/2alternative需moredata；这是related135-region竞争解释入口，不是本entry已经完成全137Nd证据审计。PDF16的135Pr比较说branching不足以逐一identify非yraststates；同样需要接读Fig7与原引用。

Table4（PDF14）为邻evenXe/Ba/Ce/Nd energies和derivedstandardparameters；Table5（PDF17）为129/131La measured/calculatedB(E2)。本轮不输出它们的科学数值表或认证fit/calibrationscope，留给完整阅读核energy/EM、parameteruncertainty和数据依赖。

A190部分由机器heading/caption定位到199Tl、195Au、193Hg、187Ir两unique-paritysystems（PDF4–14），尚未作这些核的证据/模式比较；195Au不等GU22的187Au，更不迁现代bandlabel或δ。首页提core186Os→198Hg只为abstractscope，不是本轮实验directmeasurements。

## 给root的互斥完整读分区建议

已在继续本单元targetedlocator前向root发proposal；本单元没有自行派发或越界全读。

| 建议区 | physical/printed | 要核的原件对象 |
|---|---|---|
|A|PDF1–13 /141–153|generalassumptions、standardparameterderivation、A190examples/Figs1–6/Tables1–3；coreselection、uncertainty、branchingsuccess/failure|
|B|PDF14–19 /154–159|14先接完Ir尾；A135Table4、135PrFig7、129/131LaTable5、137NdFig8、**133CeFig9与I<j/Coriolisfailure**；原实验依赖/energyreference|
|C|PDF20–25 /160–165|§4soft/rigid/PES/othermodeldiscussion/Fig10/Tables6–7、§5conclusion/limits及refs（§4开头在19已entryread，20续）；不能以模型拟合直接证rigidity|

三个区各自范围完整后才可合称全25页；entry已有页是明示的重复预暴露，不假设blind。没有新citation/experimentalclaim应只从未读metadata进入matrix。

## 尚未关闭与停止条件

未关闭：整篇PartII原件科学审核、Fig9reference/全部实验数据来源、标准β/γ/λ/Δ单位/选core/EM归一细节、全部modelerror/alternative，及WK22actualproducer/input身份。1975的singlej/rigidshape近似和Fig9历史比较不自动为2022signedRME、negativeλ或完整coreR/Harris提供actualexport。

停止在获批的**entryscope**：完整body与直接133Ce高价值读区已交root，部分locator上下文原读明确保留，没有抢先宣布fullreading或塞科学数据表。下一步root可按上表组织完整读取；资源已可用，不向用户再问正文/SI。
