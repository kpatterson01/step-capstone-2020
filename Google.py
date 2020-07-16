
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

        Calls __create_company method that implements manager hierarchy tree based on the list of
        Googlers and their attributes.

        Args:
            googlers: A list of Googler objects.
        """
        self.company = self.__create_company(googlers)
        self.num_googlers = len(googlers)
        self.googlers = googlers

    def search(self, googler_id):
        """ Searches for and returns the Googler object given their id.

        Args:
            googler_id: An integer representing the id of a googler.

        Returns:
            googler: The Googler object attached with the googler_id.
        """
        googler = next((googler for googler in self.googlers if googler.id == googler_id), None)
        if googler is not None:
            return googler
        raise ReferenceError("No Googler at Google with given id found")

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

        # Current implementation utilizes a dictionary to represent a pseudo company hierarchy.
        # Every Googler is a key with its value being the Googler object that represents its manager.
        company = {}
        for googler in googlers:
            # For every Googler, find their manager and map googler --> manager in dict
            # NOTE: Believe this is implicitly O(n) making this algo O(n^2) :( if you're reading this guys, im using the thinker
            manager = next((manager for manager in googlers if manager.id == googler.manager_id), None)
            if manager is not None:
                company[googler] = manager
        return company

    #Add any required methods for the class
