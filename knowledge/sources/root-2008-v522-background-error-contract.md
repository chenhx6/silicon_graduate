---
type: source
title: "ROOT5.22实际代码：平滑、背景返回对象与误差缓冲"
title_original: "ROOT v5-22-00 TH1 and TSpectrum source methods"
aliases: [ROOT522 background errors, R522 histogram covariance contract]
created: 2026-10-20
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: public-software-repository
reading_depth: skimmed
authors: [ROOT collaboration, Rene Brun, Fons Rademakers, Miroslav Morhac]
year: 2008
citation_key: ""
canonical_source: "root-project/root tagv5-22-00 commita365d2fa4cdc4fea91420c400280dc9fc7c64214"
source_url: https://github.com/root-project/root/tree/a365d2fa4cdc4fea91420c400280dc9fc7c64214
raw_file: raw/code/day17-20261020/ROOT-v522-TH1.cxx
raw_sha256: 9625d86fbafe47fd5da0381a82b0774a3f158fd78c60575f229f0f97300cd113
raw_storage_status: public-staging-verified-raw-archive-deferred
nuclei: [23Al, 23Mg]
methods: [histogram-analysis, background-subtraction, covariance, component-audit]
tags: [ROOT, software-provenance, smoothing, calibration, count-statistics]
---

# 自动处理对角误差不等于传播完整分析协方差

## Bibliographic Record

