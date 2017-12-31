
venv: 
	python3 -m venv .venv
	.venv/bin/pip3 install wheel
	
dev: venv
	.venv/bin/pip3 install -r requirements-dev.txt
#	.venv/bin/pip3 install -r requirements.txt
	.venv/bin/pip3 install -e .

clean: cov-clean
	rm -rf .venv cowdict.egg-info

test:
	.venv/bin/pytest cowdict/tests -vv

cov: cov-clean
	.venv/bin/pytest --cov cowdict --cov-report=term --cov-report=html cowdict/tests

cov-clean:
	rm -rf htmlcov		