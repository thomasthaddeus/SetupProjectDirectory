"""readme_generator.py
A script to generate a README.md file for a repository.

This script extracts information such as project description, dependencies,
and license from the repository, and writes them into a README.md file. It
also checks for common directory structures like tests, scripts, data, and
configurations, and notes them in the README.md file.

Returns:
    None: The script writes the README.md file to the repository directory.

Ex. Usage:
generator = READMEGenerator()
generator.generate_readme()
"""

import os

class READMEGenerator:
    """
    A class to generate a README.md file for a repository.

    This class contains methods to extract information from the repository
    and write them into a README.md file. The information includes project
    description, dependencies, license, and common directory structures.
    """
    def __init__(self, repo_path='.'):
        self.repo_path = repo_path

    def extract_description(self):
        """
        Extracts the project description from Python files.

        This method looks for the first docstring in Python files found
        in the repository to use as the project description.

        Returns:
            str: The extracted project description, or an empty string if not found.
        """
        description = ''
        for root, dirs, files in os.walk(self.repo_path):
            for file in files:
                if file.endswith('.py'):
                    with open(os.path.join(root, file), mode='r', encoding='utf-8') as f:
                        lines = f.readlines()
                    for line in lines:
                        if line.startswith('"""') or line.startswith("'''"):
                            description = line.strip('"""').strip("'''").strip()
                            break
                    if description:
                        break
        return description

    def extract_dependencies(self):
        """
        Extracts the list of dependencies from a requirements.txt file.

        This method reads the requirements.txt file from the repository,
        if it exists, to get the list of project dependencies.

        Returns:
            list: A list of dependencies, or an empty list if requirements.txt is not found.
        """
        dependencies = []
        req_file_path = os.path.join(self.repo_path, 'requirements.txt')
        if os.path.exists(req_file_path):
            with open(req_file_path, mode='r', encoding='utf-8') as f:
                dependencies = [line.strip() for line in f.readlines()]
        return dependencies

    def extract_license(self):
        """
        Extracts the license text from a LICENSE file.

        This method reads the LICENSE file from the repository, if it exists,
        to get the license text.

        Returns:
            str: The license text, or an empty string if LICENSE file is not found.
        """
        license_text = ''
        license_file_path = os.path.join(self.repo_path, 'LICENSE')
        if os.path.exists(license_file_path):
            with open(license_file_path, mode='r', encoding='utf-8') as f:
                license_text = f.read()
        return license_text

    def check_for_tests(self):
        """
        Checks for the existence of a tests directory.

        This method checks whether a directory named 'tests' exists in the repository.

        Returns:
            bool: True if 'tests' directory exists, False otherwise.
        """
        test_dir_path = os.path.join(self.repo_path, 'tests')
        return os.path.exists(test_dir_path)

    def check_for_scripts(self):
        """
        Checks for the existence of a scripts directory.

        This method checks whether a directory named 'scripts' exists in the repository.

        Returns:
            bool: True if 'scripts' directory exists, False otherwise.
        """
        script_dir_path = os.path.join(self.repo_path, 'scripts')
        return os.path.exists(script_dir_path)

    def check_for_data(self):
        """
        Checks for the existence of a data directory.

        This method checks whether a directory named 'data' exists in the repository.

        Returns:
            bool: True if 'data' directory exists, False otherwise.
        """
        data_dir_path = os.path.join(self.repo_path, 'data')
        return os.path.exists(data_dir_path)

    def check_for_config(self):
        """
        Checks for the existence of a config/conf.ini file.

        This method checks whether a file named 'conf.ini' exists in the 'config' directory
        of the repository.

        Returns:
            bool: True if 'config/conf.ini' file exists, False otherwise.
        """
        config_file_path = os.path.join(self.repo_path, 'config', 'conf.ini')
        return os.path.exists(config_file_path)

    def generate_readme(self):
        """
        Generates a README.md file for the repository.

        This method creates a README.md file in the repository root, and
        populates it with information extracted from the repository, including
        project description, dependencies, license, and common directory
        structures.
        """
        project_title = os.path.basename(self.repo_path)
        description = self.extract_description()
        dependencies = self.extract_dependencies()
        license_text = self.extract_license()
        tests_exist = self.check_for_tests()
        scripts_exist = self.check_for_scripts()
        data_exist = self.check_for_data()
        config_exist = self.check_for_config()
        with open(os.path.join(self.repo_path, 'README.md'), mode='w', encoding='utf-8') as f:
            f.write(f'# {project_title}\n\n')
            f.write(f'{description}\n\n')
            if dependencies:
                f.write('## Dependencies\n\n')
                f.write('\n'.join(dependencies) + '\n\n')
            if license_text:
                f.write('## License\n\n')
                f.write(f'```\n{license_text}\n```')

        with open(os.path.join(self.repo_path, 'README.md'), mode='w', encoding='utf-8') as f:
            f.write(f'# {project_title}\n\n')
            f.write(f'{description}\n\n')

            if dependencies:
                f.write('## Dependencies\n\n')
                f.write('\n'.join(dependencies) + '\n\n')

            f.write('## Project Structure\n\n')
            if tests_exist:
                f.write('- `tests/`: Directory containing test files\n')
            if scripts_exist:
                f.write('- `scripts/`: Directory containing script files\n')
            if data_exist:
                f.write('- `data/`: Directory containing data files\n')
            if config_exist:
                f.write('- `config/conf.ini`: Configuration file\n')

            if license_text:
                f.write('## License\n\n')
                f.write(f'```\n{license_text}\n```')
