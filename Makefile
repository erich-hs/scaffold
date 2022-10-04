# Install and upgrade pip
# Install required packages
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

# Code formatting with python black		
format:
	black *.py

# Disable extra-verbose leaving only warning and error messages
lint:
	pylint --disable=R,C hello.py

# Pytest 3rd-party library with --vv verbose and --cov coverage runing test code
test:
	python -m pytest -vv --cov=hello test_hello.py