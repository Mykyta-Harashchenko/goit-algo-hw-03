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
                next_monday = today + timedelta(days=(7 - today.weekday()))
                congrats_date = next_monday
            else:
                congrats_date = birthday_this_year

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congrats_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

users = [
{'name': 'Jane Smith', 'birthday': '1990.03.10'},
{'name': 'Nick Darsel', 'birthday': '1984.03.11'},
{'name': 'Liam Smith', 'birthday': '1995.03.12'},
{'name': 'Mohel Smith', 'birthday': '1995.03.13'},
{'name': 'John Dark', 'birthday': '1985.03.14'},
{'name': 'Mary Dark', 'birthday': '1985.03.15'},
{'name': 'Derek Dark', 'birthday': '1985.03.16'},
{'name': 'Jane Smith', 'birthday': '1990.03.17'},
{'name': 'Liam Smith', 'birthday': '1995.03.18'},
{'name': 'Mohel Smith', 'birthday': '1995.03.19'},
{'name': 'John Dark', 'birthday': '1985.03.20'}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
