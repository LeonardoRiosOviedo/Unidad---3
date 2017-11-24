"""Leonardo Rios Oviedo   23/11/2017 GITI9071-e"""

import time

class Producer:
    """Define the 'resourse-intensive objects to instantiate'"""
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Produce has time to meet you now!")

class Proxy:
    """Define the 'relatively less resourses-intensive' proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if Producer is available"""
        print("Artist checking if Producer is available...")

        if self.occupied == 'No':
            #If the producer is available, create a producer objects
             self.producer = Producer()
             time.sleep(2)
             # make the prducer meet the guest!
             self.producer.meet()

        else:
            #Otherwise, dont instanciate a producer
            time.sleep(2)
            print("Producer es busy!")

#Instantiate a proxy
p= Proxy()

#Make the proxy: Artist produce until Producer is available
p.produce()
#Change the state to 'occupied'
p.occupied = 'Yes'
#Make the Producer produce
p.produce()