# CUBI ISA-Tab Templates

This repository contains [Cookiecutter](https://github.com/cookiecutter/cookiecutter)-based [ISA-Tab](https://isa-tools.org/) templates used at [CUBI](https://www.cubi.bihealth.org/).

Example of simple usage:

```
from cookiecutter.main import cookiecutter
from cubi_isa_templates import TEMPLATES

isa_tpl = TEMPLATES["single_cell_rnaseq"]
extra_context = {"__output_dir": "template_dir", "is_triplet": isa_tpl.configuration.get("is_triplet", False)}
cookiecutter(template=isa_tpl.path, extra_context=extra_context, output_dir="/template/path/", no_input=True)
```

For proper use command line usage, see [cubi-tk](https://github.com/bihealth/cubi-tk).
