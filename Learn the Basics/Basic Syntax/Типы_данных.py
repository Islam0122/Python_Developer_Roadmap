"""'Типы данных'"""

# Числовые типы:
# int: Целочисленный тип данных.
x = 5
# float: Тип данных с плавающей точкой для представления действительных чисел.
y = 3.14
# complex: Комплексный тип данных для представления комплексных чисел.
z = 2 + 3j
print(x, y, z)
# Строковые типы:
# str: Тип данных для представления строк.
name = "John"
# bytes: Тип данных для представления последовательности байт.
data = b"Hello"
# bytearray: Массив изменяемых байтов.
bytearray_data = bytearray([65, 66, 67])
# str.format, f-строки: Специальные методы форматирования строк.
age = 25
message = f"Мой возраст: {age}"
# Логический тип:
# bool: Тип данных для представления логических значений True или False.
is_true = True
# Списки и кортежи:
# list: Упорядоченная изменяемая последовательность элементов.
numbers = [1, 2, 3, 4, 5]
# tuple: Упорядоченная неизменяемая последовательность элементов.
point = (10, 20)
print(point); print(numbers)
# Словари:
# dict: Неупорядоченная коллекция пар ключ-значение.
person = {"name": "John", "age": 30}
# Множества:
# set: Неупорядоченная коллекция уникальных элементов.
unique_numbers = {1, 2, 3, 4, 5}
# None:
# Представляет отсутствие значения или нулевую ссылку.
result = None