import pickle

# with open("Test_7.txt", mode="r") as f:
#     x = f.readline()
#     for line in f:
#         print(line.strip())

# D = {3: [5, 4, 6], "abc": "abrakadabra", (8, 9): True}


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


class OpenPair:
    def __init__(self, filename):
        self._filename = filename

    def __enter__(self):
        with open(self._filename, mode="rb") as f:
            self._pair = pickle.load(f)
        return self._pair

    def __exit__(self, exc_value, exc_type, exc_traceback):
        with open(self._filename, mode="wb") as f:
            pickle.dump(self._pair, f)


# a = Pair(5, 4)
# b = Pair(3)
#
# with open("backup_data.bin", mode="wb") as file:
#     pickle.dump((a, b), file)

# with open("backup_data.bin", mode="rb") as file:
#     c, d = pickle.load(file)
#
# print(c, d, c + d)
#
# d = Pair(7, 8)
#
# with open("backup_data.bin", mode="wb") as file:
#     pickle.dump((c, d), file)


with OpenPair("backup_data.bin") as p:
    a, b = p
    print(a, b)
    a._x += 1
    print(a, b)

