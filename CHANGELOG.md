# Changelog

## [0.2.0](https://github.com/bihealth/cubi-isa-templates/compare/v0.1.2...v0.2.0) (2025-11-14)


### Features

* Simplify mass cytometry template ([#41](https://github.com/bihealth/cubi-isa-templates/issues/41)) ([aef8d77](https://github.com/bihealth/cubi-isa-templates/commit/aef8d77be6e0423ec86646012d3c132cdd7f06d4))


### Bug Fixes

* Update dependencies & CI ([#44](https://github.com/bihealth/cubi-isa-templates/issues/44)) ([aeb6f14](https://github.com/bihealth/cubi-isa-templates/commit/aeb6f147fcb42e815e30a713c5139fbd606240cb))

## v0.1.2
- Fixed bulk_rnaseq template using wrong wrong configuration (#33)
- Fixed parameter inconsistency with Fastq prefix
- Fixed file name slash sanitization (#37) (#38)

## v0.1.1
- Fixed code styling (#30)
- Removed ontology URI workaroung (#31)

## v0.1.0

- Set up project based on templates currently in cubi-tk
- Added automated validation testing (#2, #12)
- Added new template *mass_cytometry* (#4)
- Added new template *somatic* (#23)
- Removed template *stem_cell_core* (#8)
- Removed templates *tumor_normal_dna* and *tumor_normal_triplets* (#23)
- Changed `Library Name` headers to `Extract Name` for ISA model compatibility (#3)
- Converted 'internal' variables to private (#17)
- Fixed broken templates (#5, #6, #7, #19)
