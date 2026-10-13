# Day13：一阶zero sensitivity的边界回忆

2026-10-14T02:40:12.199114+08:00

C23 Eq7与前序Jacobian后的一次计算前回忆：

- fixedlab angle cosθ=β时Jβ0，但second derivative通常非零，不能把速度项的真实传播误差宣称为0。
- 对E_lab fixed/assumed correction β有Gaussian estimator error，leading residual预计+.5E0γ^4 δβ²，mean+.5E0γ^4 σβ²，σ≈E0γ^4 σβ²/√2。
- 对actual βspread/meanβ固定校正，E_lab随trueβ变化，leading residual应为负同量级；两种输入stage/covariance不同。
- 这种δβ²分布为one-sided非Gaussian，不能把leadingσ乘2.355当真实FWHM。Actualintrinsic/angular/position noise仍在，低速小σ下二阶可能很小。
- 验收：exact vs second-order、FD second derivative、sign/units/zero-noise limits；输入全为self-chosen，不指认实际peak tail。
