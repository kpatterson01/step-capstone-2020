from .node import Node
from .parameter import Parameter
from .conjunctions import *

class Expression(Node):
    ''' This is just a superclass for the two types of expressions '''
    ''' The idea is that I can just check isinstace(expression) later on '''
    pass

class Meta_Expression(Expression):

    def __init__(self, *args):
        self.expression = None
        self.left = None
        self.conjunction = None
        self.right = None
        if len(args) == 1 and isinstance(args[0],Expression):
            self.expression =  args[0]
        elif (
                len(args) == 3 and isinstance(args[0],Expression)
                and isinstance(args[1],Conjunction)
                and isinstance(args[2],Expression)):

            self.left = args[0]
            self.conjunction = args[1]
            self.right = args[2]
        else:
            raise ValueError("invalid number or type of arguments")

    def get_lambda(self):
        if self.expression is not None:
            return self.expression.get_lambda()
        else:
            conj = self.conjunction.get_lambda()
            left = self.left.get_lambda()
            right = self.right.get_lambda
            meta_lambda = lambda user: conj(left(user),right(user))
            return meta_lambda


class Parameter_Expression(Expression):
 
    def __init__(self, *args):
        self.parameter = None
        self.left = None
        self.conjunction = None
        self.right = None
        if len(args) == 1 and isinstance(args[0],Parameter):
            self.parameter =  args[0]
        elif (
                len(args) == 3 and isinstance(args[0],Parameter)
                and isinstance(args[1],Conjunction)
                and isinstance(args[2],Parameter)):

            self.left = args[0]
            self.conjunction = args[1]
            self.right = args[2]
        else:
            raise ValueError("invalid number or type of arguments")

    def get_lambda(self):
        if self.parameter is not None:
            return self.parameter.get_lambda()
        else:
            conj = self.conjunction.get_lambda()
            left = self.left.get_lambda()
            right = self.right.get_lambda
            expression_lambda = lambda user: conj(left(user),right(user))
            return expression_lambda

