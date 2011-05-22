COVERAGE="bin/nosetests --with-coverage --cover-package=markdown_processor"

clean:
	-rm -rf build
	-rm -rf dist
	-rm -rf target_dir/*

coverage: clean
	bin/nosetests --with-coverage --cover-package=markdown_processor tests/unit
	-rm .coverage

dist: clean
	bin/python setup.py build sdist

requirements: virtualenv
	bin/pip install -r requirements.pip
	-rm README.txt # Left by Dingus installation

tdd:
	bin/nosyd -1

virtualenv:
	virtualenv --no-site-packages --distribute --python=python2.7 .

web_server:
	PYTHONPATH=. bin/python lifefeeder/web/app.py

worker:
	PYTHONPATH=. bin/python lifefeeder/workers/worker.py
