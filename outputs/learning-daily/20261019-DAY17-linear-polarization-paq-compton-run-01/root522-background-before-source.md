# ROOT5.22 actualsource前回忆

已原读Saastamoinen thesisA.1/A.2、强priming，非独立盲测。源声称ROOT5.22 Rebin/ShowBackground/Smooth/scale/Add每步传播error，最后fit16% vs Poisson2%。我尚未读实际5.22实现；假设Smooth可能只改bincontent、Sumw2可能仅保对角且不含相关，必须允许代码反证该假设。

将核5.22.00公开tag/commit/blobhash TH1与ShowBackground调用到TSpectrum，完整读相关方法/文档/variance计算，不能把majorversion匹配认证原exactpatch/job。若做组件执行，明确源码提取/适配与当前ROOT依赖，不把当前库行为冒旧库。scale由data匹配使sharedinput/Cov需额外合同；没有原hist/脚本不重造实验CI、不推源tau/branch已错。
