# 133Ce论文指定claims的独立原件审查

审查对象：`knowledge/sources/wakudyanaye-2022-triaxiality-rotational-bands-133ce.md` 的 WK22-01/03/04/08/15/19/20/21/22/23/27/28。只读canonical，不改Git。此为限定claim source self-audit，不是第二次全130页精读，不新增human-reviewed。

原件 `raw/papers/degree dissertation/Triaxiality and Rotational bands in 133Ce.pdf`，130页，实际SHA256 `48556dbfe5284efebdb901cd949f534ac5552c6504e2c744603afca386660080`，与source页一致。PDF=印刷页+11。

## 需要父代理收紧的两处

**WK22-23必须补完整单位合同。** `δ²≈0.7 Eγ² rE2/rM1`在Eγ以MeV、B(E2)以e²b²、B(M1)以μN²计的数值约定下成立；若Eγ用keV，系数对应约0.7×10^−6。只写公式而不写单位，后续极易把Table5.2的keV值直接代入，导致10^6错误。rM1本身带(μN/eb)²单位，并非与rE2相同的无量纲量。同一母态、同一分母reference与in/out身份也必须相同。

**WK22-21必须把趋势及“较好”的比较归属到图/作者正文，不能无条件认证actual producer。** Fig6.16a及PDF114正文确实描述QTR/FA均下降而实验上升；但Table6.9的QTR rM1打印为0.01→0.03，恰是上升。父页WK22-22已保留该冲突，WK22-21仍单独写“两模型rM1随spin下降”会在问答中丢失同一冲突。建议改为“Fig6.16及作者正文的比较显示……；Table6.9/6.10与图不闭合，实际producer趋势未独立复现”。同样，“九轨道rE2较好”可保留为作者基于图的判断，不是本轮在协方差下重新作出的模型优劣统计检验。

## 逐claim核查

|Claim|本次判断|独立核对及必要边界|
|---|---|---|
|WK22-01|支持|PDF61/印刷p50原文为125Te(12C,4n)133Ce、57MeV、5pnA、富集金属Te靶2mg/cm²/Au8mg/cm²、13个Compton-suppressed clovers，45°/90°/135°为1/8/4。另读PDF54/p43，Ch4确为8clovers（4+4）及“recently17”的通用介绍。source把两者分开正确，建议把PDF54加入本claim locator以便直接核一般介绍。|
|WK22-03|支持|PDF62/p51最低13/2−、最高27/2−；PDF67/Table5.2列13条带内（6 E2+7 mixed）、15条带间（7 E2+8 mixed），最低parent832.0、最高3616.2keV。原文“six new intraband M1+E2”后列369、209、399、490、380、604、332共七条，计数冲突真实存在。表中全都属于Band4相关跃迁；“15条带间”不是15条独立δ测量。|
|WK22-04|支持|Table5.2：608.3为1809.1keV 19/2−→15/2−带内；608.7为1200.8keV 15/2−→13/2−连接Band1。PDF62原文给门窗607–609及608–610keV，二者都能覆盖两条线；PDF63明确209、399与609符合而非608。399.3+209.0=608.3的平行支路身份正确。须保留“门被两线同时贡献”，不能把“重叠gate”当已完成双峰解混。|
|WK22-08|支持|PDF35/Eq2.37原图确为 `[E(I)−E(I−1)]−[E(I+1)−E(I)+E(I−1)−E(I−2)]/2`，即1.5E(I)−1.5E(I−1)−0.5E(I+1)+0.5E(I−2)。有能量单位，消掉常数零点；不是Eγ/(2I)，不是新实验数据。不同source的S符号不能自动视为同一算符。|
|WK22-15|支持其条件措辞|PDF82/Table6.3原图9/2+行振幅0.982、−0.202、+0.185无误，caption说贡献为振幅平方；直接平方和1.039353。即使各值允许±0.0005的打印舍入，最小平方和仍约1.037985>1，不能由遗漏正贡献修复。应继续只称“该打印行按所述正交归一basis解释不闭合”；不能进一步断定原程序wavefunction未归一或指定究竟哪个数字错。|
|WK22-19|支持，另加signed-error提醒|PDF112/Table6.11旋转原图确为−1.5(+0.97/−5.7)、−0.55(+0.12/−0.25)、−0.17(+0.09/−0.2)。按I_i/I_f和Band4→Band1身份分别对应Table5.2的624.6、582.7、464.4keV。625/582/465是原表标签，582/465不是对精确Eγ的严格四舍五入。PDF111把同样误差直接附到absδ的写法不能照抄：signed δ第1条端点为−7.2、−0.53，absδ端点为0.53、7.2；若表达abs误差应交换上下不对称方向。这里只核打印端点，不把它们当已知CL或完整likelihood。|
|WK22-20|支持，限定missing的对象|Table6.11确有out/out和out/in两类reference；Table5.2对17/2−@1409.8只列582.7连接线，未列该母态的Band4→Band1 ΔI2纯E2线。由Band1 13/2−能量592.1推得可能能差817.7，只是能级差，不是已观察到的817.7keV γ线或其强度。当前可说“未在Table5.2确认”，不能说物理上不存在、全部实验没见过，或据此把Table6.11该列改成零。|
|WK22-21|需收紧归属|PDF113 Fig6.15b FA三点确较接近实验signedδ；PDF114 Fig6.16a/正文两模型随spin下降而实验由约.25增至.47；PDF115称完整空间rE2较好。由于Table6.9趋势与图相反、Table6.10 rE2与图差约10倍，统一改成“作者图和正文给出的比较”，不要以此认证实际producer。δ、rE2、rM1共用输入，不宜数成三张独立胜负票。|
|WK22-22|支持|PDF111：Table6.9 QTR rM1为.01/.03，Table6.10 FA rE2为.44/.11。PDF114 Fig6.16a黑色QTR首点约.10、末点约.03；Fig6.16b绿色FA约.044/.011，当前只能读量级。图6.16b caption写in(I→I−1)/out(I→I−2)，与纵轴及随后正文out(I→I−1)/in(I→I−2)相反。source保留而不静默纠正是恰当的。|
|WK22-23|公式支持；单位合同须补|PDF48 Eq3.24原图为δ=√0.7×Eγ×E2/M1矩阵元比，PDF49 Eq3.25对应rate比。相同母态的reduced-B因子抵消，推出所述依赖。新增MeV/eb/μN单位及分母identity条款。可以诊断实验summary，不得把实测Eγ替换进理论B/δ后宣称理论不自洽；理论能差、算符归一、input仍未知。|
|WK22-27|支持当前限制|PDF58为Legendre AD式4.3、衰减取向说明、δ矩阵元式4.4；PDF59 DCO式4.5有交换门角，RAD式4.6则两者都在all-detectors门。原文给DCO约1/.5（E2门）、1/2（dipole门），RAD约1.3/.8。分析及新能级Jπ由Chinese collaborators完成。本论文这些页没有交付逐线AD/P原cells、alignment响应、Cov或δ likelihood，不能重拟CI。“RAD不依赖门多极性”是作者在其定义/实验近似下陈述，不宜扩成任意有限阵列/选门/取向的一般精确定理。|
|WK22-28|支持其谨慎结论|独立按Table5.2精确Eγ、打印Iγ和Table6.11中央δ作条件重组，下面四例与6.11不全相同。没有新拟合/新CI/显著性判断；不能据summary不闭合说原event分析错。实际AD强度处理、双峰分离、效率/角校正和共用归一仍需原producer。|

