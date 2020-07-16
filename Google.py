
# Defines a Google class that encapsulates managerial hierarchy tree
# and provides several functions to manipulate and analyze the organizational hierarchy.

class Google:
    """ This class simulates the managerial hierarchy tree of Googlers.

    The class takes in a list of Googlers and creates a tree structure that can be used
    to calculate the 1) Distance between two Googlers based on the go/who properties and
    2) Usage similarity based on resources they've accessed.

    Attributes:
        ceo: A Googler object with no manager_id acting as the head node of the tree.
        num_googlers: An integer count of Googlers within the company.
        googlers: An array of Googler objects with all Googlers in the company.
    """

    def __init__(self, googlers):
        """ Creates Google company.

        Calls __create_company method which implements manager hierarchy tree based on the list of
        Googlers and their attributes.

        Args:
            googlers: A list of Googler objects.
        """
        self.ceo = self.__create_company(googlers)
        self.num_googlers = len(googlers)
        self.googlers = googlers

    def search(self, googler_id):
        """ Searches for and returns the Googler object given their id.

        Args:
            googler_id: An integer representing the id of a googler.

        Returns:
            googler: The Googler object attached with the googler_id.
        """
        #TODO: Implement Googler Search function
        return

    def distance(self, googler_one, googler_two):
        """ Returns the distance of two Googlers in the managerial hierarchy.

        A lower distance corresponds to Googlers who have more similar attribtues.
        A higher distance corresponds to Googlers who have less similar attributes.

        Args:
            googler_one: A Googler object.
            googler_two: A Googler object.

        Returns:
            distance: An integer representing their similarity or distance in the tree.
        """
        #TODO: Implement function to determine distance between to Googlers.
        return

    def usage_similarity(self, googler_one, googler_two):
        """ Returns a usage similarity metric of two Googlers in the managerial hierarchy based
            off of the resources that Googler has accessed in a set period of time.

        A lower number corresponds to Googlers who are closer together in the tree and have more similar attribtues.
        A higher number corresponds to Googlers who are farther away in the tree and are less similar.

        Args:
            googler_one: A Googler object.
            googler_two: A Googler object.

        Returns:
            metric: An integer representing their usage similarity.
        """
        #TODO: Implement function to determine distance between googler.
        return smth

    def __create_company(self, googlers):
        """ Creates managerial hierarchy tree of Google company.

        Args:
            googlers: An list of Googler objects.

        """
        #TODO: Implement function to create managerial hierarchy.
        return

    #Add any required methods for the class
