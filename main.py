from Parser.Parser import Parser


class Main(object):
    filepath = None

    def __init__(self, filepath):
        self.filepath = filepath
        self.parser = None
        self.main_widget = None
        self.functions = None
        self.components = None

    def parse_file(self):
        self.parser = Parser(self.filepath)
        line = self.parser.parse_line()
        while line:
            print(line)
            line = self.parser.parse_line()
        self.main_widget, self.components, self.functions = self.parser.get_context()
        print(self.main_widget, self.components, self.functions)

    def render_document(self):
        pass


if __name__ == "__main__":
    program = Main("example.slang")
    program.parse_file()
    while True:
        program.render_document()
        break
