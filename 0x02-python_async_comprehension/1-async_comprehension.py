#!/usr/bin/env python3
"""This is for async comprehension"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """This is the async compreshension"""
    return [i async for i in async_generator()]
