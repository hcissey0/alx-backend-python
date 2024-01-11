#!/usr/bin/env python3
"""This is going to duck type an iterable object"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This is going to determine the element length

    Args:
        lst (Iterable[Sequence]): The list containing the elements

    Returns:
        List[Tuple[Sequence, int]]: The list of tuple with the result
    """
    return [(i, len(i)) for i in lst]
