from SystemFunctions.SystemFunctions import execute_function


class FunctionLine(object):
    def __init__(self):
        self.function_name = ""
        self.function_parameters = []

    def execute_function(self):
        execute_function(self.function_name, self.function_parameters)
