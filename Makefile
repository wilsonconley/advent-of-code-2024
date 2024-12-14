SHELL := /bin/bash

.PHONY: check
check: lint typecheck format

.PHONY: lint
lint:
	pylint $(shell git ls-files '*.py' | grep -vF "template")

.PHONY: typecheck
typecheck:
	mypy --strict --pretty --show-error-codes ./aoc/ leaderboard.py

.PHONY: format
format:
	black --diff --check .

.PHONY: leaderboard
leaderboard:
	python leaderboard.py
	git add README.md
	git commit -m "(auto) Update leaderboard"
	git push

.PHONY: day_%
day_%:
	cp -r aoc/template aoc/$@

.PHONY: env
env: .python-version
	pip install -e .
	pyenv rehash

.python-version:
	pyenv install --skip-existing 3.10
	pyenv virtualenv --force 3.10 aoc_2024
	pyenv local aoc_2024
