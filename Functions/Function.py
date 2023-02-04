from .FunctionLine import FunctionLine


class Function(object):
    function_lines = None

    def __init__(self):
        self.function_name = ""
        self.function_parameters = []
        self.variables = {}
        self.function_lines = []

    def add_function_line(self, name, parameters):
        new_func_line = FunctionLine()
        new_func_line.function_name = name
        new_func_line.function_parameters = parameters
        self.function_lines.append(new_func_line)
