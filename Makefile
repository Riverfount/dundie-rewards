# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help install venv ipython test pflake8

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

install:  ## Install in development mode.
	@.venv/bin/python -m pip install -e .[dev]

venv:  ## Create a virtualenv if it doesn't exists.
	python -m venv .venv

ipython:  ## Starts ipython.
	@.venv/bin/ipython


test:  ## Execute all tests.
	@.venv/bin/pytest

lint:  ## Execute a lint to code quality.
	@.venv/bin/pflake8