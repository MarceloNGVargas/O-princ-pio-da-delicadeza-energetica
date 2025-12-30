# Release v1.0 and DOI via Zenodo — Guide

## Prerequisites
- Public GitHub repository
- Main branch: main
- License files: LICENSE-MIT and LICENSE-CC-BY-4.0
- Citation file: CITATION.cff
- Documentation organized in docs/pt and docs/en; images in images/; script in examples/

## Create the v1.0 release on GitHub
- CLI:
  - gh release create v1.0 --repo MarceloNGVargas/O-principio-da-delicadeza-energetica --generate-notes --title "v1.0"
- Web interface:
  - Go to the repository → Releases → Draft a new release
  - Tag: v1.0, Target: main
  - Title: v1.0
  - Publish release

## Connect to Zenodo and generate a DOI
- Go to https://zenodo.org and sign in with GitHub
- Authorize access and go to Settings → GitHub
- Enable the repository MarceloNGVargas/O-principio-da-delicadeza-energetica
- Enable automatic archiving on releases
- Create or confirm the v1.0 release on GitHub
- Wait for Zenodo to archive the release and generate the DOI
- Copy the generated DOI (format 10.5281/zenodo.xxxxxxx)

## Update CITATION.cff and README with the DOI
- Edit CITATION.cff:
  - Add:
    - doi: "10.5281/zenodo.xxxxxxx"
    - identifiers:
      - type: doi
        value: "10.5281/zenodo.xxxxxxx"
- Edit README.md:
  - Badge:
    - [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.xxxxxxx.svg)](https://doi.org/10.5281/zenodo.xxxxxxx)

## Final checks
- README renders relative links (docs/, images/)
- v1.0 release visible with notes
- DOI resolves to Zenodo page with artifacts
- Licenses and CITATION present at the root

## Optional
- Add keywords and communities on Zenodo
- Include extra files as release assets
