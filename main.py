import ast
import inspect
import typing

function_param_type = {} # {'sum_list': {'nums': 'List'}, 'get_list': {'x': 'int'}}
function_result = {}

class MyVisitor(ast.NodeVisitor):
    # for function defintions
    def visit_FunctionDef(self, node):
        print(ast.dump(node, indent=2))
        print("Function Name: ", node.name)
        function_name = node.name
        function_param_type[function_name] = {}
        print("Parameters:")
        for arg in node.args.args:
            arg_name = arg.arg
            arg_type = arg.annotation.id
            print(f"    {arg_name}: {arg_type}")
            function_param_type[function_name][arg_name] = arg_type
        # print("Body: ")
        # for stmt in node.body:
        #     print(ast.dump(stmt))
        # print(ast.dump(node, indent=2))
        print(function_param_type)
        self.generic_visit(node)  # Continue traversing children nodes

    # for function cal's my_function(10,20)
    def visit_Call(self, node):
        # Extract function name
        function_name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr
        # Print function name
        print("Function getting called:", function_name)
            

        if isinstance(node.func, ast.Attribute): # Check if it's a method call
            print('Function call')

            if isinstance(node.func.value, ast.Name) and node.func.value.id == 'list': # check if the method call is on a list
                print('list function call')
                if node.func.attr == 'append':
                    print("Detected a call to list.append()")
                elif node.func.attr == 'pop':
                    print("Detected a call to list.pop()")
                    

            
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

    # set = {1, 2, 3}
    def visit_Set(self, node):
        values = [element.value for element in node.elts]
        print("Set:", values)
        self.generic_visit(node)

    def visit_Return(self, node):
        print("Came to return statement")


def analyze_function(func):
    # source = inspect.getsource(func)
    # print("Source:", source)
    # print(type(source))
    # tree = ast.parse(source)
    tree = ast.parse(func)
    # print(ast.dump(tree))

    # Create an instance of MyVisitor and visit the entire tree
    visitor = MyVisitor()
    visitor.visit(tree)


def example_1(x):
    for i in range(x):
        print('hello')
