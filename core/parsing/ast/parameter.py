from node import Node

class Parameter(Node):

    def __init__(self, key, comp, value):
        if(isinstance(key,Key) and isinstance(comp,Comparator) 
                and isinstance(value,Value)):
            self.key = key
            self.comp = comp
            self.value = value
        else:
            raise ValueError('Invalid types of input for Parameter')

    def get_lambda():
        comparator = self.comp.get_lambda()
        key = self.key.get_lambda()
        value = self.value.get_lambda()
        param = lambda user: comparator(key(user),value(user))
        return param
