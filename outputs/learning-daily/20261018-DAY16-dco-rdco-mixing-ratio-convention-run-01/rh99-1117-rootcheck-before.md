# v1网格后的孤立根补核

v1实际exit0，边界框内两EMfamily均有正布居witness，但exactcentral在0.25°网格未命中。不能从采样零命中推断连续参数无解：固定a2/a4/P是三个精确关系，可能仅在孤立δ根上满足。

本补核在见到v1网格结果之后设计，不称预先盲注册。保留全部v1输入、结果和代码；不改source均值/误差、LP容差或原coordinate。用相同kernel的rank2/rank4分解将Pcentral方程写为二次多项式，找其所有realδroot，再逐根测positive-population LP。若根对应F2=0或因正性不可行，如实记录，不用调data让其通过。

这一层只修正sampling对zero-measure根的遗漏，不是实验δ拟合/置信区间，也不映作者δphase；v1边界盒仍不是jointCI。
