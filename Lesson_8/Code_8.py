def time_decorator(func):
    def decorated_func(*args, **kwargs):
        import time
        start_time = time.time()
        res = func(*args, **kwargs)
        print(f"time of function execution: {time.time() - start_time}")
        return res
    return decorated_func


@time_decorator
def prime(value):
    div = 2
    while div ** 2 <= value:
        if value % div == 0:
            return False
        div += 1
    return True

# prime = time_decorator(prime)


#from functools import cache
# @cache - осуществляет мемоизацию


from Lesson_8.test_package.Pair import Pair
x = Pair(3, 2)




