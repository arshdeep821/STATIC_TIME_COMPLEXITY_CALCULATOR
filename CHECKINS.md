Use this file to commit information clearly documenting your check-ins' content. If you want to store more information/details besides what's required for the check-ins that's fine too. Make sure that your TA has had a chance to sign off on your check-in each week (before the deadline); typically you should discuss your material with them before finalizing it here.

## Check In 1

#### Brief description of your discussions within your team so far

- Had some ideas with regards to analyzing space complexity but much of brainstorming is still yet to be done and discucssed. 
- Also thought of an idea of using Infer to analyze errors within the code and creating a visualizer that states where these errors will occur and what type of error it is. Still a good amount of planning left to do
- Could use concurrency analysis tools to visualize problem areas like deadlocks and give warnings for concurrently accessed/changed global variables.

#### Planned follow-up tasks 

- Will hold another couple meetings to further discuss the topic and route we want to go next week.
- Also will start looking at different analysis frameworks and see which one fits our use case the best. Research about the tech stack of this project, and the pros & cons of different languages/ tools/ frameworks.
- Finalize the idea we want to create the project around and start creating a timeline for which person will take on which task 
- Brainstorm additional program properties to be analyzed (or review existing ones)

## Check In 2

#### Brief description of your planned program analysis (and visualisation, if applicable) ideas

- We plan to create a program analysis tool for specific type checking such as NULLs, strings, ints, etc.
- Visualization will be given user inputted code, to indicated where types may not align with the logic of the code

#### Notes of any important changes/feedback from TA discussion

- Our TA said not to have a general type checker but instead to create a type checker based on some types such as NULLs, Strings, Ints as that is easier to implement

#### Any planned follow-up tasks or features still to design

- Still need to discuss exact implementation strategy and how the visualization tool will actually look

#### Planned division of main responsibilities between team members

- Part of the group will work on using the libraries to perform the program analysis whereas the other part of the group will work on the visualization tool

#### Summary of progress so far

- Finalized our idea and will start implementing

## Check In 3

#### Any changes to original design
Switched up the entire design. We plan to create a static run time analyser. We are creating this to help students who are taking Data Structure and Algorithms courses to figure out the run time of their application statically. 

#### Brief description of your discussions within your team so far
- Selected tentative techstack (language & framework) -> Python and its ast module.
- Researched on the framework and it's usage for this project
- Created basic test cases for time complexity analyses and bootstrapped the project with starter code

#### Planned follow-up tasks 
- Create documentation for the project
- Discuss the implementation details (in particular, the DSA required)

#### Mockup of how your project is planned to operate (as used for your first user study). Include any sketches/examples/scenarios.
Below are functions and the run time they would output above the functions' implementations

###### O(1)
def example_function_constant(x):
    result = 0
    result += x
    return result


###### O(n)
def example_function_linear(x):
    result = 0
    for i in range(x):
        if x > 1:
            result += i
    return result


###### O(n^2)
def example_function_linear_quadratic2(x):
    result = 0
    for i in range(x):
        example_function_linear(x)
    return result


###### O(n^3)
def example_function_linear_quadratic(x):
    result = 0
    for i in range(x):
        example_function_linear_quadratic(x)
    return result

###### O(logn)
Classic binary search in a sorted array

###### O(nlogn)
Classic mergesort

###### O(n^k)
Recursive implementation of the generation of the Fibonacci Sequence, without the use of dynamic programming (memoization)

###### possible edge case
###### O(n)
def example_function3(n):
    result = 0
    for i in range(n):
        for j in range(0, 2):
            result += 1
    return result


###### O(n^2)
def example_function4(n):
    result = 0
    for i in range(n):
        for j in range(n):
            result += 1
    return result

#### First User Study

User was asked to create functions that did not contain a recursive call.

They created firstly a factorial function and a linked list traversal function.
![Screenshot 2024-03-15 at 4 15 15 PM](https://media.github.students.cs.ubc.ca/user/16895/files/4f384a57-fe3f-4234-ae99-065ce629f2c3)

![Screenshot 2024-03-15 at 4 15 11 PM](https://media.github.students.cs.ubc.ca/user/16895/files/bdbe84f7-505c-4108-9d04-39a23eeda60e)

User said that potentially if an explanation can be provided as to how that run time was formed, as well had issues in regards to importing libraries.


#### Roadmap for what should be done when, including specific goals for completion by future Milestones (propose at least three such goals per future Milestone, along with who will work on them; you can revise these later as needed)

Check in 4 (week 11):
- Create working implementation for program![Uploading Screenshot 2024-03-15 at 4.15.11 PM.png…]()
 analysis tool (done by program analysis team)
- Incorporate feedback from first user study 

Check in 5 (week 12):
- Test throughly (each team tests respective tool)
- Create video (whichever team has already finished)
- Incorpoate any final feedback from user studies (whichever team the feedback is for)
