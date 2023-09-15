# CUBI ISA-Tab Templates

![tests](https://github.com/bihealth/cubi-isa-templates/actions/workflows/main.yml/badge.svg)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This repository contains [Cookiecutter](https://github.com/cookiecutter/cookiecutter)-based [ISA-Tab](https://isa-tools.org/) templates used at [CUBI](https://www.cubi.bihealth.org/).

Example of simple usage:

```py
from cookiecutter.main import cookiecutter
from cubi_isa_templates import TEMPLATES

isa_tpl = TEMPLATES["single_cell_rnaseq"]
extra_context = {"__output_dir": "template_dir"}
cookiecutter(
    template=isa_tpl.path,
    extra_context=extra_context,
    output_dir="/template/path/",
    no_input=True
)
```

For proper command line usage, see [cubi-tk](https://github.com/bihealth/cubi-tk).
