# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help install venv ipython test pflake8 clean lint build

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

install:  ## Install in development mode.
	@.venv/bin/python -m pip install -e .[test,dev]

venv:  ## Create a virtualenv if it doesn't exists.
	python -m venv .venv

ipython:  ## Starts ipython.
	@.venv/bin/ipython


test:  ## Execute all tests.
	@.venv/bin/pytest tests

lint:  ## Execute a lint to code quality.
	# @.venv/bin/mypy --ignore-missing-imports dundie
	@.venv/bin/pflake8

fmt:  ## Format our imports with isort
	@.venv/bin/isort -m 3 dundie tests

clean:  ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

build:
	@python setup.py sdist bdist_wheel

publish-test:
	@twine upload --repository testpypi dist/*

docs:  ## Build our documentaition
	@mkdocs build --clean

docs-serve:  ## Starts our documentation server
	@mkdocs serve