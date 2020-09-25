"""
Implement a base case for this recursive function.
"""
import sys
from functools import lru_cache


RECURSION_LIMIT = 100 # Default is 1000
sys.setrecursionlimit(RECURSION_LIMIT)


"""
NOTE: This is the only function you need to implement for this exercise.
"""
def recursion_base_case(n, stop=10):
    # IMPLEMENT: Add a recursion base-case here to stop and return n when n == stop.
    # Hint: 2 lines of code.

    # <-- What goes here?

    return recursion_base_case(n - 1, stop=stop)
