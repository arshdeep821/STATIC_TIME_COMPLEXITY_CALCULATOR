from main import *
from typing import List

# O(1)
def example_function_constant(x: int):
    result = 0
    result += x
    return result

# O(n)
def example_slicing_linear(testList: List):
    return testList[len(testList)//2:]

# O(n)
def example_copy_linear(testList: List):
    return testList.copy()

# O(n)
def example_insert_linear(testList: List):
    testList.insert(len(testList)//2, -1)
    return testList

# O(n)
def example_count_linear(testList: List):
    return testList.count(-1)
