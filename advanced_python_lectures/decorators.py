import functools

from os import system
system("cls")
print("...DECORATORS...")
print("-"*15)

""" from itertools import repeat


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')


greet('Alex') """

""" import functools


def start_end_decorator(func):
    def wrapper(*args, **kwargs):
        print('Start')
        func(*args, **kwargs)
        print('End')
    return wrapper


@start_end_decorator
def say_hello(name):
    print(f'Hello {name}')


say_hello('Alex') """


class countcalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'Call Number {self.num_calls} times')
        return self.func(*args, **kwargs)


@countcalls
def say_hello():
    print('Hello')


say_hello()
