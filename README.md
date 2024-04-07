# Time Complexity Calculator - Static 

## Original Motivation

Original motivation was to help students who are having trouble in Data Structure and Algorithms courses understand why certain functions have the big-O complexity they do. Additionally most Software Engineer Interviews consist of LeetCode style questions where there will be follow-up questions consistening of the run time of the function. This analyzer can help students with figuring out the time complexity of the functions.

## Project details - Static vs Dynamic vs Anything Else

Our project uses a static analysis with the help of the Python ast library. We chose a static analysis as then we can look at only input params and figure out a big-O complexity in terms of those input params. NEED TO ADD MORE

## Summary of the content of User Studies:

In conducting the two user studies on our Python run-time analysis tool, participants were asked to test/code non-recursive functions. The first user desired deeper insights into runtime computations and faced challenges with library imports, while developing a factorial function and a linked list traversal. The second user, focusing on "Two Sum" and "Is Valid" problems from Leetcode, valued the tool's ease of use and straightforward Big O notation without needing detailed runtime explanations. The feedback from both participants led to refining the tool's focus on usability and applicability across various programming tasks, opting against detailed computational explanations to enhance user satisfaction and adding the ability to include user-defined functions. All in all, the tool was much enjoyed from both participants as it was quick and easy to receive a big-O notation of the run-time. 

## Evaluation of own work at various stages

#### Initial Implementation:

- Process of selecting an idea took the longest part as we had to figure out approaches on how to implement it (tech stack and libraries) as well as if it could be done statically
- Setting up the initial visitor pattern was difficult but once a couple visitors were set, adding to the code base to make it more complex one step at a time was much easier
- Once the basic functions were done of this analyzer we looked into more complex big-O time complexities such as log operations as well as functions calling other user-defined functions
- Cleaned up code to make more readiable and separate logic into different files

Overall we think at each stage the work was completed in an efficient manner, everything we wanted is in this analyzer in the time we had


#### Negative Points in our design/implementation and some solutions we implented:

- Initially we were confused about how to traverse the *ast* in order to calculate the time complexiity. We were thinking of just traversing each node at a time using *DFS* but then we found out the python ast library provides a Visitor Pattern which we also learned about in the first half of the course as it makes traversing the tree a lot easier and the code is cleaner. We stuck with this best design principle as it made our work easier and the code more compact (Needed less code to the same thing without the built in visitor)
- We were also confused about *if/else* statements on how to calculate the big-O complexity statically as there could be multiple control flows, but we learned in lecture in Static Program Slicing that the *if/else* statements complexities could be unioned together to form a result that is over approximated but considers both cases in its calculation. 
- While our current rendering of what the user sees is effective for understanding which function params the big-O complexity, it could be vastly improved upon by building a GUI where the user could possibly paste in python code and present it in a more visually appealing and effective way.

## Team Management and Organization:


## How to run project

1. Make sure to have python or python3 installed on computer
2. Clone Repository
3. Create a python file in root directory that consists of functions you want to know the time complexity of
4. Go to main.py in the root directory of the project
5. Add the **file path** to the function *do_from_file(file_path)*
6. Open a terminal that is in the root directory of the project and run **python main.py** or if you have a mac then **python3 main.py**

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
- Call do_from_file("test_functions.py") in main.py, add this line to the bottom of the file

```python
do_from_file("test_functions.py")

```
- Run main.py using **python** or **python3**

```zsh
python3 main.py
```

- Output should be in the terminal you ran the file in. Here's what it will look like:

```zsh
arshdeepjaggo@Arshdeeps-MacBook-Air Group11Project2 % python3 main.py

a = size of list parameter `nums`
Time complexity of function `containsDuplicate` is O(a)
```

## Restrictions:

- The time complexity of each function will be analyzed individually
- Function params can have types of either int, str, List, Tuple Set, Dict only
- Functions can use for loops, conditional statements, and most built in Python functions
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
