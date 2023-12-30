from random import choice

def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+;:,.?/"
    password = "".join(choice(characters) for _ in range(length))
    return password


name = input("Введите фио :")
password = generate_password(8)
print(password)

# Ввод пароля
passwords = input("Введите пароль: ")

if password == passwords:
    print('success')
else:
    print('stop')
