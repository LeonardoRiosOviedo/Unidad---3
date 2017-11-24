"""Leonardo Rios Oviedo   23/11/2017 GITI9071-e"""


class Dog:
    """One of the objects to be returned"""

    def speak(self):
        return "Woof!"
    def __str__(self):
        return "Dog"

class DogFactory:
    """concrete Factory"""

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """Returns a dog Food objects"""
        return "Dog Food"

class PetStore:
    """PetStore houses our abstract Factory"""

    def __init__(self, pet_factory=None):
        """ pet_factory our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display the details of the objects retured by the DogFactory"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))

#create a concrete Factory
factory = DogFactory()

#Create a pet store housing our Abstract Factory
shop = PetStore(factory)

#Invoke the utility method to show details of our pet
shop.show_pet()





