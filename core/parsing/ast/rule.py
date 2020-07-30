from .node import Node
from .expressions import *

class Rule(Node):

    def __init__(self,meta_expression):
        if isinstance(meta_expression, Expression):
            self.meta_expr = meta_expression
        else:
            raise ValueError('Rules only take meta expressions as arguments')


    def get_lambda(self):
        return self.meta_expr.get_lambda()

