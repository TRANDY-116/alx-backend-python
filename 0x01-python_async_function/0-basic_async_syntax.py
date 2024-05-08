#!/usr/bin/env python3
""" 
Async coroutine that takes in an interger, waits for random
delay(0 -10) and then returns it 
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """ Waits for a random delay between 0 and the max delay"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i