## 四组独立中央值重组

约定：Eγ以MeV计，I为相对光子强度，所选reference为纯E2，不使用总转换强度；混合线的E2/M1光子份额为δ²/(1+δ²)与1/(1+δ²)。

rE2 = (Iout/Iref) × δ²/(1+δ²) × (Eref/Eout)^5。

rM1 = 0.7 × (Iout/Iref)/(1+δ²) × Eref^5/Eout^3，数值单位(μN/eb)²。

|Out/ref（精确keV）|Iout/Iref、δ|本轮条件rE2|本轮条件rM1|Table6.11中央rE2/rM1|
|---|---|---|---|---|
|624.6/794.8，out/out|3.3/8.0，−1.5|0.952802|0.115644|1.15/0.14|
|582.7/577.8，out/in|3.53/3.22，−.55|0.244078|0.191775|.33/.25|
|464.4/608.3，out/in|1.89/1.89，−.17|0.108306|0.565767|.09/.47|
|464.4/982.0，out/out|1.89/1.95，−.17|1.150928|6.012192|1.06/5.54|

582.7的out/out未做：Table5.2缺该reference，不能用推得的817.7keV能差补造Iref。以上是选择同一打印summary后的代数重放，不是实际观测量的独立反演；原表误差不可忽略，且δ、分支强度及共同170keV归一相关。本轮未为这四组差异计算Z值或χ²。

Table6.11自身的out/out中央值按式3.24重组δ²，625/582/465三行分别约2.24609、.303737、.0289601，与其δ²=2.25、.3025、.0289近似一致；因此WK22-28不应误写成“6.11的δ与B比本身普遍冲突”。582的out/in打印中央.33/.25给.312981，打印舍入可影响此比较。它与Table5.2重放不等是另一层输入/处理谱系问题。

## 范围、命令与验证

实际原件文字读取PDF35/58/59/61/62/63/67/82/111–115；为解释公式、basis和8/13配置另读PDF47/48/49/54及110。没有扩成全130页重读。

实际视觉查看PDF35/58/59/61/62/67/82/111/112/113/114/115的三张contact sheets，另单独查看PDF112旋转表及PDF48整页。图6.16读数为量级，不是曲线数字化。核Table6.3振幅、Table6.11上下误差时以原页而非OCR记忆判断。

工具：Python3 + PyMuPDF逐页get_text/get_pixmap；Pillow制作contact sheets并旋转PDF112；view_image检查。数值检查是独立Python表达式，未运行父代理producer或任何Day22脚本。源SHA与130页数独立重算一致。未访问联网资源或凭据、未改canonical/source状态、未作Git操作。

视觉诊断资产：

- [contact-1](ce-review-assets/contact-1.jpg)
- [contact-2](ce-review-assets/contact-2.jpg)
- [contact-3](ce-review-assets/contact-3.jpg)
- [Table6.11旋转原页](ce-review-assets/pdf112-rotated.png)
- [Eq3.24原页](ce-review-assets/pdf048.png)

审查结论：指定12条claim的关键抄录及边界总体支持；需要补单位和收紧WK22-21归属。不能把本次source self-audit升级为实验错误裁决、模型actual producer复现或human-reviewed。
