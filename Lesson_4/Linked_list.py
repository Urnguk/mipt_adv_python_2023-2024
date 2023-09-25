class Node:
    def __init__(self, value, prev_pointer=None, next_pointer=None):
        self._val = value
        self._prev_ptr = prev_pointer
        self._next_ptr = next_pointer

    def get_value(self):
        return self._val

    def set_value(self, x):
        self._val = x

    def get_prev_pointer(self):
        return self._prev_ptr

    def set_prev_pointer(self, x):
        self._prev_ptr = x

    def get_next_pointer(self):
        return self._next_ptr

    def set_next_pointer(self, x):
        self._next_ptr = x


class Linked_list:
    def __init__(self):
        self._head = None
        self._tale = None
        self._len = 0

    def __len__(self):
        return self._len

    def append(self, x):
        curr_node = Node(x, self._tale)
        if len(self) == 0:
            self._head = curr_node
        else:
            self._tale.set_next_pointer(curr_node)
        self._tale = curr_node
        self._len += 1

    def pop(self):
        if len(self) > 1:
            res = self._tale.get_value()
            self._tale = self._tale.get_prev_pointer()
            self._tale.set_next_pointer(None)
            self._len -= 1
        elif len(self) == 1:
            res = self._tale.get_value()
            self._tale = None
            self._head = None
            self._len -= 1
        else:
            res = None
        return res

    def __getitem__(self, item):
        curr_node = self._head
        for i in range(item):
            curr_node = curr_node.get_next_pointer()
        return curr_node.get_value()

    def __str__(self):
        return "[" + ", ".join(str(self[i]) for i in range(len(self))) + "]"


# X = Linked_list()
# X.append(5)
# X.append(-2)
# X.append("abc")
# X.append(6)
# print(X.pop())
# print(len(X))
# print(X[1])
# print(X)



