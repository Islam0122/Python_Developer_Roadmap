"""Type casting ,Expertions"""

'''Type casting'''
# Type casting - это процесс преобразования значения из одного типа данных в другой.
# В Python существует два типа type casting:
# Widening casting - преобразование значения из более узкого типа данных в более широкий.
#                     Например, преобразование числа типа int в число типа float.
x = 10.000
print(int(x))  # 10
# Narrowing casting - преобразование значения из более широкого типа данных в более узкий.
#                     Например, преобразование числа типа float в число типа int.
x = 10
print(float(x))  # 10.0

'''Expertions'''
# Exceptions - это события, которые могут произойти во время выполнения программы.
# Exceptions могут быть вызваны различными причинами,
# например, ошибками в коде, некорректным вводом данных, или внешними факторами.
# ValueError - возникает при передаче некорректного значения в функцию или метод.
# TypeError - возникает при использовании переменной или функции неверно.
# KeyError - возникает при попытке получить значение по несуществующему ключу в словаре.
# IndexError - возникает при попытке получить элемент списка или кортежа по несуществующему индексу.

# try:
#     # Код, который может вызвать exception
# except ValueError:
#     # Обработка exception ValueError
# except TypeError:
#     # Обработка exception TypeError