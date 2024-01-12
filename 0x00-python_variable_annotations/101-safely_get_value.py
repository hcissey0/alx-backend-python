#!/usr/bin/env python3
"""This safely gets a value"""
from typing import Mapping, Any, TypeVar, Union


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[TypeVar, None]
) -> Union[Any, TypeVar]:
    """This returns key or default

    Args:
        dct (Mapping): The dict
        key (Any): The key of the object
        default (Union[_T, None]): The default

    Returns:
        Union[Any, _T]: The return value
    """
    if key in dct:
        return dict[key]
    else:
        return default
