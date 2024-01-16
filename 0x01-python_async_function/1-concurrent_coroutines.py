#!/usr/bin/env python3
"""this is the concurrent coroutines file"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """this is the wait function in pthon"""
    ts = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for t in asyncio.as_completed(ts):
        delay = await t
        delays.append(delay)
    return delays
