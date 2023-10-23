"""main.py
_summary_

_extended_summary_
"""


import os
from src.project_setup import ProjectSetup
from src.project_generator import ProjectGenerator
from src.pyproject_configure import PyProjectConfigurer
from src.readme_generator import READMEGenerator
from src.license_creator import LicenseCreator

def main():
    conf_path = 'config/conf.ini'

    # Validate config file
    if not os.path.exists(conf_path):
        print(f"Error: Config file not found at {conf_path}")
        return

    # Initialize ProjectSetup, Generator, and READMEGenerator
    try:
        project_setup = ProjectSetup(config_path=conf_path)
        generator = ProjectGenerator()
        configurer = PyProjectConfigurer()
        readme_generator = READMEGenerator()
        license_creator = LicenseCreator(config=conf_path)
    except ImportError as err:
        print(f"Error initializing classes: {err}")
        return

    project_setup.create_requirements()
    project_setup.create_venv()
    project_setup.create_pylintrc()
    project_setup.execute_git_setup()
    generator.generate_gitignore(['Python', 'Node'])
    generator.execute_script('scripts/*')

    # Execute methods to set up project, generate files, etc.
    try:
        configurer.configure_pyproject_toml()
        generator.generate_gitignore(['Python'])  # Assuming a Python project
        readme_generator.generate_readme()
        license_creator.create_license()
    except GeneratorExit as err:
        print(f"Error generating project files: {err}")

    configurer = PyProjectConfigurer()
    configurer.configure_pyproject_toml()


if __name__ == "__main__":
    main()
