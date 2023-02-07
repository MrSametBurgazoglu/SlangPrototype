from .BaseWidget import BaseWidget


class BoxWidget(BaseWidget):
    """
    BoxWidget is a box for other widgets.
    Its orientation can be vertical or horizontal
    Its horizontal align can be "begin", "center", "end
    Its vertical align can be "begin", "center", "end
    """
    def __init__(self):
        super().__init__()
        self.orientation = None
        self.horizontal_align = None
        self.vertical_align = None
        self.spacing = None
        self.reverse = False

    def set_orientation(self, orientation):
        self.orientation = orientation
        print(self.orientation, "orientation")

    def set_horizontal_align(self, align):
        self.horizontal_align = align

    def set_vertical_align(self, align):
        self.vertical_align = align

    def compute_size(self):
        self.compute_size_self()
        for x in self.children:
            x.compute_size()
        self.compute_size_self()
        if self.orientation == "vertical":
            maximum_width = 0
            for x in self.children:
                maximum_width = max(maximum_width, x.computed_width)
            self.computed_width = maximum_width
        else:
            maximum_height = 0
            for x in self.children:
                maximum_height = max(maximum_height, x.computed_height)
            self.computed_height = maximum_height


    def compute_child_positions_x_vertical_orientation(self):
        child_x_list = []
        for x in self.children:
            if self.horizontal_align == "begin":
                child_x_list.append(self.computed_pos_x)
            elif self.horizontal_align == "center":
                parent_center = self.computed_pos_x + self.computed_width / 2
                current_pos_x = parent_center
                current_pos_x -= x.computed_width / 2
                child_x_list.append(current_pos_x)
            elif self.horizontal_align == "end":
                parent_end = self.computed_pos_x + self.computed_width
                current_pos_x = parent_end - x.computed_width
                child_x_list.append(current_pos_x)
        return child_x_list

    def compute_child_positions_x_horizontal_orientation(self):
        child_x_list = []
        if self.horizontal_align == "begin":
            current_pos = self.computed_pos_x
            for x in self.children:
                child_x_list.append(current_pos)
                current_pos += x.computed_width
        elif self.horizontal_align == "center":
            parent_center = self.computed_pos_x + self.computed_width / 2
            total_width_of_widgets = 0
            for x in self.children:
                total_width_of_widgets += x.computed_width
            current_pos = parent_center - total_width_of_widgets / 2
            for x in self.children:
                child_x_list.append(current_pos)
                current_pos += x.computed_width
        elif self.horizontal_align == "end":
            current_pos = self.computed_pos_x + self.computed_width
            total_width_of_widgets = 0
            for x in self.children:
                total_width_of_widgets += x.computed_width
            current_pos -= total_width_of_widgets
            for x in self.children:
                child_x_list.append(current_pos)
                current_pos += x.computed_width
        return child_x_list

    def compute_child_positions_x_horizontal_orientation_reverse(self):
        child_x_list = []
        if self.horizontal_align == "begin":
            total_width_of_widgets = 0
            for x in self.children:
                total_width_of_widgets += x.computed_width
            current_pos = self.pos_x + total_width_of_widgets
            for x in self.children:
                current_pos -= x.computed_width
                child_x_list.append(current_pos)
        elif self.horizontal_align == "center":
            parent_center = self.computed_pos_x + self.computed_width / 2
            total_width_of_widgets = 0
            for x in self.children:
                total_width_of_widgets += x.computed_width
            current_pos = parent_center + total_width_of_widgets / 2
            for x in self.children:
                current_pos -= x.computed_width
                child_x_list.append(current_pos)
        elif self.horizontal_align == "end":
            current_pos = self.computed_pos_x + self.computed_width
            for x in self.children:
                current_pos -= x.computed_width
                child_x_list.append(current_pos)
        return child_x_list

    def compute_child_positions_x(self):
        child_x_list = []
        if self.orientation == "vertical":
            child_x_list = self.compute_child_positions_x_vertical_orientation()
        else:
            if not self.reverse:
                child_x_list = self.compute_child_positions_x_horizontal_orientation()
            else:
                child_x_list = self.compute_child_positions_x_horizontal_orientation_reverse()
        return child_x_list


    def compute_child_positions_y_vertical_orientation(self):
        child_y_list = []
        if self.vertical_align == "begin":
            current_pos = self.computed_pos_y
            for x in self.children:
                child_y_list.append(current_pos)
                current_pos += x.computed_height
        elif self.vertical_align == "center":
            parent_center = self.computed_pos_y + self.computed_height / 2
            total_height_of_widgets = 0
            for x in self.children:
                total_height_of_widgets += x.computed_height
            current_pos = parent_center - total_height_of_widgets / 2
            for x in self.children:
                child_y_list.append(current_pos)
                current_pos += x.computed_height
        elif self.vertical_align == "end":
            current_pos = self.computed_pos_y + self.computed_height
            total_height_of_widgets = 0
            for x in self.children:
                total_height_of_widgets += x.computed_height
            current_pos -= total_height_of_widgets
            for x in self.children:
                child_y_list.append(current_pos)
                current_pos += x.computed_height
        return child_y_list

    def compute_child_positions_y_vertical_orientation_reverse(self):
        child_y_list = []
        if self.vertical_align == "begin":
            total_height_of_widgets = 0
            for x in self.children:
                total_height_of_widgets += x.computed_height
            current_pos = self.pos_x + total_height_of_widgets
            for x in self.children:
                current_pos -= x.computed_height
                child_y_list.append(current_pos)
        elif self.vertical_align == "center":
            parent_center = self.computed_pos_y + self.computed_height / 2
            total_height_of_widgets = 0
            for x in self.children:
                total_height_of_widgets += x.computed_width
            current_pos = parent_center + total_height_of_widgets / 2
            for x in self.children:
                current_pos -= x.computed_height
                child_y_list.append(current_pos)
        elif self.vertical_align == "end":
            current_pos = self.computed_pos_y + self.computed_height
            for x in self.children:
                current_pos -= x.computed_height
                child_y_list.append(current_pos)
        return child_y_list

    def compute_child_positions_y_horizontal_orientation(self):
        child_y_list = []
        for x in self.children:
            if self.vertical_align == "begin":
                child_y_list.append(self.computed_pos_y)
            elif self.vertical_align == "center":
                parent_center = self.computed_pos_y + self.computed_height / 2
                current_pos_y = parent_center
                current_pos_y -= x.computed_height / 2
                child_y_list.append(current_pos_y)
            elif self.vertical_align == "end":
                parent_end = self.computed_pos_y + self.computed_height
                current_pos_y = parent_end - x.computed_height
                child_y_list.append(current_pos_y)
        return child_y_list

    def compute_child_positions_y(self):
        child_y_list = []
        if self.orientation == "vertical":
            if not self.reverse:
                child_y_list = self.compute_child_positions_y_vertical_orientation()
            else:
                child_y_list = self.compute_child_positions_y_vertical_orientation_reverse()
        else:
            child_y_list = self.compute_child_positions_y_horizontal_orientation()
        print(child_y_list)
        return child_y_list

    def compute_child_positions(self):
        pos_x_list = self.compute_child_positions_x()
        pos_y_list = self.compute_child_positions_y()
        for children, pos in zip(self.children, zip(pos_x_list, pos_y_list)):
            children.computed_pos_x = pos[0]
            children.computed_pos_y = pos[1]


    def compute_position(self, parent_position):
        self.computed_pos_x = parent_position[0]
        self.computed_pos_y = parent_position[1]
        self.compute_position_self()
        self.compute_child_positions()

    def draw(self, canvas):
        for x in self.children:
            x.draw(canvas)
