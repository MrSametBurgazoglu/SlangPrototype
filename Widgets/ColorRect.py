import skia

from .BaseWidget import BaseWidget


class ColorRectWidget(BaseWidget):
    """
    A ColorRect is widget for drawing a rect with one color.
    Like other widgets it can have child widgets.
    :param self.color:
    """
    def __init__(self):
        super().__init__()
        self.color = None
        self.paint = skia.Paint()
        self.rect = skia.Rect()

    def set_color(self, color):
        if color == "gray":
            self.paint.setColor(skia.ColorGRAY)
        elif color == "white":
            self.paint.setColor(skia.ColorWHITE)
        elif color == "red":
            self.paint.setColor(skia.ColorRED)
        elif color == "blue":
            self.paint.setColor(skia.ColorBLUE)
        self.color = color

    def compute_size(self):
        self.compute_size_self()
        for x in self.children:
            x.compute_size()
        self.compute_size_self()

    def compute_position(self, parent_position):
        self.computed_pos_x = parent_position[0]
        self.computed_pos_y = parent_position[1]
        super().compute_position(parent_position)
        for x in self.children:
            x.compute_position([self.computed_pos_x, self.computed_pos_y])

    def draw(self, canvas):
        self.rect.setXYWH(self.computed_pos_x, self.computed_pos_y, self.computed_width, self.computed_height)
        canvas.drawRect(self.rect, self.paint)
        for x in self.children:
            x.draw(canvas)
