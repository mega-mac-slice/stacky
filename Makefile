.PHONY: clean dist

install:
	@pipenv install --three -e .[dev]

lint:
	@pipenv run pycodestyle stacky tests setup.py

test: lint
	@pipenv run tox

bumpversion-patch:
	@pipenv run bumpversion patch setup.py

dist:
	@pipenv run python setup.py sdist

clean:
	@pipenv --rm
	@rm -rf stacky.egg-info .eggs dist/*

