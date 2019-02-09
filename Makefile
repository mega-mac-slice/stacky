.PHONY: clean dist

install:
	@pipenv install --three -e .[dev]

lint:
	@pipenv run pycodestyle stacky tests

test: lint
	@pipenv run tox

dist:
	tar -cvzf dist/stacky.tar.gz stacky/*.py setup.py requirements.txt README.md

clean:
	@pipenv --rm
	@rm -rf stacky.egg-info .eggs dist/*

