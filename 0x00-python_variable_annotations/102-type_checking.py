#!/usr/bin/env python3
"""This is used for type checking"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """This is for zooming

    Args:
        lst (List): the list
        factor (int, optional): The scale factor. Defaults to 2.

    Returns:
        List: The return value
    """
    zoomed_in: List = [
        item for item in lst for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x: List = zoom_array(array, 2)

zoom_3x: List = zoom_array(array, 3)
