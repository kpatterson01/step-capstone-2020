from .node import Node

class Conjunction(Node):
    ''' This is just a simple pseudo-abstract class '''
    ''' This is created so that I can test is something is a conjunction '''

class AND(Conjunction):

    def __init__(self):
        pass


    def get_lambda(self):
        return lambda a,b: a and b


class OR(Conjunction):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda a,b: a or b


