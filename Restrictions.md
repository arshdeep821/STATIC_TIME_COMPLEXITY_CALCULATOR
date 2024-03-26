### Restrictions to this time complexity calculator

- All function params must have types of either int, str, List, Tuple Set, Dict
- All logic must be defined in a function, can have functions in a class if you want
- No while loops or recursion (functions cannot call other user-defined functions)
- for loops must only run over list, range(int), or range(len(list))

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

- Everything that takes changes time complexity must be interms of a parameter
- When doing ==, !=, <, >, <=, >= the function parameter must be on the right hand-side

```python
1 == int

"hello" == string

[1, 2, 3] == list

(1, 2, 3) == tuple

{1, 2, 3} == set
```