.PHONY: clean

venv:
	pipenv install --three

install:
	pipenv install -e .

clean:
	@rm -r stacky.egg-info

pep8:
	@pycodestyle stacky --max-line-length=120
