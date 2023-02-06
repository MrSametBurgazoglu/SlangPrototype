from Widgets import BaseWidget


class Component(object):
    """
    Components are widget holder with constructor functions
    A component must have one Widget and that Widget can have other widgets.
    A component can have more than one constructor function with different parameters
    """
    def __init__(self):
        self.component_name = ""
        self.component_widget = None
        self.component_functions = []
        self.parent = None

    def add_child(self, widget: BaseWidget):
        """

        :param widget:
        :return:
        """
        self.component_widget = widget
