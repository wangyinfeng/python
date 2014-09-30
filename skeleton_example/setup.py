try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'skeleton example from LPTHW ex46',
    'author': 'author of LPTHW',
    'url': 'http://learnpythonthehardway.org/book/ex46.html.',
    'download_url': 'http://learnpythonthehardway.org/book/ex46.html.',
    'author_email': 'Learning python the hard way',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['skeleton example'],
    'scripts': [],
    'name': 'skeleton_example'
}

setup(**config)
