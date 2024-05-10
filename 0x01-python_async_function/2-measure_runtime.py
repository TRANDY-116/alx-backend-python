#!/usr/bin/env python3
"""Function that measures the total execution time """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measures Total exec time for wait_n and reutrn total_time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    time_used = end_time - start_time
    av_time = time_used / n

    return av_time
