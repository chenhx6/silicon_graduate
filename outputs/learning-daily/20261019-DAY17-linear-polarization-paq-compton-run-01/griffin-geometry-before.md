# GRIFFIN实际坐标表与固定geometry函数：分析前合同

已暴露：原36页/Table2/8/Σ曲线已读；当前codehelper用GetPosition而参数默认为145mm，paper有110/145两配置，source称52个Θ差/49个ξ且cloverpair90°。旧Smith方法也有阵列几何，因此不是盲测/新独立实验。

待解高信息问题：固定GRSIData的实际GetPosition与paper Table2的64个front-face中心方向在110/145mm是否按既定detector/crystal身份相合？保持paper crystal1–4→code0–3及ArrayNumber1–64，不在看结果后换轴/配对强配。若源函数是interaction-depth/有效位置而非front face，应以实际code definitions隔离，不能先认是table错误。

用真实TVector3抽取原函数/静态clover向量执行，声明必要薄class/shims，所有源码与bodyhash固定；这不等完整producer/actualinteractiongeometry。Table2按已视觉核的ring模板录入，并保留源印0.1deg的舍入字典；比较clover-center与crystal Θ、ξ census时明确ordered pairs/self与gate。别把print rounding破坏的对称或不同基点当实验矛盾。

停止条件：能回答同名distance是否同物理位置/角组，或精确定位不能比较的input；不扫自由几何调参、不把geometry计数当Compton效率/Q、无实际event/response/Σ不报新P。
