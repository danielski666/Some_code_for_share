import HigherLower.art
import random
from HigherLower.game_data import data as d


def compare(option_a, option_b, guess):
    """Function compares the options with the highest value taking into account player answer.
       Takes arguments:
       - option_a: follower count for option A of compare names
       - option_b: follower count for option B of compare names
       - guess: player answer in the game: 'A' or 'B'"""

    if guess == "A":
        if option_a > option_b:
            return 1
        else:
            return 0
    if guess == "B":
        if option_a < option_b:
            return 1
        else:
            return 0
    else:
        print("Please retry and provide the correct answer: 'A' or 'B'.")
        return 0


def generate_data(data, chosen={}):
    """Function to provide the cases to compare.
       Taken arguments:
       - data: provided data: list of dicts with prepared data in special manner:
       {"name":"<name of the object>", "follower_count":<int(ammount of the followers)>,
       "description":"<main activity description>", "country":"<country of origin>"}
       - chosen: dictionary, empty for firs draw, currently used for comparison in next rounds
       Returning: chosen dict from the list. Dict is different from actually provided one."""
    new_data = random.choice(data)
    while chosen == new_data:
        new_data = random.choice(data)
    return new_data


def game():
    """Main game function, created to play the Higher Lower game :)"""
    play_again, score = "y", 0
    option_a = generate_data(d)
    while play_again == "y":
        if score == 0:
            option_a = generate_data(d)
        option_b = generate_data(d, option_a)
        print(art.logo)
        if score > 0:
            print(f"You are right! Your score: {score}")
        print(f"\nCompare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.\n")
        print(art.vs)
        print(f"\nAgainst B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.\n")
        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        comparison_result = compare(option_a["follower_count"], option_b["follower_count"], choice)
        if comparison_result == 1:
            score += 1
            if choice == "B":
                option_a = option_b

        if comparison_result == 0:
            print(art.logo)
            print(f"Sorry, you are wrong. Final score: {score}")
            play_again = input("Dou you want to play again? Type 'y' or 'n': ")
            if play_again == "y":
                score = 0


game()
