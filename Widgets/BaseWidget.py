from Renderer import utils


class BaseWidget(object):
    """
    BaseWidget is subclass for all widgets.
    A widget can extend some classes (especially input classes).
    It is a base class, so it cannot be used by user
    """
    def __init__(self):
        self.extend_classes = {}
        self.name = ""
        self.pos_x = ""
        self.pos_y = ""
        self.width = "max-content"
        self.height = "max-content"
        self.margin_top = ""
        self.margin_bottom = ""
        self.margin_left = ""
        self.margin_right = ""
        self.computed_pos_x = 0
        self.computed_pos_y = 0
        self.computed_height = 0
        self.computed_width = 0
        self.computed_margin_top = 0
        self.computed_margin_bottom = 0
        self.computed_margin_left = 0
        self.computed_margin_right = 0
        self.children = []
        self.parent = None

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def set_width(self, width: str):
        self.width = width

    def set_height(self, height: str):
        self.height = height

    def set_name(self, name):
        self.name = name

    def set_margin(self, top, bottom, left, right):
        self.margin_top = top
        self.margin_bottom = bottom
        self.margin_left = left
        self.margin_right = right
        self.computed_margin_top = int(self.margin_top)
        self.computed_margin_bottom = int(self.margin_bottom)
        self.computed_margin_left = int(self.margin_left)
        self.computed_margin_right = int(self.margin_right)

    def compute_width(self):
        if self.width.endswith("px"):
            self.computed_width = int(self.width[:-2])
        elif self.width.endswith("%"):
            self.computed_width = self.parent.computed_width * int(self.width[:-1]) / 100
        elif self.width == "max-content":
            new_width = 0
            for x in self.children:
                new_width += x.computed_width
            self.computed_width = new_width


    def compute_height(self):
        if self.height.endswith("px"):
            self.computed_height = int(self.height[:-2])
        elif self.height.endswith("%"):
            self.computed_height = self.parent.computed_height * int(self.height[:-1]) / 100
        elif self.height == "max-content":
            new_height = 0
            for x in self.children:
                new_height += x.computed_height
            self.computed_height = new_height


    def compute_position_x(self):
        if self.pos_x.endswith("px"):
            self.computed_pos_x += int(self.pos_x[:-2])
        elif self.pos_x.endswith("%"):
            current_pos_x = self.computed_pos_x
            current_pos_x += self.parent.computed_width * int(self.pos_x[:-1]) / 100
            self.computed_pos_x = current_pos_x

    def compute_position_y(self):
        if self.pos_y.endswith("px"):
            self.computed_pos_y += int(self.pos_y[:-2])
        elif self.pos_y.endswith("%"):
            current_pos_y = self.computed_pos_y
            current_pos_y += self.parent.computed_height * int(self.pos_y[:-1]) / 100
            self.computed_pos_y = current_pos_y

    def compute_position(self, start_position):
        self.compute_position_x()
        self.compute_position_y()

    def compute_size_self(self):
        self.compute_height()
        self.compute_width()

    def add_child(self, child):
        self.children.append(child)

    def is_inside(self, pos_x, pos_y):
        return utils.in_rect(pos_x, pos_y, self.computed_pos_x, self.computed_pos_y, self.computed_width, self.computed_height)