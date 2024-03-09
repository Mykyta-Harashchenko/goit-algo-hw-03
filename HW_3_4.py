from datetime import datetime, timedelta 
users = [ 
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Colton Mark", "birthday": "1995.01.27"},
    {"name": "Tom Morgan", "birthday": "1992.03.05"},
    {"name": "Liam Atkins", "birthday": "1976.03.07"},
    {"name": "Ciaran Daisy", "birthday": "1989.03.10"},
]
def get_upcoming_birthsdays(users):
    def find_next_weekday(d, weekday: int): 

        days_ahead = weekday - d.weekday()  
        if days_ahead <= 0:  
            days_ahead += 7  
        return d + timedelta(days=days_ahead)  


    prepared_users = [] 
    def working_users():
    
        for user in users:  
            try:
                birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()  
                prepared_users.append({"name": user['name'], 'birthday': birthday})  
            except ValueError:
                print(f'Некоректна дата народження для користувача {user["name"]}')  
        return prepared_users


    days = 7  
    today = datetime.today().date() 
    upcoming_birthdays = [] 
    def final_users():
    
        for user in prepared_users: 
            birthday_this_year = user["birthday"].replace(year=today.year) 

            if birthday_this_year < today: 
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)  

            if 0 <= (birthday_this_year - today).days <= days:  
                if birthday_this_year.weekday() >= 5: 
                    birthday_this_year = find_next_weekday(birthday_this_year, 0) 

                congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')  
                upcoming_birthdays.append({  
                "name": user["name"],
                "congratulation_date": congratulation_date_str
            })
        return upcoming_birthdays
