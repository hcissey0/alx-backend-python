#!/usr/bin/env python3
"""This is the utils test file"""

from parameterized import parameterized
from typing import Mapping, Sequence, Any, Callable
import unittest
from unittest import mock
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """This is the unittest for the access_nested_map function

    Args:
        unittest.TestCase (class): The unittest module
    """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected_result: Any) -> None:
        """This is the test function for the access_nested_map function

        Args:
            nested_map (Mapping): The nested map to test
            path (Sequence): The sequence of the keys to check
            expected_result (Any): The expected results
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ('a',), "keyError: 'a'"),
        ({"a": 1}, ('a', 'b'), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected_message: Any) -> None:
        """This is another test case for the access_nested_map function

        Args:
            nested_map (Mapping): The mapping
            path (Sequence): The keys to test
            expected_result (Any): The expected result
        """
        with self.assertRaises(KeyError) as cont:
            c_map = nested_map
            for k in path:
                c_map = nested_map[k]
            self.assertEqual(str(cont.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """This the test cases for the get_json function

    Args:
        unittest.TestCase (class): The unittest class
    """

    @mock.patch('utils.requests.get')
    def test_get_json(self, mock_requests_get: Any) -> None:
        """The test for the get json

        Args:
            mock_json_loads (Callable): The mock json.loads()
            mock_requests_get (Callable): The mock requests.get()
        """
        test_input = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]

        for test_url, test_payload in test_input:
            mock_response = mock.Mock()
            mock_response.json.return_value = test_payload
            mock_requests_get.return_value = mock_response

            result = get_json(test_url)

            mock_requests_get.assert_called_once_with(test_url)
            mock_requests_get.call_count = 0

            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """This is the memoize class' test cases

    Args:
        unittest.TestCase (class): This is the test case class
    """

    def test_memoize(self):
        """This is the memoize test function
        """
        pass
