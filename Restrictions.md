### Restrictions to this time complexity calculator

- The time complexity of each function will be analyzed individually
- Function params can have types of either int, str, List, Tuple Set, Dict
- Functions can use for loops, conditional statements, and most built in Python functions
- For loops must only run over list, range(int), or range(len(list)) where int and list are function parameters.

```python
def form_1(nums: List):
    for num in nums:
        # Add logic

def form_2(n: int):
    for i in range(n):
        # Add logic

def form_3(nums: List):
    for i in range(len(nums)):
        # Add logic
```

- All operations that change the time complexity (for loops or built-in function) must be over a function parameter.
- Stretch Goal: Allow functions to call other user defined function.
