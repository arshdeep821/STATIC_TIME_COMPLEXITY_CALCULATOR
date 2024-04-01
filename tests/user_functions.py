from typing import *

def function0():
    i = 0
    print(i)

def function1(first: List) -> None:
    for i in range(len(first)):
        i = i + 1
    
def function2(second: List) -> None:
    for i in range(len(second)):
        i = i + 1
        
def function3(third: List) -> None:
    function1(third)
    function2(third)
    function0()
    
def function4(fourth: List) -> None:
    for i in range(len(fourth)):
        function1(fourth)
        
def function5(fifth: List) -> None:
    for i in range(len(fifth)):
        function3(fifth)
        
def function6(sixth: List) -> None:
    for i in range(len(sixth)):
        function4(sixth)

def function7(arr: List) -> None:
    return arr.sort()

def function8(nums: List) -> None:
    for i in range(len(nums)):
        function7(nums)

# O(a + b)
def function9(nums1: List, nums2: List) -> None:
    for i in range(nums1):
        pass
    for i in range(nums2):
        pass

# O(a(b + c))
def function10(arr: List) -> None:
    for i in range(len(arr)):
        function9(arr, arr)

# O(a(b))
def function11(nums1: List, nums2: List) -> None:
    for i in range(nums1):
        for i in range(nums2):
            pass

# O(a(b(c)))
def function12(arr1: List, arr2: List) -> None:
    for i in range(len(arr1)):
        function11(arr1, arr2)

def function13(nums1: List, nums2: List) -> None:
    # O(a + b)
    for i in range(len(nums1)):
        pass
    for i in range(len(nums2)):
        pass

def function14(arr1: List, arr2: List) -> None:
    # (a(d + c) + b(c + d))
    for i in range(len(arr1)):
        function13(arr1, arr1)
    for i in range(len(arr2)):
        function13(arr1, arr1)