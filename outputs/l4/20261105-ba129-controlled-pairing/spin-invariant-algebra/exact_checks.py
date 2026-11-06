"""Independent exact angular-momentum audit; no parent/model code imports.

All angular momenta and magnetic projections passed to CG/3j/6j are doubled
integers. Coefficients use factorial sums and rational square-root arithmetic.
Only conversion of final ratios to displayed angles uses floating point.
No files are written by this script; JSON is emitted on stdout.
"""

from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
import json
import math


class Radical:
    """A finite exact sum of rational coefficients times square-free roots."""

    def __init__(self, value=0):
        if isinstance(value, Radical):
            self.terms = value.terms.copy()
        elif isinstance(value, dict):
            self.terms = {int(d): F(c) for d, c in value.items() if c}
        else:
            self.terms = {} if not value else {1: F(value)}

    def __add__(self, other):
        out = self.terms.copy()
        for d, c in Radical(other).terms.items():
            out[d] = out.get(d, F(0)) + c
        return Radical(out)

    __radd__ = __add__

    def __neg__(self):
        return Radical({d: -c for d, c in self.terms.items()})

    def __sub__(self, other):
        return self + -Radical(other)

    def __rsub__(self, other):
        return Radical(other) + -self

    def __mul__(self, other):
        out = {}
        for d, c in self.terms.items():
            for e, b in Radical(other).terms.items():
                g = math.gcd(d, e)
                root = d * e // (g * g)
                out[root] = out.get(root, F(0)) + c * b * g
        return Radical(out)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = Radical(other)
        if len(other.terms) != 1:
            raise ValueError("Only nonzero single-root denominators are needed.")
        d, c = next(iter(other.terms.items()))
        return self * Radical({d: 1 / (c * d)})

    def __eq__(self, other):
        return self.terms == Radical(other).terms

    def __bool__(self):
        return bool(self.terms)

    def __abs__(self):
        if not self:
            return self
        if len(self.terms) != 1:
            raise ValueError("These controls require only a single-root absolute value.")
        d, c = next(iter(self.terms.items()))
        return Radical({d: abs(c)})

    def __float__(self):
        return sum(float(c) * math.sqrt(d) for d, c in self.terms.items())

    def __str__(self):
        if not self:
            return "0"
        return " + ".join(
            str(c) if d == 1 else f"({c})*sqrt({d})"
            for d, c in sorted(self.terms.items())
        )

    def rational(self):
        if not self:
            return F(0)
        if set(self.terms) != {1}:
            raise ValueError(f"Not rational: {self}")
        return self.terms[1]


