#!/usr/bin/env python3
"""This is the utils test file"""

from parameterized import parameterized
from typing import Mapping, Sequence, Any, Callable
import unittest
from unittest import mock
from utils import access_nested_map, get_json, memoize


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

    @parameterized.expand([
        ('http://example.com', {"payload": True}),
        ('http://holberton.io', {'payload': False})
    ])
    @mock.patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get: mock.MagicMock) -> None:
        """The test for the get json

        Args:
            mock_requests_get (Callable): The mock requests.get()
        """
        mock_requests_get.return_value.json.return_value = test_payload
        res = get_json(test_url)
        mock_requests_get.assert_called_once_with(test_url)
        self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """This is the memoize class' test cases

    Args:
        unittest.TestCase (class): This is the test case class
    """

    def test_memoize(self):
        """This is the memoize test function
        """

        class TestClass:
            """This is jus a test class
            """

            def a_method(self):
                """the a_method of the inner class
                """
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42

            test_class = TestClass()
            res1 = test_class.a_property
            res2 = test_class.a_property

            mock_a_method.assert_called_once()

            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)


if __name__ == "__main__":
    unittest.main()
