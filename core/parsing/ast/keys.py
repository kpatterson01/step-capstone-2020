from node import Node

class key(Node):
    ''' abstract key '''
    pass

class id(key):
    
    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.id

class department(key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.department

class cost_center(key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.cost_center

class manager_id(key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.manager_id

class location(key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.location

class lowest_dir_id(key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.lowest_dir_id

class job_family(key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.job_family
