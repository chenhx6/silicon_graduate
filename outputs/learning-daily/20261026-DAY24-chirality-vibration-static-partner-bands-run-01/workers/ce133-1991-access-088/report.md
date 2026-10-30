# 1991Pa04 official full-text access — independent retry 088

## Scope and stopping rule

The target is ENSDF reference **1991Pa04**, E. S. Paul *et al.*, “Electromagnetic
properties of N=75 isotones: evidence for triaxiality at low spin,” *Journal of
Physics G: Nuclear and Particle Physics* **17**(5), 605–617 (1991), DOI
`10.1088/0954-3899/17/5/009`. This worker made one route only:

1. Crossref DOI metadata (`https://api.crossref.org/works/10.1088%2F0954-3899%2F17%2F5%2F009`) to verify identity and the publisher resource;
2. the single official IOP PDF URL
   `https://iopscience.iop.org/article/10.1088/0954-3899/17/5/009/pdf`.

No alternate IOP paths, mirrors, repositories, or third-party endpoints were
tried. On an HTML challenge response, the attempt was stopped as required.

## Access record

| item | observed value |
|---|---|
| Crossref URL | `https://api.crossref.org/works/10.1088%2F0954-3899%2F17%2F5%2F009` |
| Crossref status | HTTP 200 |
| Crossref content type | `application/json` |
| Crossref identity | DOI `10.1088/0954-3899/17/5/009`; title, authors, journal, volume 17, issue 5, pp. 605–617, print date 1991-05-01; publisher IOP Publishing |
| IOP PDF URL | `https://iopscience.iop.org/article/10.1088/0954-3899/17/5/009/pdf` |
| IOP response chain | HTTP 302 to `validate.perfdrive.com` followed by HTTP 200 |
| final content type | `text/html; charset=UTF-8` |
| final size | 14,371 bytes |
| final file type | JavaScript/HTML source; not a PDF |
| final SHA-256 | `e740d939a951b4b0446bf940e5dde241be27def579cb30a3c03a82f983f86509` |
| Crossref JSON SHA-256 | `bd71960941eec9a815a38aa3fe054fe821f54ee02258e9b380a95cf12cef9751` |
| request time | 2026-10-26T20:48:41–20:48:43Z (HTTP `Date` headers) |

The complete headers, body, Crossref record, extracted metadata, status and
hashes are in [`tmp/day24-ce133-1991-access-088/`](../../tmp/day24-ce133-1991-access-088/).

## Failure reason and evidence boundary

The IOP request is blocked by Radware Bot Manager (`validate.perfdrive.com`),
and the body begins with `Radware Bot Manager Captcha`. Although curl exits 0
after the redirect, the final representation is HTML challenge code rather than
the article PDF. Therefore this attempt supplies bibliographic identity only;
it supplies **no official正文, no low-spin δ values, and no electromagnetic
transition evidence**. No scientific inference is made from the metadata.

No canonical or raw file was written, no producer output was changed, and no
Git operation was performed.
