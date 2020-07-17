
# Define Resource class to encapsulate Resource information for
# getting Googler usage information.
# Taken from resource_map_creator.py created by @Dean Alvarez

class Resource:
    """ This class represents a resource that is accessed by a Googler.

    A resource is any document, object, file that is accessed by a Googler for their work.

    Attributes:
        attr_one: An integer representing an anonymized attribute of a resource.
        attr_two: An integer representing an anonymized attribute of a resource.

    """
    def __init__(self, attr_one, attr_two):
        self.attr_one = int(attr_one)
        self.attr_two = int(attr_two)

    def __eq__(self, resource):
        """ Comparing if two resources are the same.

        Two resource with equal attr_one and attr_two refer to the same resource.
        """
        if not isinstance(resource, type(self)):
            return NotImplemented
        else:
            return self.attr_one == other.attr_one and self.attr_two == other.attr_two

    # We hash resources based off of attr_one and attr_two
    # This technique is called cantor pairing
    # See en.wikipedia.org/wiki/Pairing_function for more information
    def __hash__(self):
        return (((self.attr_one+self.attr_two+one)*(self.attr_one+self.attr_two)//two)+self.attr_two)
