"""CUBI ISA-Tab templates"""

import attr
import json
import os
import typing


#: Base directory to this file.
_BASE_DIR = os.path.dirname(__file__)


@attr.s(frozen=True, auto_attribs=True)
class IsaTabTemplate:
    """Information regarding an ISA-tab template."""

    #: Name of the ISA-tab template.
    name: str

    #: Path to template directory.
    path: str

    #: Configuration loaded from ``cookiecutter.json``.
    configuration: typing.Dict[str, typing.Any]

    #: Optional description string.
    description: typing.Optional[str] = None


def load_variables(template_name, extra=None):
    """Load variables given the template name."""
    extra = extra or {}
    config_path = os.path.join(_BASE_DIR, template_name, "cookiecutter.json")
    with open(config_path, "rt") as inputf:
        result = json.load(inputf)
    result.update(extra)
    return result


#: Known ISA-tab templates (internal, mapping generated below).
_TEMPLATES = (
    IsaTabTemplate(
        name="single_cell_rnaseq",
        path=os.path.join(_BASE_DIR, "isatab-single_cell_rnaseq"),
        description="single cell RNA sequencing ISA-tab template",
        configuration=load_variables("isatab-single_cell_rnaseq"),
    ),
    IsaTabTemplate(
        name="bulk_rnaseq",
        path=os.path.join(_BASE_DIR, "isatab-bulk_rnaseq"),
        description="bulk RNA sequencing ISA-tab template",
        configuration=load_variables("isatab-generic"),
    ),
    IsaTabTemplate(
        name="tumor_normal_dna",
        path=os.path.join(_BASE_DIR, "isatab-tumor_normal_dna"),
        description="Tumor-Normal DNA sequencing ISA-tab template",
        configuration=load_variables("isatab-tumor_normal_dna", {"is_triplet": False}),
    ),
    IsaTabTemplate(
        name="tumor_normal_triplets",
        path=os.path.join(_BASE_DIR, "isatab-tumor_normal_triplets"),
        description="Tumor-Normal DNA+RNA sequencing ISA-tab template",
        configuration=load_variables("isatab-tumor_normal_triplets", {"is_triplet": True}),
    ),
    IsaTabTemplate(
        name="germline",
        path=os.path.join(_BASE_DIR, "isatab-germline"),
        description="germline DNA sequencing ISA-tab template",
        configuration=load_variables("isatab-germline"),
    ),
    IsaTabTemplate(
        name="generic",
        path=os.path.join(_BASE_DIR, "isatab-generic"),
        description="generic RNA sequencing ISA-tab template",
        configuration=load_variables("isatab-generic"),
    ),
    IsaTabTemplate(
        name="microarray",
        path=os.path.join(_BASE_DIR, "isatab-microarray"),
        description="microarray ISA-tab template",
        configuration=load_variables("isatab-microarray"),
    ),
    IsaTabTemplate(
        name="ms_meta_biocrates",
        path=os.path.join(_BASE_DIR, "isatab-ms_meta_biocrates"),
        description="MS Metabolomics Biocrates kit ISA-tab template",
        configuration=load_variables("isatab-ms_meta_biocrates"),
    ),
    IsaTabTemplate(
        name="stem_cell_core_bulk",
        path=os.path.join(_BASE_DIR, "isatab-stem_cell_core_bulk"),
        description="Bulk RNA sequencing ISA-tab template from hiPSC for stem cell core projects",
        configuration=load_variables("isatab-stem_cell_core_bulk"),
    ),
    IsaTabTemplate(
        name="stem_cell_core_sc",
        path=os.path.join(_BASE_DIR, "isatab-stem_cell_core_sc"),
        description="Single cell RNA sequencing ISA-tab template from hiPSC for stem cell core "
        "projects",
        configuration=load_variables("isatab-stem_cell_core_sc"),
    ),
)

#: Known ISA-tab templates.
TEMPLATES = {tpl.name: tpl for tpl in _TEMPLATES}
