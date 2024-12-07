SHELL := /bin/bash

.PHONY: check
check:
	mypy --strict --pretty --show-error-codes .
	black --diff --check .
	pylint $(shell git ls-files | grep "\.py$$")

.PHONY: leaderboard
leaderboard:
	python leaderboard.py
	git add README.md
	git commit -m "(auto) Update leaderboard"
	git push
