from typing import *

### Sliding Window

## O(a)
# Best time to buy and sell stock
def maxProfit(prices: List) -> int:
    l = 0
    result = 0

    for r in range(len(prices)):
        if prices[l] > prices[r]:
            l = r
        result = max(result, prices[r] - prices[l])
    return result

## O(a)
#Longest Substring without repeating chars
def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    result = 0
    curr_set = set()

    for r in range(len(s)):
        while s[r] in curr_set and l <= r:
            curr_set.remove(s[l])
            l += 1
        curr_set.add(s[r])
        result = max(result, r - l + 1)
    return result

## O(a)
# Longest Repeating character replacement
def characterReplacement(s: str, k: int) -> int:
    count = {}
    
    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

    return (r - l + 1)