[//]: # (Badges)
[![Build Status](https://travis-ci.com/rmatsum836/mbuild-cookiecutter.svg?branch=master)](https://travis-ci.com/rmatsum836/mbuild-cookiecutter)

# Cookiecutter for mBuild recipes

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for developing a Python
package for [mBuild](https://github.com/mosdef-hub/mbuild) recipes.

## Features
* Pre-configured `setup.py` for installation and packaging which automatically registers with the ``entry_point`` group defined in mBuild
* Pre-configured Linux and OSX continuous integration on Travis-CI
* Basic testing with [PyTest](https://docs.pytest.org/en/latest/)
* Sample example directory

## Requirements

* Python 3.6 or later
* [Cookiecutter](http://cookiecutter.readthedocs.io/en/latest/installation.html)

## Usage

With `cookicutter` installed, execute the following command inside the
folder you want to create your skeletal mBuild recipe directory.

```
cookiecutter mbuild-cookiecutter
```

From here, the user will be prompted for information on how to build
the directory such as package name, module name, and authors.
