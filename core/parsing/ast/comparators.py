from .node import Node

class Comparator(Node):
    ''' This is effectively an abstract class for comparators '''
    ''' Its main use is being able to check isinstance(Comparator) '''
    pass

class Equal(Comparator):
    
    def __init__(self):
        pass

    def get_lambda(self):
        return lambda a,b: a == b

class Not_Equal(Comparator):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda a,b: a != b
