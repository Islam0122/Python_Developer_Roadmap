# Условный оператор `if` с несколькими условиями

x = 10

if x >= 0 and x <= 10:
    print("x в диапазоне от 0 до 10")

# Условный оператор `elif`

x = 5

if x == 1:
    print("x равно 1")
elif x == 2:
    print("x равно 2")
elif x == 3:
    print("x равно 3")
else:
    print("x не равно ни одному из этих значений")

# Цикл `while` с условием выхода

x = 0

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# Цикл `for` с условием выхода

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        break
    print(number)