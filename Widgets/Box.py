from .BaseWidget import BaseWidget


class BoxWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.orientation = None
        self.horizontal_align = None
        self.vertical_align = None
        self.spacing = None
        self.reverse = False

    def set_orientation(self, orientation):
        self.orientation = orientation

    def set_horizontal_align(self, align):
        self.horizontal_align = align

    def set_vertical_align(self, align):
        self.vertical_align = align

    def compute_size(self):
        self.compute_size_self()
        for x in self.children:
            x.compute_size()
        self.compute_size_self()

    def compute_child_positions_horizontal_align(self):
        pass

    def compute_child_positions_x(self):
        child_x_list = []
        if self.orientation == "vertical":
            for x in self.children:
                if self.horizontal_align == "begin":
                    child_x_list.append(self.computed_pos_x)
                elif self.horizontal_align == "center":
                    parent_center = self.computed_pos_x + self.computed_width / 2
                    current_pos_x = parent_center
                    current_pos_x -= x.computed_width
                    child_x_list.append(current_pos_x)
                elif self.horizontal_align == "end":
                    parent_end = self.computed_pos_x + self.computed_width
                    current_pos_x = parent_end - x.computed_width
                    child_x_list.append(current_pos_x)
        else:
            if not self.reverse:
                if self.horizontal_align == "begin":
                    current_pos = self.computed_pos_x
                    for x in self.children:
                        child_x_list.append(current_pos)
                        #x.compute_position([current_pos, self.computed_pos_y])
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
                    for x in self.children:
                        current_pos -= x.computed_width
                        child_x_list.append(current_pos)
                        #x.compute_position([current_pos, self.computed_pos_y])

    def compute_child_positions(self):
        pass

    def compute_position(self, parent_position):
        self.computed_pos_x = parent_position[0]
        self.computed_pos_y = parent_position[1]
        self.compute_position_self()
        if self.orientation == "vertical":
            if not self.reverse:
                current_pos_y = self.computed_pos_y
                for x in self.children:
                    current_pos_x = 0
                    if self.horizontal_align == "begin":
                        current_pos_x = self.computed_pos_x
                    elif self.horizontal_align == "center":
                        parent_center = self.computed_pos_x + self.computed_width / 2
                        current_pos_x = parent_center
                        current_pos_x -= x.computed_width
                    elif self.horizontal_align == "end":
                        pass
                    x.compute_position([current_pos_x, current_pos_y])
                    current_pos_y += x.computed_height
        else:
            if not self.reverse:
                current_pos = self.computed_pos_x
                for x in self.children:
                    x.compute_position([current_pos, self.computed_pos_y])
                    current_pos += x.computed_width

    def draw(self, canvas):
        for x in self.children:
            x.draw(canvas)
