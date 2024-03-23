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

do_from_file("test.py")
do_from_file("tests/testSort.py")