# Here is an example for a valid Abstract Method inside a class

from abc import abstractmethod


class Fruits:

    @abstractmethod
    def Taste(self):
        pass


t = Fruits()
t.Taste()