#!/usr/bin/env python3
"""This is the client test file"""

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest import mock


class TestGithubOrgClient(unittest.TestCase):
    """The GithubOrgClient test case

    Args:
        unittest.TestCase (class): The test case class
    """

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @mock.patch('client.get_json', return_value={"key": "value"})
    def test_org(self, org_name: str, mock_get_json: mock.MagicMock) -> None:
        """The test for he org function

        Args:
            org_name (str): The org name
            mock_get_json (mock.MagicMock): The mock of the get_json function
        """
        test_class = GithubOrgClient(org_name)
        res = test_class.org
        self.assertEqual(res, {"key": "value"})

        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

    @mock.patch.object(GithubOrgClient, 'org', new_callable=mock.PropertyMock)
    def test_public_repos_url(self, mock_org: mock.PropertyMock):
        """Test for the _public_repos_url
        """
        test_payload = {'repos_url': 'https://api.github.com/orgs/org_name/repos'}
        mock_org.return_value = test_payload

        test_class = GithubOrgClient('org_name')
        self.assertEqual(test_class._public_repos_url, 'https://api.github.com/orgs/org_name/repos')
