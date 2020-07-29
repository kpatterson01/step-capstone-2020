class Rule:

    def __init__(self, param_list):
        self.param_list = param_list
        self.rule = self.__build_rule()

    def __build_rule(self):
        OR = lambda a,b : a or b
        AND = lambda a,b: a and b
        EQ = lambda a,b: a == b
        NEQ = lambda a,b: a != b

        expression_1 = lambda user, comp, num: comp(user.department,num)
        rule = lambda user: expression_1(user,EQ,13)
        return rule

    def passes(self,user):
        return self.rule(user)
