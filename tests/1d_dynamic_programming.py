from typing import *

### 1-D Dynamic Programming

## O(a)
# House Robber
def rob(nums: List) -> int:
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

## O(b+a)
# House Robber 2
def helper(arr: List) -> int:
    rob1, rob2 = 0, 0

    for n in arr:
        newRob = max(rob1 + n, rob2)
        rob1 = rob2
        rob2 = newRob
    return rob2

def rob1(nums: List) -> int:
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))


## O(a)
# Maximum Product subarray
def maxProduct(nums: List) -> int:
    res = nums[0]
    curMin, curMax = 1, 1

    for n in nums:

        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res