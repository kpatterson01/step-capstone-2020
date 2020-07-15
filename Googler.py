
# Defines a Googler class encapsulating their information on go/who.

class Googler:
    """ This class encapsulates a Googlers information.

    The class takes in attributes that represent information specific to every Googler working at
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
        resources: A list of integers that represent a specific resource.
        reports: A list of Googler objects representing Googlers who report to this Googler object.
    """

    def __init__(self, attributes):
        """Initializes Googler object based on anonymized attributes from go/who.

        Args:
            attributes: An JSON object of mapping attributes to integers that represent the attributes.
                        Ex. attributes: { id: 12, job_family: 10 ...}
                            id: 12 --> 854542/Intern
                            job_family: 10 --> Intern-Technical
                            ...
        """
        self.id = attributes.get("id")
        self.department = attributes.get("department")
        self.cost_center = attributes.get("cost_center")
        self.manager_id = attributes.get("manager_id")
        self.location = attributes.get("location")
        self.lowest_dir_id = attributes.get("lowest_dir_id")
        self.job_family = attributes.get("job_family")
        self.resources = []
        self.reports = []

    def add_report(self, googler):
        """ Adds the googler to list of reports.

        Args:
            googler: A Googler object.
        """
        self.reports.append(googler)

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

    #Add any required methods for the class
