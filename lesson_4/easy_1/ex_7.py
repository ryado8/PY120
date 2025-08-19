import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

class RoadTrip(Oracle):
    def choices(self):
        return [
            'visit Vegas',
            'fly to Fiji',
            'romp in Rome',
            'go on a Scrabble cruise',
            'get hopelessly lost',
        ]

trip = RoadTrip()
print(trip.predict_the_future())

"""
On line 25, the RoadTrip class instantiates a new object 'trip'. When predict_the_future is called on trip, trip is able to access the
method since RoadTrip inherits the instance method from Oracle class. However, the self within the method definition points to the trip
object, so seelf.choices() will return the list defined within the choices method in the RoadTrip class. Therefore, the method will output
one of five strings within the list in the choices instance method of the RoadTrip class.
"""