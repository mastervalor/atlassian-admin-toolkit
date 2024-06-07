from calls.confluence import Confluence


class Spaces:

    def __init__(self):
        self.conf = Confluence()

    def create_page(self):
