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

###### O(k^n), exponential time complexity, where k is a constant
Recursive implementation of the generation of the Fibonacci Sequence, without the use of dynamic programming (memoization)

###### O(n^k), polynomial time complexity, where k is a constant

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


## Check In 4


#### Status of implementation so far.

Implementation has passed its initial stage, functions that take linear time have been added, whether that be string, int, or list, set, dictionary data structures. We are currently working on functions that take either O(nlogn) time like list.sort and functions that take in other user implemented functions. Moreover, we are evaluating how to give a little feedback as mentioned from the user study. 
We also reassessed the scope of the project, based on the feedback provided by the TA. The complexity and the functionality of the project were reevaluated. We brainstormed about additional use cases, and the possibility for supporting the estimation of recursive functions' time complexities. New use cases were added, and will be implemented after the TA's discussion with the professors.

#### Plans for final user study.
We plan to further work on our implementation before our final user study, as well as work on the specific guidelines on how a specified user would use our analyzer. 

#### Planned timeline for the remaining days.
As mentioned, working on functions that take either O(nlogn) time like list.sort and functions that take in other user defined functions is our current agenda. From then on, we will also work on areas that can improve the complexity of our project. As well as have a testing tool. 
We also allocated time for the research of providing support for recursive functions.

#### Progress against the timeline planned for your team, including the specific goals you defined (originally as part of Check-in 2) for Check-in 4; any revisions to Check-in 5 goals.

Check in 5 (week 12):
- Test throughly (each team tests respective tool)
- Create video (whichever team has already finished)
- Incorpoate any final feedback from user studies (whichever team the feedback is for)

## Check In 5

#### User Study 

After informing the user of our Project and the use of it, we introducted the restrictions and allowed them to think about the type of functions the user wanted to test, some that they would be using regularly and likely to code. The user decided to go with two problems that can be found on Leetcode. 

<img width="439" alt="Screenshot 2024-03-29 at 2 29 28 PM" src="https://media.github.students.cs.ubc.ca/user/16895/files/c95e94a3-42fe-4297-92e2-bc8fa557f052">

The first function was the well-known Two Sum problem, user was very happy with this as not only did he not have to make any changes to how they would normally code but as well as the ease of using our static analyser. User also appreciated that the labels of the big O notation was layed out as it may be confusing otherwise. Lastly, we questioned the user with a query from the former user study and that was whether they would want a quick explanation of how the notation was computed but the user did not seem to mind as they stated that they did not feel the need for an explanation and was just nice to have that quick and easy response. 

<img width="482" alt="Screenshot 2024-03-29 at 2 47 16 PM" src="https://media.github.students.cs.ubc.ca/user/16895/files/c86ff839-a063-4847-8f2d-54fad7894c78">

<img width="487" alt="Screenshot 2024-03-29 at 2 29 05 PM" src="https://media.github.students.cs.ubc.ca/user/16895/files/896f2785-b64e-4e28-bfa9-84e0f7eac0d4">

Second function is a function called Is Valid, given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The first screenshot is the first attempt at trying to decipher the run-time but realised that the List stack had to be in the parameters for the function to run. Realising this issue, we immediately corrected the implementation as the list, stack, did not take significant time in terms of Big O and our restrictions are that anything that takes significant time complexity must be a function param. After the adjustment, the user was able to use the second screenshot and was happy with the results. 

All in all, user was happy with the results of both functions, especially the ease and the range of functions applicable of being used. Moreover, after considering their thoughts on the need of an explanation of the final Big O, we have decided to not go with the first user study's comments on providing that explanation. 

#### Planned Timeline + Final Video 

Timeline is going accordingly, with only two features being yet to settle and test, being able to call user-defined functions as well as array/string slicing. Once that has been accomplished, we will go ahead with recording the video where we will not only talk about the motivation behind this project, both user studies but as well as the implementation and how this project can be used and further worked upon. 

