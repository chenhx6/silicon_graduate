# L25 finite-J/参数合同：量化前预测

2026-10-16T10:00:04.433774+08:00

问题前priming已存day15-alignment-formula-before-analysis.md；新body/HTML核publisher Eq10/12–15原字面，Eq13确为2sigma分母而非2sigma²，Eq14为1−3m²/S及1−10m²/S+35m4/(3S²)，S=J(J+1)。Ref39实际为Morinaga/Yamazaki1976书，不是1967表；未读取书的原近似声明，不将独立来源的原文预先归给该书。保持raw/publisher原字面与旧review状态。

以下是待代码/独立CG验证的本任务解析预测，不是作者实验或code结果：
- uniform m的<m²>=S/3、<m4>=S(3S−1)/15，printed第四阶若直接当exactnormalized rank4，可能留下−7/(9S)，与真正纯rank4 uniform为0不同；二阶uniform为0。
- exact normalized weights应为T2/T2(mref)、T4/T4(mref)，T2=3m²−S，T4=35m4−(30S−25)m²+3S²−6S；mref整数0、半整数1/2。先对多个spin逐m与独立CG有限和比较。
- printed第四阶可在exact rank4/rank2/rank0基底内分解；若有低rank分量，不能在未换基下直接按pure-U4传播。反证应针对字面公式的精确适用性，不针对未取到的作者code。
- 等号一致的large-J形式与finiteJ边界须分开。尤其不能因uniform残差小就证明任意population或actualsigma/delta影响小。
- Gaussian width合同W以exp[-m²/(2s²)]，literal variance合同V以exp[-m²/(2v)]；仅v=s²时布居相同。两者相同标签sigma/J=.3并不必然相同population。对J23/13/2只作chosen参数比较，不反拟Fig8或以quotedfiterrors给CL。

只做一个bounded公式一致性审计；若书中近似/code/实际σ定义缺，记preciseboundary。仍DAY14内Day15无信用preview，不给formal分数或开Day16。
