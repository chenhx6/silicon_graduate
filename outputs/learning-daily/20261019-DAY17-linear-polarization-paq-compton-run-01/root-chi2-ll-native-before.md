# 原表达式native组件设计冻结

已完整读6.40.04 Chi2Test文档/Chi2TestX/Chisquare并逐差核6.24.06，LL未被Contains消费；同一API的内部MLE用于homogeneityprob，不等固定modelPoissondeviance。原thesisROOT版/producer未知。声明以下fixture只测试接口，非实验counts。

base D=[0,5,20,0,7,0],M=[3,10,15,0,4,0]，两和32；stored模型误差²=M/10模拟weighted有效stat，不标原MC实际误差。比较LL CHI2/CHI2与auto UU/UW/WW、Chi2TestX返回ndf/igood、stored/noerror，以及共同零bin/axisrange端点。函数log_likelihood从原Tools.C精确摘取、原样编译，范围[0,6]及[0,2.5]。额外D首bin2/M首bin0控制真实deviance∞而原if跳过；含o0s>0缺项。禁止fullMC、修producer或推原paperCI/χ²。
