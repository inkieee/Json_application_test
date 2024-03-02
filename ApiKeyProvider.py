class ApiKeyProvider:
    """
    Class to read and provide the API key.
    """
    def __init__(self, api_key_file="api_key.conf"):
        """
        Initializes the provider with the API key file path.

        Args:
                api_key_file (str): Path to the file containing the API key. 
        """
        with open(api_key_file, "r") as file:
            file_content = file.read()
            self.api_key = file_content.split("=")[1].strip()

    def get_api_key(self):
        """
        Returns the stored API key.

        Returns:
                str: The API key from the file.
        """
        return self.api_key