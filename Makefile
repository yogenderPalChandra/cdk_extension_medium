SHELL:=/bin/bash

.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

GIT_COMMIT ?= $(shell git rev-parse HEAD)
VERSION = $(shell python setup.py --version)
REPOSITORY ?= $(shell basename $(CWD))

######################################################
# CUSTOM config!
SRC_DIR = aws_cdk_extensions
######################################################

CWD := $(shell pwd)
JUNIT_XML ?= ./build/test-reports/report/$(REPOSITORY).xml
COV_REPORT_HTML ?= ./build/test-reports/coverage/$(REPOSITORY)/

# Jenkins required commands
.PHONY: install
install: 	## install the dependencies
	PIPENV_VENV_IN_PROJECT=1 PIPENV_IGNORE_VIRTUALENVS=1 pipenv run pipenv sync --dev
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run pipenv graph

.PHONY: init
init: 	## init the pipenv on Windows10 / Ubuntu subsystem
	sudo python3 -m pipenv --python 3.10
	sudo chown -R $(shell whoami):$(shell whoami) ~/.local/share/virtualenvs/

.PHONY: lock
lock: 	## install the dependencies
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run pipenv lock
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run pipenv sync --dev
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run pipenv graph

.PHONY: lint
lint:		## lint the project
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run pylint $(SRC_DIR)
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run mypy $(SRC_DIR)

# --namespace-packages

.PHONY: test
test:		## run test and generate reports
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run pytest $(SRC_DIR)_test \
		--junitxml=$(JUNIT_XML) \
		--cov-report=html:$(COV_REPORT_HTML) \
		--cov=$(SRC_DIR)
.PHONY: clean
clean:
	rm -rf build/
	rm -rf dist/

.PHONY: bundle
bundle: clean
	PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python setup.py bdist_wheel

deploy: bundle
	@twine upload --repository-url https://jfrog.io/api/pypi/pypi-Your-Link-Comes-Here -u $(PYPI_USER) -p $(PYPI_PASS) dist/*
