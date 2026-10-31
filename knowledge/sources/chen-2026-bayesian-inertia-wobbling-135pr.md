---
type: source
title: "Chen et al. 2026: Bayesian inertias in 135Pr, accepted-record and inference boundaries"
aliases: [Chen 2026 Bayesian inertia 135Pr, Bayesian inference of moments of inertia for wobbling motion in 135Pr]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: theoretical-paper
reading_depth: metadata-only
title_original: "Bayesian inference of moments of inertia for wobbling motion in 135Pr"
authors: [Yeruoxi Chen, Q. B. Chen, R. V. Jolos]
year: 2026
doi: 10.1103/phhq-9vmt
arxiv: ""
canonical_source: https://journals.aps.org/prc/accepted/10.1103/phhq-9vmt
citation_key: chen_2026_bayesian_wobbling_135Pr
raw_file: raw/papers/gpt/learning-daily/20261029-DAY27-cross-mass-region-transferability/crossref-work.json
raw_sha256: 5f0beebf4feb6365241079cc20fdd96cea482efad18f736e07faf5b935756eab
nuclei: [135pr]
models: [core-quasiparticle-coupling]
observables: [energy-levels, moments-of-inertia, electromagnetic-transitions]
methods: [bayesian-inference, metropolis-hastings-mcmc]
tags: [a130, wobbling, identifiability, conditional-prediction, metadata-only]
---

# Bayesian inertia inference in 135Pr

## Scope and Reading Depth

Identity and version checks were performed on 2026-10-29 UTC. Covered scope: the Crossref work JSON, DOI content-negotiated CSL JSON, the author's ECNU publication list, five official arXiv Atom searches, and the official APS accepted page successfully opened through the web tool on the correction pass. In that rendered page, the abstract is at lines 76-78 and acceptance is at line 146. Fresh terminal HTTP requests still returned 403; this does not negate the successful web open. The `raw_file` above is a metadata original, not a paper PDF.

**Not covered:** any manuscript version, numerical tables, figures, equations, reference list, SI, code, posterior samples, or sampling implementation. No original manuscript full text or SI was acquired. `reading_depth: metadata-only` deliberately includes the public abstract without implying a methods reading. Acquisition receipt: `outputs/literature-acquisition/20261029-day27-bayesian135pr.json`. This bounded task does not close Day27 or advance curriculum state; the parent session owns that lifecycle.

## Abstract extraction correction

The initial source page incorrectly attributed a Gaussian-process emulator to this article. A fresh direct `web.open` of the exact official accepted DOI resolves the supported method as CQPC with Metropolis-Hastings MCMC. Energies-only constraints and fixed electromagnetic inputs are explicitly supported by the current direct page; they remain in the corrected record.

The prior scratch observation saved identity and asserted abstract locators, but no verbatim abstract. The archived terminal accepted-page response is a 403 response, not a historical copy of the scientific page. Consequently, the earlier GP claim has no saved matching primary text and is withdrawn as an extraction error. There is no evidence establishing an official abstract revision or allowing a stale-versus-mismatched lookup diagnosis. The parent's intervening search rendering also differed; its proposed FA/VMI/HP comparison is not supported by the directly opened page and is not adopted. The receipt preserves these lookup differences and the correction provenance without treating them as official text variants.

## Bibliographic Record

The normalized title, author order, journal **Physical Review C**, publisher APS, and DOI agree between APS and Crossref. The Crossref title contains MathML for the mass number; flattening it gives the title recorded above.

| Record | Precise locator | Verified content and boundary |
| --- | --- | --- |
| APS accepted article | direct web-open lines 74, 79, 146 and 148 | Yeruoxi Chen; Q. B. Chen; R. V. Jolos; accepted **2026-10-19**. Direct web open succeeded on correction; terminal HTTP requests remained blocked. |
| Crossref original `crossref-work.json` | `/message/DOI`, `/message/author`, `/message/container-title`, `/message/publisher`, `/message/accepted/date-parts` | Same identity and journal; accepted date `[2026,10,19]`. |
| Crossref original | `/message/assertion/0`, `/message/created/date-time`, `/message/deposited/date-time` | Received **2026-09-08**; created/deposited **2026-10-19T18:11:08Z**. |
| Crossref original | `/message/published-online/date-parts`, `/message/issued/date-parts`, `/message/published/date-parts` | All give **2026-10-19**. These deposited dates must be reported alongside the accepted-page status. |
| Crossref original | absent `/message/volume`, `/message/issue`, `/message/page`, `/message/article-number`; `/message/license/0/content-version` | No final issue/article coordinates supplied; the license entry says `vor`. That label alone does not establish delivery of a version of record. |
| DOI CSL original `doi-csl.json` | `/DOI`, `/author`, `/container-title`, `/accepted`, `/published-online` | Same deposited record through DOI content negotiation; not independent bibliographic evidence. |
| Author's ECNU page `ecnu-qb-chen-publications.html` | publication list, 2026 section, unique entry with this exact title | Same three authors; lists PRC and 2026, leaving volume/page blank. No target manuscript/PDF link found in its anchors. |
| APS Harvest | metadata and `/fulltext` routes for this DOI | Both HTTP 404. This is an endpoint result, not proof that no manuscript exists. |

