class BaseWidget(object):
    def __init__(self):
        self.extend_classes = {}
        self.name = ""
        self.pos_x = ""
        self.pos_y = ""
        self.width = ""
        self.height = ""
        self.computed_pos_x = 0
        self.computed_pos_y = 0
        self.computed_width = 0
        self.computed_height = 0
        self.children = []
        self.parent = None

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def set_width(self, width: str):
        self.width = width

    def set_height(self, height: str):
        self.height = height

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

    def compute_position_self(self):
        if self.pos_x.endswith("px"):
            self.computed_pos_x += int(self.pos_x[:-2])
        if self.pos_y.endswith("px"):
            self.computed_pos_y += int(self.pos_y[:-2])

    def compute_size_self(self):
        self.compute_height()
        self.compute_width()

    def set_name(self, name):
        self.name = name

    def add_child(self, child):
        self.children.append(child)
