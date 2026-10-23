# Singh Present Qt趋势图合同

本图回答：在保留单侧界限和原打印非对称误差时，已声明的有限点加权线性趋势能支持多大范围的描述？核心结论是Ce与Pr的有限点提供不同的条件斜率，有限点拟合不能替代完整带、原profile或结构机制判决。

- archetype: quantitative grid；两面板等权并排，比较同一提取量的不同核素/带，不能合并成一条回归。
- a：131Ce是方法转换与不显著条件斜率的边界案例；展示4个有限值及3个限值。
- b：133Pr是较负条件斜率的对照；展示3个有限值及2个限值，防止把低spin拟合外推成整带下降。
- 同一原文的重复引用、Ref31/32转载不是独立观测；不纳入Present回归。台账负宇称12行全部显示；另2个正宇称feeding行不属于目标带，CSV保留为excluded，不能在同带拟合中拼接。
- 误差条严格取原打印minus/plus；只在回归中令sigma=(minus+plus)/2，设已知独立Gaussian误差。只画有限点覆盖范围的直线；无实验CI带、无bound likelihood、无p值标签，不把条件SE冒称原实验精度。
- 单侧界限用空心三角和方向箭头，CL未指定；箭长为视觉提示，不是误差大小。
- backend: Python/matplotlib，继承本任务已保存的Python选择。图宽180mm、高100mm；正文8pt，mathtext子标5.6pt以上；PDF/SVG可编辑文字、PNG600dpi。
- 图为学习证据可视化，无目标期刊投稿合规认证。无图像复用、裁切、局部亮度处理或随机数据；原raw只读，校验SHA256。
- 导出前final draw后强制1.5pt panel alignment；最终source/font/collision检查及整体/逐panel视觉审查。FAIL修正后重导出及重审，WARN逐项说明。
- 可推翻本图的情况：台账抄录错、未显示目标带Present行、raw身份不符、原误差条方向错、回归漏披露筛选/假设。不能由本图确定actual Cov、feeding偏差、K分布或真实beta演化。
