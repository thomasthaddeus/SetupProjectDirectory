import requests

class LicenseCreator:
    def __init__(self, config):
        self.config = config

    def create_license(self):
        """
        Fetches and creates a LICENSE file based on the license specified in the config file.

        Sends an HTTP request to fetch the text of the specified license from
        'https://choosealicense.com', and writes the license text to a LICENSE
        file in the project directory.
        """
        license_name = self.config['Settings']['License']
        # Update the URL to fetch the raw text of the license
        url = f'https://raw.githubusercontent.com/github/choosealicense.com/gh-pages/_licenses/{license_name.lower()}.txt'
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            with open(file='LICENSE', mode='w', encoding='utf-8') as file:
                file.write(response.text)  # Corrected attribute access to response.text
        else:
            print(f'Failed to fetch license. HTTP Status Code: {response.status_code}')

# Example usage:
config = {
    'Settings': {
        'License': 'MIT'
    }
}
# license_creator = LicenseCreator(config)
