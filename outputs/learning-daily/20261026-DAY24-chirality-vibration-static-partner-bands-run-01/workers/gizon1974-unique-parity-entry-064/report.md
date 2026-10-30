# Gizon1974原实验入口核验（064）

已合法取得完整22页PDF并核验身份；本单元只读入口与历史zero的定向位置，**未全文阅读**。这是实际包含133Ce的原实验论文，不是仅由MTV75 PartII Ref26推定的对象。

## 身份与获取

J. Gizon, A. Gizon, M. R. Maier, R. M. Diamond, F. S. Stephens, *Deformed states of neutron-deficient cerium and neodymium nuclei*, Nuclear Physics A222(3)(1974)557–578。DOI **10.1016/0375-9474(74)90339-X**。Crossref exact记录与PDF首页题名/五作者/卷页匹配；Crossref给1974年4月，PDF记Received8August1973/Revised22January1974。第一页原生抽取误识别年份为1914，已看原图确认1974。

PDF：`tmp/day24-gizon1974-unique-parity-entry-064/attachment-object-response.pdf`，**22页，1,264,150bytes**；SHA256 **9d09f0fca35c125cb35241bbd2f231a65ec710702889c8b0262a529af7f56dac**。物理页+556=印刷页。FULLXML为137,188bytes，SHA256 `09621f1eda231b172f22bf3517b1bc2528f7444e49df24fe389f1814c49138be`。实际解析FULLXML的MAIN attachment `1-s2.0-037594747490339X-main.pdf`，由标准Elsevier Object API取回，两个请求均HTTP200。没有猜测PII对象或使用未授权镜像。

本轮明确包含SI，因此运行`--si`。FULLXML附件/objects中没有supplementary候选；`si1.gif/si2.gif/si3.gif`被标为ALTIMG/thumbnail，只有15–20px高、190–194bytes，是行内科学符号图像，不是补充文件。记录仅限所查正式附件目录，**不声称普遍不存在SI**。配置/凭据未改写或打印。完整获取回执保留在同tmp目录`access-manifest.json`。

先查了knowledge/raw文件名，以及Gizon、exact题名、DOI尾90339、A222/557文本；未见本篇已有source/raw命中。已有Gizon1977的131Ce/129Ce缺全文记录和1977/78Ba129引用属于不同论文，不是本篇重叠。未对全部未命名PDF做全库内容/哈希扫描，故这不是数学上的全库无重复证明。

## 已实际读到的入口事实与locator

- **PDF1／557，abstract、reaction box、§1**：明确报告133,135Ce与135,137Nd的in-beam gamma实验，方法包括prompt/delayed spectra、excitation functions、angular distributions、gamma-gamma coincidences。133Ce来自120Sn(16O,3n)，不是现代文献转引补写。作者的prolate shape措辞是对混合比和能级顺序的解释，尚未在本单元审完δ方法。
- **PDF2–4／558–560，§2**：实际Berkeley氧束、Sn/Te靶、校准/计时/符合及角分布取向衰减。入口已看到相对强度在55°测量且按最强线100归一（PDF3；**不是5.5°，原生OCR误读已看图核正**）；这不能直接当角积分光子branch。PDF4角分布含αk与Yamazaki完全取向系数；其完整δ推导须与PDF18–19连读。
- **PDF14／570，Fig8上部**：133Ce图以**9/2−、5.4h态为0**；负宇称主序为11/2−170.0、13/2−554.9、15/2−789.7、17/2−1306.3、19/2−1552.3keV。这里只是核验历史reference node，不将这些值重写为现代绝对能量。Fig8下部为135Nd。虚线侧带说明跃迁顺序不确定。
- **PDF17／573，Table4之后第一段**：原文在atomic-beam magnetic-resonance旧结果之后明确说 **“It is not yet known which state is the isomer and which is the ground state.”** 5.4h与97min活动的ground/isomer顺序当时未定。因此1974图的zero不能直接宣称现代ground，也不能未经跨版本逐node核算就加现代adopted37.2keV。
- **PDF15／571，§3.4入口及Fig9/10**：133Ce旧衰变谱系与本实验120Sn+16O谱/激发函数入口；**PDF18／574，§3.4尾段（只读§4前定向文本）**说明按energy sums/coincidence/intensity balance/excitation/angular distribution/mixing建谱，侧带顺序不明。这里尚未逐表核定全部转移/节点。

## 阅读范围及后续分区

本单元完整原生正文阅读页为PDF1–4、15；定向读PDF17的Table4后文字及PDF18的§3.4尾；Fig8/PDF14直接看图。实际看过整页视觉为PDF1–4、14、15、17；看过整页不等于逐个Table4数值已审核。其余页仅抽取保存并做章节/图表位置扫描，不能记为已读。

|模块|正文物理页／印刷页|图表位置（物理PDF页）|
|---|---|---|
|共同入口/实验方法|1–4／557–560（§3在4中途开始）|Fig1:2；δ方法还需18–19|
|137Nd §3.1|4–8／560–564（8上部尾段）|Table1:5；Fig2:4；Fig3、4:6；共享Fig5:7|
|135Ce §3.2|8–9及11底部／564–567|Table2:10–11；Fig6:8；共享Fig5:7|
|135Nd §3.3|13／569，图表提前/后移|Table3:12–13；Fig7:9；共享Fig8:14|
|133Ce §3.4|15、17下部、18上部／571–574|Table4:16–17；Fig9、10:15；共享Fig8:14|
|Mixing ratios §4|18下部–19上部／574–575|Fig11:18|
|Discussion §5|19–21／575–577|§5.1:19–20；§5.2:20–21|
|References|21–22／577–578|21中途开始|

分区按common methods、各核谱、共同δ/讨论推进；注意浮动图表：**Fig7在135Ce正文邻近却属于135Nd**，Table3早于§3.3正文，Fig5/Fig8为跨核共享图。不要仅按相邻标题分配图表。机器可读位置见`reading-partition.json`。

停止原因为入口身份核验完成；下一步需要正式逐页读各模块并与MTV75 Fig9、现代node/zero逐项对照。未给整篇学分、未给primary全部主张放行，也未改canonical/raw/Git/PLAN/Bib或派生模型。Wiki可复用事实由父任务按证据门写入knowledge。
