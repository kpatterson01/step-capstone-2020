
# Defines a Company class that encapsulates managerial hierarchy tree
# and provides several functions to manipulate and analyze the organizational hierarchy.

import json
from .employee import Employee
from .resource import Resource

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

    def __init__(self, employees, ceo):
        """ Creates Google company.

        Calls __create_directory method that implements manager hierarchy tree based on the list of
        employees and their attributes.

        Args:
            employees: A list of employee objects.
            ceo: An int representing where the managerial hierarchy should start., CEO manager is always -1
        """
        self.company = self.__create_directory(employees)
        self.ceo = int(ceo)
        self.hierarchy = self.__create_hierarchy(employees)
        # self.depth = self.__max_depth(employees)
        self.num_employees = len(employees)
        self.employees = employees

    def __str__(self):
        return json.dumps(self.hierarchy, indent=2)

    def __create_directory(self, employees):
        """ Creates directory Google company.

        Args:
            employees: A list of employee objects.

        Returns:
            company: A dictionary with <employee.id:Employee objects>
        """
        company = {}
        for employee in employees:
            company[employee.id] = employee

        for employee in employees:
            if(company.get(employee.manager_id) is not None):
                manager = company.get(employee.manager_id)
                manager.add_report(employee)

        return company

    def __create_hierarchy(self, employees):
        """ Creates managerial hierarchy tree of Google company.

        Args:
            employees: A list of employee objects.

        Returns:
            hierarchy: A dictionary representing managerial hierarchy.
        """
        ceo = self.search(self.ceo)
        return self.__to_dict(ceo) #Create hierarchal structure starting with CEO

    def __to_dict(self, employee):
        """ Recursive function to create dictonary hierarchy """
        if(len(employee.reports) == 0): return { "Employee": employee.id }

        hierarchy = {"Employee": employee.id, "Reports":[]}
        for report in employee.reports:
            hierarchy.get("Reports").append(self.__to_dict(report))

        return hierarchy

    # def __max_depth(self, employees): #Can be improved using a DFS with new hierarchy data structure, come back to if time
    #     """ Calculates max depth of company aka distance from lowest employee to CEO. """
    #     max_depth = 0
    #     for employee in employees:
    #         employee_managers = set()
    #         if(employee.manager_id != -1):
    #             employee_manager = self.company.get(employee.manager_id)
    #             while(employee_manager is not None):
    #                 employee_managers.add(employee_manager)
    #                 employee_manager = self.company.get(employee_manager.manager_id)
    #         if(len(employee_managers) > max_depth): max_depth = len(employee_managers)
    #     return max_depth



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
        if(employee_one.manager_id == -1): employee_one_managers.add(employee_one.id)
        if(employee_two.manager_id == -1): employee_two_managers.add(employee_two.id)
        while(len(employee_one_managers.intersection(employee_two_managers)) == 0):
            if(employee_one.manager_id != -1):
                employee_one_managers.add(employee_one.manager_id)
                employee_one = self.search(employee_one.manager_id)
            if(employee_two.manager_id != -1):
                employee_two_managers.add(employee_two.manager_id)
                employee_two = self.search(employee_two.manager_id)

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
            metric: A float representing their usage similarity.
        """
        employee_one_resources = set(employee_one.resources)
        employee_two_resources = set(employee_two.resources)
        num_in_common = len(employee_one_resources.intersection(employee_two_resources))
        num_total = len(employee_one_resources) + len(employee_two_resources) - num_in_common
        if(num_total == 0 or num_in_common == 0): return 0
        return num_in_common/num_total
