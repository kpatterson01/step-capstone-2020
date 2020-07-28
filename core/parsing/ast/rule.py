from node import Node
from expressions import Meta_Expression

class Rule(Node):

    def __init__(meta_expr):
        if not isinstance(meta_expression, Meta_Expression):
            self.meta_expr = meta_expr
        else:
            raise ValueError('Rules only take meta expressions as arguments')


    def get_lambda():
        return self.meta_expr.get_lambda()

