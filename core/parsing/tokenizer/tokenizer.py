from enum import Enum

class Tokenizer:
    accepted_tokens = { '(', ')', 'and', 'or', '==', '!=', 'id', 'department',
            'cost_center', 'manager_id', 'location', 'lowest_dir_id',
            'job_family'}

    # Basic function to tokenize string
    def tokenize(string):
        tokens = []
        string = string.strip()
        start = 0
        for i in range(len(string)):
            if string[i] == ' ':
                tokens.append(string[start:i].strip())
                start = i+1
            elif string[i] == '(':
                tokens.append('(')
                start = i+1
            elif string[i] == ')':
                tokens.append(string[start:i].strip())
                tokens.append(')')
                start = i+1

        tokens.append(string[start:len(string)])

        for token in tokens:
            if not Tokenizer.passes_token_check(token):
                print(token)
                print(string)
                raise Exception('invalid token: ' , token)

        return tokens

    # This is a VERY basic syntax check
    # It returns true if the given token is of the expected form
    def passes_token_check(token):
        return (token in Tokenizer.accepted_tokens) or token.isdigit()
      
