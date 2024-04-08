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

## O(b)
class TwoSum:
    def twoSum(self: TwoSum, nums: List, target: int) -> None:

        elem_map = {}
        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in elem_map:
                return [elem_map[diff], i]
            else:
                elem_map[n] = i

        return -1
    
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