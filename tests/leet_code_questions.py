from typing import *

# class TwoSum:
#     def twoSum(self: TwoSum, nums: List, target: int) -> None:

#         elem_map = {}
#         for i in range(len(nums)):
#             n = nums[i]
#             diff = target - n
#             if diff in elem_map:
#                 return [elem_map[diff], i]
#             else:
#                 elem_map[n] = i

#         return -1

def isValid(s: str) -> bool:
    stack = []
    match = {"}": "{", ")": "(", "]":"["}

    for b in s:
        if b in match:
            if len(stack) != 0 and stack[-1] == match[b]:
                stack.pop()
            else:
                return False
        else:
            stack.append(b)

    return len(stack) == 0