@lru_cache(None)
def sqrt(value):
    value = F(value)
    if value < 0:
        raise ValueError("Real roots only.")
    if not value:
        return Radical()
    n = value.numerator * value.denominator
    outside, inside, prime = 1, 1, 2
    while prime * prime <= n:
        count = 0
        while n % prime == 0:
            n //= prime
            count += 1
        outside *= prime ** (count // 2)
        if count % 2:
            inside *= prime
        prime += 1
    inside *= n
    return Radical({inside: F(outside, value.denominator)})


def sign(n):
    assert isinstance(n, int)
    return -1 if n % 2 else 1


def triangle(a, b, c):
    return min(a, b, c) >= 0 and abs(a - b) <= c <= a + b and (a + b + c) % 2 == 0


def projection(j, m):
    return abs(m) <= j and (j - m) % 2 == 0


def delta_squared(a, b, c):
    if not triangle(a, b, c):
        return F(0)
    fact = math.factorial
    return F(
        fact((a + b - c) // 2) * fact((a - b + c) // 2)
        * fact((-a + b + c) // 2),
        fact((a + b + c) // 2 + 1),
    )


@lru_cache(None)
def three_j(a, b, c, u, v, w):
    if not triangle(a, b, c) or u + v + w:
        return Radical()
    if not all(projection(j, m) for j, m in [(a, u), (b, v), (c, w)]):
        return Radical()
    fact = math.factorial
    pref = delta_squared(a, b, c)
    for j, m in [(a, u), (b, v), (c, w)]:
        pref *= fact((j + m) // 2) * fact((j - m) // 2)
    lo = max(0, (b - c - u) // 2, (a + v - c) // 2)
    hi = min((a + b - c) // 2, (a - u) // 2, (b + v) // 2)
    total = F(0)
    for z in range(lo, hi + 1):
        args = [z, (a + b - c) // 2 - z, (a - u) // 2 - z,
                (b + v) // 2 - z, (c - b + u) // 2 + z,
                (c - a - v) // 2 + z]
        total += F(sign(z), math.prod(fact(x) for x in args))
    return sign((a - b - w) // 2) * total * sqrt(pref)


@lru_cache(None)
def cg(a, u, b, v, c, w):
    if u + v != w:
        return Radical()
    return sign((a - b + w) // 2) * sqrt(c + 1) * three_j(a, b, c, u, v, -w)


@lru_cache(None)
def six_j(a, b, c, d, e, f):
    tris = [(a, b, c), (a, e, f), (d, b, f), (d, e, c)]
    if not all(triangle(*t) for t in tris):
        return Radical()
    pref = math.prod(delta_squared(*t) for t in tris)
    xs = [(a + b + c) // 2, (a + e + f) // 2,
          (d + b + f) // 2, (d + e + c) // 2]
    ys = [(a + b + d + e) // 2, (a + c + d + f) // 2,
          (b + c + e + f) // 2]
    total = F(0)
    fact = math.factorial
    for z in range(max(xs), min(ys) + 1):
        den = math.prod(fact(z - x) for x in xs) * math.prod(fact(y - z) for y in ys)
        total += F(sign(z) * fact(z + 1), den)
    return total * sqrt(pref)


@dataclass(frozen=True)
class State:
    two_j: int
    channel: int = 0


def magnetic_element(final, mf, initial, mi, q, rme):
    if not projection(final.two_j, mf) or not projection(initial.two_j, mi):
        return Radical()
    return cg(initial.two_j, mi, 4, 2 * q, final.two_j, mf) * rme(final, initial) / sqrt(final.two_j + 1)


def recoupled_moments(initial, states, rme):
    j = initial.two_j
    q2 = sum(sign((a.two_j - j) // 2) * rme(initial, a) * rme(a, initial)
             for a in states) / Radical(j + 1)
    total = sum(
        six_j(4, 4, 4, j, a.two_j, b.two_j)
        * rme(initial, a) * rme(a, b) * rme(b, initial)
        for a in states for b in states
    )
    q3 = -sign(j) * sqrt(F(35, 2)) * total / Radical(j + 1)
    return q2, q3


def direct_moments(initial, states, rme, m):
    q2 = Radical()
    scalar3 = Radical()
    for q in range(-2, 3):
        for a in states:
            q2 += sign(q) * magnetic_element(initial, m, a, m - 2*q, q, rme) * magnetic_element(a, m - 2*q, initial, m, -q, rme)
    for mu in range(-2, 3):
        for nu in range(-2, 3):
            lam = -mu - nu
            if abs(lam) > 2:
                continue
            coefficient = sign(mu + nu) * cg(4, 2*mu, 4, 2*nu, 4, 2*(mu + nu))
            if not coefficient:
                continue
            for a in states:
                for b in states:
                    scalar3 += coefficient * magnetic_element(initial, m, a, m - 2*mu, mu, rme) * magnetic_element(a, m - 2*mu, b, m + 2*lam, nu, rme) * magnetic_element(b, m + 2*lam, initial, m, lam, rme)
    return q2, -sqrt(F(7, 2)) * scalar3


def literal_proxy(initial, states, rme):
    raw2 = sum(rme(initial, a) * rme(a, initial) for a in states)
    triple = sum(rme(initial, a) * rme(a, b) * rme(b, initial) for a in states for b in states)
    raw3 = sqrt(F(7, 10)) * abs(triple)
    ratio = raw3 / (raw2 * sqrt(raw2.rational()))
    l = initial.two_j + 4
    c = cg(l, initial.two_j, 4, 0, initial.two_j, initial.two_j)
    beta_squared = (raw2 / Radical(l + 1) / (c*c)).rational()
    return raw2, raw3, ratio, sqrt(beta_squared)


def encode(x):
    if isinstance(x, Radical):
        return {"exact": str(x), "value": float(x)}
    if isinstance(x, F):
        return {"exact": str(x), "value": float(x)}
    if isinstance(x, (tuple, list)):
        return [encode(y) for y in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    return x


def angle_record(cosine):
    # All controls have a single exact root. Test its squared magnitude exactly.
    square = (cosine * cosine).rational()
    if square > 1:
        return {"status": "outside-real-acos-domain", "gamma_degrees": None, "clipped": False}
    return {"status": "real-angle", "gamma_degrees": math.degrees(math.acos(float(cosine))) / 3, "clipped": False}


def spectator_rme(two_spectator, transitions, middle):
    """Construct coupled RMEs directly from magnetic CG expansions, not 6j."""
    def core_rme(final, initial):
        if final.channel == 0 and initial.channel == 0:
            return Radical()
        if initial.channel == 0:
            return Radical(transitions[final.channel - 1])
        if final.channel == 0:
            return Radical(transitions[initial.channel - 1])
        return Radical(middle[final.channel - 1][initial.channel - 1])

    @lru_cache(None)
    def result(final, initial):
        rf = 0 if final.channel == 0 else 4
        ri = 0 if initial.channel == 0 else 4
        mi = initial.two_j
        for q in range(-2, 3):
            mf = mi + 2*q
            weight = cg(initial.two_j, mi, 4, 2*q, final.two_j, mf)
            if not weight:
                continue
            element = Radical()
            for ms in range(-two_spectator, two_spectator + 1, 2):
                mci, mcf = mi - ms, mf - ms
                element += (
                    cg(rf, mcf, two_spectator, ms, final.two_j, mf)
                    * cg(ri, mci, two_spectator, ms, initial.two_j, mi)
                    * cg(ri, mci, 4, 2*q, rf, mcf)
                    * core_rme(final, initial) / sqrt(rf + 1)
                )
            return element * sqrt(final.two_j + 1) / weight
        return Radical()
    return result, core_rme


def matrix_product(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def one_boson_ibm(chi):
    matrices = {}
    for mu in range(-2, 3):
        a = [[Radical() for _ in range(6)] for _ in range(6)]
        for mf in range(-2, 3):
            a[mf + 3][0] = Radical(int(mf == mu))
            a[0][mf + 3] = Radical(sign(mf) * int(mf == -mu))
            for mi in range(-2, 3):
                a[mf + 3][mi + 3] = chi * sign(mi) * cg(4, 2*mf, 4, -2*mi, 4, 2*mu)
        matrices[mu] = a
    q2 = sum(sign(mu) * matrix_product(matrices[mu], matrices[-mu])[0][0] for mu in range(-2, 3))
    scalar3 = Radical()
    for mu in range(-2, 3):
        for nu in range(-2, 3):
            lam = -mu - nu
            if abs(lam) <= 2:
                coefficient = sign(mu + nu) * cg(4, 2*mu, 4, 2*nu, 4, 2*(mu + nu))
                scalar3 += coefficient * matrix_product(matrix_product(matrices[mu], matrices[nu]), matrices[lam])[0][0]
    return q2, -sqrt(F(7, 2)) * scalar3, matrices


def main():
    checks = []

    def expect(name, actual, expected):
        if actual != expected:
            raise AssertionError(f"{name}: actual={encode(actual)} expected={encode(expected)}")
        checks.append({"id": name, "passed": True})

    expect("CG_0_to_2", cg(0, 0, 4, 0, 4, 0), Radical(1))
    expect("CG_2_stretched_diagonal", cg(4, 4, 4, 0, 4, 4), sqrt(F(2, 7)))
    expect("CG_2_zero_projection", cg(4, 0, 4, 0, 4, 0), -sqrt(F(2, 7)))
    expect("six_j_J0_reduction", six_j(4, 4, 4, 0, 4, 4), Radical(F(1, 5)))
    for a, b in [(1, 4), (3, 4), (4, 4), (11, 4)]:
        for u in range(-a, a + 1, 2):
            for v in range(-b, b + 1, 2):
                norm = sum(cg(a, u, b, v, c, u + v) * cg(a, u, b, v, c, u + v) for c in range(abs(a-b), a+b+1, 2))
                expect(f"CG_completeness_{a}_{b}_{u}_{v}", norm, Radical(1))

    rotors = []
    for j2 in [0, 1, 2, 3, 5, 7, 9, 11, 13]:
        j = F(j2, 2)
        initial = State(j2)
        states = [State(x) for x in range(j2, j2 + 5, 2)]

        @lru_cache(None)
        def rme(final, incoming):
            return sqrt(incoming.two_j + 1) * cg(incoming.two_j, j2, 4, 0, final.two_j, j2)

        q2, q3 = recoupled_moments(initial, states, rme)
        expect(f"rotor_full_q2_J{j}", q2, Radical(1))
        expect(f"rotor_full_signed_q3_J{j}", q3, Radical(1))
        for m in sorted({j2, -j2, j2-2 if j2 >= 2 else j2}):
            expect(f"rotor_direct_component_contraction_J{j}_M{F(m,2)}",
                   direct_moments(initial, states, rme, m), (q2, q3))
        for a in states:
            for b in states:
                expect(f"rotor_RME_Hermiticity_J{j}_{a.two_j}_{b.two_j}",
                       rme(a, b), sign((a.two_j - b.two_j)//2) * rme(b, a))

        raw2, raw3, cosine, beta = literal_proxy(initial, [State(j2 + 4)], rme)
        cosine2_formula = F(7, 60) * (2*j*j - 5*j - 6)**2 * (2*j+5) / ((2*j+1)*(j+3)*(2*j+7))
        expect(f"rotor_literal_cosine_squared_J{j}", cosine*cosine, Radical(cosine2_formula))
        expect(f"rotor_Eq14_beta_J{j}", beta, Radical(1))
        strengths = [
            (rme(a, initial)*rme(a, initial) / Radical(j2+1)).rational()
            for a in states
        ]
        expected_strengths = [
            j*(2*j-1)/((j+1)*(2*j+3)),
            3*j/((j+1)*(j+2)),
            F(6)/((j+2)*(2*j+3)),
        ]
        expect(f"rotor_spin_channel_strengths_J{j}", strengths, expected_strengths)
        expect(f"rotor_negative_q0_signed_q3_J{j}",
               recoupled_moments(initial, states, lambda a,b: -rme(a,b)), (Radical(1), Radical(-1)))
        rotors.append({
            "J": str(j), "K": str(j), "q0": 1,
            "full_q2": q2, "full_signed_q3": q3,
            "full_gamma_degrees": 0,
            "q2_strengths_J_Jplus1_Jplus2": strengths,
            "literal_q2_raw": raw2, "literal_q3_abs_raw": raw3,
            "literal_cosine": cosine, "literal_cosine_squared": cosine2_formula,
            "literal_gamma": angle_record(cosine),
            "literal_beta_over_invariant_beta": beta,
        })

    spectators = []
    for case, transitions, middle in [
        ("axial_core", [1], [[-sqrt(F(10, 7))]]),
        ("two_core_2plus_multiplets", [1, 2], [[2, F(1, 3)], [F(1, 3), -1]]),
    ]:
        core2 = Radical(sum(F(x)**2 for x in transitions))
        core_triple = sum(Radical(transitions[a]) * Radical(middle[a][b]) * Radical(transitions[b])
                          for a in range(len(transitions)) for b in range(len(transitions)))
        core3 = -sqrt(F(7, 10)) * core_triple
        core_folded = abs(core3) / (core2 * sqrt(core2.rational()))
        for j2 in [1, 3, 5, 7, 9, 11, 13]:
            j = F(j2, 2)
            initial = State(j2, 0)
            states = [State(l, ch) for ch in range(1, len(transitions)+1)
                      for l in range(abs(4-j2), 4+j2+1, 2)]
            rme, core_rme = spectator_rme(j2, transitions, middle)
            # Independently verify the spectator reduced-element 6j identity.
            for a in [initial] + states:
                for b in [initial] + states:
                    rf, ri = (0 if a.channel == 0 else 4), (0 if b.channel == 0 else 4)
                    recoupled = (
                        sign((rf+j2+b.two_j+4)//2)
                        * sqrt((a.two_j+1)*(b.two_j+1))
                        * six_j(rf, a.two_j, j2, b.two_j, ri, 4)
                        * core_rme(a,b)
                    )
                    expect(f"spectator_RME_direct_vs_6j_{case}_{j}_{a}_{b}", rme(a,b), recoupled)
            q2, q3 = recoupled_moments(initial, states, rme)
            expect(f"spectator_inherits_q2_{case}_{j}", q2, core2)
            expect(f"spectator_inherits_signed_q3_{case}_{j}", q3, core3)
            for m in sorted({j2, -j2}):
                expect(f"spectator_direct_full_moments_{case}_{j}_{m}",
                       direct_moments(initial, states, rme, m), (core2, core3))
            restricted = [a for a in states if a.two_j == j2+4]
            raw2, raw3, cosine, beta = literal_proxy(initial, restricted, rme)
            beta_ratio = beta / sqrt(core2.rational())
            factor2 = (2*j+5)/5
            beta2 = (2*j+5)*(2*j+4)*(2*j+3)/(60*(2*j+1))
            factor3_2 = 2*(j+3)*(2*j+7)/(7*(j+2)*(2*j+3))
            factor3 = sqrt(factor3_2)
            expect(f"spectator_parent_q2_conjecture_{case}_{j}", raw2, factor2 * core2)
            expect(f"spectator_parent_beta_conjecture_{case}_{j}", beta_ratio, sqrt(beta2))
            expect(f"spectator_parent_cosine_conjecture_{case}_{j}", cosine, factor3 * core_folded)
            spectators.append({
                "core_control": case, "spectator_j": str(j),
                "core_q2": core2, "core_signed_q3": core3,
                "odd_full_q2": q2, "odd_full_signed_q3": q3,
                "literal_q2_raw": raw2, "q2_raw_over_core_q2": factor2,
                "beta_proxy_over_beta_invariant": beta_ratio,
                "beta_ratio_squared": beta2,
                "core_folded_cosine": core_folded, "literal_cosine": cosine,
                "F_j": factor3, "F_j_squared": factor3_2,
                "literal_gamma": angle_record(cosine),
                "spectral_scope": "all core-2 channels; no n=5 omission in this control",
            })

    ibm_q2, ibm_q3, qmat = one_boson_ibm(-sqrt(7)/Radical(2))
    expect("one_boson_IBM_q2", ibm_q2, Radical(5))
    expect("one_boson_IBM_signed_q3", ibm_q3, F(35,4)*sqrt(2))
    ibm_cos = ibm_q3 / (ibm_q2*sqrt(ibm_q2.rational()))
    expect("one_boson_IBM_cosine_squared", ibm_cos*ibm_cos, Radical(F(49,40)))
    for mu in range(-2,3):
        for row in range(6):
            for col in range(6):
                expect(f"one_boson_IBM_tensor_Hermiticity_{mu}_{row}_{col}",
                       qmat[mu][col][row], sign(mu)*qmat[-mu][row][col])
    a = matrix_product(qmat[2],qmat[-2])
    b = matrix_product(qmat[-2],qmat[2])
    comm_norm2 = sum((a[i][j]-b[i][j])*(a[i][j]-b[i][j])
                     for i in range(6) for j in range(6))
    assert comm_norm2.rational() > 0
    checks.append({"id":"one_boson_IBM_Q_components_do_not_commute","passed":True})

    fluct_q2 = Radical(F(1,2))
    fluct_q3 = Radical(F(1,2))
    fluct_cos = fluct_q3/(fluct_q2*sqrt(F(1,2)))
    expect("commuting_beta_fluctuation_cosine", fluct_cos, sqrt(2))

    print(json.dumps(encode({
        "schema": "nomura-v2-spin-invariant-exact-audit/1",
        "source_scope": "archived arXiv:1704.07101v2; literal Eqs.12-15 under the requested Wigner-Eckart convention",
        "convention": "<Jf Mf|Q_kq|Ji Mi> = CG(Ji Mi,kq|Jf Mf)*<Jf||Q_k||Ji>/sqrt(2Jf+1)",
        "arithmetic": "stdlib factorial Racah sums with exact rational/square-free-root arithmetic",
        "parent_or_production_code_imported": False,
        "nuclear_model_fit_or_data_change": False,
        "angular_coefficients_from_external_package": False,
        "checks_passed": len(checks), "checks_failed": 0,
        "checks": checks,
        "strong_K_equals_J_rotor_controls": rotors,
        "spectator_controls": spectators,
        "noncommuting_IBM_counterexample": {
            "N_bosons": 1, "state": "s boson, core R=0",
            "operator": "Q_mu=d_mu^dag*s+s^dag*tilde_d_mu+chi*[d^dag x tilde_d]^(2)_mu",
            "chi": -sqrt(7)/Radical(2),
            "boundary": "operator-algebra counterexample, not the paper's chi-prime=0.35 or an A130 calculation",
            "q2": ibm_q2, "signed_q3": ibm_q3, "ratio": ibm_cos,
            "commutator_Q2_Qminus2_Frobenius_norm_squared": comm_norm2,
            "angle": angle_record(ibm_cos),
        },
        "commuting_beta_fluctuation_counterexample": {
            "distribution": "beta=0 or 1, each with probability 1/2; gamma=0 at nonzero beta",
            "q2": fluct_q2, "signed_q3": fluct_q3, "ratio": fluct_cos,
            "angle": angle_record(fluct_cos),
        },
        "published_figures_reconstructed": False,
        "published_implementation_error_claimed": False,
        "novelty_claimed": False,
    }), indent=2))


if __name__ == "__main__":
    main()
