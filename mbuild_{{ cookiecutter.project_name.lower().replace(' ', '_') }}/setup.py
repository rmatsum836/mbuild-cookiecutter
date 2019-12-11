from setuptools import setup


setup(
    # Self-descriptive entries which should always be present
    name='{{cookiecutter.directory_name}}',
    author='{{cookiecutter.author_name}}',
    author_email='{{cookiecutter.author_email}}',
    license='{{cookiecutter.open_source_license}}',
    version='0.0.0',
    description='{{cookiecutter.description}}',
    zip_safe=False,
    entry_points={
        'mbuild.plugins':[
        "{{cookiecutter.first_plugin_name}} = {{cookiecutter.directory_name}}.{{cookiecutter.first_module_name}}:{{cookiecutter.first_plugin_name}}"
        ]
        }
    )
