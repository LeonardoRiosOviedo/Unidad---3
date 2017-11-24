"""Leonardo Rios Oviedo   23/11/2017 GITI9071-e"""


class Handler: #Abstract handler
    """Abstract Handler"""
    def __init__(self, successor):
        self._successor = successor# Define who is the nex handler

    def handle(self, request):
        handled = self._handle(request)#If handler, stop here

        #Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')

class ConcreteHandler1(Handler):# Inherits from the abstract hadler
    """Concrete hadler 1"""
    def _handle(self, request):
        if 0 < request <=10:#Provide a condition for handling
            print("Request {} handled in handler 1".format(request))
            return True # Indicates that the request has been handled

class DefaultHandler(Handler): # Inherits from the abstract handler
    """Dafault handler"""

    def _handle(self, request):
        """If there is no handler available"""
        #No condition chacking since this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True # Indicates that the request has been handler

class Client:#Using handlers
    def __init__(self):
         self.handler = ConcreteHandler1(DefaultHandler(None))# Create handlers and use them in a sequence you want
                                                            #Note that default handler has no successor

    def delegate(self, requests):# Send your requests one at a time for handlers to handle
        for request in requests:
            self.handler.handle(request)

# Create a client
c = Client()

#Create request
requests = [2,5,30]
#Send th requests
c.delegate(requests)