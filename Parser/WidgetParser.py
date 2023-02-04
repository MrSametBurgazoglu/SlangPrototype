from Parser.Variables import elements, extend_classes


def create_widget(line: str):
    element_name_index = line.index(':')
    element_name = line[:element_name_index]
    element = elements[element_name]()
    extend_classes_string = line[element_name_index + 1:]
    is_main_widget = False
    if extend_classes_string:
        extend_classes_string_list = extend_classes_string.split(",")
        for x in extend_classes_string_list:
            element.extend_classes[x] = extend_classes[x]()
    if element_name == "MainWidget":
        is_main_widget = True
    return element, is_main_widget
