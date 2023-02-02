from FunctionLine import FunctionLine

class Function(object):
    def __int__(self):
        self.function_name = ""
        self.function_parameters = []
        self.variables = {}
        self.function_lines = []

    def add_function_line(self, name, parameters):
        new_func_line = FunctionLine()
        new_func_line.name = name
        new_func_line.function_parameters = parameters
