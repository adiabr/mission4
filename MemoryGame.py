import random
import os
from time import sleep
from Utils import screen_cleaner


def generate_sequence(difficulty):
    rand_list = []
    try:
        for i in range(1, (difficulty + 1)):
            num = random.randint(1, 101)
            rand_list.append(num)
    except ValueError as e:
        print(f"Error {e.args}")

    print(rand_list)
    sleep(0.7)
    screen_cleaner()

    return rand_list


def get_list_from_user(difficulty):
    user_list = []

    # user_input = input("Enter you list seprated by comma:")
    # user_list = user_input.split(",")

    i = 0
    while i < difficulty:
        try:
            num = input(f"Please write your number {i + 1} in the list:")
            user_list.append(num)
            i = i + 1
        except ValueError as e:
            print("You should to provide only numbers")

    return user_list


def is_list_equal(list1, list2):
    res = True

    for i in range(0, len(list1)):
        if int(list1[i]) != int(list2[i]):
            res = False

    return res


def play(difficulty):
    gen_seq = generate_sequence(difficulty)
    gen_user_seq = get_list_from_user(difficulty)
    res = is_list_equal(gen_seq, gen_user_seq)

    if res == True:
        print("You won")
    else:
        print(f"You lost, you guess {gen_user_seq} and the real list was {gen_seq}")

    return res

# play(4)
