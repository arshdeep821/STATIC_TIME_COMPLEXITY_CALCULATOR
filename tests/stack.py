from typing import *

### Stack

## O(a)
# Valid Parenthesis
def isValid(s: str) -> bool:
    stack = []
    match = {"}": "{", ")": "(", "]":"["}

    for b in s:
        if b in match:
            if len(stack) != 0 and stack[-1] == match[b]:
                stack.pop()
            else:
                return False
        else:
            stack.append(b)

    return len(stack) == 0

## O(a)
# Evaluate Reverse Polish Notation
def evalRPN(tokens: List) -> int:
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(float(b) / a))
        else:
            stack.append(int(c))
    return stack[0]

## O(a)
# Correct time complexity even though while loop is present
# Daily Temperatures
def dailyTemperatures(temperatures: List) -> List:
    stack = []
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and stack[-1][0] < temperatures[i]:
            result[stack[-1][1]] = i - stack[-1][1]
            stack.pop()
        stack.append([temperatures[i],i])

    return result

## O(aloga)
# NOT A VALID EXAMPLE BECAUSE arr IS A LOCAL THAT TAKES SIGNIFICANT TIME COMPLEXITY
# def carFleet(target: int, position: List, speed: List) -> int:
#     arr = [[position[i], speed[i]] for i in range(len(speed))]
#     arr.sort()

#     stack = []

#     for i in range(len(arr)):
#         time = float((target - arr[i][0])/arr[i][1])

#         while stack and stack[-1] <= time:
#             stack.pop()
#         stack.append(time)
#     return len(stack)

## O(blogb)
# Car Fleet
def carFleet(target: int, arr: List) -> int:
    arr.sort()
    stack = []

    for i in range(len(arr)):
        time = float((target - arr[i][0])/arr[i][1])

        while stack and stack[-1] <= time:
            stack.pop()
        stack.append(time)
    return len(stack)