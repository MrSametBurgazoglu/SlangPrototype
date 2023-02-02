from .BaseWidget import BaseWidget


class TextWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.text = ""

    def set_text(self, text):
        self.text = text

    def render(self):
        for x in self.children:
            x.render()
