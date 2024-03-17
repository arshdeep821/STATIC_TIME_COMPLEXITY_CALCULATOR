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

code_6_find = """
def populate_list(x: int, nums: List) -> None:
    nums.find()
"""

code_6_insert = """
def add_num(x: int, nums: List) -> None:
    nums.insert(0,5)
"""

code_6_index = """
def add_num(x: int, nums: List) -> None:
    nums.index(5)
"""

code_6_count = """
def add_num(x: int, nums: List) -> None:
    nums.count(5)
"""

code_6_reverse = """
def add_num(x: int, nums: List) -> None:
    nums.reverse()
"""

code_7_list = """
def do_smt(n: int, nums: List) -> None:
    if n in nums:
        print('hello')
"""

code_7_string = """
def do_smt(s: str, curr: str) -> None:
    if s in curr:
        print('hello')
"""

code_8 = """
def do_smt(x: int, nums: List):
    if x in list:
        hello('X is in list')
    elif nums[0] in nums:
        bye('ALWAYS TRUE')
"""

code_9 = """
def for_loop_list(nums: List) -> None:
    result = 0
    for num in nums:
        result += num
        result += num
        result += num
    return result

def for_loop_range_int(x: int) -> None:
    for i in range(x):
        print(i)

def for_loop_range_list(lst: List) -> None:
    for i in range(len(lst)):
        print(i)
"""

code_10 = """
def complex(nums: List, s: str) -> None:
    for i in range(len(nums)):
        if 'a' in s:
            print('a')
        if 5 in nums:
            print(5)
"""

code_11 = """
def complex(nums: List, s: str) -> None:
    for i in range(len(nums)):
        for j in range(len(s)):
            if 'a' in s:
                print('a')
            if 5 in nums:
                nums.count('a')
                nums.reverse()
    
    for i in range(len(nums)):
        for j in range(len(s)):
            nums.find(5)
            if 'a' in s:
                print('a')
            if 5 in nums:
                print(5)
"""

code_12 = """
def so_good(s: str) -> None:
    s.upper()
"""

code_13 = """
def lets_go(set1: Set, set2: Set) -> None:
    set1.union(set2)
"""

code_14 = """
def your_mom(map1: Dict) -> None:
    map1.keys()
"""

code_15 = """
def arsh_deep(tuple: Tuple) -> None:
    tuple.count()
"""

code_16 = """
def do_reverse(nums: List):
    return nums.reverse()
"""

code_17 = """
class MyClass: 
    def reverseNum(nums: List) -> None:
        nums.reverse()

    def reverseString(hello: List) -> None:
        hello.count()
"""

do_from_string(code_17)


# source = inspect.getsource(func)
# print("Source:", source)
# print(type(source))
# tree = ast.parse(source)

def example_1(x):
    for i in range(x):
        print('hello')