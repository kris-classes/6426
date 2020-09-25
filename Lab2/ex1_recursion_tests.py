"""
DO NOT MODIFY THIS FILE.

ISCG6426 Lab 2 Semester 2 2020 by Kris Pritchard / @krisrp

Tests used to check correctness of answers.

Run the file with:
    python ex1_recursion_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.
"""
import pytest
import time
from ex1_recursion import *


print('=== Recursion 1 Question ===')
print('Solve this problem: Testing recursion_base_case() function')
try:
    n = recursion_base_case(100, stop=95) #) == 95
except RecursionError:
    print('ERROR: You forgot to add a base-case to the recursion_base_case function. Do it for marks.')
else:
    if n == 95:
        print('Solved!')
    else:
        print(f'n == {n}. Keep trying!')

