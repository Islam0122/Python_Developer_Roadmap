# Добавление новых функций
import time


def log(f):
    def wrapper(*args, **kwargs):
        print("Вызов функции:", f.__name__)
        return f(*args, **kwargs)
    return wrapper

@log
def say_hello():
    print("Hello, world!")

say_hello()

# Изменение существующих функций
def uppercase(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs).upper()
    return wrapper

@uppercase
def say_hello():
    return "Hello, world!"

print(say_hello())

# Проверка входных параметров
def check_positive(f):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg < 0:
                raise ValueError("Аргумент должен быть положительным")
        return f(*args, **kwargs)
    return wrapper

@check_positive
def add(a, b):
    return a + b

add(1, 2)

# Учет времени выполнения
def timeit(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print("Время выполнения:", end - start)
        return result
    return wrapper

@timeit
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

factorial(10)

# Запись логов
import logging

def log_to_file(f):
    def wrapper(*args, **kwargs):
        logging.info("Вызов функции:", f.__name__)
        return f(*args, **kwargs)
    return wrapper

@log_to_file
def say_hello():
    print("Hello, world!")

say_hello()