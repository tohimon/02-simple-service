.PHONY: build test clean package

VENV_NAME?=venv

.DEFAULT: help
help:
	@echo "make build"
	@echo "       run linter against the project code"
	@echo "make test"
	@echo "       run tests"
	@echo "make package"
	@echo "       build a .tar.gz package"
	@echo "make clean"
	@echo "       clean up project directories"
	@echo "make docker"
	@echo "       build a docker container"

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

build: venv lint

test:
	py.test tests.py

clean:
	rm -rf simple_service.egg-info
	rm -rf dist
	rm -rf simple_service/__pycache__

lint: 
	pylint simple_service	

container:
	docker build -t simple_service .

package: 
	python setup.py sdist
	


