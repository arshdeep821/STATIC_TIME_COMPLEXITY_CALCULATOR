import ast
import inspect


class MyVisitor(ast.NodeVisitor):
    # for function defintions
    def visit_FunctionDef(self, node):
        print("Function Name: ", node.name)
        print("Parameters: ", [arg.arg for arg in node.args.args])
        print("Body: ")
        for stmt in node.body:
            print(ast.dump(stmt))
        self.generic_visit(node)  # Continue traversing children nodes

    # for function cal's my_function(10,20)
    def visit_Call(self, node):
        print("Function call:", node.func.id)
        self.generic_visit(node)  # Continue traversing children nodes
        
    def visit_For(self, node):
        print("Found a for loop")
        # You can access more information about the for loop here
        # For example, node.iter would give you the iterator expression
        # node.target would give you the loop variable
        print("For loop var:", node.target.id)
        self.generic_visit(node)  # Continue traversing children nodes
        
    def visit_If(self, node):
        print("Found an if statement")
        # You can access more information about the if statement here
        # For example, node.test would give you the condition expression
        # node.body would give you the statements inside the if block
        self.generic_visit(node)  # Continue traversing children nodes

    # list = [1, 3, 4]
    def visit_List(self, node):
        values = [element.value for element in node.elts]
        result = ', '.join(map(str, values))
        print("List:", values)
        self.generic_visit(node)

def analyze_function(func):
    # source = inspect.getsource(func)
    # print("Source:", source)
    # print(type(source))
    # tree = ast.parse(source)
    tree = ast.parse(func)
    print(ast.dump(tree))

    # Create an instance of MyVisitor and visit the entire tree
    visitor = MyVisitor()
    visitor.visit(tree)


# tests visit_Call function
code_1 = """
my_function(10,20)
"""
# tests visit_Call, visit_FunctionDef, and visit_List
code_2 = """
def my_function(x,y):
    list = [1,3,4]
    print(x)
    print(y)
"""

code_3 = """
def sum_list(nums):
    result = 0
    for num in nums:
        print(num)
        result += num
    return result
"""


def example_1(x):
    for i in range(x):
        print('hello')

analyze_function(code_3)