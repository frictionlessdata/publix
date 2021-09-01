class Snippet:
    """Livemark snippet

    API      | Usage
    -------- | --------
    Public   | `from livemark import Snippet`

    Parameters:
        input (str): textual snippet for the snippet
        header (str[]): an array of the snippet's header

    """

    def __init__(self, input, *, header):
        self.__input = input
        self.__header = header
        self.__output = None

    def __setattr__(self, name, value):
        if name == "output":
            self.__output = value
        else:  # default setter
            super().__setattr__(name, value)

    @property
    def input(self):
        return self.__input

    @property
    def output(self):
        return self.__output

    @property
    def header(self):
        return self.__header

    @property
    def lang(self):
        lang = None
        if len(self.__header) >= 1:
            lang = self.__header[0]
        return lang

    @property
    def type(self):
        type = None
        if len(self.__header) >= 2:
            type = self.__header[1]
        return type

    @property
    def props(self):
        props = {}
        for item in self.__header[2:]:
            parts = item.split("=")
            name = parts[0]
            value = parts[1] if len(parts) == 2 else True
            props[name] = value
        return props

    # Process

    def process(self, document):
        for plugin in document.plugins:
            plugin.process_snippet(self)
