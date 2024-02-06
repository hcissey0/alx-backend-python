#!/usr/bin/env python3
"""This is the client test file"""

from client import GithubOrgClient
import fixtures
from parameterized import parameterized, parameterized_class
from requests import HTTPError
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

    @mock.patch('client.get_json', return_value=[{"name": "r1"}, {"name": "r2"}])
    def test_public_repos(self, mock_get_json: mock.PropertyMock):
        """tester for public_repos

        Args:
            mock_public_repos_url (mock.Mock): The _public_repos_url mock
            mock_get_json (mock.Mock): The get_json mock
        """
        with mock.patch.object(GithubOrgClient,
                               '_public_repos_url',
                               new_callable=mock.PropertyMock,
                               return_value="https://api.github.com/orgs/org_name/repos") as mock_public_repos_url:

            test_class = GithubOrgClient('org_name')
            self.assertEqual(test_class.public_repos(), ['r1', 'r2'])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: str, license_key: str, expected_output: bool):
        """_summary_

        Args:
            repo (str): _description_
            license_key (str): _description_
            expected_output (bool): _description_
        """
        test_class = GithubOrgClient('org_name')
        self.assertEqual(test_class.has_license(repo, license_key), expected_output)


@parameterized_class([
    {
        "org_payload": fixtures.TEST_PAYLOAD[0][0],
        "repos_payload": fixtures.TEST_PAYLOAD[0][1],
        "expected_repos": fixtures.TEST_PAYLOAD[0][2],
        "apache2_repos": fixtures.TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestCase class for the public_repos

    Args:
        unittest (_type_): _description_
    """

    @classmethod
    def setUpClass(cls):
        """Setting up the class
        """

        def side_effect(url: str) -> mock.Mock:
            """The side effect of the mocking

            Args:
                url (str): the url of the repo

            Returns:
                mock.Mock: The returned mock
            """
            payloads = {
                'https://api.github.com/orgs/google': cls.org_payload,
                'https://api.github.com/orgs/google/repos': cls.repos_payload
            }
            if url in payloads:
                return mock.Mock(**{'json.return_value': payloads[url]})
            return HTTPError
            # if url.endswith("/google"):
            #     return mock.Mock(json=lambda: cls.org_payload)
            # elif url.endswith("/google/repos"):
            #     return mock.Mock(json=lambda: cls.repos_payload)
            # else:
            #     return mock.Mock(json=lambda: {})
        cls.get_patcher = mock.patch('requests.get', side_effect=side_effect)

        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """The teardown function of the test class
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """This is a tester for the public_repos function
        """
        test_class = GithubOrgClient('google')
        self.assertEqual(test_class.public_repos(), self.expected_repos)

    def test_repos_with_license(self):
        """Test case for repos with license
        """
        test_class = GithubOrgClient('google')
        self.assertEqual(test_class.public_repos(license='apache-2.0'), self.apache2_repos)
