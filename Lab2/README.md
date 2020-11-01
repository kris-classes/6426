# ISCG 6426 Lab 2 Semester 2 2020.
## by Kris Pritchard

ISCG6426 Lab2 Semester 2 2020. Code by Kris Pritchard / @krisrp
Implement the following:

## Part 1 - Test-driven Development of Data Structures
### NOTE: Each method here only requires 1-7 lines of code. If you have more you're doing it wrong.
* ex1: A recursion base case.
* ex2: Stack class and Stack Exceptions
* ex3: Queue class and Queue Exceptions
* ex4: Tuple class and Tuple Exceptions
* ex5: Dictionary class and Dictionary Exceptions (Technically just the interface for now, but illustrative nonetheless)
* ex6: Set class and Set Exceptions
* ex7: PriorityQueue class and import the Queue Exceptions from exercise 3.

ex0_list_example.py has been implemented to show how to do it.


Lab2: Implement the data structures to make all the tests pass.

### Step 1 - Download the code

```shell
git clone https://github.com/kris-classes/6426
```

### Step 2 - Install the required libraries


```shell
pip install pytest pyexpect
```

### Step 3 - Running the tests.


```shell
# Example with Lists
pytest -xv ex0_list_example_tests.py
# Recursion
python ex1_recursion_tests.py  # NOTE: This example just uses python, not pytest.
# Stack
pytest -xv ex2_stack_tests.py
# Queue
pytest -xv ex3_queue_tests.py
# Tuple
pytest -xv ex4_tuple_tests.py
# Dictionary
pytest -xv ex5_dictionary_tests.py
# Set
pytest -xv ex6_set_tests.py
# PriorityQueue
pytest -xv ex7_priorityqueue_tests.py
```

### Step 4 - Make the data structures work.

Fix each of the tests one by one.

The files you need to fix are:
* ex1_recursion.py
* ex2_stack.py
* ex3_queue.py
* ex4_tuple.py
* ex5_dictionary.py
* ex6_set.py
* ex7_priorityqueue.py

Add these files to a Labs/Lab2 directory in your class repository.

``` shell
pytest -xv ex2_stack_tests.py  # Runs the Stack tests.
```

Here you will get 
```python
AssertionError: Expect 'Stack __str__(): FIX ME' to equal '<Stack __str__: []>'
```

Fix the Stack.__str__ method in ex2_stack.py so that the test passes.
Commit your fixed code to GitHub.

Now fix the __repr__ method.
Commit your fixed code to GitHub.

And continue.

## Part 2 - Creation and Testing of Data Structures
* ex8: Heap class and tests for it.
* ex9: HeapPriorityQueue class and tests for it.
* ex10: AVL Tree and tests for it.

Do the same as Part 1, but this time you also need to implement the tests.


## Submission
Add your solutions to the Labs/Lab2 directory of your repository and push the
changes to GitHub. Use one commit per test fixed.

