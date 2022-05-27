import random
from currency_converter import CurrencyConverter


def get_money_interval(difficulty, exchage_rate):
    res = (exchage_rate - (5 - difficulty), exchage_rate + (5 - difficulty))
    return res


def get_guess_from_user(num):
    while (True):
        try:
            user_guess_num = int(input(f"Enter a guess of value to a given amount of USD for ILS {num}:"))
            break
        except ValueError as e:
            print("You should to provide only numbers")

    return user_guess_num


def play(difficulty):
    num = random.randint(1, 100)
    c = CurrencyConverter()
    val = c.convert(num, 'USD', 'ILS')
    val_interval = get_money_interval(difficulty, val)
    user_num = get_guess_from_user(num)
    res = False

    if val_interval[0] <= user_num <= val_interval[1]:
        print("won")
        res = True
    else:
        print("lost")

    return res

# play(3)
