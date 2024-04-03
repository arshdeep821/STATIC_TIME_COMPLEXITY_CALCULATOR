import ast

list_functions_that_take_O_n = ['insert', 'remove', 'index', 'count', 'reverse', 'extend', 'clear', 'copy']

list_functions_that_take_O_nlogn = ['sort']

string_functions_that_take_O_n = ['join', 'split', 'replace', 'strip', 'rstrip', 'lstrip', 'upper', 'lower', 'title', 'capitalize', 'find', 'rfind', 'index', 'rindex', 'count', 'startswith', 'endswith', 'encode']

set_functions_that_take_O_n = ['update', 'intersection_update', 'difference_update', 'intersection', 'union' 'clear', 'copy']

tuple_functions_that_take_O_n = ['count']

dictionary_functions_that_take_O_n = ['items', 'keys', 'values', 'clear', 'copy' ]


class MyVisitor(ast.NodeVisitor):
    
    def __init__(self):
        super().__init__()
        self.function_param_type = {} # {'sum_list': {'nums': 'List'}, 'get_list': {'x': 'int'}}
        self.function_result = {} # {function_name: "expression in terms of variable names"}
        self.recursive_list = []
        self.function_defs = []
        
    
    def analyze(self, root):
        self.visit(root)
        # print out the results
        for function_name, time_complexity_as_variable_names in self.function_result.items():
            self.print_time_complexity(function_name, time_complexity_as_variable_names)
            print()

    # for function defintions
    def visit_FunctionDef(self, node):

        self.recursive_list = []
        function_name = node.name
        self.function_param_type[function_name] = {}
        self.function_defs.append(function_name)
        for param in node.args.args:
            param_name = param.arg
            param_type = param.annotation.id
            self.function_param_type[function_name][param_name] = param_type
        self.generic_visit(node)

        self.function_result[function_name] = f"O({'+'.join(list(set(self.recursive_list)))})"
        self.recursive_list = []
                    
    
    # for loops must only run over list, range(int), or range(len(list))  
    # recursion must be done iteratively  
    def visit_For(self, node):

        iterator_information = node.iter
        iterating_variable_name = None

        if isinstance(iterator_information, ast.Name):
            # Example case 1: for val in lst
            iterating_variable_name = iterator_information.id

        elif isinstance(iterator_information, ast.Call):
            if iterator_information.func.id == 'range':
                range_arg = iterator_information.args[0]
                if isinstance(range_arg, ast.Name):
                    # Example case 2: for i in range(var)
                    iterating_variable_name = range_arg.id
                elif isinstance(range_arg, ast.Call) and range_arg.func.id == 'len':
                    # Example ase 3: for i in range(len(lst))
                    list_name = range_arg.args[0]
                    iterating_variable_name = list_name.id

        length_before_recursion = len(self.recursive_list)

        # don't use generic visit because we don't want to calculate time complexity of range()
        for inner_node in node.body:
            self.visit(inner_node)

        length_after_recursion = len(self.recursive_list)

        inner_variables_set = set()
        for _ in range(length_after_recursion - length_before_recursion):
            inner_variables_set.add(self.recursive_list.pop())
        
        if len(inner_variables_set):
            result = iterating_variable_name + "(" + "+".join(list(inner_variables_set)) + ")"
            self.recursive_list.append(result)
        else:
            self.recursive_list.append(iterating_variable_name)

        # print("DEBUG visit_For result:", result)

    
    # for function cal's my_function(10,20)
    def visit_Call(self, node):
        # function_name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr

        if isinstance(node.func, ast.Attribute): # Check if it's a method call
            # print('Function call')
            recent_func = self.function_defs[-1]
            variable_name = node.func.value.id
            if isinstance(node.func.value, ast.Name) and variable_name in self.function_param_type[recent_func] and self.function_param_type[recent_func][variable_name] == 'List':
                if node.func.attr in list_functions_that_take_O_n:
                    self.recursive_list.append(variable_name)
                if node.func.attr in list_functions_that_take_O_nlogn:
                    self.recursive_list.append(f"{variable_name}log({variable_name})")

            if isinstance(node.func.value, ast.Name) and variable_name in self.function_param_type[recent_func] and self.function_param_type[recent_func][variable_name] == 'str':
                if node.func.attr in string_functions_that_take_O_n:
                    self.recursive_list.append(variable_name)
                    
            if isinstance(node.func.value, ast.Name) and variable_name in self.function_param_type[recent_func] and self.function_param_type[recent_func][variable_name] == 'Set':
                if node.func.attr in set_functions_that_take_O_n:
                    self.recursive_list.append(variable_name)
                    
            if isinstance(node.func.value, ast.Name) and variable_name in self.function_param_type[recent_func] and self.function_param_type[recent_func][variable_name] == 'Dict':
                if node.func.attr in dictionary_functions_that_take_O_n:
                    self.recursive_list.append(variable_name)

            if isinstance(node.func.value, ast.Name) and variable_name in self.function_param_type[recent_func] and self.function_param_type[recent_func][variable_name] == 'Tuple':
                if node.func.attr in tuple_functions_that_take_O_n:
                    self.recursive_list.append(variable_name)

        if isinstance(node.func, ast.Name) and node.func.id in self.function_param_type: # Check to see if its a function call 
            # print(f"{node.func.id} detected ----- in {self.function_defs[-1]}")
            # print(f"currently the defs {self.function_defs}")
            current_func = self.function_defs[-1]
            detected_func = node.func.id
            
            # original parameters in detected_func
            original_param = self.function_param_type[detected_func] 
            
            # new_param is the original paramaters with the function name in front of it
            new_param = {f"{detected_func}_{key}": value for key, value in original_param.items()}
            
            # placeholder for result_runtime, need to swap the names
            modified_result = self.function_result[detected_func]
            # for each paramater
            for original_key in original_param.keys():
                new_key = f"{detected_func}_{original_key}"
                modified_result = modified_result.replace(original_key, new_key)

            # updating the current_func's params and run time
            if len(modified_result[2:-1]): # this "if" ensures the function is not O(1)
                self.recursive_list.append(modified_result[2:-1]) 
                self.function_param_type[current_func].update(new_param)
        
        self.generic_visit(node)
        
    def visit_If(self, node):
        self.generic_visit(node)

    
    def visit_Compare(self, node):
        # print(ast.dump(node))

        for op in node.ops:
            # if isinstance(op, (ast.Eq, ast.NotEq, ast.Gt, ast.Lt, ast.GtE, ast.LtE)):
            #     continue

            try:
                variable_name = node.comparators[0].id
                most_recent_function_defined = self.function_defs[-1]
                if isinstance(op, (ast.Eq, ast.NotEq, ast.Gt, ast.Lt, ast.GtE, ast.LtE)) and self.function_param_type[most_recent_function_defined][variable_name] == 'str':
                    self.recursive_list.append(node.comparators[0].id)
                    continue
            except:
                pass

            try:
                variable_name = node.comparators[0].id
                most_recent_function_defined = self.function_defs[-1]
                if isinstance(op, (ast.Eq, ast.NotEq, ast.Gt, ast.Lt, ast.GtE, ast.LtE)) and self.function_param_type[most_recent_function_defined][variable_name] == 'List':
                    self.recursive_list.append(node.comparators[0].id)
                    continue
            except:
                pass

            try:
                variable_name = node.comparators[0].id
                most_recent_function_defined = self.function_defs[-1]
                if isinstance(op, (ast.Eq, ast.NotEq, ast.Gt, ast.Lt, ast.GtE, ast.LtE)) and self.function_param_type[most_recent_function_defined][variable_name] == 'Tuple':
                    self.recursive_list.append(node.comparators[0].id)
                    continue
            except:
                pass

            try:
                variable_name = node.comparators[0].id
                most_recent_function_defined = self.function_defs[-1]
                if isinstance(op, (ast.Eq, ast.NotEq, ast.Gt, ast.Lt, ast.GtE, ast.LtE)) and self.function_param_type[most_recent_function_defined][variable_name] == 'Set':
                    self.recursive_list.append(node.comparators[0].id)
                    continue
            except:
                pass                

            try:
                if node.comparators[0].func.id == "range" or node.comparators[0].func.id == "len":
                    continue
            except:
                pass
    

            try:
                variable_name = node.comparators[0].id
                most_recent_function_defined = self.function_defs[-1]
                if isinstance(op, ast.In) and self.function_param_type[most_recent_function_defined][variable_name] == 'List':
                    self.recursive_list.append(node.comparators[0].id)
                elif isinstance(op, ast.In) and self.function_param_type[most_recent_function_defined][variable_name] == 'str': 
                    self.recursive_list.append(node.comparators[0].id)
                elif isinstance(op, ast.In) and self.function_param_type[most_recent_function_defined][variable_name] == 'Tuple':
                    self.recursive_list.append(node.comparators[0].id)
            except:
                pass
            
        self.generic_visit(node) 


    # for array indexing syntax, e.g. array[0:4:-1]
    def visit_Subscript(self, node):
        if isinstance(node.slice, ast.Tuple):
            slices = node.slice.dims # e.g. s[::-1], dims would be [-1]
            if len(slices) == 1 and slices[0].upper is None and isinstance(slices[0], ast.Slice):
                if isinstance(node.value, ast.Constant):
                    self.recursive_list.append(node.value)

        self.generic_visit(node)


    # list = [1, 3, 4]
    def visit_List(self, node):
        self.generic_visit(node)


    # set = {1, 2, 3}
    def visit_Set(self, node):
        self.generic_visit(node)


    def visit_Return(self, node):
        self.generic_visit(node)


    def print_time_complexity(self, function_name, time_complexity_as_variable_names):

        available_variables = list("abcdefghijklmnopqrstuvwxyz")
        param_type_tuples = list(self.function_param_type[function_name].items())
        add_in_new_variable_name = [(available_variables[i], param_type_tuples[i][0], param_type_tuples[i][1]) for i in range(len(param_type_tuples))]

        for new_param_name, param, param_type in add_in_new_variable_name:
            time_complexity_as_variable_names = time_complexity_as_variable_names.replace(param, new_param_name)
            if param_type == "int":
                print(f"{new_param_name} = integer value of parameter `{param}`")
            elif param_type == "str":   
                print(f"{new_param_name} = size of string parameter `{param}` string")
            elif param_type == "List":
                print(f"{new_param_name} = size of list parameter `{param}`")
            elif param_type == "Set":
                print(f"{new_param_name} = size of set parameter `{param}`")
            elif param_type == "Dict":
                print(f"{new_param_name} = size of dictionary parameter `{param}`")
            elif param_type == "Tuple":
                print(f"{new_param_name} = size of tuple parameter `{param}`")
        if time_complexity_as_variable_names  == "O()":
            print(f"Time complexity of function `{function_name}` is O(1)")
        else:
            print(f"Time complexity of function `{function_name}` is {time_complexity_as_variable_names}")

        # print(f"Time complexity of function `{function_name}` is {time_complexity_as_variable_names}")