#!/usr/bin/env python3
"""This is the async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """This is the async generatory"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
