from Widgets.BaseWidget import BaseWidget


class Widget(BaseWidget):
    def __int__(self):
        pass

    def render(self):
        for x in self.children:
            x.render()
