.PHONY: clean

venv:
	@virtualenv -p python3 .venv

install:
	@source .venv/bin/activate && pip install -e .

clean:
	@rm -r .venv stacky.egg-info

pep8:
	@pycodestyle stacky --max-line-length=120

test: pep8
	source .venv/bin/activate && python -m unittest discover

freeze:
	source .venv/bin/activate && pip freeze > requirements.txt