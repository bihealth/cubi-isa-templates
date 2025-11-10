#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

from setuptools import setup


def parse_requirements(path):
    """Parse ``requirements.txt`` at ``path``."""
    requirements = []
    with open(path, "rt") as reqs_f:
        for line in reqs_f:
            line = line.strip()
            if line.startswith("-r"):
                fname = line.split()[1]
                inner_path = os.path.join(os.path.dirname(path), fname)
                requirements += parse_requirements(inner_path)
            elif line != "" and not line.startswith("#"):
                requirements.append(line)
    return requirements


with open("README.md") as readme_file:
    readme = readme_file.read()

install_requirements = parse_requirements("requirements.txt")

package_root = os.path.abspath(os.path.dirname(__file__))
version = {}
with open(os.path.join(package_root, "cubi_isa_templates/version.py")) as fp:
    exec(fp.read(), version)
version = version["__version__"]

setup(
    author="Berlin Institute of Health, Core Unit Bioinformatics",
    author_email=("cubi@bih-charite.de"),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
    description="CUBI ISA-Tab templates",
    install_requires=install_requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    name="cubi-isa-templates",
    packages=["cubi_isa_templates"],
    url="https://github.com/bihealth/cubi-isa-templates",
    version=version,
    project_urls={
        "Changelog": "https://github.com/bihealth/cubi-isa-templates/blob/main/CHANGELOG.md",
    },
)
