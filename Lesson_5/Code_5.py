# class Base:
#     name = "Base"
#
#     def say_hello(self):
#         print(self)
#
#     def __str__(self):
#         return "this is Base class"
#
#
# class Derived(Base):
#     name = "Derived"
#
#     def __str__(self):
#         return "this is Derived class"
#
#
# print(Base.__dict__)
# print(Derived.__dict__)
# x = Derived()
# x.say_hello()

# --------------------------------------------

# class Vehicle:
#     def __init__(self, engine_power=1000, model="", capacity=1):
#         self._engine_power = engine_power
#         self._model = model
#         self._cap = capacity
#
#     def move(self):
#         pass
#
#
# class Car(Vehicle):
#     def __init__(self, engine_power=1000, model="", capacity=1, drive_type="front", number_of_wheels = 4):
#         super().__init__(engine_power, model, capacity)
#         self._drive_type = drive_type
#         self._wheels = number_of_wheels
#
#     def move(self):
#         print("rotate wheels")
#
#     def __str__(self):
#         return "I'm a car and I can move"
#
#
# class Boat(Vehicle):
#     def __init__(self, engine_power=1000, model="", capacity=1, sank_depth=3):
#         super().__init__(engine_power, model, capacity)
#         self._sank_depth = sank_depth
#
#     def move(self):
#         print("bul bul")
#
#     def dock(self):
#         print("I'm home")
#
#
# class Hybrid_car(Car, Boat):
#     def __str__(self):
#         return super().__str__() + " and also dock"
#
#
# x = Hybrid_car(2000, "Hydra", 5, "full", 4)
# x.move()
# x.dock()
# print(x)

# -----------------------------------------
# try:
#     raise IndentationError
#     print("this is unreachable")
# except ValueError:
#     print("this won't be called")
# except ArithmeticError:
#     print("overruled")
# except ZeroDivisionError:
#     print("oops")
# except:
#     print("I'll catch you anyway")
# else:
#     print("everything is ok")
# finally:
#     print("finally!")

# ---------------------------------------------

class MyException(Exception):
    pass


a = 3
b = 0
try:
    if b == 0:
        raise MyException("b = {}, you can't do that".format(b))
except MyException as Err:
    print(Err)
    print("it's fine")

