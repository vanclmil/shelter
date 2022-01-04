
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from shelter import __version__ as VERSION


class PyTest(TestCommand):

    user_options = [
        ('pytest-args=', 'a', "Arguments to pass to py.test"),
    ]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


description = (
    "Simple Python's Tornado wrapper which provides helpers for creation"
    "a new project, writing management commands, service processes, ..."
)

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = description

setup(
    name="shelter",
    version=VERSION,
    author='Jan Seifert (Seznam.cz, a.s.)',
    author_email="jan.seifert@firma.seznam.cz",
    description=description,
    long_description=long_description,
    license="BSD",
    url='https://github.com/seznam/shelter',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    packages=find_packages(include=['shelter*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'tornado>=4.5',
        'setproctitle>=1.1',
    ],
    tests_require=[
        'pytest-cov',
        'pytest',
    ],
    test_suite='tests',
    cmdclass={
        'test': PyTest,
    },
    entry_points={
        'console_scripts': [
            'shelter-admin = shelter.main:main',
        ]
    },
)
