from main import *

# tests visit_Call function
code_1 = """
my_function(10,20)
"""
# tests visit_Call, visit_FunctionDef, and visit_List
code_2 = """
def my_function(x: int,y: int) -> None:
    list = [1,3,4]
    print(x)
    print(y)
"""

code_3 = """
def sum_list(nums: List) -> None:
    result = 0
    for num in nums:
        print(num)
        result += num
    return result
"""

code_4 = """
def sum_list(nums: List) -> None:
    result = 0
    for num in nums:
        print(num)
        result += num
    return result

def get_list(x: int) -> None:
    for i in range(x):
        print(i)
"""

code_5 = """
def set_function(x: int) -> None:
    set = {1,2,3}
    for num in set:
        print(num)
"""

code_6 = """
def populate_list(x: int) -> None:
    list = []
    list.append(1)
"""

analyze_function(code_4)