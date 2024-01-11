#!/usr/bin/env python3
"""Sums up mixed lists"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Sums up a mixed list

    Args:
        mxd_list (List[int  |  float]): The list

    Returns:
        float: The sum
    """
    return sum(mxd_list)
