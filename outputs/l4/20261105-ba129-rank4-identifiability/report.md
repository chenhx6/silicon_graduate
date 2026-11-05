---
type: l4-report
title: "129Ba companion-coefficient source audit and conditional profiles"
created: 2026-11-05
status: partial
research_level: L4-conditional-summary-analysis
project: "[[ba129-rank4-identifiability]]"
---

# 129Ba 同母态系数：原件取证改变了草稿结论

上一轮是有进展的目标轮次：产生了两行公开输入的计算与初稿。本轮继续取得原始
文献正文、完成独立反审、改变了研究判断并重写稿件；不把“已有PDF”当作目标完成。

## Decision and belief revision

此前将该路线称为最强文章创新点过早。Diamond1966已明确同母态纯跃迁标定取向的
方法；本次的−8/3是标准角动量代数的具体应用。它仍值得研究，但新颖性和实验
信息闭环未证明，状态改为 exploratory/not-ready。

独立反审确认数学关系正确，同时要求纠正三个实质问题：rank4仅识别f_E2*s4，
不能单独识别delta；gate/核取向与detector Q是不同层次；边际误差盒不能当作
实验排除。重写稿件已落实这些修改，也撤回“作者按模型偏好选根”的无依据归因。

## Primary-source acquisition

通过已授权Elsevier API取得Gizon1977 FULL JSON全文OCR，覆盖印刷pp.464–476。
PDF请求只返回p.464。Table1扫描页尚未取得。原文§2补充了七角度单谱测量和
55°强度定义；§3.1支持365.0/461.8的同母态连接，但不能恢复原始协方差。

OCR的若干误差尺度与2014评价不同。两版本保留分离：采用OCR参考A4误差0.06的
条件情景时，二倍边际盒在s4=1下相交，推翻了将原稿非相交视为稳健结论的想法。
OCR没有视觉认证，不据此修改任何原始数据或给出“纠正测量”。

Gizon1978：APS PDF 403、Harvest401、HAL notice、CORE精确DOI搜索0。
HAL提供的1977 ISTEX外链进入认证；没有登录。所有实际取得物、状态和SHA256
记录在`raw/papers/gpt/query/20261105-ba129-primary/evidence/manifest.json`。
可用正文与未取得扫描页明确区别。

另一个值得后续物理研究的原文限制位于p.475 §4.2末尾：作者报告模型混合比和
相对B(E2)与实验派生量符合不佳，因而没有列出显式比较。该来源事实已写回GI77-8；
它可支持独立的能量定标后电磁预测课题，不能被能谱定性符合所替代。

## Conditional calculation

共同选后母态、纯E2参考及标量response下：

- rank4：`A4_t=-(8/3) f_E2 s4 A4_r`，当前中心乘积为−0.75；
- rank2：`q(delta)=(-7+14sqrt(11)delta-delta²)/(10(1+delta²))`，范围为
  `[(-2-sqrt137)/5,(-2+sqrt137)/5]`；中心比−35/11在s2=1时低于下限，
  但s2≥1.16085可以消除这一中心幅值障碍。

联合诊断直接使用四个系数及声明的Gaussian covariance，profile两个实数参考
系数，不对接近零的参考A4作Gaussian比值近似。它放松了正布居约束。

| 情景，s2=s4=1、对角covariance | 最小距离 | 诊断极小点delta | small−large距离 |
| --- | ---: | ---: | ---: |
| 评价误差 | 12.879736 | −1.026982 | 0.013563 |
| 原文OCR尺度敏感性 | 8.235700 | −1.241168 | 0.468479 |

这些delta不是新实验值。50个预声明cells来自两种误差尺度与5×5相关矩阵族。
评价误差、cross-line rho=0的slice中，within-line rho从−.8到+.8使分支距离
对比从+3.529667变为−1.931312，排序反转。该扫描不确定真实covariance，亦不
产生p值、置信区间、branch probability或核结构裁决。

## Validation

- 标准SymPy Wigner符号独立核验−8/3、rank2矩阵和谱界。
- 直接CG/光子旋转矩阵对14个磁子态的rank4关系验证，最大差约3.7e−15。
- 投影残差与直接whitened GLS的最大差1.14e−12。
- 1025与2049网格加局部细化的对角极小值差小于9e−15。
- 错误parent ID、自旋、重复行、非有限数、负误差、错误多极参考均被拒绝；
  ratio入口拒绝零分母，coefficient-space入口允许零参考。
- 独立审查原稿的报告和脚本保存在本目录`independent-review/`；其中发现的
  原稿漏洞与修订后验证不同，不能把其“检查通过”当作当前科学认证。

## Goal coverage

本轮推进了“原件学习/知识修正”和“单点课题调查/可重放稿件”。全库逐文语义
学习、科学新颖性、真实response/误差闭环及最终投稿准入仍未证明完成。
P-ADO现有稿与私有133Ce分析本轮未修改；其它session的skill安装文件未处理。

## Durable knowledge and next work

长期知识已同步到：

- `knowledge/sources/gizon-1977-ba129-angular-distribution-primary.md`
- `knowledge/projects/ba129-rank4-identifiability.md`
- `knowledge/index.md`

下一项最有判别力的证据是原始Table1扫描和1978更新，之后验证同定义的
response/purity/covariance。并行研究可寻找具有独立标定的同母态控制案例。
若不能获得超出既有方法的实质信息增益，应保留此包为方法笔记并返回其它A≈130
候选，不以继续扩写稿件替代创新性。作者身份、许可/永久归档及最终claim审核
也仍是未完成项。goal保持active。

## Next control: independence retained

已入库Zobel1979的Table2给67Ga 843/1202-keV同母态对。其rank4因子比−16/9与
表列系数给条件f_E2=0.904639、|delta|=3.080014，接近该文3.1(3)/3.08。
数值与原件SHA/视觉locator保存在`next-control.json`，长期边界已写回project。
该结果很可能属于同一分析的信息重放，不能充当独立holdout；暂不把它加入稿件
作为新验证，更不与129Ba合并统计。
