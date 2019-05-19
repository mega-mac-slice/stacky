.PHONY: clean dist

install:
	@pipenv install --three -e .[dev]

lint:
	@pipenv run pycodestyle stacky tests setup.py

test: lint
	@pipenv run tox

it: install
	@pushd it && make install && make test && popd

bumpversion-patch:
	@pipenv run bumpversion patch setup.py

dist:
	@pipenv run python setup.py sdist && ls dist/* | xargs -I {} shasum -a 256 {}

clean:
	@pipenv --rm
	@rm -rf stacky.egg-info .eggs .tox Pipfile*

