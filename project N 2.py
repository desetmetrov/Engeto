#"""
#projekt N 2.py: druрý projekt do Engeto Online Python Akademie

# Vladimír Kosťukovič

# kostyukovyc@gmail.com

#"""
#tady bude začínat tvůj kód

import random
from time import time

print("Hi There!"
      "I've generated a random 4 digit number for you. Let's play a bulls and cows game.")

# Function to generate 4 digit unique number
def generate_random_num():
    while True:
        num = random.randint(1000, 9999)  # Generation
        if len(set(str(num))) == 4:  # Check if number is 4 digit and unique (set)
            return str(num)

# random generation result save
random_num_save = generate_random_num()

# Function for user generation
def user_num_generation():
    while True:
        user_input = input("Enter a number:")
        if not user_input.isdigit() or not 1000 <= int(user_input) <= 9999:
            print(f"Your choice {user_input} is not correct, use 4 digits to start game.")
            continue
        if len(set(user_input)) != 4:
            print(f"Your choice {user_input} has repeated digits, but you can continue.")
        print(f"Let's play! Your chosen number is {user_input}.")
        return user_input

# Function to count if numbers are in PC choice
# Bulls
def count_bulls(secret_num, user_num):
    bulls = 0
    for x in range(len(secret_num)):
        if secret_num[x] == user_num[x]:
            bulls += 1
    return bulls

# Cows
def count_cows(secret_num, user_num):
    cows = 0
    for i in range(len(secret_num)):
        if user_num[i] in secret_num and user_num[i] != secret_num[i]:
            cows += 1
    return cows

# Gaming
def start_game():
    random_num_save = generate_random_num()
    start_game_time = time()
    how_many_times = 0
    while True:
        users_try = user_num_generation()
        bulls = count_bulls(random_num_save, users_try)
        cows = count_cows(random_num_save, users_try)
        how_many_times += 1
        print(f"Bulls: {bulls}, Cows: {cows}")
        if bulls == 4:
            end_game_time = time()
            total_time = round(end_game_time - start_game_time, 2)
            print(f"Congratulations! You've guessed the number {random_num_save} in {how_many_times} attempts.")
            print(f"Total time taken: {total_time} seconds.")
            break

start_game()