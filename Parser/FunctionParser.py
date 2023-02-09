from Functions.Function import Function


def parse_function_parameters(line: str, functions):
    parameters = []
    current_index = 0
    while current_index < len(line):
        if line[current_index] == '"':
            end_str = line.index('"', current_index + 1)
            parameters.append(line[current_index + 1:end_str])
            current_index = end_str + 2
        elif line[current_index] == '$':  # global functions or variables
            end_str = line.find(',', current_index)
            variable_name = line[current_index + 1:] if end_str == -1 else line[current_index + 1:end_str]
            if variable_name in functions:
                parameters.append(functions[variable_name])
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


def parse_function_line(line, functions):
    function_parameter_start = line.index("(")
    function_parameter_end = line.index(")", function_parameter_start)
    function_name = line[:function_parameter_start]
    function_parameters = parse_function_parameters(line[function_parameter_start+1:function_parameter_end], functions)
    return function_name, function_parameters


def create_function(line: str, functions):
    new_func = Function()
    function_name_start_index = line.index(" ") + 1
    function_name_end_index = line.index("(", function_name_start_index)
    function_parameter_end = line.index(")", function_name_end_index)
    function_parameters = line[function_name_end_index + 1:function_parameter_end]
    function_name = line[function_name_start_index: function_name_end_index]
    new_func.function_name = function_name
    parameters = parse_function_parameters(function_parameters, functions)
    new_func.function_parameters = parameters
    return new_func


def parse_inline_function(line: str, current_element, functions):
    function_parameter_start = line.index("(")
    function_parameter_end = line.index(")", function_parameter_start)
    function_name = line[:function_parameter_start]
    function_parameters = line[function_parameter_start+1:function_parameter_end]
    function = getattr(current_element, function_name)
    parameters = parse_function_parameters(function_parameters, functions)
    return function, parameters