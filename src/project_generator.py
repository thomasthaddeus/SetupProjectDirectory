"""project_generator.py

This module provides a class for generating and configuring project files.

The ProjectGenerator class simplifies the creation and configuration of project
files such as .gitignore. It can fetch template files from a remote repository,
generate a .gitignore file based on specified templates, and execute scripts
to further configure or setup the project environment.

# Ex. Usage:
# generator = Generator()
# generator.generate_gitignore(['Python', 'Node'])
# generator.execute_script('scripts/*')
"""

import os
import subprocess
import requests


class ProjectGenerator:
    """
    A class for generating project setup files and executing scripts.

    This class provides methods for fetching .gitignore templates from a remote
    repository, generating a .gitignore file from specified templates, and
    executing shell scripts. It can be used to automate the setup and
    management of a project repository.
    """

    def __init__(self, templates_dir="gitignore_templates"):
        """
        Initializes a new instance of the ProjectGenerator class.

        This constructor creates a new ProjectGenerator instance and ensures the
        existence of a directory for storing .gitignore templates.

        Args:
            templates_dir (str): The path of the directory where .gitignore
            templates will be stored.
        """
        self.templates_dir = templates_dir
        if not os.path.exists(templates_dir):
            os.mkdir(templates_dir)

    def fetch_template(self, template_name):
        """
        Fetches a .gitignore template from a remote repository.

        This method sends an HTTP request to fetch a specified .gitignore
        template from GitHub's collection of .gitignore templates, and saves
        the template to a local file.

        Args:
            template_name (str): The name of the .gitignore template to fetch.
        """
        url = f"https://raw.githubusercontent.com/github/gitignore/main/{template_name}.gitignore"
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"{self.templates_dir}/{template_name}.gitignore", mode="w", encoding='utf-8') as file:
                file.write(response.text)
        else:
            print(
                f"Failed to fetch {template_name} template. HTTP Status Code: {response.status_code}"
            )

    def generate_gitignore(self, template_names):
        """
        Generates a .gitignore file based on specified templates.

        This method creates a .gitignore file for the project by concatenating
        the contents of the specified template files. If a template is not found
        locally, it fetches the template from a remote repository.

        Args:
            template_names (list): A list of template names to be used for generating the .gitignore file.
        """
        with open(file=".gitignore", mode="w", encoding="utf-8") as gitignore_file:
            for template_name in template_names:
                template_path = f"{self.templates_dir}/{template_name}.gitignore"
                if not os.path.exists(template_path):
                    self.fetch_template(template_name)
                with open(file=template_path, mode="r", encoding='utf-8') as template_file:
                    gitignore_file.write(template_file.read())
                    gitignore_file.write("\n")

    def execute_script(self, script_path):
        """
        Executes a specified script using the bash shell.

        This method runs the specified script file in a bash shell, capturing
        and displaying the output. It is useful for executing setup scripts or
        other bash scripts required for project configuration.

        Args:
            script_path (str): The path to the script to be executed.
        """
        result = subprocess.run(["bash", script_path], capture_output=True, text=True, check=True)
        if result.returncode == 0:
            print(f"Success: {result.stdout}")
        else:
            print(f"Error: {result.stderr}")
