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

    def render(self, canvas):
        self.compute_metrics()
        for x in self.children:
            x.render(canvas)
        self.compute_metrics()
        self.rect.setXYWH(self.computed_pos_x, self.computed_pos_y, self.computed_width, self.computed_height)
        print(self.computed_pos_x, self.computed_pos_y, self.computed_width, self.computed_height, self.color, "wow")

    def draw(self, canvas):
        canvas.drawRect(self.rect, self.paint)
        for x in self.children:
            x.draw(canvas)
