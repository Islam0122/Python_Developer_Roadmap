import re

pattern = re.compile(r'\d+')
text = "The price is $10 and $20"

match = pattern.search(text)
if match:
    print("Найдено совпадение:", match.group())
else:
    print("Совпадений не найдено.")


pattern = re.compile(r'(\w+), (\w+)')
text = "Doe, John; Smith, Jane; Brown, Mike"

matches = pattern.findall(text)
for match in matches:
    last_name, first_name = match
    print("Фамилия:", last_name, "Имя:", first_name)

pattern = re.compile(r'(\+\d{1,3})?\s?(\d{10})')
text = "Phone numbers: +1 1234567890, +96 9876543210"

matches = pattern.findall(text)
for match in matches:
    country_code, phone_number = match
    print("Код страны:", country_code, "Номер телефона:", phone_number)