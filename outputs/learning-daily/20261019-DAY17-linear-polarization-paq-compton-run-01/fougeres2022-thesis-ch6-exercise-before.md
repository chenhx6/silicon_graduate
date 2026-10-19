# Ch6数值/协方差合同练习前冻结

已完整文本/视觉读Ch6/PDF105–126，强priming非盲测。现在核实际Table6.4/6.7/6.9打印值：hbar/tau的精确非线性映射，包括DCLM9.5fs所列60meV、final9.9所列66meV、BR.68(.06)%对Γp量级，与F23版本.68(.17)%分别保留；不把两个版本当独立测量或修原表。

Eq6.2明确同data，先选仅供代数检查的sigma=(upper+lower)/2，求实际11(+6,-4)和9.5(+4.5,-2)逆varianceweighted中心；不称已知作者如何处理asymmetry。固定该权重，完整rho∈[-1,1]方差范围与minσ政策何时不保守；只是条件高斯合同，不重建实验CI。Table6.1数值以scipy chi2分位核joint/projection阈值，非新coverage认证。

新API疑点Ch6正文maximumlikelihood与publicChi2Test LL、manualloglikelihood不同；只已grep方法字符串及旧ROOT5.22 parser，没有新版本body/readiness核。后续另冻再取matchingAPI，不在本练习预填结果。
