class BaseWidget(object):
    def __init__(self):
        self.extend_classes = {}
        self.name = ""
        self.pos_x = 0
        self.pos_y = 0
        self.width = 0
        self.height = 0
        self.children = []
        self.parent = None

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_name(self, name):
        self.name = name

    def add_child(self, child):
        self.children.append(child)
