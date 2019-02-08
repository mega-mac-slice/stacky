.PHONY: clean

install:
	@pipenv install --three -e .

test:
	@pipenv run python setup.py test

clean:
	@pipenv --rm
	@rm -r stacky.egg-info

