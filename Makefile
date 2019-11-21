.PHONY: clean dist
APP_NAME=$(shell ./setup.py --name)
APP_VERSION=$(shell ./setup.py --version)

install:
	@pipenv install --three --pre -e .[dev]

format:
	@pipenv run black setup.py stacky tests it

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

pypi:
	LATEST_DIST=dist/${APP_NAME}-${APP_VERSION}.tar.gz
	twine check ${LATEST_DIST} && twine upload ${LATEST_DIST}

clean:
	@pipenv --rm
	@rm -rf stacky.egg-info .eggs .tox Pipfile*

