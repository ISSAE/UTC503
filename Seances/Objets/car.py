print ("Un print de name", __name__)
class Car:

    wheels = 0

    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

if __name__ == '__main__':
    car = Car('red', 'Renault', 2015)
    print(car)