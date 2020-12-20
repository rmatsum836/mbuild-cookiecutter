[//]: # (Badges)
[![Build Status](https://dev.azure.com/rayamatsumoto/mbuild-cookiecutter/_apis/build/status/rmatsum836.mbuild-cookiecutter?branchName=refs%2Fpull%2F6%2Fmerge)](https://dev.azure.com/rayamatsumoto/mbuild-cookiecutter/_build/latest?definitionId=4&branchName=refs%2Fpull%2F6%2Fmerge)

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

With `cookiecutter` installed, execute the following command inside the
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
added in `mbuild_{{cookiecutter.directory_name}}/tests/` are to check that the cookiecutter package
has been successfully integrated with mBuild recipes via entrypoints.  

Additional tests can be added to the `project/tests/` folder.  Any
function starting with `test_*` will be automatically included into
the testing framework.

To run the suite of unit tests, type `pytest -v` on the command line.

## Continuous Integration

Continuous integration is done with
[Azure](https://azure.microsoft.com/en-us/services/devops/) for both Linux and MacOS testing.
Azure DevOps is free for open source projects and allows you to test and
verify that your mBuild recipe works with various OS and Python
versions.

Currently, continuous integration is setup to test Linux and MacOS
builds for Python versions 3.7 and 3.8.  The build instructions are
contained in `azure-pipelines.yml` and is designed to work out of the box.
However, you may have to edit the instructions to include any new
dependencies.

## Using `entry points` with mBuild

To connect your mBuild recipe to mBuild, the first step is to install your recipe locally by running
`pip install -e .` in the project root directory.  You can test that your recipe classes are
recognized by mBuild by running the following list of commands:

```
python
import mbuild
mbuild.recipes.name_of_your_plugin()
```

## Docker Image
mBuild recipes using the cookiecutter template can be built using the provided docker image.  To
run the docker image, simply execute the following command `docker run -it
rmatsum/mbuild-cookiecutter:latest` which will pull the most recent docker image from Docker Hub.
Running this image will drop you into the `software` directory which contains the installed
`mbuild-cookiecutter` package.  From there, the instructions in the `Usage` section can be
followed to build the mBuild recipe.
