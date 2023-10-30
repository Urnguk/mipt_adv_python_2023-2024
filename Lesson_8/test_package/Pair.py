class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod                    # часто используется как альтернативный инициализатор
    def init_from_tuple(cls, t):
        return cls(t[0], t[1])

    @staticmethod
    def dist(a, b):
        return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5


# print(2)
if __name__ == "__main__":
    a = Pair(3, 4)
    b = Pair.init_from_tuple((0, 0))
    print(Pair.dist(a, b))

