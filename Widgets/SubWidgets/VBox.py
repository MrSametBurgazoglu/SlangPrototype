def compute_child_position_y_begin(children, computed_pos_y, spacing):
    child_y_list = []
    current_pos = computed_pos_y
    for x in children:
        child_y_list.append(current_pos)
        current_pos += x.computed_height
        current_pos += spacing
    return child_y_list


def compute_child_position_y_center(children, computed_pos_y, computed_height, spacing):
    child_y_list = []
    parent_center = computed_pos_y + computed_height / 2
    total_height_of_widgets = 0
    for x in children:
        total_height_of_widgets += x.computed_height
    total_height_of_widgets += spacing * (len(children) - 1)
    current_pos = parent_center - total_height_of_widgets / 2
    for x in children:
        child_y_list.append(current_pos)
        current_pos += x.computed_height
        current_pos += spacing
    return child_y_list


def compute_child_position_y_end(children, computed_pos_y, computed_height, spacing):
    child_y_list = []
    current_pos = computed_pos_y + computed_height
    total_height_of_widgets = 0
    for x in children:
        total_height_of_widgets += x.computed_height
    total_height_of_widgets += spacing * (len(children) - 1)
    current_pos -= total_height_of_widgets
    for x in children:
        child_y_list.append(current_pos)
        current_pos += x.computed_height
        current_pos += spacing
    return child_y_list


def compute_child_position_y_begin_reverse(children, computed_pos_y, spacing):
    child_y_list = []
    total_height_of_widgets = 0
    for x in children:
        total_height_of_widgets += x.computed_height
    total_height_of_widgets += spacing * (len(children) - 1)
    current_pos = computed_pos_y + total_height_of_widgets
    for x in children:
        current_pos -= x.computed_height
        child_y_list.append(current_pos)
        current_pos -= spacing
    return child_y_list


def compute_child_position_y_center_reverse(children, computed_pos_y, computed_height, spacing):
    child_y_list = []
    parent_center = computed_pos_y + computed_height / 2
    total_height_of_widgets = 0
    for x in children:
        total_height_of_widgets += x.computed_height
    total_height_of_widgets += spacing * (len(children) - 1)
    current_pos = parent_center + total_height_of_widgets / 2
    for x in children:
        current_pos -= x.computed_height
        child_y_list.append(current_pos)
        current_pos -= spacing
    return child_y_list


def compute_child_position_y_end_reverse(children, computed_pos_y, computed_height, spacing):
    child_y_list = []
    current_pos = computed_pos_y + computed_height
    for x in children:
        current_pos -= x.computed_height
        child_y_list.append(current_pos)
        current_pos -= spacing
    return child_y_list


def compute_child_position_x_begin(children, computed_pos_x):
    child_x_list = []
    for x in children:
        child_x_list.append(computed_pos_x)
    return child_x_list


def compute_child_position_x_center(children, computed_pos_x, computed_width):
    child_x_list = []
    parent_center = computed_pos_x + computed_width / 2
    for x in children:
        current_pos_x = parent_center - x.computed_width / 2
        child_x_list.append(current_pos_x)
    return child_x_list


def compute_child_position_x_end(children, computed_pos_x, computed_width):
    child_x_list = []
    parent_end = computed_pos_x + computed_width
    for x in children:
        current_pos_x = parent_end - x.computed_width
        child_x_list.append(current_pos_x)
    return child_x_list


class VBox(object):
    @staticmethod
    def compute_child_positions_y(children, vertical_align, computed_pos_y, computed_height, spacing):
        match vertical_align:
            case "begin":
                return compute_child_position_y_begin(children, computed_pos_y, spacing)
            case "center":
                return compute_child_position_y_center(children, computed_pos_y, computed_height, spacing)
            case "end":
                return compute_child_position_y_end(children, computed_pos_y, computed_height, spacing)

    @staticmethod
    def compute_child_positions_y_reverse(children, vertical_align, computed_pos_y, computed_height, spacing):
        match vertical_align:
            case "begin":
                return compute_child_position_y_begin_reverse(children, computed_pos_y, spacing)
            case "center":
                return compute_child_position_y_center_reverse(children, computed_pos_y, computed_height, spacing)
            case "end":
                return compute_child_position_y_end_reverse(children, computed_pos_y, computed_height, spacing)

    @staticmethod
    def compute_child_positions_x(children, horizontal_align, computed_pos_x, computed_width):
        match horizontal_align:
            case "begin":
                return compute_child_position_x_begin(children, computed_pos_x)
            case "center":
                return compute_child_position_x_center(children, computed_pos_x, computed_width)
            case "end":
                return compute_child_position_x_end(children, computed_pos_x, computed_width)
