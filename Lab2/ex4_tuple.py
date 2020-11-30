"""
ISCG6426 Lab 2 Semester 2 2020 by Kris Pritchard / @krisrp

Tests used to check correctness.
This file requires 'pytest' and 'pyexpect' to run.
Install them with the following command:
    pip install pytest pyexpect

Then run the file with:
    pytest -xv ex4_tuple_tests.py

You need to implement this code so that all of the tests pass.
Feel free to comment out specific tests, but only submit your answers files.
When checking your answers I will use the test files from this repository.


Tuple (Immutable Container):
    For this introductory lab you need to implement functionality for a basic tuple data structure.
    Performance doesn't matter for this.
    None of the method implementations require more than 6 lines of code.
"""

class TupleException(Exception):
    pass

class TupleIndexException(TupleException):
    pass

class TupleModifyException(TupleException):
    pass


# IMPLEMENT a TupleException.


# IMPLEMENT a TupleIndexException which inherits from TupleException.


# IMPLEMENT a TupleModifyException which inherits from TupleException.



class Tuple:
    """
    A tuple is an immutable data structure which only supports simple operations.
    """
    def __init__(self, initial_data=None):
        # NOTE: Don't change this from a list.
        if initial_data:
            self.data = initial_data
        else:
            self.data = []

    def __str__(self):
        # Print class name and contents of tuple
        # e.g. print(my_tuple) returns <Tuple __str__: [1, 2, 3]>
        return f'<Tuple __str__: {self.data}>'

    def __repr__(self):
        # Display class name and contents of tuple
        # e.g. Typing my_tuple in shell displays <Tuple __repr__: [1, 2, 3]>
        return f'<Tuple __repr__: {self.data}>'

    def __getitem__(self, index):
        # Returns item at index 123 when we type my_tuple[123].
        # IMPLEMENT: Raise a TupleIndexException if accessing index that doesn't exist.
        if self.data[index] in self.data:
            return self.data[index]
        else:
            raise TupleIndexException()

    def __setitem__(self, index, item):
        # Tuple's don't support item assignment.
        # IMPLEMENT: Immediately raise a TupleModifyException when trying to change an item.
        if index == item:
            print(f'tuple __setitem__(). {self.data}.')
        else:
            raise TupleModifyException()

    def __add__(self, other):
        # Add two Tuples together and return a new Tuple.
        for i in self.data:
            if i not in other:
                self.data.append(i)
        return self.data

    def count(self, value):
        # Return number of occurrences of value.
        if len(self.data) != 0:
            return self.data.count(value)
        print(f'tuple count(). {self.data}.')

    def index(self, value):
        # Return the index of value in self.data.
        return self.data[value-1]
