#!/usr/bin/env python3
"""thisbfile is also hete to create a task"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """this fubction is similar to wait_n"""
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    delays = []
    while tasks:
        done, tasks = await asyncio.wait(
                tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            delays.append(task.result())
    return delays
