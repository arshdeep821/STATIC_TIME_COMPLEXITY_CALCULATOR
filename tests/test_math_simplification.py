from typing import List

# O(ab + a) should simplify to O(ab)
def test_big_O_simplify(l1: List, l2: List):
    l3 = l1[::-1] # this takes O(a)

    for i in range(len(l1)): # this nested loop takes O(a*b)
        for num in l2:
            print("HI")
    
    return l3


# O(aloga + a) should simplify to O(aloga)
def test_big_O_simplify_log(nums: List):
    new_nums = nums[::-1]
    return nums.sort()