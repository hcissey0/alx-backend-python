#!/usr/bin/env python3
"""This is the client test file"""

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
        pass
