#!/usr/bin/env python3
"""this is the concurrent coroutines file"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n, max_delay):
    """this is the wait function in pthon"""
    delays = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    re = await asyncion.gather(*delays, return_exceptions=True)
    delays[:] = [r[0] for r in res]
    return delays
