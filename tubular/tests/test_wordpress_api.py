from unittest import TestCase

import mock

from tubular.wordpress_api import WordPressAPI


class WordPressAPITests(TestCase):

  def setUp(self):
    self.base_url = 'https://example.com'
    self.username = 'tubularworker'
    self.password = 'password'


  def test_retire_user(self):
        with mock.patch('tubular.wordpress_api.requests.post') as mock_post:
            mock_post.return_value.status_code = 200
            response = WordPressAPI.retire_user(self, learner={'original_username': 'test'})

        assert response.status_code == 200
