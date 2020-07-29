from .node import Node

class Value(Node):

    def __init__(self, val):
        self.val = val

    def get_lambda(self):
        return lambda: self.val
