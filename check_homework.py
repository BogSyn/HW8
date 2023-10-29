from datetime import datetime
from main import get_birthday_per_week
import copy

test_counter = 0

# Test 1: коли усі дні народження користувачів є у майбутньому і не випадають на вихідні.
day_test_1 = datetime(2023, 10, 22).date()
test_1 = [
    {"name": "Aria Blackwood", "birthday": datetime(1988, 10, 24).date()},
    {"name": "Ethan Nightingale", "birthday": datetime(1976, 11, 3).date()},
    {"name": "Luna Starling", "birthday": datetime(1992, 10, 25).date()},
    {"name": "Caspian Ashford", "birthday": datetime(1985, 11, 1).date()},
    {"name": "Isadora Hart", "birthday": datetime(2000, 10, 26).date()},
    {"name": "Sebastian Frost", "birthday": datetime(1980, 12, 26).date()},
    {"name": "Aurora Woods", "birthday": datetime(1995, 10, 27).date()},
    {"name": "Xander Storm", "birthday": datetime(1972, 10, 27).date()},
    {"name": "Violet Winter", "birthday": datetime(1987, 10, 28).date()},
    {"name": "Phoenix Rivers", "birthday": datetime(2005, 10, 29).date()},
]
compare_list_1 = {
    'Tuesday': ['Aria'],
    'Wednesday': ['Luna'],
    'Thursday': ['Isadora'],
    'Friday': ['Aurora', 'Xander']
}

if get_birthday_per_week(test_1, today=day_test_1) == compare_list_1:
    test_counter += 1
    print("\033[92m1. Успішно пройдений тест коли усі дні народження користувачів є у майбутньому і не випадають на вихідні.\033[0m")
else:
    print("\033[91m1. Провалено тест коли коли усі дні народження користувачів є у майбутньому і не випадають на вихідні.\033[0m")


# Test 2: коли дні народження деяких користувачів випадають на вихідні.
day_test_2 = datetime(2023, 10, 25).date()
test_2 = [
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
compare_list_2 = {
    'Monday': ['Aurora', 'Xander'],
    'Tuesday': ['Violet'],
    'Thursday': ['Phoenix'],
    'Friday': ['Isadora', 'Sebastian']
}

if get_birthday_per_week(test_2, today=day_test_2) == compare_list_2:
    test_counter += 1
    print("\033[92m2. Успішно пройдений тест коли дні народження деяких користувачів випадають на вихідні.\033[0m")
else:
    print("\033[91m2. Провалено тест коли дні народження деяких користувачів випадають на вихідні.\033[0m")


# Test 3: коли деякі дні народження користувачів вже минули у цьому році.
day_test_3 = datetime(2023, 12, 28).date()
test_3 = [
    {"name": "Aria Blackwood", "birthday": datetime(1988, 5, 15).date()},
    {"name": "Ethan Nightingale", "birthday": datetime(1976, 12, 28).date()},
    {"name": "Luna Starling", "birthday": datetime(1992, 7, 20).date()},
    {"name": "Caspian Ashford", "birthday": datetime(1985, 12, 29).date()},
    {"name": "Isadora Hart", "birthday": datetime(2000, 3, 27).date()},
    {"name": "Sebastian Frost", "birthday": datetime(1980, 12, 31).date()},
    {"name": "Aurora Woods", "birthday": datetime(1995, 1, 1).date()},
    {"name": "Xander Storm", "birthday": datetime(1972, 1, 2).date()},
    {"name": "Violet Winter", "birthday": datetime(1987, 1, 3).date()},
    {"name": "Phoenix Rivers", "birthday": datetime(2005, 1, 10).date()},
]
compare_list_3 = {
    'Monday': ['Sebastian', 'Aurora'],
    'Tuesday': ['Xander'],
    'Wednesday': ['Violet'],
    'Thursday': ['Ethan'],
    'Friday': ['Caspian']
}
if get_birthday_per_week(test_3, today=day_test_3) == compare_list_3:
    test_counter += 1
    print("\033[92m3. Успішно пройдений тест коли деякі дні народження користувачів вже минули у цьому році.\033[0m")
else:
    print("\033[91m3. Провалено тест коли коли деякі дні народження користувачів вже минули у цьому році.\033[0m")


# Test 4: коли у списку немає користувачів.
test_4 = [copy.deepcopy(test_3)]
test_4.clear()

if get_birthday_per_week(test_4) == {}:
    test_counter += 1
    print("\033[92m4. Успішно пройдений тест коли у списку немає користувачів.\033[0m")
else:
    print("\033[91m4. Провалено тест коли коли у списку немає користувачів.\033[0m")


# Test 5: коли всі дні народження користувачів вже минули у цьому році.
day_test_5 = datetime(2023, 12, 29).date()
test_5 = [
    {"name": "Aria Blackwood", "birthday": datetime(1988, 1, 3).date()},
    {"name": "Ethan Nightingale", "birthday": datetime(1976, 1, 2).date()},
    {"name": "Luna Starling", "birthday": datetime(1992, 5, 28).date()},
    {"name": "Caspian Ashford", "birthday": datetime(1985, 7, 29).date()},
    {"name": "Isadora Hart", "birthday": datetime(2000, 9, 27).date()},
    {"name": "Sebastian Frost", "birthday": datetime(1980, 8, 27).date()},
    {"name": "Aurora Woods", "birthday": datetime(1995, 10, 2).date()},
    {"name": "Xander Storm", "birthday": datetime(1972, 1, 1).date()},
    {"name": "Violet Winter", "birthday": datetime(1987, 4, 25).date()},
    {"name": "Phoenix Rivers", "birthday": datetime(2005, 1, 1).date()},
]
compare_list_5 = {
    'Monday': ['Xander', 'Phoenix'],
    'Tuesday': ['Ethan'],
    'Wednesday': ['Aria'],
}
if get_birthday_per_week(test_5, today=day_test_5) == compare_list_5:
    test_counter += 1
    print(
        "\033[92m5. Успішно пройдений тест коли всі дні народження користувачів вже минули у цьому році.\033[0m\n")
else:
    print("\033[91m5. Провалено тест коли всі дні народження користувачів вже минули у цьому році.\033[0m\n")


# Кількіст пройдених тестів
print(f"Всього пройдено тестів {test_counter}")

# Кількість провалених тестів
if test_counter < 5:
    print(f"\033[91mПровалених тестів: {5 - test_counter}\033[0m")

# Сепаратор для розмежування
separator = "-" * 100
print(separator)
