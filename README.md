# Python Time Complexity Calculator - Static 

## Original Motivation

Original motivation was to help students who are having trouble in Data Structure and Algorithms courses understand why certain functions have the big-O complexity they do. Additionally most Software Engineer Interviews consist of LeetCode style questions where there will be follow-up questions consistening of the run time of the function. This analyzer can help students with figuring out the time complexity of the functions.

## Project details - Static vs Dynamic vs Anything Else

Our project uses a static analysis with the help of the Python ast library. We chose a static analysis as then we can look at only input params and figure out a big-O complexity in terms of those input params. Though a static analysis may over-estimate the run-time, since a static analysis does not require the program to be executed, it can be performed without setting up a runtime environment.

#### Negative Points in our design/implementation and some solutions we implented:

- Initially we were confused about how to traverse the *ast* in order to calculate the time complexiity. We were thinking of just traversing each node at a time using *DFS* but then we found out the python ast library provides a Visitor Pattern which we also learned about in the first half of the course as it makes traversing the tree a lot easier and the code is cleaner. We stuck with this best design principle as it made our work easier and the code more compact (Needed less code to the same thing without the built in visitor)
- We were also confused about *if/else* statements on how to calculate the big-O complexity statically as there could be multiple control flows, but we learned in lecture in Static Program Slicing that the *if/else* statements complexities could be unioned together to form a result that is over approximated but considers both cases in its calculation. 
- While our current rendering of what the user sees is effective for understanding which function params the big-O complexity, it could be vastly improved upon by building a GUI where the user could possibly paste in python code and present it in a more visually appealing and effective way.

## How to run project

1. Make sure to have python or python3 installed on computer
2. Clone Repository
3. Create a python file in root directory that consists of functions you want to know the time complexity of (make sure params have types of str, int, List, Tuple, Set, Dict)
4. Open a terminal that is in the root directory of the project and run **python main.py** or if you have a mac then **python3 main.py**
5. You will be prompted to enter the file name of the file you are trying to analyzer, please add it and click enter
6. A list of complexities should be rendered along side function details

### Example:

- Create a file called test_functions.py in root directory and populate it with functions you are curious to know big-O time complexity about. Example file structure could be:

```python
from typing import *

def containsDuplicate(nums: List) -> bool:
    s = set()
    for num in nums:
        if num in s:
            return True
        s.add(num)
    return False
```

- Run main.py using **python** or **python3**

```zsh
python3 main.py
```

- An input in the terminal should pop up and prompt you to enter the file name and click enter
- Here's what it will look like:

```zsh
arshdeepjaggo@Arshdeeps-MacBook-Air Group11Project2 % python3 main.py
This is a static time complexity program analysis tool.
Please input a file name and click enter: test_functions.py

a = size of list parameter `nums`
Time complexity of function `containsDuplicate` is O(a)
```

## Restrictions:

- The time complexity of each function will be analyzed individually
- Function params must have types of either int, str, List, Tuple Set, Dict only
- Functions can use for loops, conditional statements, and most built in Python functions, and call other user implemented functions in a non-circular way
- For loops must only run over list, range(int), or range(len(list)) where int and list are function parameters.

```python
def form_1(nums: List) -> None:
    for num in nums:
        # Add logic

def form_2(n: int) -> None:
    for i in range(n):
        # Add logic

def form_3(nums: List) -> None:
    for i in range(len(nums)):
        # Add logic
```

- All operations that change the time complexity (for loops or built-in function) must be over a function parameter.
- User-defined functions can call other user defined functions as long as the function getting called within another function is implemented **BEFORE** in the file

```python
from typing import *

def function_1(i: int) -> None:
    # Function Logic ...

def function_2(nums: List) -> None:
    for num in nums:
        function_1(num)
```
