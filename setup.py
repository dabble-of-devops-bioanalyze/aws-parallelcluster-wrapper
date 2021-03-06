#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Jillian Rowe",
    author_email='jillian@dabbleofdevops.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Wrapper around AWS ParallelCluster for common Automation tasks",
    entry_points={
        'console_scripts': [
            'awsp=aws_parallelcluster_wrapper.cli:main',
        ],
    },
    py_modules=['aws_parallelcluster_wrapper'],
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='aws_parallelcluster_wrapper',
    name='aws_parallelcluster_wrapper',
    packages=find_packages(include=['aws_parallelcluster_wrapper', 'aws_parallelcluster_wrapper.*']),
    # packages = find_packages('aws_parallelcluster_wrapper'),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Dabble-of-DevOps-BioHub/aws-parallelcluster-wrapper',
    version='0.1.0',
    zip_safe=False,
)
