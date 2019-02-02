all: install

clean:
	rm dist/*.whl dist/*.zip

dist-build:
	./setup.py sdist bdist_wheel

dist-push:
	twine upload dist/*.whl dist/*.zip

install:
	pip install --ignore-installed -r requirements.txt .

install-dev:
	pip install --ignore-installed -r requirements.txt -e .

install-user:
	pip install --ignore-installed --user .

test:
	./testrunner.sh

uninstall:
	pip uninstall --yes fb-reporter

.PHONY: all clean dist-build dist-push install install-dev install-user test uninstall