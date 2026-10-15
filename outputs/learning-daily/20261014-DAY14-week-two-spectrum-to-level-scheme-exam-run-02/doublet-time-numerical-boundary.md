# 数值检查的失败与修正

首74-check主体通过。新增localprompt设计时，offset score用h=1e−5的朴素centraldifference与解析Ty比较，最大误差1.7294e−9超过1e−9门，exit1，未采用该扩展的通过声明。逐h收敛检查发现h=.001/.0005/.0001/.00001误差分别约1.60e−5/3.99e−6/1.60e−7/1.73e−9，符合O(h²)与浮点相消。改用h=.001/.0005的Richardson消去O(h²)，误差2.85e−11；未放宽验收阈值、不改科学模型。完整结果以此后实际script exit与content-checkpoint为准。

在第一次lint尚运行时启动的content检查属于先前74-check版本，后续扩展后必须freshlint和重新生成最终content-checkpoint；未把该旧检查用于发布扩展。
