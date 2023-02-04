from .BaseWidget import BaseWidget


class MainWidget(BaseWidget):
    def __init__(self):
        super().__init__()

    def render(self):
        for x in self.children:
            x.render()
