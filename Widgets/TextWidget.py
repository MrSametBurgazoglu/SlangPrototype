import skia

from .BaseWidget import BaseWidget


class TextWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.text = ""
        self.paint = skia.Paint()
        self.font_size = 24
        self.font = skia.Font(None, self.font_size)

    def set_text(self, text):
        self.text = text

    def set_color(self, color):
        if color == "red":
            self.paint.setColor(skia.ColorRED)

    def render(self, canvas):
        text_width = self.font.measureText(self.text)
        self.computed_width = text_width
        self.computed_height = self.font_size

    def draw(self, canvas):
        canvas.drawSimpleText(self.text, self.computed_pos_x, self.computed_pos_y + self.font_size, font=self.font,
                              paint=self.paint)