**Version conclusion:** a PRC accepted article with a registered DOI is verified. Crossref also assigns an online publication date, but an accessible final numbered version was not verified. Do not silently replace acceptance with a demonstrated version-of-record publication, or assert that the article is definitely unpublished.

The official arXiv queries returned: exact title phrase **0**; DOI suffix **0**; `au:"Chen_Yeruoxi"` **1 unrelated fusion-barrier paper**; `all:Bayesian AND all:wobbling` **6 unrelated papers**; `au:Chen AND all:wobbling` **29 entries, none matching this title/author trio/DOI**. The latter query requested 100, so it was not truncated. No arXiv identifier was assigned to this work. Negative searches do not prove that no preprint exists under another title or in another repository.

All eight archived originals and their hashes are listed in the acquisition receipt. Crossref and DOI CSL share the same deposition lineage; the ECNU entry is author-maintained, not another experiment. OpenAlex was used only to look for a public location: it returned no PDF or repository location. Its `publishedVersion` flag was not accepted as version evidence.

## Summary

The directly opened abstract describes energy-constrained CQPC inference and conditional predictions. Its numerical inference contract remains inaccessible. The reported agreement and transition stability are author claims, not independent certification or exclusion of competing mechanisms.

## Key Results

Locators below refer to the official accepted page successfully opened on the correction pass: line 76 contains abstract sentences 1-2, line 77 sentences 3-4, and line 78 sentence 5. They are web-page locators, not manuscript page numbers. No paper equation, figure, or table locator is available.

| ID | Narrow statement | claim_kind; evidence_level; source_independence | Exact locator | confidence; needs_review |
| --- | --- | --- | --- | --- |
| CH26-B1 | The named framework is core-quasiparticle coupling (CQPC), sampled using Metropolis-Hastings MCMC. No GP method is established by this page. | model-result; contextual; single | APS accepted page, line 76, sentence 1 | medium; true |
| CH26-B2 | The stated constraints consist only of experimental yrast and wobbling energies. | model-result; contextual; single | APS accepted page, line 76, sentence 2 | medium; true |
| CH26-B3 | Authors report the ordering Jm > Js > Jl and quantified inertia correlations; no numerical matrix or ordering probability is available here. | author-interpretation; contextual; single | APS accepted page, line 76, sentence 2 | medium; true |
| CH26-B4 | Authors report posterior-propagated wobbling energies, E2 strengths and other observables at fixed EM inputs, with 68% and 95% credible bands. Values of the fixed inputs remain unspecified. | model-result; contextual; single | APS accepted page, line 77, sentence 1 | medium; true |
| CH26-B5 | Parameter posteriors within an assumed model are not posterior odds against an alternative model. | our-inference; none; single | This page, Mathematical inference contract, equations A and E | high for the mathematical distinction; false |
| CH26-B6 | A prediction conditional on fixed operator inputs excludes their uncertainty unless it is separately propagated. | our-inference; none; single | This page, Mathematical inference contract, equation C | high for the conditional-probability statement; false |
| CH26-B7 | Authors say measured spectra and E2 strengths agree with their predictions and the transverse-to-longitudinal transition persists over the energy-compatible inertia region. This is a within-model stability claim. | author-interpretation; contextual; single | APS accepted page, line 77, sentence 2 | medium; true |

`contextual` here restricts the scientific statements to what the abstract reports; it does not certify the unobserved numerical analysis. `needs_review: false` on B5/B6 records a bounded mathematical self-audit, not a human review or paper-use admission.

## Competing Interpretations and Limitations

The following extraction gaps remain explicit; none is evidence that an analysis was absent from the unread manuscript.

