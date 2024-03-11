from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = datetime(today.year, birthday_date.month, birthday_date.day).date()

        if birthday_this_year < today:
            birthday_this_year = datetime(today.year + 1, birthday_date.month, birthday_date.day).date()

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:
                next_monday = today + timedelta(days=(7 - today.weekday()) + 1)
                congrats_date = next_monday
            else:
                congrats_date = birthday_this_year

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congrats_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.12"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
