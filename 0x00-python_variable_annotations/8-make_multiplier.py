#!/usr/bin/env python3
"""This is going to make a multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This is going to make a multiplier

    Args:
        multiplier (float): The multiplier

    Returns:
        Callable: The return function
    """
    return lambda x: multiplier * x