| Requested item | What is actually available | Missing text/locator |
| --- | --- | --- |
| Hamiltonian and conditioning | CQPC framework named | Configuration, deformation, pairing, single-particle alignment, axis convention, level assignments, fitted versus fixed Hamiltonian inputs. |
| Energy data | Experimental yrast/wobbling energies are the only stated constraints | Spin range, values, errors, energy reference, whether "wobbling energies" means band energies or derived excitation differences, training/validation split. |
| Likelihood | Not exposed | Distribution, residual definition, covariance, fitted noise scales, outliers, normalization, discrepancy term. |
| Priors | Not exposed | Bounds, shape, independence/correlations, axis-order restrictions, inertia parameterization and spin dependence. |
| Inertias and posterior | Ordering Jm > Js > Jl and correlation quantification reported | Numerical units, central estimates, intervals, joint correlation values, ordering probabilities, effective sample size, convergence and prior sensitivity. |
| Sampler | Metropolis-Hastings MCMC named | Proposals, initialization, sample counts, acceptance rate, convergence diagnostics and numerical approximation error. No GP implementation is inferred. |
| EM inputs and outputs | Fixed EM inputs; E2 strengths and credible-band levels named | Which charges, quadrupole parameters or magnetic factors, their values/provenance, full observable list and numerical intervals. Those are possible input categories to inspect, not an extracted fixed-input list. |
| Competing interpretation | Robustness of a transverse-to-longitudinal transition is claimed within the energy-compatible inertia region | Alternative mechanism likelihoods, matched inputs, marginal likelihoods or predictive scores. No FA/VMI/HP comparison is stated in the direct abstract; this does not establish its absence from the manuscript. |
| SI/data/code availability | No accessible original or attachment list | No justified statement that SI does not exist. |

## Mathematical inference contract

The equations A-E below are **our generic audit framework, not reconstructed equations from Chen et al.** No particular likelihood, prior, parameter count, numerical inertia, or EM operator is attributed to the unread text. The abstract establishes the energy-only and fixed-EM description, but not this mathematical implementation.

Let \(D_E\) denote the actual energy observations, \(M\) the selected Hamiltonian/model, \(A\) the adopted state/band assignments, \(F\) fixed structural inputs, and \(\theta\) the genuinely fitted parameters. The inference has the form

\[
p(\theta\mid D_E,M,A,F)
 = \frac{p(D_E\mid\theta,M,A,F)\,\pi(\theta\mid M,A,F)}
        {Z_M(D_E\mid A,F)}. \tag{A}
\]

An energies-only fit can constrain combinations of \(\theta\) to which the energy map is sensitive **inside this conditioning**. Locally, for \(K_{i\alpha}=\partial E_i/\partial\theta_\alpha\), likelihood curvature contains \(K^\mathsf{T}\Sigma_E^{-1}K\). Small singular directions are weakly identified; priors or fixed inputs can narrow them. Neither full rank nor narrow published marginals can be established from this abstract. Axis permutations and inertia/deformation/alignment tradeoffs must be assessed in the actual model. Eigenvalues alone do not specify a unique transition operator or, across different Hamiltonians, unique eigenvectors.

For illustration only, a Gaussian likelihood would require the complete contract

\[
\log L=-\tfrac12\left[
r^\mathsf{T}\Sigma^{-1}r+\log|\Sigma|+N\log(2\pi)\right],
\quad \Sigma=\Sigma_{\rm exp}+\Sigma_{\rm num}+\Sigma_{\rm disc}. \tag{B}
\]

This is not a claim that the paper uses Gaussian errors, independent additive components, numerical-error covariance \(\Sigma_{\rm num}\), or any discrepancy term. Those choices remain unknown, and no emulator is inferred. The determinant matters if covariance depends on fitted parameters. If a chosen data vector is a linear transformation \(D_E=T e\) of shared measured levels, its covariance is \(T\Sigma_eT^\mathsf{T}\); including both levels and derived differences as independent data can double count information. Whether that caution applies here depends on the unavailable definition of the fitted energies.

For an EM observable \(O=h(\theta,\eta;M,A,F)\) with operator inputs fixed to \(\eta_0\), propagating the energy posterior gives

\[
p(O\mid D_E,M,A,F,\eta_0)
 = \int \delta_{\rm D}\!\left[O-h(\theta,\eta_0;M,A,F)\right]
       p(\theta\mid D_E,M,A,F)\,d\theta. \tag{C}
\]

