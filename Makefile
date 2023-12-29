all: default

clean: clean-output clean-test

clean-output: 

clean-test: 

deps:
	pip install -r requirements.txt

dev_deps:
	pip install -r requirements-dev.txt

check-format: dev_deps
	yapf -rd ./

format: dev_deps
	yapf -ri ./

lint: check-format
	pylint -r n ./

lint-no-error: 
	pylint --exit-zero -r n ./

test: build dev_deps
	python3 -m pytest -v --durations=0 --cov=./ --cov-report html

build: deps
	# might re-add clean 
