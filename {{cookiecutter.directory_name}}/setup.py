"""
{{cookiecutter.project_name}}
{{cookiecutter.description}}
"""

from setuptools import setup

short_description = __doc__.split("\n")

setup(
    # Self-descriptive entries which should always be present
    name='{{cookiecutter.directory_name}}',
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    license='{{cookiecutter.open_source_license}}',
    version=0.0.0,
    description=short_description[0],
    zip_safe=False,
    entry_points={
        'mbuild.plugins':[
        "FILL IN LATER"
        ]
        }
    )
