import math


class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_distance(self, other):
        return math.sqrt((self._x - other._x)**2 + (self._y - other._y)**2)

    @property
    def coordinates(self):
        return self._x, self._y

    @coordinates.setter
    def coordinates(self, value):
        self._x, self._y = value


# Пример использования:
point1 = Point(3, 4)
point2 = Point(6, 8)

print("Координаты точки 1:", point1.coordinates)
print("Координаты точки 2:", point2.coordinates)

distance = point1.get_distance(point2)
print("Расстояние между точками:", distance)

point1.coordinates = (5, 7)
print("Новые координаты точки 1:", point1.coordinates)
