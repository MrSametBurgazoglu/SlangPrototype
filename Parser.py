from MainWidget import MainWidget
from Widget import Widget
from Box import BoxWidget
from ColorRect import ColorRectWidget
from TextWidget import TextWidget
from Function import Function
from Component import Component

elements = {
    "MainWidget": MainWidget,
    "Widget": Widget,
    "Box": BoxWidget,
    "ColorRect": ColorRectWidget,
    "TextWidget": TextWidget,
}


class Parser(object):
    filepath = None

    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(self.filepath, "r")
        self.main_widget = None
        self.functions = {}
        self.components = {}
        self.current_element = None

    def parse_line(self):
        line = self.file.readline()
        if len(line) > 0:
            if self.current_element is None:
                if line.startswith("func"):
                    self.create_function(line)
                elif line.startswith("component"):
                    print("component beginning")
                else:
                    self.create_widget(line)
            elif isinstance(self.current_element, (Widget, MainWidget, BoxWidget, ColorRectWidget, TextWidget)):
                if line.startswith("./"):
                    print("inline function from extend")
                elif line.startswith("."):
                    print("inline function")
                else:
                    print("new widget")
            elif isinstance(self.current_element, Function):
                self.parse_function_line(line)
            elif isinstance(self.current_element, Component):
                print("component line")
        else:
            print("end current statement")
        return line

    def parse_inline_function_from_extend(self):
        pass

    def parse_function_parameters(self, line: str):
        parameters = []
        current_index = 0
        while current_index < len(line):
            if line[current_index] == '"':
                end_str = line.index('"', current_index)
                parameters.append(line[current_index:current_index+end_str])
                current_index += end_str+1
            elif line[current_index] == '$':
                end_str = line.index(',', current_index)
                #parameters.append(line[current_index:current_index + end_str])
                print("variable", line[current_index:current_index + end_str])
                current_index += end_str + 1
            elif line[current_index] == ',':
                current_index += 1
            else:  # space
                current_index += 1
        return parameters

    '''if current element is none or current element don't have that function return error'''
    def parse_inline_function(self, line: str):
        function_parameter_start = line.index("(")
        function_parameter_end = line.index(")", function_parameter_start)
        function_name = line[:function_parameter_start]
        function_parameters = line[function_parameter_start:function_parameter_start+function_parameter_end]
        function = self.current_element.__getattribute__(function_name)
        parameters = self.parse_function_parameters(function_parameters)
        function(*parameters)

    def create_function(self, line: str):
        new_func = Function()
        function_name_start_index = line.index(" ")+1
        function_name_end_index = line.index("(", function_name_start_index)
        function_name = line[function_name_start_index: function_name_start_index+function_name_end_index]
        self.functions[function_name] = new_func
        self.current_element = new_func

    def parse_function_line(self, line):
        function_parameter_start = line.index("(")
        function_parameter_end = line.index(")", function_parameter_start)
        function_name = line[:function_parameter_start]
        function_parameters = line[function_parameter_start:function_parameter_start + function_parameter_end]
        self.current_element.add_function_line(function_name, function_parameters)

    def parse_component(self):
        pass

    def create_widget(self, line: str):
        element_name = line[:line.index(':')]
        element = elements[element_name]()
        if self.main_widget is None:
            self.main_widget = element
        else:
            self.current_element.add_child(element)
        self.current_element = element

