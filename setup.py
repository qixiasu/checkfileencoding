#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from checkfileencoding.filefunc.version import version
with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['cchardet','rich']

test_requirements = ['cchardet','rich']

setup(
    author="QinXuan",
    author_email='qin__xuan@yeah.net',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="check file encoding",
    entry_points={
        'console_scripts': [
            'cfc=checkfileencoding.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='checkfileencoding',
    name='checkfileencoding',
    packages=find_packages(include=['checkfileencoding', 'checkfileencoding.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/qinxian1989/checkfileencoding',
    version=version,
    zip_safe=False,
)
