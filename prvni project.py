#"""
#projekt_1.py: první projekt do Engeto Online Python Akademie


#"""
#tady bude začínat tvůj kód

#---------------------------------------------------------

# Users database
user_list = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# User authorization
input_user = input("Enter your username: ").strip().lower()
input_password = input("Enter your password: ").strip()

# Login and pass check
if input_user in user_list:
    if user_list[input_user] == input_password:
        access_granted = True
    else:
        print("Your password is incorrect.")
        access_granted = False
else:
    print(
        f"Username: {input_user}\n"
        f"Password: {input_password}\n"
        "Unregistered user, terminating the program..."
    )
    access_granted = False

# Texts database
texts = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Check the number of texts available
text_split_len = len(texts)

# If login successful
if access_granted:
    print(
        f"User: {input_user}\n"
        f"Password: {input_password}\n"
        f"{'-' * 40}\n"
        f"Welcome to the app: {input_user}\n"
        f"We have {text_split_len} texts to be analyzed.\n"
        f"{'-' * 40}\n"
    )

    # User choice
    while True:
        user_choice = input(f"Enter a number between 1 and {text_split_len} to select: ").strip()

        # Check if input is a digit
        if not user_choice.isdigit():
            print("Please enter a valid number.")
            continue

        user_choice = int(user_choice)

        # Check if digit is in range
        if 1 <= user_choice <= text_split_len:
            break
        else:
            print(f"Enter a correct digit between 1 and {text_split_len}.")

    # Analyze the selected text
    user_choice_text = texts[user_choice - 1]
    user_choice_text_sum_word = len(user_choice_text.split())
    user_choice_text_len_cap = sum(word.istitle() for word in user_choice_text.split())
    user_choice_text_sum_upper = sum(word.isupper() for word in user_choice_text.split())
    user_choice_text_sum_low = sum(word.islower() for word in user_choice_text.split())
    user_choice_text_sum_dig = sum(word.isdigit() for word in user_choice_text.split())
    sum_of_numbers = sum(int(word) for word in user_choice_text.split() if word.isdigit())

    # Calculate words and their lengths
    cleaned_words = [word.strip(",.?!") for word in user_choice_text.split()]
    word_lengths = [len(word) for word in cleaned_words]

    length_counts = {}
    for length in word_lengths:
        if length in length_counts:
            length_counts[length] += 1
        else:
            length_counts[length] = 1

    # Output results
    print(
        f"There are {user_choice_text_sum_word} words in the selected text.\n"
        f"There are {user_choice_text_len_cap} titlecase words.\n"
        f"There are {user_choice_text_sum_upper} uppercase words.\n"
        f"There are {user_choice_text_sum_low} lowercase words.\n"
        f"There are {user_choice_text_sum_dig} numeric strings.\n"
        f"The sum of all the numbers is {sum_of_numbers}.\n"
        f"{'-' * 40}\n"
        f"{'NR':<5}| {'OCCURRENCES':<29}| {'NR':<3}"
    )

    print(f"{'-' * 5}| {'-' * 29}| {'-' * 3}")

    for length, count in sorted(length_counts.items()):
        stars = '*' * count
        print(f"{length:<5}| {stars:<29}| {count:<3}")
