variables = {
    'APP_NAME',
    'AUTHOR',
    'AUTHOR_EMAIL',
    'DESCRIPTION',
    'REPO_NAME',
    'ORG_NAME',
    'VERSION'
}

generators = {
    'python': {
        'Makefile':
        """
        """,
        'setup.py':
        """

        """,
        'constants.py':
        """
        APP_NAME = '${APP_NAME}'
        AUTHOR = '${AUTHOR}'
        AUTHOR_EMAIL = '${AUTHOR_EMAIL}'
        DESCRIPTION = '${DESCRIPTION}'
        REPO_NAME = '${REPO_NAME}'
        ORG_NAME = '${ORG_NAME}'
        VERSION = '${VERSION}'
        """,
        'tests/__init__.py': '',
        '${APP_NAME}/__init__.py': '',
        '${APP_NAME}/settings.py': ''
    }
}
generators['django'] = deepcopy(generators['python'])
generators['django']['tests/__init__.py'] =
"""
"""

def generate(**options):
    for file_name, file_contents in files.iteritems():
        pass

