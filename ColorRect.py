from BaseWidget import BaseWidget


class ColorRectWidget(BaseWidget):
    def __int__(self):
        self.color = None

    def set_color(self, color):
        self.color = color

    def render(self):
        for x in self.children:
            x.render()
