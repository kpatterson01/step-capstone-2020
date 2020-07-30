from .tokenizer.tokenizer import Tokenizer
from .ast.node import Node
from .ast.value import Value
from .ast.keys import *
from .ast.comparators import *
from .ast.parameter import Parameter
from .ast.conjunctions import *
from .ast.expressions import *
from .ast.rule import Rule

class Syntax_Tree:

    keys = {'id': Id(),
            'department': Department(),
            'cost_center': Cost_Center(),
            'manager_id': Manager_Id(),
            'location': Location(),
            'lowest_dir_id': Lowest_Dir_Id(),
            'job_family': Job_Family()}
    comparators = {'==': Equal(), '!=': Not_Equal()}
    conjunctions = {'and': AND(), 'or': OR()}


    def __init__(self, rule_string):
        self.rule_string = rule_string
        self.ast = self.__build_tree(rule_string)
        self.rule = self.ast.get_lambda()

    def __build_tree(self,rule_string):
        tokens = Tokenizer.tokenize(rule_string)
        ast = self.__build_ast_from_tokens(tokens)
        return ast
    
    def __build_ast_from_tokens(self,tokens):

        if len(tokens) != 3:
            raise NotImplementedError('Advanced Parsing not yet supported')
        else:
            key_node = self.keys[tokens[0]]
            comp_node = self.comparators[tokens[1]]
            value_node = Value(int(tokens[2]))
            param_node = Parameter(key_node,comp_node,value_node)
            expr_node = Parameter_Expression(param_node)
            meta_expr_node = Meta_Expression(expr_node)
            rule_node = Rule(meta_expr_node)
            return rule_node

    def passes(self,user):
        return self.rule(user)
