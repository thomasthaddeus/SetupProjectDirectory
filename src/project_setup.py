"""project_setup.py
A utility script to set up Python projects with essential configurations and
files.

This script provides a class `ProjectSetup` that automates the creation of key
project files such as `requirements.txt`, a virtual environment, `.pylintrc`,
and `LICENSE`, based on configurations specified in a `config.ini` file. It
also provides a method to execute a git setup script, facilitating a
streamlined setup process for new projects.

Ex. Usage:
setup = ProjectSetup()
setup.create_requirements()
setup.create_venv()
setup.create_pylintrc()
setup.create_license()
setup.execute_git_setup()
"""

import os
import configparser
import subprocess
import requests

class ProjectSetup:
    """
    A class to automate the setup of key project configurations and files.

    The class reads configurations from a specified `config.ini` file and
    provides methods to create a `requirements.txt` file, a virtual
    environment, a `.pylintrc` file, and a `LICENSE` file. It also provides a
    method to execute a git setup script.
    """
    def __init__(self, config_path='config/conf.ini'):
        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def create_requirements(self):
        """
        Creates a requirements.txt file from the dependencies listed in the config file.

        Reads the [Dependencies] section from the config file and writes each
        dependency and its specified version to a new line in the requirements.
        txt file.
        """
        with open(file='requirements.txt', mode='w', encoding='utf-8') as file:
            for item in self.config['Dependencies']:
                file.write(f'{item}=={self.config["Dependencies"][item]}\n')

    def create_venv(self):
        """
        Creates a virtual environment in the project directory.

        Executes the command to create a new virtual environment named 'venv'
        in the project directory.
        """
        subprocess.run(["python", "-m", "venv", ".venv"], check=True)

    def create_pylintrc(self):
        """
        Generates a .pylintrc configuration file using Pylint's default
        settings.

        Executes the command to generate a .pylintrc file with Pylint's default
        configuration settings.
        """
        subprocess.run(['pylint', '--generate-rcfile'], check=True, stdout=open(file='.pylintrc', mode='w', encoding='utf-8'))

    # def create_license(self):
    #     """
    #     Fetches and creates a LICENSE file based on the license specified in the config file.

    #     Sends an HTTP request to fetch the text of the specified license from
    #     'https://choosealicense.com', and writes the license text to a LICENSE
    #     file in the project directory.
    #     """
    #     license_name = self.config['Settings']['License']
    #     url = f'https://github.com/github/choosealicense.com/tree/gh-pages/_licenses/{license_name.lower()}/#'
    #     response = requests.get(url, timeout=30)
    #     if response.status_code == 200:
    #         with open(file='LICENSE', mode='w', encoding='utf-8') as file:
    #             file.write(response.txt)
    #     else:
    #         print(f'Failed to fetch license. HTTP Status Code: {response.status_code}')

    def execute_git_setup_shell(self):
        """
        Executes a git setup shell script specified in the project's script directory.

        Attempts to execute the 'setup_git.sh' script located in the 'scripts'
        directory to perform git setup tasks.
        """
        try:
            subprocess.check_call(["../scripts/setup_git.sh"])
            print("Git setup (shell) completed successfully!")
        except subprocess.CalledProcessError:
            print("Error occurred while setting up git using shell script.")

    def execute_git_setup_powershell(self):
        """
        Executes a git setup PowerShell script specified in the project's script directory.

        Attempts to execute the 'setup_git.ps1' script located in the 'scripts'
        directory to perform git setup tasks.
        """
        try:
            subprocess.check_call(["powershell", "-ExecutionPolicy", "Unrestricted", "../scripts/setup_git.ps1"])
            print("Git setup (PowerShell) completed successfully!")
        except subprocess.CalledProcessError:
            print("Error occurred while setting up git using PowerShell script.")

    def execute_git_setup(self):
        """
        Determines the environment and decides which git setup script to run.
        """
        # Check the OS to determine the script to run
        if os.name == 'posix':  # Unix-like OS
            self.execute_git_setup_shell()
        elif os.name == 'nt':  # Windows
            self.execute_git_setup_powershell()
        else:
            print("Unsupported OS.")
