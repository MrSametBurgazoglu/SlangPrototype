class MouseButtonInput(object):
    def __int__(self):
        self.parent = None
        self.connections = {}

    def connect(self, signal, function_name):
        self.connections[signal] = function_name

    def control(self):
        pass