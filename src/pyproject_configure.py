"""
This module provides a class for configuring a pyproject.toml file based on a
specified configuration file.

The PyProjectConfigurer class reads a configuration file (default is config.
ini), extracts metadata and dependencies information, and uses it to generate
or update a pyproject.toml file for a Python project.
"""

import configparser
import toml

class PyProjectConfigurer:
    """
    A class for configuring a pyproject.toml file based on a specified
    configuration file.

    This class reads the specified configuration file to extract project
    metadata and dependencies information. It then generates or updates a
    pyproject.toml file to reflect this information, facilitating the
    management of build system configurations and project dependencies.
    """
    def __init__(self, config_path='../config/conf.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def configure_pyproject_toml(self):
        """
        Configures a pyproject.toml file based on the information in the
        specified configuration file.

        This method reads the project metadata and dependencies from the
        configuration file, constructs the data for pyproject.toml, and writes
        it to the pyproject.toml file.
        """
        metadata = self.config['Metadata']
        dependencies = self.config['Dependencies']

        data = {
            "tool": {
                "poetry": {
                    "name": metadata.get('name', 'Python Repository and Deployment Automator'),
                    "version": metadata.get('version', 'v1.0.0'),
                    "description": metadata.get('description'),
                    "authors": [metadata.get('authors', 'Thaddeus Thomas <thaddeus.r.thomas@gmail.com>')],
                },
                "dependencies": dict(dependencies.items())
            }
        }

        with open(file='pyproject.toml', mode='w', encoding='utf-8') as file:
            toml.dump(data, file)
