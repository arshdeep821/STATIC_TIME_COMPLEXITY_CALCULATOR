from typing import *

def complex(nums: List, s: str) -> None:
    for i in range(len(nums)):
        for j in range(len(s)):
            if 'a' in s:
                print('a')
            if 5 in nums:
                nums.count('a')
                nums.reverse()
    
    for i in range(len(nums)):
        for j in range(len(s)):
            nums.find(5)
            if 'a' in s:
                print('a')
            if 5 in nums:
                print(5)


def for_loop_list(nums: List) -> None:
    result = 0
    for num in nums:
        result += num
        result += num
        result += num
    return result


def for_loop_range_int(x: int) -> None:
    for i in range(x):
        print(i)


def for_loop_range_list(lst: List) -> None:
    for i in range(len(lst)):
        print(i)

class MyClass: 
    def reverseNum(nums: List) -> None:
        nums.reverse()

    def reverseString(hello: List) -> None:
        hello.count()