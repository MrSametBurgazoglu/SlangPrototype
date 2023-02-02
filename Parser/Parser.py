from Widgets.MainWidget import MainWidget
from Widgets.Widget import Widget
from Widgets.Box import BoxWidget
from Widgets.ColorRect import ColorRectWidget
from Widgets.TextWidget import TextWidget
from Functions.Function import Function
from Components.Component import Component

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


    def create_element(self, line):
        if line.startswith("func"):
            self.create_function(line)
        elif line.startswith("component"):
            self.create_component(line)
        else:
            self.create_widget(line)

    def parse_inside_widget(self, line):
        if line.startswith("./"):
            print("inline function from extend")
        elif line.startswith("."):
            print("inline function")
        elif line.startswith("}"):
            print("end of current widget")
        else:
            print("new widget")

    def parse_inside_function(self, line):
        if line.startswith("var"):
            print("create variable")  # will implement later
        elif line.startswith("}"):  # exit from current function
            self.current_element = None
        else:
            self.parse_function_line(line)

    def parse_inside_component(self, line):
        if line.startswith("{"):
            print("component context start")
        elif line.startswith("}"):
            print("component context end")
        elif line.startswith(self.current_element.component_name):
            print("constructor")
            constructor_func = Function()
            function_name_start_index = line.index(" ") + 1
            function_name_end_index = line.index("(", function_name_start_index)
            function_name = line[function_name_start_index: function_name_start_index + function_name_end_index]
            self.current_element.component_functions.append(constructor_func)
            self.current_element = constructor_func
        else:
            print("create component widget")

    def parse_line(self):
        line = self.file.readline()
        if len(line) > 0 and not line.isspace():
            if self.current_element is None:
                self.create_element(line)
            elif isinstance(self.current_element, (Widget, MainWidget, BoxWidget, ColorRectWidget, TextWidget)):
                self.parse_inside_widget(line)
            elif isinstance(self.current_element, Function):
                self.parse_inside_function(line)
            elif isinstance(self.current_element, Component):
                self.parse_inside_component(line)
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
        function_parameter_end = line.index(")", function_name_end_index)
        function_parameters = line[function_name_end_index:function_name_end_index + function_parameter_end]
        function_name = line[function_name_start_index: function_name_start_index+function_name_end_index]
        self.functions[function_name] = new_func
        self.current_element = new_func

    def parse_function_line(self, line):
        function_parameter_start = line.index("(")
        function_parameter_end = line.index(")", function_parameter_start)
        function_name = line[:function_parameter_start]
        function_parameters = line[function_parameter_start:function_parameter_start + function_parameter_end]
        self.current_element.add_function_line(function_name, function_parameters)

    def create_component(self, line):
        new_component = Component()
        component_name_start_index = line.index(" ") + 1
        component_name_end_index = line.index("(", component_name_start_index)
        component_name = line[component_name_start_index: component_name_start_index + component_name_end_index]
        self.components[component_name] = new_component
        self.current_element = new_component

    def create_widget(self, line: str):
        element_name = line[:line.index(':')]
        element = elements[element_name]()
        if self.main_widget is None:
            self.main_widget = element
        else:
            self.current_element.add_child(element)
        self.current_element = element

