from Widgets.BaseWidget import BaseWidget


class Widget(BaseWidget):
    """
    Widget is the simplest widget.
    It can have any child widget.
    """
    def __init__(self):
        super().__init__()

    def compute_size(self):
        self.compute_size_self()
        for x in self.children:
            x.compute_size()
        self.compute_size_self()

    def compute_position_children(self, parent_position):
        self.computed_pos_x = parent_position[0]
        self.computed_pos_y = parent_position[1]
        for x in self.children:
            x.compute_position([self.computed_pos_x, self.computed_pos_y])

    def draw(self, canvas):
        for x in self.children:
            x.draw(canvas)
