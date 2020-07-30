from .node import Node

class Key(Node):
    ''' abstract key '''
    pass

class Id(Key):
    
    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.id

class Department(Key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.department

class Cost_Center(Key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.cost_center

class Manager_Id(Key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.manager_id

class Location(Key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.location

class Lowest_Dir_Id(Key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.lowest_dir_id

class Job_Family(Key):

    def __init__(self):
        pass

    def get_lambda(self):
        return lambda user: user.job_family
