all :
	python setup.py install --user 

lint :
	~/.local/bin/pylint -E --output-format=parseable *.py */*.py
