from GuessGame import play as GPlay
from MemoryGame import play as MPlay
from CurrencyRouletteGame import play as CPlay
from Score import add_score as CScore
from Utils import screen_cleaner


def welcome(name):
    str = f"Hello {name} and welcome to the World of Games(WoG)\nHere you can find many cool games to play\n"
    return str


def check_number(name, number):
    # variables
    game_number = 0
    result = 0

    if name == "choose_game":
        while (True):
            try:
                game_number = int(input("Please choose number between 1-3:"))
                if 1 <= game_number <= number:
                    break
                else:
                    print("the input suppose to be a number between 1 to 3")
            except ValueError as e:
                print("You insert a character, please choose only number between 1-3")
    elif name == "difficulty":
        while (True):
            try:
                game_number = int(input("Please choose game difficulty from 1 to 5:"))
                if 1 <= game_number <= number:
                    break
                else:
                    print("input should be a number between 1 to 5")
            except ValueError as e:
                print("You insert a character, please choose only number between 1-5")
    else:
        print("The name needs to be only choose_game or difficulty")

    result = game_number
    return result


def load_game():
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")

    game_number = check_number("choose_game", 3)
    game_difficulty_number = check_number("difficulty", 5)

    print(f"User choose number of game {game_number} and difficulty number {game_difficulty_number}")

    screen_cleaner()

    while (True):
        if game_number == 1:
            user_win = MPlay(game_difficulty_number)
            break
        elif game_number == 2:
            user_win = GPlay(game_difficulty_number)
            break
        elif game_number == 3:
            user_win = CPlay(game_difficulty_number)
            break
        else:
            print("Please provide number between 1-3")

    if user_win:
       CScore(game_difficulty_number)
