from core import root_widget


def console_print(parameters):
    print(*parameters)


def change_property(parameters):
    print(parameters)
    print(root_widget.root_widget.change_property(parameters[0], parameters[1], parameters[2]))


system_functions = {
    "print": console_print,
    "change_property": change_property,
}


def execute_function(name, parameters):
    system_functions[name](parameters)
