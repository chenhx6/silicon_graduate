# Day26 E3 cross-source consistency audit 038

## Scope

Read-only audit of the archived E3 sources and artifacts: Bucher 2016/2017, Bernard 2016, Gaffney 2013, Butler 2020, and artifacts 018/027/029/032/035. No new physics or new literature was added.

## Findings

### Units

Bucher and Butler reduced E3 matrix elements use (e,b^{3/2}); Gaffney uses (e,mathrm{fm}^3). The conversion (1,b^{3/2}=1000,mathrm{fm}^3) is consistent throughout the new ledgers. Intrinsic (Q_3) values are separate rotor-convention conversions in (e,mathrm{fm}^3), not the raw reduced matrix elements.

### Central values and uncertainties

The Ba values are consistent: `144Ba` (M(E3)=0.65^{+0.17}_{-0.23},e b^{3/2}), (B_downarrow=48^{+25}_{-34}) W.u.; `146Ba` (0.65^{+0.14}_{-0.20},e b^{3/2}), (48^{+21}_{-29}) W.u. The ordering in earlier notes is now explicit and does not imply a new result. Gaffney's `224Ra` `940(30) e fm³` is the Table 1 E3 reduced matrix element; `2520(90) e fm³` in Table 2 is (Q_3). Bernard's `0.460 e b^(3/2)` and `25 W.u.` are a 2D-GCM model result, so they do not conflict with Bucher's experimental `0.65` and `48 W.u.`.

### Direction and partial sums

The correct definition is (B(E3;J_i\to J_f)=|M|^2/(2J_i+1)). Artifact 035 gives conditional forward/reverse values for each Butler row. Artifact 029 and its note explicitly guard against treating 027's illustrative downward proxy as certified because row bra-ket direction must be verified. 027's raw square sums (`30.9635` for `222Ra`, `5.6942` for `228Ra`) mix different (J_i), so they are partial diagnostics in (e^2b^3), not a (0^+) closure sum.

### Butler coupling and Q3 scatter

All artifacts agree that Butler Table I asterisks mark E3 entries coupled through rotational relations. The `228Ra 2+→3−` central value (-0.06^{+0.23}_{-0.16},e b^{3/2}) has interval ([-0.22,0.17]), crossing zero; no new fit was made. `222Ra` Q3 is described by Butler as approximately constant in Fig.4, but printed unstarred values span `2000–3100 e fm³` and starred values extend to `3200–5500 e fm³`. This is a qualitative/model-layer statement, not exact equality or an independent statistical constancy claim.

### 018 cluster geometry

The earlier logical overstatement was corrected. With E1 and E3 equations (D=w e|c_1|R) and (Q_3=2w e|c_3|R^3), a mathematical joint solution exists at (R=219.84) fm and (w=4.46\times10^{-5}). The 018 limitation is now restricted to a nuclear-scale local distance and common transition-weight assumption; (w) is not (S_\alpha).

## Overall assessment

No fatal unit or central-value contradiction was found. Residual risks are conditional row direction, fit-coupled stars, signed phase conventions, and overreading partial sums or qualitative (Q_3) flatness. No complete (m_0), energy-weighted (m_1), joint GOSIA covariance, released-star refit or model-independent static density was produced.
