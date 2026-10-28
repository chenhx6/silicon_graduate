# Discrete symmetry/current observable audit 034

## Scope

This is a conditional audit of the Gaussian fields in 017 and the source-grounded TAC boundaries in Frauendorf (2001), Starosta (2001), and Olbratowski (2002 v1). The fields have arbitrary units and are not EDF/HFB solutions.

## Transformations

For a time-odd current field:

\[
\mathcal T: \mathbf j(\mathbf r)\mapsto-\mathbf j(\mathbf r),\qquad
\mathcal R_z(\pi):\mathbf j(\mathbf r)\mapsto R_z(\pi)\mathbf j(R_z^{-1}\mathbf r),
\]

\[
\mathcal S_y=\mathcal T\mathcal R_y(\pi):\mathbf j(\mathbf r)\mapsto- R_y(\pi)\mathbf j(R_y^{-1}\mathbf r).
\]

The axis labels depend on the body-frame convention. Starosta’s Fig. 1 and text use a chiral operator combining time reversal and a 180° rotation; the exact axis must remain tied to that convention.

## 017 toy-field residuals

Residuals are maximum Euclidean differences on the symmetric grid used by 017. The integrated orbital moment is an arbitrary diagnostic, not a measured magnetic moment.

| Field | T only | Rz(pi) | T Rz(pi) | Ry(pi) | T Ry(pi) | integrated moment |
|---|---:|---:|---:|---:|---:|---|
| MR toy | 0.675086901 | 0.675086901 | 0 | 0 | 0.675086901 | (0, 0.912314, 0) |
| AMR toy | 1.015426626 | 1.015426626 | 0 | 0 | 1.015426626 | (0, 0, 0) to grid precision |

The fields therefore illustrate that an antiunitary rotation can preserve a nonzero current pattern while separate (T) and (R_z(\pi)) are broken. The result depends on the constructed vortices and axis convention. It is not an MR or AMR classifier.

## Intrinsic versus laboratory statements

A cranked TAC/HF state minimizes a Routhian containing (-\boldsymbol\omega\cdot\mathbf J). Its oriented intrinsic current is time odd and generally breaks separate (\mathcal T). Angular-momentum projection constructs good-(I) laboratory states; the projected state has quantized (J^2) and laboratory projections, while a classical intrinsic direction is not itself a laboratory observable. TAC’s left/right minima require symmetry restoration or a quantum model to discuss partner bands and tunnelling. Frauendorf 2001, PDF pp.473–476 and 484–485, states this intrinsic/laboratory and TAC/PRM distinction.

If a state is invariant under (\mathcal T), every expectation value of a time-odd current operator vanishes. An (\mathcal S_y=\mathcal T\mathcal R_y(\pi)\)-invariant intrinsic field can remain nonzero because the rotation compensates the time-reversal sign. This is a statement about the complete field and density, not pointwise vanishing.

## Observable boundary

A local-current residual from an arbitrary (\mathbf j(\mathbf r)\) has no direct experimental counterpart. MR/AMR/chiral assignments require band-resolved laboratory evidence: transition multipolarities, lifetimes and absolute strengths, branching, alignment, (S(I)), and a consistent configuration/model comparison. A vanishing integrated moment in the AMR toy does not prohibit local current, static longitudinal magnetization, cross-band M1, or an alternative weak-collectivity explanation.

The machine-readable values and transformation definitions are in `discrete-symmetry-current-observable-034.json`.
