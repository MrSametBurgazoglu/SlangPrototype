class Component(object):
    def __init__(self):
        self.component_name = ""
        self.component_parameters = []
        self.component_widget = None
        self.component_functions = []
        self.parent = None

    def add_child(self, widget):
        self.component_widget = widget
