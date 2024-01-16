#!/usr/bin/env python3
"""This is used to test the basic async syntax"""
import asyncio
import random


async def wait_random(max_delay=10):
    """This function is just a wait function """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
