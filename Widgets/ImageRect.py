import skia

from .BaseWidget import BaseWidget


class ImageRectWidget(BaseWidget):
    """
    A ImageRect is widget for drawing an image to with one color.
    Like other widgets it can have child widgets.
    :param self.image_source:
    """
    def __init__(self):
        super().__init__()
        self.source = None
        self.image = None
        self.paint = skia.Paint()
        self.rect = skia.Rect()

    def set_source(self, path):
        self.source = path

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
        self.image = skia.Image.open(self.source)
        self.rect.setXYWH(self.computed_pos_x, self.computed_pos_y, self.computed_width, self.computed_height)
        canvas.drawImage(self.image, 0, 0, self.paint)
        for x in self.children:
            x.draw(canvas)
