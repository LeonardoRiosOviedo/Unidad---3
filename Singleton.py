"""Leonardo Rios Oviedo   23/11/2017 GITI9071-e"""


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state #make it an attribute dictionary

class Singleton(Borg):#Inherits from the Borg class
    """This class now shares all its attributes among its various instances"""
    #This essenstially makes the singleton objects an objects-otiented global variable

    def __init__(self, **kwargs):
        Borg.__init__(self)
        #Update the attribute dictionary by inserting a new-value pair
        self._shared_state.update(kwargs)

    def __str__(self):
        #Returns the attribute dictionary for printing
        return str(self._shared_state)

#let´s create a singleton objects and add our first acronym
x = Singleton(HTTP = "Hyper Text Transfer Protocol")
# Print the object
print(x)

#Let´s create another singleton object and if it refers to the same atribute dictionary by adding another acronym.
y = Singleton(SNMP = "Simple Network Managment Protocol")
print(y)