from . import __summary__, __title__, __version__


class MqGenAbout:

    def __init__(self):
        self.version = __version__
        self.title = __title__
        self.summary = __summary__

    def __str__(self):
        return "%s %s version %s" % (__title__, __summary__, __version__)
