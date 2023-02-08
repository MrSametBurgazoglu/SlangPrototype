from .BaseWidget import BaseWidget


class MainWidget(BaseWidget):
    """
    MainWidget must be the first widget in widget tree.
    Its directly draw to screen.
    """
    def __init__(self):
        super().__init__()

    def compute_size(self):
        for x in self.children:
            x.compute_size()

    def compute_position(self, start_position):
        super().compute_position(start_position)
        for x in self.children:
            x.compute_position([self.computed_pos_x, self.computed_pos_y])

    def draw(self, canvas):
        for x in self.children:
            x.draw(canvas)