公开[root-project/root v5-22-00](https://github.com/root-project/root/tree/a365d2fa4cdc4fea91420c400280dc9fc7c64214)：annotated tag对象`3daefae5e7d71a628f103f62802ba283c97b352b`实际解到commit`a365d2fa4cdc4fea91420c400280dc9fc7c64214`。下载TH1.cxx、TH1.h、TSpectrum.cxx、TSpectrum.h及TArrayD两文件；computed Git blob与公开exact tree核对前三文件，另存辅助文件hash。thesis只说5.22，未指定patch，这个tag不能认证原job。

[身份/hash](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root522-source-downloads.json)、[exact tree](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root522-exact-tree-identity.json)、[tag解析](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root522-tag-resolved.json)。缓存`tmp/day17-root522/`，下载原字节保留；TSpectrum历史文本非UTF8，Latin1可逆读取，初decode失败记录保留。

## Scope and Reading Depth

来源前回忆明确“Smooth可能不传播error”是待证伪假设。实际读TH1的Add两重载、Rebin、Scale、SmoothArray/Smooth、Reset、Sumw2/GetBinError、ShowBackground和TH1D SetBinContent；TSpectrum两Background重载完整算法/选项及StaticBackground；TArrayD Reset/Set与相关header。未读整个ROOT库/全部历史/原作者analysis脚本。[实际范围](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root522-reading-scope.json)。

## Summary

源码直接限制[[saastamoinen-2011-thesis-al23-proton-response]] AppendixA“每个ROOT步骤自动传播error”的概括：Smooth明确不修改已有errors；ShowBackground返回clone/reset后只填内容，不给估计背景写误差。Add会传播固定系数的对角误差，但没有数据估计scale、平滑跨bin或共同数据的协方差。这个发现不直接量化原实验16%误差或其Bp/τ偏差，因为实际patch/job/histogram尚未取得。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| R522-1 | 实际tag/commit/下载hash与tree相符；thesis只指5.22，exactpatch/job未知。只定向API，不以当前ROOT安装或tag名字冒原实验producer。 | software-identity-and-scope | direct-code | tag-resolved；exact-tree-identity；SA11-11 | true |
| R522-2 | TH1::Smooth文档明确Errors(if any)not modified；实现取content→SmoothArray→SetBinContent，仅恢复entries，不写fSumw2/SetBinError。stored error保留不是平滑误差已传播。 | actual-method-contract | direct-code | TH1.cxx L5558–5596 | true |
| R522-3 | ShowBackground委托TSpectrum::StaticBackground；后者调用histBackground，原对象clone→Reset→逐binSetBinContent。没有SetBinError或由输入error计算背景误差。返回哪个hist与实际脚本如何用它是必要输入。 | actual-callpath-and-return-object | direct-code | TH1.cxx L7351–7390；TSpectrum.cxx L133–229/L5569–5577 | true |
| R522-4 | TH1::Reset调用fSumw2.Reset，TArrayD::Reset只zero原数组不改长度；TH1D::SetBinContent只改内容/entries，不填errors。因此有buffer的Background输出可有非零content但零stored errors；无buffer的GetBinError走sqrt(abs(content))fallback，二者都非估计背景fullCov。 | stored-buffer-and-fallback | direct-code | TH1.cxx L5770–5808/L7207–7227/L8630–8655；TArrayD.h L49 | true |
| R522-5 | Add(一源)对已有buffer加c1²e1²，Add(两源)写c1²e1²+c2²e2²；Scale委托Add。它们处理给定系数的diagonal，不含估计c误差、源间Cov或平滑跨binCov；不能从方法名认证原实验CI。 | variance-propagation-contract | direct-code | TH1.cxx L815–1050/L5279–5316 | true |
| R522-6 | Rebin若已有Sumw2按旧binerror²求和；Sumw2在已填histogram按现有bincontent初始化buffer，只有适当未加权Poisson等条件才可读作正确variance；不能恢复之前丢失的统计历史/协方差。重复初始化与fgDefaultSumw2角色需实际job，不只加一个Sumw2调用即认证。 | rebin-and-error-history | direct-code | TH1.cxx L4986–5168/L7169–7192 | true |
| R522-7 | ShowBackground文字对默认direction/Compton与TSpectrum实际默认不同：hist调用实际decreasing、Comptonfalse，TH1声明niter20/same而旧方法prose写2。执行选项优先，不能用注释重建原默认响应。 | actual-default-versus-comment | direct-code | TH1.h L345；TH1.cxx L7351–7390；TSpectrum.cxx L177–195 | true |
| R522-8 | 另名原SmoothArray/Smooth及Background两重载组件已编译执行，容器ROOT6.40.04提供hist/TMath/TString等helper；非完整旧ROOT二进制/原实验。声明21bins，两buffer分支背景contents逐值同；storedSmootherrors不变，Background有23cellbuffer且errors全0，无buffer则sqrtcontent。 | actual-component-control-and-boundary | native-old-expression-current-helper | component-extraction；delivery-result | true |
| R522-9 | 原buffer输入designErrors2.1…4.1，Smooth后仍原样而content改变；无buffer分支的显示error随content改变只是fallback，非算法传播。该组件不提供真实bin数、背景方差或原fit误差。 | positive-and-negative-control | declared-component-control | delivery-result cases | true |
| R522-10 | 声明D−aB且a=Dk/Bk时matchingbin残差恒0，完整primitiveJacobian对应variance0；固定a的Add式给正variance。四bin设计中matchingbin的固定式75.7778而joint0，其它bins有正crossCov。只说明estimatedscale共享信息，非原hist/原matching实现或实验Σ。 | conditional-normalization-algebra | task-design | exercise matching_algebra_declared_design | true |
| R522-11 | 源A.2的16%/2%/13%是作者分析报告；本API审计只能否定“所有步骤自动传播”的一般保证，未得原script/patch/数据不能断言其最终16%用了零背景误差、重报BpCI或否定实验结果。 | scientific-impact-boundary | source-companion-and-readiness | SA11-11/12；R522-2/3/5/8 | true |

## Analytical Reconstruction and Self-Audit

[组件前冻结](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root522-component-before.md)、[提取记录](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root522-component-extraction.json)、[发布fixture](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root522-legacy-component.cc)、[hash合同](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root522-exercise-contract.json)、[复算程序](../../system/scripts/day17_root522_background_contract.py)、[结果](../../outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01/root522-exercise-result.json)。原方法体只改class/method名以隔离符号，helper为当前ROOT；发布copy仅增加版权/边界注释与去尾空格，非注释tokens一致，原下载不改。初UTF8/NumPybool序列化失败分别留档，不删除失败历史。

对`r_i=D_i−(D_k/B_k)B_i`的primitiveJacobian：

\[
\frac{\partial r_i}{\partial D_j}=\delta_{ij}-\frac{B_i}{B_k}\delta_{jk},\qquad
\frac{\partial r_i}{\partial B_j}=-a\delta_{ij}+a\frac{B_i}{B_k}\delta_{jk}.
\]

`Cov(r)=J Cov(D,B) Jᵀ`含matching信息；实际平滑/背景估计还需其Jacobian或完整拟合/重抽样合同，不能把本unsmoothed四bin设计当实验错误条。

## Competing Interpretations and Limitations

原thesis可能另行设置backgrounderrors、用旧hist作为error源或做额外fit；公开文字不足以判实际调用对象。代码和组件证据共同限制自动传播主张，不提供其真实覆盖率。重复更多designbins/MonteCarlo不能补原data/producer；下一输入必须改变实际method合同或补独立实验reference。

## Knowledge Impact and Learning Decision

`revises`工具名/Sumw2意味着平滑和估计scale完整误差自动闭合；`supports`区分content/errorbuffer/完整Cov与固定/估计校准。新claim均needs_review，无human-reviewed，没有新实验τ、Bp、Jπ或CI。此问题回连Day17计数/共享校准，仍只Day18无学分preview而不另授卡。

## Extracted Pages

[[saastamoinen-2011-thesis-al23-proton-response]]、[[lifetime-strength-audit-165tm-136nd]]、[[linear-polarization-asymmetry]]、[[polarimetry-shared-calibration-count-design]]。
