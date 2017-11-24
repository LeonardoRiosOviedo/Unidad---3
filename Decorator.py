"""Leonardo Rios Oviedo   23/11/2017 GITI9071-e"""

from functools import wraps
def make_blink(function):
    """Defines the decorator"""

    #this makes the decorator transparent in terms if its name and docstring
    @wraps(function)
    #Define the inner function
    def decorator():
        #Grap the return value of the function being decorated
         ret=function()
        #Add new functionality to the function being decorated
         return "<blink" +ret+"</blink>"

    return decorator

#Apply the decorator here!
@make_blink
def hello_world():
    """Original function!"""

    return "Hello, World"

#Check the result of decorating
print(hello_world())
#Check if the function name is till the name of the function being decorated
print(hello_world.__name__)
#Check if the docstring is still the same as that if the function being decorated
print(hello_world.__doc__)
