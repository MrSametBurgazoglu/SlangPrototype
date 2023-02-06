import skia

from .BaseWidget import BaseWidget


class ColorRectWidget(BaseWidget):
    def __init__(self):
        super().__init__()
        self.color = None
        self.paint = skia.Paint()
        self.rect = skia.Rect()

    def set_color(self, color):
        if color == "gray":
            self.color = "gray"
            self.paint.setColor(skia.ColorGRAY)
        self.color = color

    def compute_size(self):
        self.compute_size_self()
        for x in self.children:
            x.compute_size()
        self.compute_size_self()

    def compute_position(self, parent_position):
        self.computed_pos_x = parent_position[0]
        self.computed_pos_y = parent_position[1]
        self.compute_position_self()
        for x in self.children:
            x.compute_position([self.computed_pos_x, self.computed_pos_y])

    def draw(self, canvas):
        self.rect.setXYWH(self.computed_pos_x, self.computed_pos_y, self.computed_width, self.computed_height)
        canvas.drawRect(self.rect, self.paint)
        for x in self.children:
            x.draw(canvas)
