import requests
from requests.auth import HTTPBasicAuth


RETIREMENT_ENDPOINT = '/wp-json/edly/v1/retirement'

class WordPressAPI():
    """
    WordPress API to retire user data.
    """

    def __init__(self, wordpress_base_url, wordpress_username, wordpress_app_password):
        self.base_url = wordpress_base_url
        self.username = wordpress_username
        self.password = wordpress_app_password

    def retire_user(self, learner):
        """
        Retires the user with the given username in the WordPress.
        """

        url = "{}{}".format(self.base_url, RETIREMENT_ENDPOINT)
        data = {'username': learner['original_username']}
        response = requests.post(url, data=data, auth=HTTPBasicAuth(self.username, self.password))

        if response.status_code == 200:
            return response
        else:
            raise Exception(response.json()['message'])
