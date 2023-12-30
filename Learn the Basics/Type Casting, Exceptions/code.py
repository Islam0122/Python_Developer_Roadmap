
try:
    # Блок кода, где может возникнуть исключение
    result = int("abc")
except ValueError as e:
    # Блок кода, выполняемый при возникновении ValueError
    print(f"Ошибка: {e}")
else:
    # Блок кода, выполняемый, если исключение не возникло
    print("Преобразование прошло успешно.")
finally:
    # Блок кода, выполняемый всегда
    print("Завершение операции.")
print('_________________________________________________________________________________')
def divide(x, y):
    if y == 0:
        raise ValueError("Деление на ноль недопустимо.")
    return x / y

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Ошибка: {e}")
else:
    print(f"Результат деления: {result}")