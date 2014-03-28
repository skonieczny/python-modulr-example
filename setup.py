import os
from setuptools import setup, find_packages

root = os.path.abspath(os.path.dirname(__file__))

setup(
    name='modulr-example',
    version='0.0.1.dev',
    description='Example modular, plugginable application. ',
    author='Stanislaw Skonieczny',
    author_email='stanislaw.skonieczny@gmail.com',
    url='https://github.com/stanislaw-skonieczny/python-modulr-example',
    packages=['awesome_game'],
    package_dir={'': 'src'},
    install_requires=['modulr'],
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
)
