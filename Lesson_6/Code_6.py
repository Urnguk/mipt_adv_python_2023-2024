# for --------------------

# A = [2, 5, 7, 0, -4, 8]
# it = iter(A)
# print(it)
#
# while True:
#     try:
#         x = next(it)  # x - cycle variable
#         print(x)  # here goes cycle inside
#     except StopIteration:
#         break


# iter --------------------------

# class Stack:
#     def __init__(self, data):
#         self._data = []
#         if isinstance(data, (int, float, str, bool)):
#             self._data.append(data)
#         else:
#             for element in data:
#                 self._data.append(element)
#
#     def __len__(self):
#         return len(self._data)
#
#     def append(self, element):
#         self._data.append(element)
#
#     def pop(self):
#         return self._data.pop()
#
#     def __iter__(self):
#         return StackIterator(self)
#
#     def __getitem__(self, item):
#         return self._data[item]
#
#
# class StackIterator:
#     def __init__(self, stack):
#         self._index = -1
#         self._stack = stack
#
#     def __next__(self):
#         self._index += 1
#         if self._index == len(self._stack):
#             raise StopIteration
#         return self._stack[self._index]
#
#
# x = Stack([2, 5, 7, 8])
# print(x.pop())
# x.append(9)
# x.append(15)
# for element in x:
#     print(element)


# gen ----------------------

# def squares():
#     curr = 0
#     for i in range(1000):
#         yield curr ** 2
#         curr += 1
#     return  # нет смысла ничего возвращать в return, он кидает StopIteration
#
#
# def my_range(start, stop=None, step=1):
#     if stop is None:
#         start, stop = 0, start
#     curr = start
#     while curr < stop:
#         yield curr
#         curr += step


# for x in squares():
#     print(x)

# for i in my_range(5, 10, 2):
#     print(i)

x = (x ** 2 for x in range(1000))
print(x)
print(*x)
