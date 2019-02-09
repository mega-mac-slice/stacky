.PHONY: clean

install:
	@pipenv install --three -e .

test:
	@pipenv run python setup.py test

dist:
	tar -cvzf dist/stacky.tar.gz stacky/*.py setup.py requirements.txt

clean:
	@pipenv --rm
	@rm -rf stacky.egg-info .eggs dist/*

