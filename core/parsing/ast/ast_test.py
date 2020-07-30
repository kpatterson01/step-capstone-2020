import unittest
import inspect
from comparators import *
from conjunctions import *
from expressions import *
from keys import *
from node import Node
from parameter import Parameter
from rule import Rule
from value import Value

class mock_user():
    def __init__(self,user_id,department):
        self.id = user_id
        self.department = department

class test_ast_build(unittest.TestCase):

    def test_simple_case(self):
        id_node = Id()
        val_node = Value(13)
        comp_node = Equal()
        param_node = Parameter(id_node,comp_node,val_node)
        expr_node = Parameter_Expression(param_node)
        meta_expr_node = Meta_Expression(expr_node)
        rule_node = Rule(meta_expr_node)
        expected = lambda user: user.id == 13
        actual = rule_node.get_lambda()
        a_user = mock_user(13,13)
        another_user = mock_user(20,20)
        self.assertEqual(expected(a_user),actual(a_user))
        self.assertEqual(expected(another_user),actual(another_user))

if __name__ == "__main__":
    unittest.main()
