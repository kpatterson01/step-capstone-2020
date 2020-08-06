
# Defines a employee class encapsulating their information.

class Employee:
    """ This class encapsulates a employees information.

    The class takes in attributes that represent information specific to every employee working at
    Google that can be found on their go/who. These attributes are anonymized integers
    that represent each piece of information.

    Attributes:
        id
        department
        cost_center
        manager_id
        location
        lowest_dir_id
        job_family
        resources: A list of Resource objects that represent resources this employee has accessed.
        reports: A list of Employee objects representing employees who report to this employee object.
    """
    def __init__(self, attributes):
        """Initializes employee object based on anonymized attributes from go/who.

        Args:
            attributes: An JSON object of mapping attributes to integers that represent the attributes.
                        Ex. attributes: { id: 12, job_family: 10 ...}
                            id: 12 --> 854542/Intern
                            job_family: 10 --> Intern-Technical
                            ...
        """
        self.id = int(float(attributes.get("id")))
        self.department = int(float(attributes.get("department")))
        self.cost_center = int(float(attributes.get("cost_center")))
        self.manager_id = int(float(attributes.get("manager_id")))
        self.location = int(float(attributes.get("location")))
        self.lowest_dir_id = int(float(attributes.get("lowest_dir_id")))
        self.job_family = int(float(attributes.get("job_family")))
        # self.person_type = int(float(attributes.get("person_type"))) 
        self.resources = [] #List of Resource objects from resource.py module
        self.reports = []

    def __hash__(self):
        """ Hash function for employee object """
        return hash(self.id)

    def __eq__(self, employee):
        """Compare if two employees are the same person.

        Two employees are only equal if their id's are equal to each other.
        """
        if isinstance(employee, type(self)):
            return self.id == employee.id
        return False

    def __str__(self):
        return 'Employee: '+ f'{self.id}'

    def __repr__(self):
        return 'Employee: '+ f'{self.id}'

    def add_report(self, employee):
        """ Adds the employee to list of reports.

        Args:
            employee: A employee object.
        """
        self.reports.append(employee)

    def add_resource(self, resource):
        """ Adds the resource to list of resources.

        Args:
            resources: An integer id representing the resource. **NOTE: Resource object? @Dean?**
        """
        self.resources.append(resource)

    def get_attributes(self):
        """ Returns attributes in a list.

        Returns:
            Attribute list. Ex. [1, 12, 1, 18, 1219, 220, 1234]
        """
        attr = []
        attr.append(self.department)
        attr.append(self.cost_center)
        attr.append(self.manager_id)
        attr.append(self.location)
        attr.append(self.lowest_dir_id)
        attr.append(self.job_family)
        return attr
