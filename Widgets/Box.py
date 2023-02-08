import skia

from .BaseWidget import BaseWidget
from .SubWidgets import VBox, HBox

class BoxWidget(BaseWidget):
    """
    BoxWidget is a box for other widgets.
    Its orientation can be vertical or horizontal
    Its horizontal align can be "begin", "center", "end
    Its vertical align can be "begin", "center", "end
    """
    def __init__(self):
        super().__init__()
        self.orientation = "vertical"
        self.horizontal_align = "center"
        self.vertical_align = "center"
        self.spacing = 0
        self.reverse = False

    def set_orientation(self, orientation):
        self.orientation = orientation

    def set_horizontal_align(self, align):
        self.horizontal_align = align

    def set_vertical_align(self, align):
        self.vertical_align = align

    def set_spacing(self, spacing):
        self.spacing = int(spacing)

    def set_reverse(self, reverse):
        if reverse == "True":
            self.reverse = True

    def compute_size_by_orientation(self):
        if self.orientation == "vertical":
            maximum_width = 0
            for x in self.children:
                maximum_width = max(maximum_width, x.computed_width)
            self.computed_width = max(self.computed_width, maximum_width)
        else:
            maximum_height = 0
            for x in self.children:
                maximum_height = max(maximum_height, x.computed_height)
            self.computed_height = max(self.computed_height, maximum_height)

    def get_space_size(self):
        if self.orientation == "vertical":
            self.computed_height += (len(self.children)-1) * self.spacing
        else:
            self.computed_width += (len(self.children) - 1) * self.spacing

    def compute_size(self):
        self.compute_size_self()
        self.get_space_size()
        self.compute_size_by_orientation()
        for x in self.children:
            x.compute_size()
        self.compute_size_self()
        self.compute_size_by_orientation()

    def compute_child_positions_x(self):
        if self.orientation == "vertical":
            return VBox.VBox.compute_child_positions_x(self.children, self.horizontal_align, self.computed_pos_x, self.computed_width)
        else:
            if not self.reverse:
                return HBox.HBox.compute_child_positions_x(self.children, self.horizontal_align, self.computed_pos_x, self.computed_width, self.spacing)
            else:
                return HBox.HBox.compute_child_positions_x_reverse(self.children, self.horizontal_align, self.computed_pos_x, self.computed_width, self.spacing)

    def compute_child_positions_y(self):
        if self.orientation == "vertical":
            if not self.reverse:
                return VBox.VBox.compute_child_positions_y(self.children, self.vertical_align, self.computed_pos_y, self.computed_height, self.spacing)
            else:
                return VBox.VBox.compute_child_positions_y_reverse(self.children, self.vertical_align, self.computed_pos_y, self.computed_height, self.spacing)
        else:
            return HBox.HBox.compute_child_positions_y(self.children, self.vertical_align, self.computed_pos_y, self.computed_height)

    def compute_child_positions(self):
        pos_x_list = self.compute_child_positions_x()
        pos_y_list = self.compute_child_positions_y()
        for children, pos in zip(self.children, zip(pos_x_list, pos_y_list)):
            children.computed_pos_x = pos[0]
            children.computed_pos_y = pos[1]

    def compute_position(self, parent_position):
        self.computed_pos_x = parent_position[0]
        self.computed_pos_y = parent_position[1]
        super().compute_position(parent_position)
        self.compute_child_positions()
        for x in self.children:
            x.compute_position([x.computed_pos_x, x.computed_pos_y])

    def draw(self, canvas):
        rect = skia.Rect()
        rect.setXYWH(self.computed_pos_x, self.computed_pos_y, self.computed_width, self.computed_height)
        paint = skia.Paint()
        paint.setARGB(255, 0, 0, 0)
        paint.setStyle(skia.Paint.Style.kStroke_Style)
        paint.setStrokeWidth(4)
        canvas.drawRect(rect, paint)
        for x in self.children:
            x.draw(canvas)
