#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

import versioneer

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

setup(
    author="Berlin Institute of Health, Core Unit Bioinformatics",
    author_email=("cubi@bih-charite.de"),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
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
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    project_urls={
        "Changelog": "https://github.com/bihealth/cubi-isa-templates/blob/main/CHANGELOG.md",
    },
)
