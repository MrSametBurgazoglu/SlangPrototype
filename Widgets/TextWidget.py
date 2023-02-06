import skia

from .BaseWidget import BaseWidget


class TextWidget(BaseWidget):
    """
    Text widget for drawing text to screen
    """
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

    def compute_size(self):
        text_width = self.font.measureText(self.text)
        self.computed_width = text_width
        self.computed_height = self.font_size

    def compute_position(self, parent_position):
        self.computed_pos_x = parent_position[0]
        self.computed_pos_y = parent_position[1]
        self.compute_position_self()
        print(self.computed_pos_x, self.computed_pos_y, "computed pos for text")
        for x in self.children:
            x.compute_position([self.computed_pos_x, self.computed_pos_y])

    def draw(self, canvas):
        canvas.drawSimpleText(self.text, self.computed_pos_x, self.computed_pos_y + self.font_size, font=self.font,
                              paint=self.paint)
