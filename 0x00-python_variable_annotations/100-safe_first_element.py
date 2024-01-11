#!/usr/bin/env python3
"""Duck typing first element of a sequence"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns a safe first element

    Args:
        lst (Sequence[Any]): The list

    Returns:
        Union[Any, None]: The returned
    """
    if lst:
        return lst[0]
    else:
        return None
