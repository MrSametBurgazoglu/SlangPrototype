from .BaseWidget import BaseWidget


class MainWidget(BaseWidget):
    def __init__(self):
        pass

    def render(self):
        for x in self.children:
            x.render()
