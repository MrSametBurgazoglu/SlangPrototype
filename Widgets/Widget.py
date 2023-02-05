from Widgets.BaseWidget import BaseWidget


class Widget(BaseWidget):
    def __init__(self):
        super().__init__()

    def render(self, canvas):
        self.compute_metrics()
        for x in self.children:
            x.render(canvas)
        self.compute_metrics()

    def draw(self, canvas):
        for x in self.children:
            x.draw(canvas)
