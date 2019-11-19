# Cookiecutter for mBuild recipes

A [cookiecutter](https://github.com/audreyr/cookiecutter) template for developing a Python
package for [mBuild](https://github.com/mosdef-hub/mbuild) recipes.
Based on the [MolSSI](https://github.com/MolSSI/cookiecutter-cms)
Cookiecutter.

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
cookiecutter /path/to/mbuild-cookiecutter/
```

From here, the user will be prompted for information on how to build
the directory such as package name, module name, and authors.

## Testing

Unit testing with [pytest](https://pytest.org) has been integrated
within this cookiecutter.  This testing framework is used 
in [mBuild](https://github.com/mosdef-hub/mbuild).  The default tests
added in `{{cookiecutter.directory_name}}/tests/` are to check that the cookiecutter package
has been successfully integrated with mBuild recipes via entrypoints.  

Additional tests can be added to the `project/tests/` folder.  Any
function starting with `test_*` will be automatically included into
the testing framework.

To run the suite of unit tests, type `pytest -v` on the command line.

## Continuous Integration

Continuous integration is done with
[Travis-CI](https://travis-ci.org) for both Linux and MacOS testing.
Travis-CI is free for open source projects and allows you to test and
verify that your mBuild recipe works with various OS and Python
versions.

Currently, continuous integration is setup to test Linux and MacOS
builds for Python versions 3.6 and 3.7.  The build instructions are
contained in `.travis.yml` and is designed to work out of the box.
However, you may have to edit the instructions to include any new
dependencies.
