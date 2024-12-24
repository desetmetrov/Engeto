#"""
#projekt_1.py: první projekt do Engeto Online Python Akademie

#author: Vladimír Kosťukovič

#email: kostyukovych@gmail.com
#"""
#tady bude začínat tvůj kód

#---------------------------------------------------------

import sys

user_list_puv = {
    "user |   password  |": """
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   """
}

user_list = {}
lines = user_list_puv["user |   password  |"].split("\n")
for line in lines:
    if "|" in line and "+" not in line:
        parts = line.split("|")
        user = parts[0].strip().lower()
        password = parts[1].strip()
        user_list[user] = password

input_user = sys.argv[1].strip().lower()
input_password = sys.argv[2]

access_granted = False

if input_user in user_list:
    if user_list[input_user] == input_password:
        print("Pristup otevren")
        access_granted = True
    else:
        print("Nejsi prihlasen, spatne heslo")
else:
    print(f"login: {input_user}\npassword: {input_password}")
    print("Unregistered user, terminating the program...")
    sys.exit()

if access_granted:
    print(f"login: {input_user}\npassword: {input_password}")
    print(f"Welcome to the app, {input_user}. We have texts to be analyzed.")
    print("-" * 40)

    try:
        with open("task_template.py", "r") as file:
            data = file.read()
        texts = data.split("'''")
        texts = [text.strip() for text in texts if text.strip()]
    except FileNotFoundError:
        print("File 'task_template.py' not found. Terminating the program.")
        sys.exit()

    print(f"We have {len(texts)} texts to analyze.")
    print("-" * 40)
    try:
        user_choice = int(input(f"Enter a number between 1 and {len(texts)} to select: "))
        if 1 <= user_choice <= len(texts):
            user_choise_text = texts[user_choice - 1]
        else:
            print("Invalid choice. Please select a valid number.")
            sys.exit()
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit()

    user_choise_text_sum_word = len(user_choise_text.split())
    user_choise_text_len_cap = sum(word.istitle() for word in user_choise_text.split())
    user_choise_text_sum_upper = sum(word.isupper() for word in user_choise_text.split())
    user_choise_text_sum_low = sum(word.islower() for word in user_choise_text.split())
    user_choise_text_sum_dig = sum(word.isdigit() for word in user_choise_text.split())
    user_choise_text_sum_symb = len(user_choise_text)

    stars_sum_word = "*" * user_choise_text_sum_word
    stars_len_cap = "*" * user_choise_text_len_cap
    stars_sum_upper = "*" * user_choise_text_sum_upper
    stars_sum_low = "*" * user_choise_text_sum_low


    print(f"There are {user_choise_text_sum_word} words in {user_choise_text}.\n"
          f"There are {user_choise_text_len_cap} capitalized words.\n"
          f"There are {user_choise_text_sum_upper} upper words.\n"
          f"There are {user_choise_text_sum_low} lowercase words.\n"
          f"There are {user_choise_text_sum_dig} numeric strings.\n"
          f"There are {user_choise_text_sum_symb} symbols in the text.")

    stars_sum_word = min(len("*" * user_choise_text_sum_word), 40)
    stars_len_cap = min(len("*" * user_choise_text_len_cap), 40)
    stars_sum_upper = min(len("*" * user_choise_text_sum_upper), 40)
    stars_sum_low = min(len("*" * user_choise_text_sum_low), 40)

    values = [stars_sum_word, stars_len_cap, stars_sum_upper, stars_sum_low]

    max_value = min(max(values), 40)


    print("----------------------------------------\n"
          "LEN|  OCCURRENCES  |NR.{max_value}\n"
          "----------------------------------------\n"
          f"  1|{stars_sum_word:<{max_value}} |{len(stars_sum_word)}\n"
          f"  2|{stars_len_cap:<{max_value}} |{len(stars_len_cap)}\n"
          f"  3|{stars_sum_upper:<{max_value}} |{len(stars_sum_upper)}\n"
          f"  4|{stars_sum_low:<{max_value}} |{len(stars_sum_low)}")















