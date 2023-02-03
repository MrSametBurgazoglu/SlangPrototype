from Widgets.MainWidget import MainWidget
from Widgets.Widget import Widget
from Widgets.Box import BoxWidget
from Widgets.ColorRect import ColorRectWidget
from Widgets.TextWidget import TextWidget
from Functions.Function import Function
from Components.Component import Component
from Inputs.MouseButtonInput import MouseButtonInput

elements = {
    "MainWidget": MainWidget,
    "Widget": Widget,
    "Box": BoxWidget,
    "ColorRect": ColorRectWidget,
    "TextWidget": TextWidget,
}

extend_classes = {
    "MouseButtonInput": MouseButtonInput
}

#  TODO MAKE ELEMENT TREE


class Parser(object):
    filepath = None

    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(self.filepath, "r")
        self.main_widget = None
        self.functions = {}
        self.components = {}
        self.element_stack = []


    def create_element(self, line):
        if line.startswith("func"):
            self.create_function(line)
        elif line.startswith("component"):
            self.create_component(line)
        else:
            self.create_widget(line)

    def parse_inside_widget(self, line):
        if line.startswith("./"):
            self.parse_inline_function_from_extend(line[2:])
        elif line.startswith("."):
            self.parse_inline_function(line[1:])
            print("hello")
        elif line.startswith("}"):
            print("end of current widget")
        else:
            print("new widget")

    def parse_inside_function(self, line):
        if line.startswith("var"):
            print("create variable")  # will implement later
        elif line.startswith("}") or line.startswith("{"):  # exit from current function
            self.element_stack.pop(-1)
        else:
            self.parse_function_line(line)

    def parse_inside_component(self, line):
        if line.startswith("{"):
            self.element_stack.pop(-1)  # remove last constructor function
        elif line.startswith("}"):
            self.element_stack.pop(-1)
        elif line.startswith(self.element_stack[-1].component_name):
            print("constructor")
            constructor_func = Function()
            function_name_end_index = line.index("(")
            function_name = line[function_name_end_index]
            constructor_func.function_name = function_name
            self.element_stack[-1].component_functions.append(constructor_func)
            self.element_stack.append(constructor_func)
        else:
            self.create_widget(line)

    def parse_line(self):
        line_c = self.file.readline()
        line = line_c.strip(" \n")
        if len(line) > 0 and not line.isspace():
            if len(self.element_stack) == 0:
                self.create_element(line)
            elif isinstance(self.element_stack[-1], (Widget, MainWidget, BoxWidget, ColorRectWidget, TextWidget)):
                self.parse_inside_widget(line)
            elif isinstance(self.element_stack[-1], Function):
                self.parse_inside_function(line)
            elif isinstance(self.element_stack[-1], Component):
                self.parse_inside_component(line)
        else:
            self.element_stack.pop(-1)
        return line_c

    def parse_inline_function_from_extend(self, line):
        extend_class_ending = line.index(".")
        extend_class_name = line[:extend_class_ending]
        function_parameter_start = line.index("(", extend_class_ending)
        function_parameter_end = line.index(")", function_parameter_start)
        function_name = line[extend_class_ending+1:function_parameter_start]
        function_parameters = line[function_parameter_start+1:function_parameter_end]
        extend_class = self.element_stack[-1].extend_classes[extend_class_name]
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
                end_str = line.index(',', current_index)
                #parameters.append(line[current_index:current_index + end_str])
                print("variable", line[current_index:end_str])
                current_index += end_str + 1
            elif line[current_index] == ',':
                current_index += 1
            elif line[current_index] == ' ':
                current_index += 1
            else:  # variables or functions in current environment
                current_index += 1
        return parameters

    '''if current element is none or current element don't have that function return error'''
    def parse_inline_function(self, line: str):
        function_parameter_start = line.index("(")
        function_parameter_end = line.index(")", function_parameter_start)
        function_name = line[:function_parameter_start]
        function_parameters = line[function_parameter_start+1:function_parameter_end]
        function = getattr(self.element_stack[-1], function_name)
        parameters = self.parse_function_parameters(function_parameters)
        function(*parameters)

    def create_function(self, line: str):
        new_func = Function()
        function_name_start_index = line.index(" ")+1
        function_name_end_index = line.index("(", function_name_start_index)
        function_parameter_end = line.index(")", function_name_end_index)
        function_parameters = line[function_name_end_index+1:function_parameter_end]
        function_name = line[function_name_start_index: function_name_end_index]
        self.functions[function_name] = new_func
        new_func.function_name = function_name
        parameters = self.parse_function_parameters(function_parameters)
        new_func.function_parameters = parameters
        self.element_stack.append(new_func)

    def parse_function_line(self, line):
        function_parameter_start = line.index("(")
        function_parameter_end = line.index(")", function_parameter_start)
        function_name = line[:function_parameter_start]
        function_parameters = line[function_parameter_start+1:function_parameter_end]
        self.element_stack[-1].add_function_line(function_name, function_parameters)

    def create_component(self, line):
        new_component = Component()
        component_name_start_index = line.index(" ") + 1
        component_name_end_index = line.index(":", component_name_start_index)
        component_name = line[component_name_start_index: component_name_end_index]
        print(line[component_name_start_index: component_name_start_index + 1])
        new_component.component_name = component_name
        self.components[component_name] = new_component
        self.element_stack.append(new_component)

    def create_widget(self, line: str):
        element_name_index = line.index(':')
        element_name = line[:element_name_index]
        element = elements[element_name]()
        extend_classes_string = line[element_name_index+1:].split(",")
        for x in extend_classes_string:
            element.extend_classes[x] = extend_classes[x]
        if element_name == "MainWidget":
            self.main_widget = element
        else:
            self.element_stack[-1].add_child(element)
        self.element_stack.append(element)
        print(self.element_stack)

