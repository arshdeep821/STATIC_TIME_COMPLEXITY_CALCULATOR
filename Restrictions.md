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
