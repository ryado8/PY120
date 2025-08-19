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

oracle = Oracle()
print(oracle.predict_the_future())

"""
On Line 15, the Oracle class instantiates an instance object "oracle". The instance method predict_the_future is invoked on the
oracle object. The choices() instance method is called on the instance object oracle, or self, which returns a list of four strings.
A random choice is chosen among these strings and the string is returned. Everytime the predict_the_future method is called, a string
"You will" and a random string from choices list will be concatenated and returned.
"""