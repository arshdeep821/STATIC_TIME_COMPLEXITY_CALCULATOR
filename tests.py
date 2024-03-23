from main import *

# O(1)
def example_function_constant(x):
    result = 0
    result += x
    return result


# O(n)
def example_function_linear(x):
    result = 0
    for i in range(x):
        if x > 1:
            result += i
    return result


# O(n^2)
def example_function_linear_quadratic2(x):
    result = 0
    for i in range(x):
        example_function_linear(x)
    return result


# O(n^3)
def example_function_linear_quadratic(x):
    result = 0
    for i in range(x):
        example_function_linear_quadratic(x)
    return result


# possible edge case
# O(n)
def example_function3(n):
    result = 0
    for i in range(n):
        for j in range(0, 2):
            result += 1
    return result


# O(n^2)
def example_function4(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += 1
    return result


# analyze_function(example_function_constant)
# analyze_function(example_function2)
