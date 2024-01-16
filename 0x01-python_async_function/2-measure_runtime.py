#!/usr/bin/env python3
"""This file us userd to measuure the runtion"""
from time import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """This is used to measure thr run tikme"""
    st_time = time()
    asyncio.run(wait_n(n, max_delay))
    end_time = - time()
    total_time = end_time - st_time
    return total_time / n
