# This allows a user to install the project at a later time

try :
    import sys
    from setuptools import setup
except ImportError as e :
    sys.stderr.write('Failure to import setup from setuptools.')
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'author' : 'Brian McEntee',
    'url' : 'URL to get it at',
    'download_url' : 'Where to download it',
    'author_email' : 'Brian.M.McEntee@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'projectname'
}

setup(**config)