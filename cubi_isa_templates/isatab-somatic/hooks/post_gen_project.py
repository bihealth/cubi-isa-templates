"""Remove files not needed by the ISA-tab."""

from pathlib import Path

REMOVE_PATHS = [
    (
        "{% if not cookiecutter.is_triplet %}"
        "a_{{cookiecutter.s_file_name}}_transcriptome_profiling.txt"
        "{% endif %}"
    ),
]

for path in REMOVE_PATHS:
    if path:
        path = Path(path)
        if path.exists():
            if path.is_dir():
                path.rmdir()
            else:
                path.unlink()
