"""Leonardo Rios Oviedo   23/11/2017 GITI9071-e"""


from copy import copy, deepcopy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attribute"""
        obj = deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    def __init__(self):
        self.name = "Slylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)


c = Car()
prototype = Prototype()
prototype.register_object('Slylark', c)

c1 = prototype.clone('Slylark')
#hace clonacion de variables
print(c1)
