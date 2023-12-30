def check_age(age):
    if age < 0:
        print("Возраст не может быть отрицательным.")
    elif age < 18:
        print("Вы несовершеннолетний.")
    elif 18 <= age < 65:
        print("Вы взрослый.")
    else:
        print("Вы пожилой человек.")


attempts = 3
while attempts > 0:
    user_age_str = input("Введите ваш возраст: ")

    try:
        user_age = int(user_age_str)
        check_age(user_age)
        break
    except ValueError:
        print("Ошибка: Введите целое число.")
        attempts -= 1
        if attempts == 0:
            print("Превышено количество попыток. Завершение программы.")
