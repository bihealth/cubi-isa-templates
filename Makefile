.PHONY: black
black:
	black -l 100 .

.PHONY: black-check
black-check:
	black -l 100 --check .
