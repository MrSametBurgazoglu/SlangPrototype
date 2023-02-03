class BaseWidget(object):
    def __init__(self):
        self.extend_classes = {}
        self.pos_x = 0
        self.pos_y = 0
        self.width = 0
        self.height = 0
        self.children = []

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def add_child(self, child):
        self.children.append(child)
