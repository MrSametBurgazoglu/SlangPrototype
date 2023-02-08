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

    def set_source(self, path):
        self.source = path
        self.image = skia.Image.open(self.source)

    def compute_size(self):
        self.compute_size_self()
        for x in self.children:
            x.compute_size()
        self.compute_size_self()
        image_size = self.image.dimensions()
        self.computed_width = image_size.width()
        self.computed_height = image_size.height()

    def compute_position(self, parent_position):
        self.computed_pos_x = parent_position[0]
        self.computed_pos_y = parent_position[1]
        super().compute_position(parent_position)
        for x in self.children:
            x.compute_position([self.computed_pos_x, self.computed_pos_y])

    def draw(self, canvas):
        canvas.drawImage(self.image, self.computed_pos_x, self.computed_pos_y, self.paint)
        for x in self.children:
            x.draw(canvas)
