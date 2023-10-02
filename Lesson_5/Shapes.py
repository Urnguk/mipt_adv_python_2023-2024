class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"


def dist(p1, p2):
    return ((p2.get_y() - p1.get_y()) ** 2 + (p2.get_x() - p1.get_x()) ** 2) ** 0.5


class Shape:
    def __init__(self, type="Shape"):
        self._type = type

    def __str__(self):
        return str(self._type)


class Triangle(Shape):
    def __init__(self, p1, p2, p3, type="Triangle"):
        super().__init__(type)
        self._point_1 = p1
        self._point_2 = p2
        self._point_3 = p3

    # def __str__(self):
    #     return " ".join([super().__str__(), self._point_1.__str__(), self._point_2.__str__(),
    #                      self._point_3.__str__()])


a = Triangle(Point(), Point(1, 1), Point(2, 3))
print(a)
