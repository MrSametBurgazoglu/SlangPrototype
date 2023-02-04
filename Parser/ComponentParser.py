from Components.Component import Component


def create_component(line: str):
    new_component = Component()
    component_name_start_index = line.index(" ") + 1
    component_name_end_index = line.index(":", component_name_start_index)
    component_name = line[component_name_start_index: component_name_end_index]
    new_component.component_name = component_name
    return new_component
