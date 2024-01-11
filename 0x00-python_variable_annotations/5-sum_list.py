#!/usr/bin/env python3
"""This is a function that sums up list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums up a list of floats

    Args:
        input_list (list[float]): The list

    Returns:
        float: The sum
    """
    return sum(input_list)
