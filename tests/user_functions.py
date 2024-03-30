from typing import *

def function1(first: List) -> None:
    for i in range(len(first)):
        i = i + 1
    
def function2(second: List) -> None:
    for i in range(len(second)):
        i = i + 1
        
def function3(third: List) -> None:
    function1(third)
    function2(third)
    
def function4(fourth: List) -> None:
    for i in range(len(fourth)):
        function1(fourth)
        
def function5(fifth: List) -> None:
    for i in range(len(fifth)):
        function3(fifth)
        
def function6(sixth: List) -> None:
    for i in range(len(sixth)):
        function4(sixth)