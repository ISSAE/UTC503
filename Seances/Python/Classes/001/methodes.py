import math

class Point:
    def __init__(self,x,y):
        self._x=x
        self._y=y
    def getX(self):
        return(self._x)
    def setX(self,x):
        self._x=x
    
    def move(self, x, y):
        self._x = x
        self._y = y
    def reset(self):
        self.move(0, 0)
    def calculer_distance(self, other_point):
        return math.sqrt(
            (self._x - other_point._x) ** 2
            + (self._y - other_point._y) ** 2
        )

class NPoint(Point):
    def translate(self,tx,ty):
        self._x += tx
        self._y += ty


point1 = Point()
point2 = Point()

point1.reset()
point2.move(5, 0)
print(point2.calculer_distance(point1))
assert point2.calculer_distance(point1) == point1.calculer_distance(
    point2
)
point1.move(3, 4)
print(point1.calculer_distance(point2))
print(point1.calculer_distance(point1))

