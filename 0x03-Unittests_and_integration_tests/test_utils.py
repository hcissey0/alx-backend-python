#!/usr/bin/env python3
"""This is the utils test file"""

from parameterized import parameterized
from typing import Mapping, Sequence, Any
import unittest
from utils import access_nested_map


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
                               path: Sequence, expected_result: Any):
        """This is the test function for the access_nested_map function

        Args:
            nested_map (Mapping): The nested map to test
            path (Sequence): The sequence of the keys to check
            expected_result (Any): The expected results
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
