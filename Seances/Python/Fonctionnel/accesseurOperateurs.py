class Car:
    def __init__(self):
        self._speed = 100

    @property
    def speed(self):
        print("Speed est", self._speed)
        return self._speed

    @speed.setter
    def speed(self, value):
        print("Assigné à ", value)
        self._speed = value

car = Car()
#set
car.speed = 100
#get
x = car.speed 