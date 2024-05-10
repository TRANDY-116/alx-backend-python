#!/usr/bin/env python3
""" async routint that takes 2 args """


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawns wait_Return n times with the specified max_delay """
    # Create a list of coroutine objects using a generator expression
    coroutines = (wait_random(max_delay) for _ in range(n))

    # Wait for coroutines using asyncio.gather
    gatheredResults = asyncio.gather(*coroutines)

    # Await results and store in delays
    delays = sorted(await gatheredResults)
    return delays
# #!/usr/bin/env python3
# """
# Spawns wait_random n tinmes with the specided delays.

# Parameters:
#     n (int): Number of times to call wait_random.
#     Max_delays (int): Maximum Delay for each wait_random call

# Returns:
#     List[float]: List of delays in ascending order
# """

# import asyncio

# wait_random = __import__('0-basic_async_syntax').wait_random


# async def wait_n(n: int, max_delay: int) -> [float]:
#     """ Spawns wait_Return n times with the specified max_delay """
#     # Create a list of coroutine objects using a generator expression
#     coroutines = (wait_random(max_delay) for _ in range(n))

#     # Wait for coroutines using asyncio.gather
#     gatheredResults = asyncio.gather(*coroutines)

#     # Await results and store in delays
#     delays = sorted(await gatheredResults)
#     return delays
