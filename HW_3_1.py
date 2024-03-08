import datetime


def get_days_from_today(date):
    date = datetime.datetime.strptime(date,'%Y-%m-%d')
    now = datetime.datetime.today()
    difference = now - date
    return difference

checking = get_days_from_today('2024-10-9')
print(checking)
