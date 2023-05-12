import sys

sample_factors = "{{cookiecutter.sample_factors}}".split(",")
sample_factor_types = "{{cookiecutter.sample_factor_types}}".split(",")
if not len(sample_factors) == len(sample_factor_types):
    print("ERROR: Sample factors needs to be the same length as Sample factor types.")
    sys.exit(1)
