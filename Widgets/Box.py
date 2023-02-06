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

    def compute_position(self, parent_position):
        self.computed_pos_x = parent_position[0]
        self.computed_pos_y = parent_position[1]
        self.compute_position_self()
        if self.orientation == "vertical":
            if not self.reverse:
                current_pos = self.computed_pos_y
                for x in self.children:
                    x.compute_position([self.computed_pos_x, current_pos])
                    current_pos += x.computed_height
        else:
            if not self.reverse:
                current_pos = self.computed_pos_x
                for x in self.children:
                    x.compute_position([current_pos, self.computed_pos_y])
                    current_pos += x.computed_width

    def draw(self, canvas):
        for x in self.children:
            x.draw(canvas)