Thus wavefunctions and EM values can vary with sampled inertias even while EM operator inputs stay fixed. Such intervals are conditional; they do not automatically include uncertain charges, quadrupole shape/scale, magnetic factors, band assignments, numerical approximation error, or model inadequacy. Their actual uncertainty budget cannot be audited here. The more general propagation would integrate a justified joint distribution of \((\theta,\eta,F)\) and any predictive discrepancy. "EM was not fitted" also does not establish independent validation if fixed inputs or model choices had previously been selected using the same EM measurements. Likewise, predicted wobbling energies are not known to be held out.

A generic unequal-inertia or ordering assessment needs a resolution statement. Under an absolutely continuous prior, exact equality already has probability zero. A useful check is, for declared \(\epsilon>0\) in stated inertia units,

\[
P\!\left(\mathcal J_m>\max(\mathcal J_s,\mathcal J_l),\
\min_{a<b}|\mathcal J_a-\mathcal J_b|>\epsilon
\mid D_E,M,A,F\right). \tag{D}
\]

Here \(s,m,l\) must denote declared shape axes, not inertia values sorted after fitting. Differences and ordering probabilities require the joint posterior; disjoint or overlapping marginal intervals alone are insufficient. No value of this probability is known. Effective triaxial rotational response within a PRM is not automatically a unique microscopic static-shape determination.

Finally, discrimination between \(M_w\) and a competing \(M_c\) needs an explicit comparison, for example

\[
\frac{p(M_w\mid D)}{p(M_c\mid D)}
=\frac{p(D\mid M_w)}{p(D\mid M_c)}
 \frac{p(M_w)}{p(M_c)}. \tag{E}
\]

Each evidence integrates its own justified prior and nuisance/discrepancy treatment. A normalized posterior within \(M_w\) supplies neither the competing evidence nor these odds. Energies could discriminate models whose predictive energy distributions differ; the absence of EM in a fit does not make that impossible. The authors' reported stability of a transverse-to-longitudinal transition over their energy-compatible inertia region does not supply odds against a different mechanism. What is unsupported here is a claim that this particular conditional fit excludes signature-partner, mixed-configuration, or other competing interpretations. No old 135Pr experimental audit was repeated.

## One useful public-input follow-up

Reuse the already audited public 135Pr energy and transition inputs for **one matched-input, leave-EM-out predictive test**. Fit a declared wobbling model and one declared competitor to the same energies, then compare their predictive distributions for one preselected interband E2 fraction \(f_{E2}=\delta^2/(1+\delta^2)\), with \(\delta\) the E2/M1 amplitude mixing ratio in a declared convention. Propagate the published measurement likelihood and the same justified EM nuisance inputs in both models; if the public record supplies only asymmetric intervals rather than a likelihood, present an interval sensitivity test instead of inventing Gaussian errors. The transformation is for this mixed transition, not for an unrelated branching ratio.

This would test whether an energy-calibrated interpretation predicts a withheld transition. It is a proposed test, not a new experimental audit, a reproduced Chen posterior, or a completed calculation. Reproducing Chen specifically first requires the original manuscript's likelihood, priors, energy table, fixed-input list, and sampler/discrepancy contract.

## Agent self-audit

- P0 identity/raw/secret/overlap: none identified within this bounded deliverable. The original metadata response is hashed; no blocked HTML is represented as a PDF, no arXiv ID was guessed, and no pre-existing raw file was overwritten.
- Extraction error corrected: the GP method attribution is withdrawn. The direct official page supports CQPC/MH-MCMC, energy-only constraints and fixed-EM predictions. No official text revision or FA/VMI/HP comparison is established.
- P1 scientific boundary: B1-B4/B7 remain abstract-level reports; all numerical methods, fixed EM values, full-text locators and SI remain unresolved. The absence of text is not attributed to the authors as an omitted analysis.
- P1 inference boundary: equations A-E are our analysis; no posterior reanalysis, Bayes factor, mechanism exclusion or experimental confirmation is claimed.
- No human-review event, shared-index update, handoff/log edit, BibTeX write, Git write, publication action, or Day27 lifecycle transition occurred. Those exclusions follow the task's explicit scope.

## Extracted Pages

This source page is the sole knowledge writeback. No manuscript pages were read or extracted, and no shared nucleus, model or index page was edited. Reusable mathematical cautions and the proposed predictive test are preserved here with explicit inference labels.
