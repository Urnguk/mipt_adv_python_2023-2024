# print(len(4))

# class A:
#     pass
# print(len(A()))

# class B:
#     def __len__(self):
#         return 0
#
#
# print(len(B()))

# print(isinstance("abc", int))
# print(isinstance("abc", str))

# x = 4
# if isinstance(x, (float, int)):
#     print("this is a number")

# class Pair:
#     def __init__(self, x=0, y=0):
#         self._x = x
#         self._y = y
#
#     def get_x(self):
#         return self._x
#
#     def get_y(self):
#         return self._y
#
#     def __abs__(self):
#         return (self._x ** 2 + self._y ** 2) ** 0.5
#
#     def __str__(self):
#         return "{} {}".format(self._x, self._y)
#
#     def __add__(self, other):
#         if isinstance(other, Pair):
#             return Pair(self.get_x() + other.get_x(), self.get_y() + other.get_y())
#         elif isinstance(other, (int, float)):
#             return Pair(self.get_x() + other, self.get_y() + other)
#
#
# a = Pair(3, 4)
# b = Pair()
# print(a, b)
# print(abs(a), abs(b))
# print(a + b, b + 5, 3 + a)

class Pair:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def __abs__(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

    def __str__(self):
        return "{} {}".format(self._x, self._y)

    def __add__(self, other):
        if isinstance(other, Pair):
            return Pair(self.get_x() + other.get_x(), self.get_y() + other.get_y())
        elif isinstance(other, (int, float)):
            return Pair(self.get_x() + other, self.get_y() + other)

    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return Pair(self.get_x() + other, self.get_y() + other)

    def __eq__(self, other):
        if isinstance(other, Pair):
            # if Pair.get_x == other.get_x() and Pair.get_y == other.get_y():      # красный флаг, конструкция if-else
            #     return True                                                      # дорогая и здесь бесполезна
            # else:
            #     return False
            return self.get_x() == other.get_x() and self.get_y() == other.get_y()
        return False


a = Pair(2, 6)
b = Pair(1)

print(a + b, b + 5, 3 + a)
print(a == b, a == 3, Pair(3, 0) == Pair(3))
