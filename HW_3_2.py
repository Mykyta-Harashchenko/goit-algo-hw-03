import random

def get_numbers_ticket(min, max, quantity:int):
    
    if not (1 <= min < max <= 1000 and 1 <= quantity <= (max - min + 1)):
        return []
    else:
        second_try = random.sample(range(min, max+1), k=quantity)
        return sorted(second_try)
    

checking = get_numbers_ticket(1, 1000, 5)
print('Ваші лотерейні числа:', checking)