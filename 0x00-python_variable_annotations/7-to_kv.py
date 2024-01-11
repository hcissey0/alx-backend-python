#!/usr/bin/env python3
"""This converts to kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """converts k and v to kv

    Args:
        k (str): The string k
        v (Union[int, float]): The v int or float

    Returns:
        Tuple[str, float]: the kv to be returned
    """
    return k, v**2
