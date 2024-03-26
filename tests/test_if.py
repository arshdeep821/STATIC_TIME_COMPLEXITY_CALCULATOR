from typing import *

# O(a)
def char_in_string(s :str) -> None:
    if 'a' in s:
        return 'found a'
    
# O(a)
def element_in_list(nums: List) -> None:
    i: int = 5
    if i in nums:
        return f"found {i}"

# O(a)
def element_in_tuple(nums: Tuple) -> None:
    i: int = 5
    if i in nums:
        return f"found {i}"
    
# O() -> O(1)
def element_in_set(nums: Set) -> None:
    i: int = 5
    if i in nums:
        return f"fount {i}"

#O() -> O(1)
def element_in_dict(nums: Dict) -> None:
    i: int = 5
    if i in nums:
        return f"found {i}"

# O() -> O(1)
def equal_to_1(n: int) -> None:
    i: int = 5
    if i == n:
        return True
    else:
        return False
    
# O() -> O(1)
def equal_to_2(n: int) -> None:
    i: int = 5
    if n == i:
        return True
    else:
        return False

# O() -> O(1)
def not_equal_to(n:int, i:int) -> None:
    if n != i:
        return True
    else:
        return False

# O() -> O(1)
def greater_than(n: int, i: int) -> None:
    if n > i:
        return True
    else:
        return False
    
# O() -> O(1)
def less_than(n: int, i: int) -> None:
    if n < i:
        return True
    else:
        return False

# O() -> O(1)
def greater_than_or_equal(n: int, i: int) -> None:
    if n >= i:
        return True
    else:
        return False
    
# O() -> O(1)
def greater_than_or_equal(n: int, i: int) -> None:
    if n >= i:
        return True
    else:
        return False
    
# O() -> O(1)
def less_than_or_equal(n: int, i: int) -> None:
    if n <= i:
        return True
    else:
        return False

# O(a) -> O(aums)
def else_if_test(n: int, nums: List) -> None:
    if n > 5:
        return f"{n} is greater than 5"
    elif n in nums:
        return f"{n} is in {nums}"
    else:
        return f"{n} is not greater than 5 and is not in {nums}"

# O() -> O(1)
def in_range(n: int) -> None:
    i: int = 5
    if i in range(n):
        return f"found {i}"

# O() -> O(1)
def use_len(nums: List) -> None:
    i: int = 5
    if 5 == len(nums):
        return True
    else:
        return False

# O(b)
def compare_strings(one: str, two: str) -> None:
    if one > two:
        return True
    else:
        return False
    
# O(b)
def compare_lists(one: List, two: List) -> None:
    if one > two:
        return True
    else:
        return False

# O(b)
def compare_tuples(one: Tuple, two: Tuple) -> None:
    if one == two:
        return True
    else:
        return False

# O(b)
def compare_sets(one: Set, two: Set) -> None:
    if one != two:
        return True
    else:
        return False