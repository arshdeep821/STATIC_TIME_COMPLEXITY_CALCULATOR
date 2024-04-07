from typing import List

# features: nested for loop
# Expected: O(a(b(aloga)))
def demo_for_loop(lst1: List, lst2: List):

    result = 0

    for i in range(len(lst1)):
        for num in lst2:
            result += i * num
    
    return lst1


# features: if statement, slicing, math simplification (dropping constants)
# Expected: O(aloga)
def demo_if_statement(lst1: List, element: int):

    lst = lst[::-1]

    if element in lst1:
        lst1.sort()
    else:
        lst1 = lst1[1:-1:-1]

    return lst1


# features: calling other functions
# Expected: O(1)
def function1(lst: List):
    return lst[::-1]

# Expected(aloga + b)
def function2(arr: List) -> None:
    
    new_lst = function1([x*2 for x in arr])
    arr.sort()

    return arr
