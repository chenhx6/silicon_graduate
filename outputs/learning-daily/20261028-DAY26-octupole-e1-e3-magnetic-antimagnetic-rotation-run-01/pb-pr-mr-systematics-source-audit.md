---
type: audit
graph-excluded: true
created: 2026-10-29
status: complete-with-source-gaps
---

# Pb–Pr磁转动系统学独立核验

完整可复用推导见 [[pb-pr-magnetic-rotation-core-crossing-systematics]]。

原件依据推翻了“Pb只单调闭合且无芯、Pr才重新张开”的二分：Hübel2005 p.49给199Pb旧配置51/2叶片和与实测57/2之间的3ℏ芯贡献，并描述破对后更高段重新张开；pp.50–51汇编196Pb交叉后绝对B(M1)从0.7附近跳至约9 μN²，随后下降。Clark2000 pp.16–18亦有197Pb交叉与重开。

对题定哈密顿量明确向量/平行芯假设，导出κ=3JcoreV2/(j1j2)、I=Js(1+κcosθ)、芯份额及动态惯量；有限芯模型本身不强制终止于j1+j2。由固定有效g、Q的Clark电磁核得到bE2=bM1²，因此固定配置单调闭合也可伴随M1/E2上升，不能从比值单独判M1反弹。

生成 `mr-core-shears-dimensionless-response.py/pdf/svg/csv/json`；为j1=5、j2=7、κ=0/.25/1的条件示例，无核素拟合。

200Pb仅据Hübel Fig10核验3条、0条连接低能级；未取得本核原始寿命与绝对自旋，不填定量终止结论。137Pr原2007论文称交叉.48 MeV，2015对比称.42 MeV，保留未对齐边界；ε2亦不直接写成β2。

本轮定向读取Clark pp.5–6/15–18、Hübel pp.13/16–17/19/25–26/49–51/53、Agarwal pp.6–8；来源哈希及页数已写入长期笔记。未跑全库lint、测试、commit/push，未改共享页面、学分或正式回执。
