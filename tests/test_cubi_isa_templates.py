import typing

from altamisa.apps import isatab_validate
from cookiecutter.main import cookiecutter
from fnmatch import fnmatch
import pytest

import cubi_isa_templates


@pytest.mark.filterwarnings("error::altamisa.exceptions.CriticalIsaValidationWarning")
def test_isatabs(tmp_path):
    for tpl in cubi_isa_templates.TEMPLATES.values():
        extra_context = {"__output_dir": tpl.name}
        cookiecutter(
            template=tpl.path, extra_context=extra_context, output_dir=tmp_path, no_input=True
        )

        output = tmp_path / tpl.name
        assert output.exists()

        class dummyArgs(typing.NamedTuple):
            input_investigation_file: typing.TextIO
            show_duplicate_warnings: bool = False

        invs = []
        for f in output.iterdir():
            if fnmatch(f.name, "i_*.txt"):
                invs.append(f)
        assert len(invs) == 1

        with (output / invs[0].name).open() as f:
            args = dummyArgs(input_investigation_file=f)
            isatab_validate.run(args)
