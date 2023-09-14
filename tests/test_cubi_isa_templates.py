from fnmatch import fnmatch
import shutil
import typing

from altamisa.apps import isatab_validate
from cookiecutter.main import cookiecutter
import pytest

from cubi_isa_templates import TEMPLATES


@pytest.mark.filterwarnings("error::altamisa.exceptions.CriticalIsaValidationWarning")
@pytest.mark.parametrize("tpl", TEMPLATES.values())
def test_isatabs(tpl, tmp_path):
    print("Testing " + tpl.name)
    for key, value in tpl.configuration.items():
        if isinstance(value, bool):
            value = [True, False]
        if isinstance(value, list) and not key.startswith("_"):
            for choice in value:
                extra_context = {"__output_dir": tpl.name, key: choice}
                cookiecutter(
                    template=tpl.path,
                    extra_context=extra_context,
                    output_dir=tmp_path,
                    no_input=True,
                )

                output = tmp_path / tpl.name
                assert output.exists()

                class dummyArgs(typing.NamedTuple):
                    input_investigation_file: typing.TextIO
                    show_duplicate_warnings: bool = False

                invs = [f for f in output.iterdir() if fnmatch(f.name, "i_*.txt")]
                assert len(invs) == 1

                with (output / invs[0].name).open() as f:
                    args = dummyArgs(input_investigation_file=f)
                    isatab_validate.run(args)

                # cleanup
                shutil.rmtree(output)
