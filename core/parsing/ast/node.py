from abc import ABC, abstractmethod

class Node(ABC):

    @abstractmethod
    def get_lambda(self):
        pass
