"""Calculates and displays a user's birth year based on their age.

Input:
    user_name (str): Manually entered
    user_age_str (str): Manually entered.
    CURRENT_YEAR (int): Automatically retrieved from the system.

Process:
    Subtract user's age from the current year to find out the year of birth.

Output:
    Greeting that is personalized with the individuals year of birth. String will be displayed on the output terminal.

Typical usage example:
    What is your name? Layla
    How old are you? 39
    Hello Layla! You were born in 1987.
"""
# === Imports ===
from datetime import date


# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    user_name = input("What is your name? ")
    user_age_str = input("How old are you? ")

    # Calculate user's approximate birth year.
    user_age = int(user_age_str)
    birth_year = CURRENT_YEAR - user_age

    # Output personalized message with user's name and birth year.
    print(f"Hello {user_name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
zyBooks. (2026).Zybooks.Com. https://learn.zybooks.com/zybook/IT-140-11100-M01_Introduction_to_Scripting_2026_C-5

