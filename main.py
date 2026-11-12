
import re
from datetime import date

# Регулярное выражение для поиска email-адресов
email_pattern = (
    r'(?<![\w@])'
    r'(?:'
    r'[A-Za-z0-9!#$%&\'*+/=?^_`{|}~-]+'
    r'(?:\.[A-Za-z0-9!#$%&\'*+/=?^_`{|}~-]+)*'
    r'|'
    r'"(?:[^"\\\r\n]|\\.)*"'
    r')'
    r'@'
    r'(?:'
    r'[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?'
    r'(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?)*'
    r'|'
    r'\[(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
    r'(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}\]'
    r')'
    r'(?![\w.-])'
)

# Регулярное выражение для поиска дат
date_pattern = (
    r'\b(?P<day>\d{1,2})\s+'
    r'(?P<month>января|февраля|марта|апреля|мая|июня|'
    r'июля|августа|сентября|октября|ноября|декабря)'
    r'\s+(?P<year>\d{4})\s+года\b'
)

# Словарь для преобразования названий месяцев в числа
months = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}

# Ввод исходного текста
print("Введите текст. Для завершения ввода нажмите Enter на пустой строке:")

text = ""

while True:
    line = input()
    if line == "":
        break
    text += line + "\n"

# Поиск email-адресов
emails = list(re.finditer(email_pattern, text))
# Поиск дат
date_matches = list(re.finditer(date_pattern, text, re.IGNORECASE))

# Вывод найденных email
print("\n--- Результаты поиска email ---")

if emails:
    for match in emails:
        print("Найден адрес:", match.group())
else:
    print("Email-адреса не найдены.")

# Проверка и вывод дат
print("\n--- Результаты поиска датированных событий ---")

valid_dates = 0

for match in date_matches:
    day = int(match.group("day"))
    month = months[match.group("month").lower()]
    year = int(match.group("year"))

    try:
        date(year, month, day)
        print("Найдена корректная дата:", match.group())
        valid_dates += 1
    except ValueError:
        print("Обнаружена некорректная дата:", match.group())

if valid_dates == 0:
    print("Корректные даты не найдены.")

print("\n--- Статистика ---")
print("Найдено email-адресов:", len(emails))
print("Найдено упоминаний дат:", len(date_matches))
print("Корректных дат:", valid_dates)
