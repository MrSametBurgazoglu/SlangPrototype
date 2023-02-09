class SingletonClass(object):
    def __init__(self):
        self.root_widget = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance


root_widget = SingletonClass()
