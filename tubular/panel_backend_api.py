import requests


RETIREMENT_ENDPOINT = '/api/v1/retirement/'


class PanelBackendAPI():
    """
    Panel Backend API to retire user data.
    """

    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.auth_token = auth_token

    def retire_user(self, learner):
        """
        Retires the user with the given username in the Edly Panel Backend.
        """

        url = '{}{}'.format(self.base_url, RETIREMENT_ENDPOINT)
        headers = {'Authorization': 'Token {}'.format(self.auth_token)}
        data = {'username': learner['original_username']}

        response = requests.post(url, data=data, headers=headers)
        response.raise_for_status()
        return response
