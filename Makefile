################## BOILER PLATE CHECKS ##########

# Guard against running Make commands outside a virtualenv or conda env
venv:
ifndef VIRTUAL_ENV
ifndef CONDA_PREFIX
$(error VIRTUAL / CONDA ENV is not set - please activate environment)
endif
endif

############### PUBLIC API #############

all: deps

test:
	GI_ENV=TEST python setup.py pytest

deps: venv
	@echo "Installing Dependencies"
	pip install -U setuptools
	pip install -e . --force-reinstall

clean:
	find . -name "*.pyc" -exec rm {} +

#######################################
