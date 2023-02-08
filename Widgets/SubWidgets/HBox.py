def compute_child_position_x_begin(children, computed_pos_x, spacing):
    child_x_list = []
    current_pos = computed_pos_x
    for x in children:
        child_x_list.append(current_pos)
        current_pos += x.computed_width
        current_pos += spacing
    return child_x_list


def compute_child_position_x_center(children, computed_pos_x, computed_width, spacing):
    child_x_list = []
    parent_center = computed_pos_x + computed_width / 2
    total_width_of_widgets = 0
    for x in children:
        total_width_of_widgets += x.computed_width
    total_width_of_widgets += spacing * (len(children) - 1)
    current_pos = parent_center - total_width_of_widgets / 2
    for x in children:
        child_x_list.append(current_pos)
        current_pos += x.computed_width
        current_pos += spacing
    return child_x_list


def compute_child_position_x_end(children, computed_pos_x, computed_width, spacing):
    child_x_list = []
    current_pos = computed_pos_x + computed_width
    total_width_of_widgets = 0
    for x in children:
        total_width_of_widgets += x.computed_width
    current_pos -= total_width_of_widgets + (len(children) - 1) * spacing
    for x in children:
        child_x_list.append(current_pos)
        current_pos += x.computed_width
        current_pos += spacing
    return child_x_list


def compute_child_position_x_begin_reverse(children, computed_pos_x, spacing):
    child_x_list = []
    total_width_of_widgets = 0
    for x in children:
        total_width_of_widgets += x.computed_width
    total_width_of_widgets += spacing * (len(children) - 1)
    current_pos = computed_pos_x + total_width_of_widgets
    for x in children:
        current_pos -= x.computed_width
        child_x_list.append(current_pos)
        current_pos -= spacing
    return child_x_list


def compute_child_position_x_center_reverse(children, computed_pos_x, computed_width, spacing):
    child_x_list = []
    parent_center = computed_pos_x + computed_width / 2
    total_width_of_widgets = 0
    for x in children:
        total_width_of_widgets += x.computed_width
    total_width_of_widgets += spacing * (len(children) - 1)
    current_pos = parent_center + total_width_of_widgets / 2
    for x in children:
        current_pos -= x.computed_width
        child_x_list.append(current_pos)
        current_pos -= spacing
    return child_x_list


def compute_child_position_x_end_reverse(children, computed_pos_x, computed_width, spacing):
    child_x_list = []
    current_pos = computed_pos_x + computed_width
    for x in children:
        current_pos -= x.computed_width
        child_x_list.append(current_pos)
        current_pos -= spacing
    return child_x_list


def compute_child_position_y_begin(children, computed_pos_y):
    child_y_list = []
    for x in children:
        child_y_list.append(computed_pos_y)
    return child_y_list


def compute_child_position_y_center(children, computed_pos_y, computed_height):
    child_y_list = []
    parent_center = computed_pos_y + computed_height / 2
    for x in children:
        current_pos_y = parent_center - x.computed_height / 2
        child_y_list.append(current_pos_y)
    return child_y_list


def compute_child_position_y_end(children, computed_pos_y, computed_height):
    child_y_list = []
    parent_end = computed_pos_y + computed_height
    for x in children:
        current_pos_y = parent_end - x.computed_height
        child_y_list.append(current_pos_y)
    return child_y_list


class HBox(object):
    @staticmethod
    def compute_child_positions_x(children, horizontal_align, computed_pos_x, computed_width, spacing):
        match horizontal_align:
            case "begin":
                return compute_child_position_x_begin(children, computed_pos_x, spacing)
            case "center":
                return compute_child_position_x_center(children, computed_pos_x, computed_width, spacing)
            case "end":
                return compute_child_position_x_end(children, computed_pos_x, computed_width, spacing)

    @staticmethod
    def compute_child_positions_x_reverse(children, horizontal_align, computed_pos_x, computed_width, spacing):
        match horizontal_align:
            case "begin":
                return compute_child_position_x_begin_reverse(children, computed_pos_x, spacing)
            case "center":
                return compute_child_position_x_center_reverse(children, computed_pos_x, computed_width, spacing)
            case "end":
                return compute_child_position_x_end_reverse(children, computed_pos_x, computed_width, spacing)

    @staticmethod
    def compute_child_positions_y(children, vertical_align, computed_pos_y, computed_height):
        match vertical_align:
            case "begin":
                return compute_child_position_y_begin(children, computed_pos_y)
            case "center":
                return compute_child_position_y_center(children, computed_pos_y, computed_height)
            case "end":
                return compute_child_position_y_end(children, computed_pos_y, computed_height)
