files = {
    'Makefile':
    """
ORG_NAME := $(grep "ORG_NAME" constants.py | sed -E "s#^\w*[A-Z_]+\w*=\w*['"](.*)['"]$#")
REPO_NAME := $(grep "REPO_NAME" constants.py | sed -E "s#^\w*[A-Z_]+\w*=\w*['"](.*)['"]$#")
APP_NAME := $(grep "APP_NAME" constants.py | sed -E "s#^\w*[A-Z_]+\w*=\w*['"](.*)['"]$#")
INSTALL_PREFIX := /usr/local

INSTALL_DIR  := $(INSTALL_PREFIX)/$(REPO_NAME)/$(APP_NAME)

.PHONY: test

install: $(INSTALL_DIR)
    . $(INSTALL_DIR)/bin/activate; python setup.py install

$(INSTALL_DIR): $(INSTALL_DIR)/bin/activate
$(INSTALL_DIR)/bin/activate: requirements.txt
    test -d $(INSTALL_DIR) || virtualenv $(INSTALL_DIR)
    . $(INSTALL_DIR)/bin/activate; python setup.py install
    touch $(INSTALL_DIR)/bin/activate

clean_working_directory:
    rm -rf ./build ./dist ./$(APP_NAME).egg-info;

clean: clean_working_directory
    rm -rf $(INSTALL_DIR)

test: lint install
    . $(INSTALL_DIR)/bin/activate; \
      python manage.py test --settings=tests.settings

run: install
    . $(INSTALL_DIR)/bin/activate; \
      python manage.py $(CMD) --settings=tests.settings

migrations: install
    . $(INSTALL_DIR)/bin/activate; \
      python manage.py makemigrations --settings=$(APP_NAME).settings

shell: install
    . $(INSTALL_DIR)/bin/activate; \
      python manage.py migrate --settings=tests.settings; \
      python manage.py shell --settings=tests.settings

lint: clean_working_directory
    find . -type f -name '*.py' | xargs flake8

format: clean_working_directory
    find . -type f -name '*.py' | xargs flake8 | sed -E 's/^([^:]*\.py).*/\1/g' | uniq | xargs autopep8 --experimental -a --in-place
""",
    'setup.py':
"""
from setuptools import setup
import codecs
import os
import re
from constants import (
    AUTHOR,
    AUTHOR_EMAIL,
    DESCRIPTION,
    ORG_NAME,
    REPO_NAME,
    PACKAGE_NAME,
    VERSION
)

BASE_DIR = os.path.dirname(__file__) or "."

setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    name=APP_NAME,
    packages=[
        PACKAGE_NAME
    ],
    scripts=['manage.py'],
    url="http://github.com/%s/%s" % (ORG_NAME, APP_NAME),
    version=VERSION,
    install_requires=open("requirements.txt").read().split("\n"),
    test_suite='runtests.runtests'
)

""",
    'constants.py':
"""
APP_NAME = ''
AUTHOR = ''
AUTHOR_EMAIL = ''
DESCRIPTION = ''
REPO_NAME = ''
ORG_NAME = ''
VERSION = ''
""",
    'tests/__init__.py': '',
    '{APP_NAME}/__init__.py': '',
    '{APP_NAME}/settings.py': ''
}

def generate():
    for file_name, data in files.iteritems():
        #

