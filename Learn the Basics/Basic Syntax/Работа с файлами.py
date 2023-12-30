# Чтение файла
with open("example.txt", "r") as file:
    content = file.read()

# Запись в файл
with open("example.txt", "w") as file:
    file.write("Новый текст")

# Добавление в файл
with open("example.txt", "a") as file:
    file.write("\nДополнительная строка")