#!/usr/bin/env python3

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name='colorinche',
    version='0.0.2',
    author='Felipe Lerena',
    author_email='felipelerena@gmail.com',
    packages=['colorinche'],
    include_package_data=True,
    scripts=[],
    url='http://pypi.python.org/pypi/colorinche/',
    license='LICENSE.txt',
    description='Lets you use Jinja2 to generate output for the console.',
    long_description="",
    install_requires=["Jinja2", "blessings"],
)
