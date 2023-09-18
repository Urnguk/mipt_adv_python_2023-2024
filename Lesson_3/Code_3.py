# --Example 1--
# class Student:
#     x = 0
#
#
# a = Student()
# b = Student()
#
# print(a.x, b.x, Student.x)
#
# a.x = 5
# print(a.x, b.x, Student.x)
#
# Student.x = 3
# print(a.x, b.x, Student.x)
#---------------------------------------

# --Example 2--

# class Student:
#     A = []
#
#
# a = Student()
# b = Student()
#
# a.A.append(1)
# print(b.A)
#----------------------------------------


# --Example 3--

# class Student:
#     def __init__(self, age=18, name="John"):
#         self._age = age
#         self._name = name
#
#     def grow(self):
#         self._age += 1
#
#     def get_name(self):
#         return self._name
#
#     def set_age(self, new_age):
#         self._age = new_age
#
#
# a = Student()
# b = Student(20, "Mary")
#
# print(a)
# print(a.__dict__)
# b.grow()
# print(b.__dict__)
# print(Student.__dict__)
#
# print(b._age)
# print(a.get_name())
#
# b.__dict__["scholarship"] = True
# print(b.__dict__)
# print(b.scholarship)


# ---------------------------------------

# --Example 4--
def func(cl):
    print(cl.a)


class A:
    def __init__(self):
        self.a = 0


x = A()
func(x)
func(5)