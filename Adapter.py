"""Leonardo Rios Oviedo   23/11/2017 GITI9071-e"""

class korean:
    """korean speaker"""
    def __init__(self):
        self.name = "korean"

    def speak_korean(self):
        return "An_neyong?"

class British:
    """english speaker"""
    def __init__(self):
        self.name = "British"

    #note the diference method name here!
    def speak_english(self):
        return "Hello!"

class Adapter:
    """This changes the generic method name to individualized method names"""

    def __init__(self, object, **adapted_method):
        """Change the name if the method"""
        self._object = object

        #Add a new dictionary item that establishes the mapping between the generic method name: speak() and the concrete method
        #for example speak() will be traslated to speak_korean() if the mapping says so
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        """Simply return the best of atributes"""
        return  getattr(self._object, attr)
#List to store speaker objects
objects = []

#Create a korean object
korean = korean()

#create a Britash object
british = British()

#append the objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_korean))
objects.append(Adapter(british, speak=british.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))


