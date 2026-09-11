TODO: import datetime

Input:
    TODO: current_year = datetime.date.today().year
    TODO: user_name = input("What is your name?")
    TODO: user_age_str = input("How old are you?")

Process:
    TODO: user_age = int(user_age_str)
    birth_year = current_year - user_age

Output:
    TODO: print(f"Hello {user_name}! You were born in {birth_year}.")

Typical usage example:
    TODO: Replace with the input prompt and original name-input example.
    TODO: Replace with the input prompt and original age-input example.
    TODO: Replace with the resulting output from those inputs.
"""
# === Imports ===
from datetime import date


# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    # TODO: Replace with code to get user's name as a string. See zyBooks 1.3.
    # TODO: Replace with code to get user's age as an integer. See zyBooks 2.6.

    # Calculate user's approximate birth year.
    # TODO: Replace with code to process data. See zyBooks 1.16 & 1.17.

    # Output personalized message with user's name and birth year.
    # TODO: Replace with code to output formatted results. zyBooks 1.3 & 2.7.


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
# TODO: Replace with an APA-style reference for a source you used, or delete.
# TODO: Replace with another APA-style reference, or delete this TODO line.
