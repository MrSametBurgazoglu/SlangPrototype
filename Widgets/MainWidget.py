from .BaseWidget import BaseWidget


class MainWidget(BaseWidget):
    def __init__(self):
        super().__init__()

    def render(self, canvas):
        for x in self.children:
            x.render(canvas)

    def draw(self, canvas):
        for x in self.children:
            x.draw(canvas)
