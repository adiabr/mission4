import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficult):
    while (True):
        try:
            user_number = int(input(f"Please choose a number between 1 to {difficult}:"))
            break
        except ValueError as e:
            print(f"Please choose a number between 1 to {difficult}")
    return user_number


def compare_results(secret, user_number):
    if secret == user_number:
        res = True
    else:
        res = False
    return res


def play(stop):
    difficulty = random.randint(1, stop)
    secret_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    res = compare_results(secret_number, user_number)

    if res == True:
        print("You won")
    else:
        print(f"You lost, you guess {user_number} and the real number was {secret_number}")

    return res

# stop = 10
# play(stop)
