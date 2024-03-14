import ast
import inspect

def eval(tree):
    print('hi')

class MyVisitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print("Function Name: ", node.name)
        print("Parameters: ", [arg.arg for arg in node.args.args])
        print("Body: ")
        for stmt in node.body:
            print(ast.dump(stmt))
        self.generic_visit(node)  # Continue traversing children nodes

    def visit_Call(self, node):
        # print("Function call:", node.func.id)
        self.generic_visit(node)  # Continue traversing children nodes
        
    def visit_For(self, node):
        print("Found a for loop")
        # You can access more information about the for loop here
        # For example, node.iter would give you the iterator expression
        # node.target would give you the loop variable
        self.generic_visit(node)  # Continue traversing children nodes
        
    def visit_If(self, node):
        print("Found an if statement")
        # You can access more information about the if statement here
        # For example, node.test would give you the condition expression
        # node.body would give you the statements inside the if block
        self.generic_visit(node)  # Continue traversing children nodes

def analyze_function(func):
    source = inspect.getsource(func)
    tree = ast.parse(source)
    print(ast.dump(tree))
    eval(tree)

    # Create an instance of MyVisitor and visit the entire tree
    visitor = MyVisitor()
    visitor.visit(tree)



