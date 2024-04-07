from typing import List

# features: nested for loop
# Expected: O(a(b))
def demo_for_loop(lst1: List, lst2: List, num: int) -> List:

    result = 0

    for i in range(len(lst1)):
        for k in lst2:
            for j in range(num):
                result += i * j * k
    
    return lst1


# features: if statement, slicing, math simplification (dropping constants)
# Expected: O(aloga)
def demo_if_statement(lst1: List, element: int) -> List:

    lst1 = lst1[::-1]

    if element in lst1:
        lst1.sort()
    else:
        lst1 = lst1[1:-1:-1]

    return lst1


# features: calling other functions
# Expected: O(1)
def function1(lst: List) -> List:
    return lst[::-1]

# Expected(aloga + b)
def function2(arr: List) -> List:
    
    new_lst = function1([x*2 for x in arr])
    arr.sort()

    return arr

# features: Sets, for loops, if statements (LeetCode 217)
# Expected: O(a)
def containsDuplicate(nums: List) -> bool:
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False

############## could also add this next option for sets

# features: Set, for loop, if statement, while loop (LeetCode 3)
# Expected: O(a)
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

# features: Dict, for loops, if statements (LeetCode 242)
# Expected: O(a)
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

############## could also add this next option for sets

# features: Dict, for loop, if statement (LeetCode 424)
# Expected: O(a)
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

# features: String Input, Local Stack Data Structure, for loop, if statement
# Expected: O(a)
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

