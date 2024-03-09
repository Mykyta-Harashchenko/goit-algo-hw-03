from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date,'%Y-%m-%d')
        now = datetime.today()
        difference = (now - date).days
        return difference
    except ValueError:
        return 'Wrong entering format, enter it in format "YYYY-MM-DD"'

checking = get_days_from_today('2024-10-09')
print(checking)
