#!/usr/bin/env python

"""The setup script."""

import os

from setuptools import setup, find_packages
from setuptools.command.install import install


BASEPATH = ".corporate_design_handler"

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "matplotlib >= 3",
    "dynaconf >= 3",
]

test_requirements = [
    "pytest >= 6",
    "numpy >= 1",
    "tox >= 3.24",
    "flake8 >= 4",
    "black >= 21.12b0",
    "mypy >= 0.91",
    "twine >= 3.7"
]

extras = {
    "test": test_requirements,
}


class InstallSetup(install):
    def run(self):
        self.create_corporate_design_handler_path()
        install.run(self)

    @staticmethod
    def create_corporate_design_handler_path():
        corporate_design_handler_path = os.path.join(
            os.path.expanduser("~"), BASEPATH)

        if not os.path.isdir(corporate_design_handler_path):
            os.mkdir(corporate_design_handler_path)


setup(
    author="Kilian Helfenbein",
    author_email="kilian.helfenbein@rl-institut.de",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.1ß",
    ],
    description=("Corporate design handler to generate color maps for plotting"
                 " with python."),
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="corporate_design_handler",
    name="corporate_design_handler",
    package_dir={"corporate_design_handler": "corporate_design_handler"},
    packages=find_packages(
        include=["corporate_design_handler", "corporate_design_handler.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    extras_require=extras,
    url="https://github.com/khelfen/corporate_design_handler",
    version="0.1.0",
    zip_safe=False,
)
