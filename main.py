import ast
from visitor import MyVisitor


def do_from_string(s):
    tree = ast.parse(s)
    visitor = MyVisitor()
    visitor.analyze(tree)


def do_from_file(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
    do_from_string(file_contents)

# do_from_file("test.py")
# do_from_file("tests/testSort.py")
# do_from_file("tests/test_if.py")
do_from_file("tests/user_functions.py")
# do_from_file("tests/array_hashing.py")
# do_from_file("tests/two_pointers.py")
# do_from_file("tests/sliding_window.py")
# do_from_file("tests/stack.py")
# do_from_file("tests/1d_dynamic_programming.py")

# do_from_file("tests.py")
