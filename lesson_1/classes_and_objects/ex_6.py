class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self._speed = 0

    def turn_on(self):
        print(f"{self._model} turned on.")

    def accelerate(self, speed_increase):
        self._speed += speed_increase
        print(f"{self._model} is accelerating by {speed_increase} mph.")

    def brake(self, speed_decrease):
        self._speed = max(0, self._speed - speed_decrease)
        print(f"{self._model} is decelerating by {speed_decrease} mph.")

    def turn_off(self):
        self._speed = 0
        print(f"{self._model} turned off.")

    def current_speed(self):
        print(f"{self._model}'s current speed is {self._speed} mph.")

mazda = Car('Mazda3', 2020, 'black')
mazda.turn_on()
mazda.accelerate(30)
mazda.current_speed()
mazda.brake(20)
mazda.current_speed()
mazda.turn_off()