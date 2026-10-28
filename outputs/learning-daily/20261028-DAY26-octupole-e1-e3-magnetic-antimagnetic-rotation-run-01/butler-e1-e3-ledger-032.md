# Butler 2020 E1/E2/E3 ledger 032

## Source scope

The ledger uses Butler *et al.* PRL **124**, 042503 (2020), Table I (published PDF p.3), and the appended arXiv `2001.09681` Table II (PDF p.16). No new fit or external data were used.

## Units and B(Eλ) direction

Butler Table I uses (e,b^{\lambda/2}): E2 matrix elements are (e,b), E3 are (e,b^{3/2}). Appended Table II uses (e,b^{1/2}) for E1. Thus (M(E3)/M(E1)) has units (b), and the numerical conversion to (e,mathrm{fm}^3/(e,mathrm{fm})) gives the same numerical ratio because (b^{3/2}/b^{1/2}=b).

For a verified initial spin (J_i), (B(E\lambda;J_i\to J_f)=|M|^2/(2J_i+1)). The bra-ket table notation must be read before assigning (J_i); this ledger does not manufacture B ratios where the row direction is ambiguous. It also separates same-state-pair E1/E3 ratios from the ground-band scale comparison (0^+\to3^-) versus (0^+\to1^-), which has different final spins.

## Central E3/E1 ratios

| Nucleus / pair | E3 central | E1 central | signed (M(E3)/M(E1)) | Interpretation |
|---|---:|---:|---:|---|
| `222Ra 2+→1−` | `0.85` | `−0.0114` | `−74.56 b` | same state pair; E1 sign follows Table II convention |
| `222Ra 2+→3−` | `−0.90` | `0.026` | `−34.62 b` | same pair; signed ratio is phase-convention dependent |
| `222Ra 4+→3−` | `2.60*` | `−0.027` | `−96.30 b` | E3 starred/coupled |
| `222Ra 4+→5−` | `−1.70*` | `0.018` | `−94.44 b` | E3 starred/coupled |
| `228Ra 2+→1−` | `1.36*` | `0.0051` | `266.67 b` | E3 starred/coupled |
| `228Ra 2+→3−` | `−0.06*` | `−0.009` | `6.67 b` | near-zero E3; both signs model-linked |

For the ground-band scale comparison, `222Ra` gives (1.13/0.0082=137.80,b), while `228Ra` gives (0.87/(-0.0043)=-202.33,b). These compare different final states (`3−` versus `1−`) and are not same-transition multipole ratios. The signs are not independent phase measurements: Table II states that E1 signs follow the rotational assumption that (Q_1) has the same sign as (Q_3) for `222Ra` and the opposite sign for `228Ra`.

## E2 context and derived quantities

Table I E2 examples include `222Ra` (\langle2^+||E2||4^+\rangle=2.98(15),e b) and `228Ra` (3.87(19),e b); the aggregate rotor-derived (Q_2) values are `578(18)` and `798(21) e fm²`. These Q values are conversions or fit outputs under rotational relations, while the GOSIA matrix elements are the fitted quantities. E3 per-transition (Q_3) values are likewise rotor-convention conversions.

## 228Ra near-zero test

The Table I central `228Ra 2+→3−` E3 value is (-0.06,e b^{3/2}) with (+0.23/-0.16) one-sigma uncertainty. The interval is ([-0.22,0.17],e b^{3/2}), which crosses zero. Its listed (Q_3=150^{+360}_{-500},e fm^3) interval ([-350,510]) also crosses zero. This is a direct interval check on the printed fit result, not a new re-fit or a claim of an exact zero.

## 222Ra Q3 scatter

The printed per-transition `222Ra` Q3 values are `3030, 2000, 2100, 3100, 4400, 5500, 3200, 4600 e fm³`; the first four unstarred entries span `2000–3100`, with mean `2557.5` and population SD `509.3 e fm³`. Starred entries extend the list to `4400–5500` and are coupled through rotational assumptions. Therefore “approximately constant” is the authors’ qualitative rotor-like interpretation (PRL p.4 Fig.4 and text), not a statement that all printed values are equal or statistically independent. The aggregate rotor-derived `Q3=3120(190)` is a separate fitted quantity.

## Fit versus rotor-derived quantities

- **GOSIA fit:** E1/E2/E3 matrix elements, with E3 asterisk rows coupled to higher matrix elements.
- **Rotor-derived:** per-transition (Q_1,Q_2,Q_3), aggregate rotor (Q_2/Q_3), and E1 sign assignments tied to assumed relative (Q_1/Q_3) phases.
- **Not produced:** a new fit, joint covariance, complete (m_0), energy-weighted (m_1), or phase-independent signed E1/E3 ratio.

The machine-readable values and arithmetic are in `butler-e1-e3-ledger-032.json`.
