# 051：LL75写回窄审查

**未发现科学实质P0/P1；核心写回verified no-op。** 仅有下列两处低优先级记号建议，不改变推导或证据状态。canonical未由本单元修改。

## 最小建议

1. `knowledge/sources/leander-larsson-1975-potential-energy-surfaces-n-equals-z.md` **LL75-D24-011（当前line68）**写“pointwise Q0=…”。同页Eq10解释又用Q0表示总proton sum，故建议最小改为“pointwise **O20≡2z²−x²−y²**=…”，并将Qt明确成`Ot≡2ζ²−ξ²−η²`。现有显式坐标式line79–81正确，无需改公式。此为记号歧义，未发现root据此混算总质子Q0。
2. 同源**line83**的“ρ²=ξ²+η²+ζ²是普通stretched半径”建议改“**普通stretched半径平方**”。其后非物理E0的判断正确；ρ²项仍是恢复physical rank2算符所需的坐标项。

## 核验通过的具体项

- **CG到standard R/B/比值：**A2为F=rLL·CG；在同CG相位和声明3j WE下，Rstd=√(2j′+1)rLL。因此若实际输出确属此CG-reduced约定，B=(2If+1)|rCG|²/(2Ii+1)正确。同一初末spin端点、两个算符采用同约定时，比例因子才在RME比中消去；当前没有将此强加给actual PROBMO、普通分量ME或既有δ。
- **坐标/原符号：**A1 dimensionless及其b_i/ℓ0²桥正确；A7上置circle的ω0°保持独立，未与无圈ω0合并。历史体积约定没有被扩大为所有stretch的通则。
- **特别核Eq7：**复用已核PDF4/printed96原页并抽取其原嵌扫描图、逐像素看smearing公式；`γs=1.6ℏω0`的ω0上方**没有可见circle标记**。A7和Eq5参考频率的circle在其它原式中清晰可见，不以这些位置或物理预期反推Eq7应有circle。当前Setup无圈转录可保；没有发现必须补圈的原件证据。此次只核该小式，未重读整篇或用OCR作裁决。
- **A8：**源中同ν、无prime、段首neglecting γ、Q-like √(16π/5)r²Y20与+2ε〈ρ²〉/3均正确。一般bra/ket推广仍标任务代数，完整三轴五分量仍标042推导；没有把A8印成历史完整off-diagonal库。A8轴向pointwise式的p/s/length²系数正确。
- **ρ²解释：**ordinary stretched scalar一般不与physical L对易，因此其坐标项不代表physical E0；canonical没有删除此项或用L^t偷换physical L。
- **moments：**Eq10 Q0总proton Q-like、Eq11 Q40显式Z^−1且r⁴Y40、Table1 fm²/fm⁴及B(E2)只经rotational模型给|Q0|而不定sign均保持。
- **Table2/失败范围：**复核044报告和原Table2已渲染脚注：min与minimal barrier height都以ground-state minimum为零；canonical没有把GS-relative saddle误当well内barrier。24Mg的6/17MeV surface敏感性和40Ca的9–13MeV过绑定/另一参组min在本图仅ledge边界与044原读一致，没有写成实测shape或Ce预测。
- **下游写回：**LLR78 Ref23续接、133Ce blueprint及三核matrix继续区分历史定义、任务坐标恒等式与actual2022 producer；未声称完整signed input或Ce数值结果恢复。

## Scope与边界

本轮读LL75 canonical全部及三个下游页的相关新增段，复用043/044已完成的原读报告与关键视觉，只定向追加Eq7原嵌图和Table2脚注核验。未重新阅读21页，未新网络、模型代码或toy；不新增科学主张、课程学分或session状态。只写051 worker与对应tmp；canonical/raw/PLAN/Bib/Git均未改。
