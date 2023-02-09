from Widgets.MainWidget import MainWidget
from Widgets.Widget import Widget
from Widgets.Box import BoxWidget
from Widgets.ColorRect import ColorRectWidget
from Widgets.ImageRect import ImageRectWidget
from Widgets.TextWidget import TextWidget
from Functions.Function import Function
from Components.Component import Component


from Parser import ComponentParser, FunctionParser, WidgetParser

#  TODO MAKE ELEMENT TREE


class Parser(object):
    filepath = None

    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(self.filepath, "r")
        self.main_widget = None
        self.functions = {}
        self.components = {}
        self.current_element = None
        self.parent_element = None


    def create_element(self, line):
        if line.startswith("func"):
            self.create_function(line)
        elif line.startswith("component"):
            self.create_component(line)
        else:
            self.create_widget(line)

    def parse_inside_widget(self, line: str):
        if line.startswith("./"):
            self.parse_inline_function_from_extend(line[2:])
        elif line.startswith("."):
            self.parse_inline_function(line[1:])
        elif line.startswith("}"):
            self.current_element, self.parent_element = self.parent_element, self.parent_element.parent
        elif line.startswith("{"):
            self.parent_element = self.current_element
        elif line.startswith("component"):
            self.add_component(line[10:])
        else:
            self.create_widget(line)

    def parse_inside_function(self, line: str):
        if line.startswith("var"):
            print("create variable")  # will implement later
        elif line.startswith("{"):  # exit from current function
            self.current_element = self.parent_element
        else:
            self.parse_function_line(line)

    def parse_inside_component(self, line):
        if line.startswith("{"):
            self.current_element = self.parent_element
        elif line.startswith("}"):
            self.parent_element = None
            self.current_element = None
        elif line.startswith(self.parent_element.component_name):
            constructor_func = Function()
            function_name_end_index = line.index("(")
            function_name = line[function_name_end_index]
            constructor_func.function_name = function_name
            self.parent_element.component_functions.append(constructor_func)
            self.current_element = constructor_func
        else:
            self.create_widget(line)

    def parse_line(self):
        line_c = self.file.readline()
        line = line_c.strip(" \n")
        if len(line) > 0 and not line.isspace():
            if self.parent_element is None:
                self.create_element(line)
            elif isinstance(self.current_element, (Widget, MainWidget, BoxWidget, ColorRectWidget, TextWidget, ImageRectWidget)):
                self.parse_inside_widget(line)
            elif isinstance(self.current_element, Function):
                self.parse_inside_function(line)
            elif isinstance(self.current_element, Component):
                self.parse_inside_component(line)
        else:
            self.current_element = None
            self.parent_element = None
        return line_c

    def parse_inline_function_from_extend(self, line):
        extend_class_ending = line.index(".")
        extend_class_name = line[:extend_class_ending]
        function_parameter_start = line.index("(", extend_class_ending)
        function_parameter_end = line.index(")", function_parameter_start)
        function_name = line[extend_class_ending+1:function_parameter_start]
        function_parameters = line[function_parameter_start+1:function_parameter_end]
        extend_class = self.current_element.extend_classes[extend_class_name]
        function = getattr(extend_class, function_name)
        parameters = self.parse_function_parameters(function_parameters)
        function(*parameters)

    def parse_function_parameters(self, line: str):
        parameters = []
        current_index = 0
        while current_index < len(line):
            if line[current_index] == '"':
                end_str = line.index('"', current_index+1)
                parameters.append(line[current_index+1:end_str])
                current_index += end_str+1
            elif line[current_index] == '$': # global functions or variables
                end_str = line.find(',', current_index)
                variable_name = ""
                if end_str == -1:
                    variable_name = line[current_index+1:]
                else:
                    variable_name = line[current_index+1:end_str]
                if variable_name in self.functions:
                    parameters.append(self.functions[variable_name])
                #parameters.append(line[current_index:current_index + end_str])
                current_index += end_str + 1
                if end_str == -1:
                    break
            elif line[current_index] == ',':
                current_index += 1
            elif line[current_index] == ' ':
                current_index += 1
            else:  # variables or functions in current function
                current_index += 1
        return parameters

    def parse_inline_function(self, line: str):
        function, parameters = FunctionParser.parse_inline_function(line, self.current_element, self.functions)
        function(*parameters)

    def create_function(self, line: str):
        new_func = FunctionParser.create_function(line, self.functions)
        self.functions[new_func.function_name] = new_func
        self.current_element = new_func
        self.parent_element = new_func

    def parse_function_line(self, line):
        function_name, function_parameters = FunctionParser.parse_function_line(line, self.functions)
        self.current_element.add_function_line(function_name, function_parameters)

    def create_component(self, line):
        new_component = ComponentParser.create_component(line)
        self.components[new_component.component_name] = new_component
        self.parent_element = new_component
        self.current_element = new_component

    def add_component(self, line):
        component_name_end_index = line.index("(")
        component_name = line[:component_name_end_index]
        self.parent_element.add_child(self.components[component_name].component_widget)
        #execute constructor function
        #exit(0)

    def create_widget(self, line: str):
        new_element, is_main_widget = WidgetParser.create_widget(line)
        self.current_element = new_element
        if is_main_widget:
            self.main_widget = self.current_element
            self.parent_element = self.current_element
        else:
            self.parent_element.add_child(self.current_element)
            self.current_element.parent = self.parent_element

    def get_context(self):
        return self.main_widget, self.components, self.functions
