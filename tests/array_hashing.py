from typing import *

### Array and hashing

# O(a)
def containsDuplicate(nums: List) -> bool:
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False



## O(a)
def isAnagram(s: str, t: str) -> bool:
    mapS = {}
    mapT = {}

    if len(s) != len(t):
        return False
    
    for i in range(len(s)):
        if s[i] in mapS:
            mapS[s[i]] += 1
        else:
            mapS[s[i]] = 1
    
        if t[i] in mapT:
            mapT[t[i]] += 1
        else:
            mapT[t[i]] = 1
    
    return mapS == mapT

## O(a)
def twoSum(nums: List, target: int) -> None:

    elem_map = {}
    for i in range(len(nums)):
        n = nums[i]
        diff = target - n
        if diff in elem_map:
            return [elem_map[diff], i]
        else:
            elem_map[n] = i

    return -1


# Does not work right now due to difference in for loop
# def productExceptSelf(nums: List) -> List:
#     result = []
#     prefix = []
#     postfix = [0] * len(nums)

#     curr = nums[0]
#     for i in range(1, len(nums)):
#         prefix.append(curr)
#         curr *= nums[i]
#     prefix.append(curr)

#     curr = nums[-1]
#     for i in range(len(nums) - 2, -1, -1):
#         postfix[i + 1] = curr
#         curr *= nums[i]
#     postfix[0] = curr

#     for i in range(len(nums)):
#         if i == 0:
#             result.append(postfix[i + 1])
#         elif i == len(nums) - 1:
#             result.append(prefix[i - 1])
#         else:
#             result.append(prefix[i - 1] * postfix[i + 1])
#     return result
    
## O(a), does not work
# Concatentation of array
# def getConcatenation(nums: List) -> List:
#     ans = []
#     for i in range(2):
#         for n in nums:
#             ans.append(n)
#     return ans

## O(a), does not work
 # Is Sub Sequence   
# def isSubsequence(s: str, t: str) -> bool:
#     i, j = 0, 0
#     while i < len(s) and j < len(t):
#         if s[i] == t[j]:
#             i += 1
#         j += 1
#     return i == len(s)
    
## O(a)
# Majority Element
def majorityElement(nums: List) -> int:
    res, count = 0, 0

    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
        
    return res

## O(a)
# Find pivot index
def pivotIndex(nums: List) -> int:
    total = sum(nums)  # O(n)

    leftSum = 0
    for i in range(len(nums)):
        rightSum = total - nums[i] - leftSum
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1