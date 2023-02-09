from .FunctionLine import FunctionLine


class Function(object):
    """
    Functions are a box for function lines. They have their own variables and parameters.
    """
    def __init__(self):
        self.function_name = ""
        self.function_parameters = []
        self.variables = {}
        self.function_lines = []

    def add_function_line(self, name, parameters):
        """
        This function add function lines (script lines) to current function.
        This function is private. Shouldn't be used by developer
        :param name:
        :param parameters:
        :return:
        """
        new_func_line = FunctionLine()
        new_func_line.function_name = name
        new_func_line.function_parameters = parameters
        self.function_lines.append(new_func_line)

    def execute_function(self):
        for x in self.function_lines:
            x.execute_function()
