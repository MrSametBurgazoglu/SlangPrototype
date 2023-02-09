from .BaseWidget import BaseWidget


class MainWidget(BaseWidget):
    """
    MainWidget must be the first widget in widget tree.
    Its directly draw to screen.
    """
    def __init__(self):
        super().__init__()

    def compute_size(self):
        for x in self.children:
            x.compute_size()

    def compute_position(self, start_position):
        super().compute_position(start_position)
        for x in self.children:
            x.compute_position([self.computed_pos_x, self.computed_pos_y])

    def draw(self, canvas):
        for x in self.children:
            x.draw(canvas)

    def change_property(self, widget_name, property_name, value):
        current_widget_list = [self]
        new_widget_list = []
        result = []
        while len(current_widget_list) > 0:
            for x in current_widget_list:
                if x.name == widget_name:
                    result.append(x)
                for y in x.children:
                    new_widget_list.append(y)
            current_widget_list = new_widget_list
            new_widget_list = []
        for x in result:
            setattr(x, property_name, value)
            print(getattr(x, property_name))
        print(result)
        print(widget_name, property_name, value)
