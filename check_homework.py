from datetime import datetime
from main import get_birthday_per_week
import copy

test_counter = 0

# Test 1: Перевірка коли всі дні народження вже минули в цьому році
day_test_1 = datetime(2023, 10, 26).date()
test_1 = [
    {"name": "Aria Blackwood", "birthday": datetime(1988, 5, 15).date()},
    {"name": "Ethan Nightingale", "birthday": datetime(1976, 9, 3).date()},
    {"name": "Luna Starling", "birthday": datetime(1992, 7, 20).date()},
    {"name": "Caspian Ashford", "birthday": datetime(1985, 5, 8).date()},
    {"name": "Isadora Hart", "birthday": datetime(2000, 3, 27).date()},
    {"name": "Sebastian Frost", "birthday": datetime(1980, 6, 12).date()},
    {"name": "Aurora Woods", "birthday": datetime(1995, 4, 4).date()},
    {"name": "Xander Storm", "birthday": datetime(1972, 10, 15).date()},
    {"name": "Violet Winter", "birthday": datetime(1987, 8, 22).date()},
    {"name": "Phoenix Rivers", "birthday": datetime(2005, 1, 10).date()},
]

if get_birthday_per_week(test_1, today=day_test_1) == {}:
    test_counter += 1
    print("\033[92m1. Успішно пройдений тест коли всі дні народження вже минули в цьому році\033[0m")
else:
    print("\033[91m1. Провалено тест коли всі дні народження вже минули в цьому році. Функція повинна повернути пустий словник\033[0m")


# Test 2: Перевірка коли список користувачів пустий
test_2 = [copy.deepcopy(test_1)]
test_2.clear()

if get_birthday_per_week(test_2) == []:
    test_counter += 1
    print("\033[92m2. Успішно пройдений тест коли у функцію передали пустий список користувачів\033[0m")
else:
    print("\033[91m2. Провалено тест коли у функцію передали пустий список користувачів. Функція повинна повернути пустий список\033[0m")


# Test 3: Перевірка коли правильний список користувачів які не припадають на вихідні
day_test_3 = datetime(2023, 10, 26).date()
test_3 = [
    {"name": "Aria Blackwood", "birthday": datetime(1988, 5, 15).date()},
    {"name": "Ethan Nightingale", "birthday": datetime(1976, 9, 3).date()},
    {"name": "Luna Starling", "birthday": datetime(1992, 10, 26).date()},
    {"name": "Caspian Ashford", "birthday": datetime(1985, 12, 8).date()},
    {"name": "Isadora Hart", "birthday": datetime(2000, 10, 27).date()},
    {"name": "Sebastian Frost", "birthday": datetime(1980, 10, 27).date()},
    {"name": "Aurora Woods", "birthday": datetime(1995, 10, 30).date()},
    {"name": "Xander Storm", "birthday": datetime(1972, 11, 30).date()},
    {"name": "Violet Winter", "birthday": datetime(1987, 10, 22).date()},
    {"name": "Phoenix Rivers", "birthday": datetime(2005, 11, 1).date()},
]
compare_list_3 = {
    'Monday': ['Aurora'],
    'Wednesday': ['Phoenix'],
    'Thursday': ['Luna'],
    'Friday': ['Isadora', 'Sebastian']
}

if get_birthday_per_week(test_3, today=day_test_3) == compare_list_3:
    test_counter += 1
    print("\033[92m3. Успішно пройдений тест коли функція повернула правильний список днів народження користувачів які не припадають на вихідні\033[0m")
else:
    print("\033[91m3. Провалено тест коли функція повернула не правильний список днів народження які є у майбутньому і не припадають на вихідні\033[0m")


# Test 4: Перевірка коли правильний список користувачів, де дні народження вже минули в цьому році, але будуть на наступному тижні
day_test_4 = datetime(2023, 12, 28).date()
test_4 = [
    {"name": "Aria Blackwood", "birthday": datetime(1988, 1, 3).date()},
    {"name": "Ethan Nightingale", "birthday": datetime(1976, 1, 2).date()},
    {"name": "Luna Starling", "birthday": datetime(1992, 12, 28).date()},
    {"name": "Caspian Ashford", "birthday": datetime(1985, 12, 29).date()},
    {"name": "Isadora Hart", "birthday": datetime(2000, 10, 27).date()},
    {"name": "Sebastian Frost", "birthday": datetime(1980, 10, 27).date()},
    {"name": "Aurora Woods", "birthday": datetime(1995, 1, 2).date()},
    {"name": "Xander Storm", "birthday": datetime(1972, 12, 30).date()},
    {"name": "Violet Winter", "birthday": datetime(1987, 12, 31).date()},
    {"name": "Phoenix Rivers", "birthday": datetime(2005, 1, 1).date()},
]
compare_list_4 = {
    'Monday': ['Xander', 'Violet', 'Phoenix'],
    'Tuesday': ['Ethan', 'Aurora'],
    'Wednesday': ['Aria'],
    'Thursday': ['Luna'],
    'Friday': ['Caspian']
}
if get_birthday_per_week(test_4, today=day_test_4) == compare_list_4:
    test_counter += 1
    print(
        "\033[92m4. Успішно пройдений тест коли функція повернула правильний список днів народження користувачів, де деяі дні нарождення вже минули в цьому році, але вони будуть на наступному тижні\033[0m")
else:
    print("\033[91m4. Провалено тест коли функція повернула не правильний список днів народження користувачів, де деякі вже минули в цьому році, але вони будуть на наступному тижні\033[0m")


# Test 5: Перевірка коли дні народження деяких користувачів випадають на вихідні.
day_test_5 = datetime(2023, 10, 26).date()
test_5 = [
    {"name": "Aria Blackwood", "birthday": datetime(1988, 11, 1).date()},
    {"name": "Ethan Nightingale", "birthday": datetime(1976, 11, 2).date()},
    {"name": "Luna Starling", "birthday": datetime(1992, 12, 28).date()},
    {"name": "Caspian Ashford", "birthday": datetime(1985, 12, 29).date()},
    {"name": "Isadora Hart", "birthday": datetime(2000, 10, 27).date()},
    {"name": "Sebastian Frost", "birthday": datetime(1980, 10, 27).date()},
    {"name": "Aurora Woods", "birthday": datetime(1995, 10, 29).date()},
    {"name": "Xander Storm", "birthday": datetime(1972, 10, 28).date()},
    {"name": "Violet Winter", "birthday": datetime(1987, 10, 31).date()},
    {"name": "Phoenix Rivers", "birthday": datetime(2005, 10, 26).date()},
]
compare_list_5 = {
    'Monday': ['Aurora', 'Xander'],
    'Tuesday': ['Violet'],
    'Wednesday': ['Aria'],
    'Thursday': ['Phoenix'],
    'Friday': ['Isadora', 'Sebastian']
}

if get_birthday_per_week(test_5, today=day_test_5) == compare_list_5:
    test_counter += 1
    print("\033[92m5. Успішно пройдений тест коли функція повернула правильний список днів народження користувачів, причому деякі припадають на вихідні\033[0m\n")
else:
    print("\033[91m5. Провалено тест коли дні народження деяких користувачів випадають на вихідні. Функція повернула не правильний словник\033[0m\n")


# Кількіст пройдених тестів
print(f"Всього пройдено тестів {test_counter}")

# Кількість провалених тестів
if test_counter < 5:
    print(f"\033[91mПровалених тестів: {5 - test_counter}\033[0m")

# Сепаратор для розмежування
separator = "-" * 100
print(separator)
