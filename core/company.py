
# Defines a company class that encapsulates managerial hierarchy tree
# and provides several functions to manipulate and analyze the organizational hierarchy.

class Company:
    """ This class simulates the managerial hierarchy tree of a company.

    The class takes in a list of employees and creates a tree structure that can be used
    to calculate the 1) Distance between two employees based on the go/who properties and
    2) Usage similarity based on resources they've accessed.

    Attributes:
        ceo: A employee object with no manager_id acting as the head node of the tree.
        num_employees: An integer count of employees within the company.
        employees: An array of employee objects with all employees in the company.
    """

    def __init__(self, employees):
        """ Creates Google company.

        Calls __create_company method that implements manager hierarchy tree based on the list of
        employees and their attributes.

        Args:
            employees: A list of employee objects.
        """
        self.company = self.__create_company(employees)
        self.num_employees = len(employees)
        self.employees = employees

    def search(self, employee_id):
        """ Searches for and returns the employee object given their id.

        Args:
            employee_id: An integer representing the id of a employee.

        Returns:
            employee: The employee object attached with the employee_id.
        """
        employee = self.company.get(employee_id)
        if employee is not None:
            return employee
        raise ReferenceError("No employee at Google with given id found")

    def distance(self, employee_one, employee_two):
        """ Returns the distance of two employees in the managerial hierarchy.

        A lower distance corresponds to employees who have more similar attribtues.
        A higher distance corresponds to employees who have less similar attributes.

        Args:
            employee_one: A employee object.
            employee_two: A employee object.

        Returns:
            distance: An integer representing their similarity or distance in the tree.
        """
        if(employee_one == employee_two):
            return 0
        employee_one_managers = set()
        employee_two_managers = set()
        while(len(employee_one_managers.intersection(employee_two_managers)) == 0):
            if((employee_one.manager_id is None) and (self.search(employee_one.id) not in employee_one_managers)):
                employee_one_managers.add(employee_one.manager_id)
            else:
                employee_one_managers.add(employee_one.manager_id)
                employee_one = self.search(int(float(employee_one.manager_id)))
            if((employee_two.manager_id is None) and (self.search(employee_two.id) not in employee_two_managers)):
                employee_two_managers.add(employee_two.manager_id)
            else:
                employee_two_managers.add(employee_two.manager_id)
                employee_two = self.search(int(float(employee_two.manager_id)))

        return max(len(employee_one_managers), len(employee_two_managers))

    def usage_similarity(self, employee_one, employee_two):
        """ Returns a usage similarity metric of two employees in the managerial hierarchy based
            off of the resources that employee has accessed in a set period of time.

        A lower number corresponds to employees who are closer together in the tree and have more similar attribtues.
        A higher number corresponds to employees who are farther away in the tree and are less similar.

        Args:
            employee_one: A employee object.
            employee_two: A employee object.

        Returns:
            metric: An integer representing their usage similarity.
        """
        #TODO: Implement function to determine distance between employee.
        return smth

    def __create_company(self, employees):
        """ Creates managerial hierarchy tree of Google company.

        Args:
            employees: An list of employee objects.
        """
        company = {}
        for employee in employees:
            company[int(employee.id)] = employee
        return company

    #Add any required methods for the class
