from typing import List

# O(n)
def example_slice_simple(testList: List):
    return testList[:2]

# O(n)
def example_slice_reverse(testList: List):
    return testList[::-1]

# O(n)
def example_slice_complex(testList: List):
    return testList[4:5:-1]

# O(1)
def example_constant_test(testList: List):
    return testList[3]