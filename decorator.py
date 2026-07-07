# def log(func):
#     def wrapper(*args, **kwargs):
#         print('log start')
#         result = func(*args, **kwargs)
#         print(f'{func.__name__} log end')
#         return result
#     return wrapper
# @log
# def count():
#     print("count function")

# count()


import functools


def log(level):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kvargs):
            print(f"{level}: log start{args}{inner.__name__}")
            return func(*args, **kvargs)

        return inner

    return wrapper


@log("info")
def count(a):
    print(f"count function {a}")


count(1)
