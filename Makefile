.PHONY: clean

venv:
	@virtualenv venv

install:
	@pip install -e .

clean:
	@rm -r venv stacky.egg-info

pep8:
	@pycodestyle stacky --max-line-length=120

test: pep8
	@python -m unittest discover

freeze:
	@pip freeze > requirements.txt