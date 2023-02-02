from BaseWidget import BaseWidget


class BoxWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.orientation = None
        self.horizontal_align = None
        self.vertical_align = None
        self.spacing = None

    def set_orientation(self, orientation):
        self.orientation = orientation

    def set_halign(self, align):
        self.horizontal_align = align

    def set_valign(self, align):
        self.vertical_align = align

    def render(self):
        for x in self.children:
            x.render()
