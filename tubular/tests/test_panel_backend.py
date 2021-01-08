from unittest import TestCase

import mock

from tubular.panel_backend_api import PanelBackendAPI


class PanelBackendAPITests(TestCase):
    """
    Unit tests for Panel Backend.
    """

    def setUp(self):
        """
        Setup data for test cases.
        """
        self.base_url = 'https://example.com'
        self.auth_token = 'token'

    def test_api_with_valid_response(self):
        """
        Test that api endpoint.
        """
        with mock.patch('tubular.panel_backend_api.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            response = PanelBackendAPI.retire_user(self, learner={'original_username': 'test'})

        assert response.status_code == 200

    def test_api_with_invalid_response(self):
        """
        Test that api endpoint with invalid response.
        """
        with mock.patch('tubular.panel_backend_api.requests.post') as mock_post:
            mock_post.return_value.status_code = 400
            response = PanelBackendAPI.retire_user(self, learner={'original_username': 'test'})

        assert response.status_code == 400
