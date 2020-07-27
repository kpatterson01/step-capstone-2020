import unittest
from tokenizer import Tokenizer

class TestTokenizerFunctionality(unittest.TestCase):

    def test_simple_case(self):
        expected_tokens = ['id', '==', '123']
        string = "id == 123"
        self.assertEqual(expected_tokens, Tokenizer.tokenize(string))

    def test_extra_spaces_outer(self):
        expected_tokens = ['id', '==', '123']
        string = "    id == 123            "
        self.assertEqual(expected_tokens, Tokenizer.tokenize(string))

    def test_invalid_token(self):
        with self.assertRaises(Exception):
            string = "badtoken == 123"
            Tokenizer.tokenize(string)

    def test_simple_paren_case(self):
        expected_tokens = ['(','id', '==', '123',')']
        string = "(id == 123)"
        self.assertEqual(expected_tokens, Tokenizer.tokenize(string))

    def test_AND_case(self):
        expected_tokens = ['(','id','==','123',')','and',
                '(','department','!=','456',')']
        string = "(id == 123) AND (department != 456)"
        self.assertEqual(expected_tokens, Tokenizer.tokenize(string))

    def test_nested_paren_case(self):
        expected_tokens = ['(','(','id','==','123',')','and',
                '(','department','!=','456',')',')']
        string = "((id == 123) AND (department != 456))"
        self.assertEqual(expected_tokens, Tokenizer.tokenize(string))


if __name__ == "__main__":
    unittest.main()
