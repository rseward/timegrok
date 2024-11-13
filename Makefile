install:
	pip install .

lint:
	cd src
	ruff check --verbose
