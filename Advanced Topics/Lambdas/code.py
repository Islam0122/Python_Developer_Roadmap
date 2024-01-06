numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)

square = lambda x: x * x

print(square(5))  # 25
