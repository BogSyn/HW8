from datetime import date, datetime, timedelta
import copy


def get_birthdays_per_week(users):

    today = date.today()

    # Створення словника для днів тижня
    week_dict = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': [],
    }

    # Глибока копія, щоб не вносити зміни в оригінал
    users_list = copy.deepcopy(users)

    # Корекція дати народження для порівняння
    for data_dict in users_list:
        if data_dict["birthday"].month < today.month:
            data_dict["birthday"] = data_dict["birthday"].replace(
                year=today.year+1)
        else:
            data_dict["birthday"] = data_dict["birthday"].replace(
                year=today.year)

    # Визначення алгоритму обробки тижня в залежності від поточного дня
    if today.weekday() == 0:
        start_week = today
        end_week = today + timedelta(days=4)
    elif today.weekday() == 6:
        start_week = today
        end_week = today + timedelta(days=5)
    else:
        start_week = today
        end_week = today + timedelta(days=6)

    # Ітерація по користувачам та додавання імен до відповідних днів тижня
    for user_dict in users_list:
        birth_day = datetime.strftime(user_dict["birthday"], '%A')
        if start_week <= user_dict["birthday"] <= end_week:
            if birth_day in ['Saturday', 'Sunday']:
                week_dict['Monday'].append(user_dict["name"])
            else:
                week_dict[birth_day].append(user_dict["name"])

    # Створення словника з ім'ям дня тижня та списком імен, які мають дні народження цього тижня
    users = {}
    for key, value in week_dict.items():
        if value:
            users[key] = value
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 10, 30).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
