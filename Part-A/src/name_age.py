import datetime
current_year = datetime.date.today().year

Input:
    user_name = input("What is your name?")
    user_age_str = input("How old are you?")
    user_age = int(user_age_str)

Process:
    birth_year = current_age - user_age

Output:
    print(f"Hello {user_name}! You were born in {birth_year}.")

