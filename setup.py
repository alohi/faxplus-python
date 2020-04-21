# coding: utf-8

"""
    FAX.PLUS REST API

    OpenAPI spec version: 1.2.0
    Contact: info@fax.plus
"""

from setuptools import setup, find_packages  # noqa: H301
from os import path
import re

NAME = "faxplus-api"
VERSION = "1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
long_description = re.sub(r'### Documentation for API Endpoints.*#', '#', long_description, flags=re.S)
long_description = re.sub(r'### Documentation For Models.*#', '#', long_description, flags=re.S)

setup(
    name=NAME,
    version=VERSION,
    description="FAX.PLUS REST API",
    author="Alohi SA",
    author_email="info@fax.plus",
    url="https://github.com/alohi/faxplus-python",
    keywords=["Swagger", "FAX.PLUS REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
