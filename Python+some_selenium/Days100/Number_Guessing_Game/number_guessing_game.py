from random import randint
import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def game():
    """Game function, providing some fun."""
    number_to_guess = randint(1, 100)
    print(logo.art)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = EASY_LEVEL_TURNS if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy' else HARD_LEVEL_TURNS

    while difficulty > 0:
        print(f"You have {difficulty} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number_to_guess:
             print(f"You got it! The answer was: {number_to_guess}")
             break
        elif guess < number_to_guess:
            difficulty -= 1
            print("Too low. \nGuess again.")
        else:
            difficulty -= 1
            print("Too high. \nGuess again.")
    if difficulty == 0:
        print("You are run out of guesses. Try luck next time.")
    game() if input("Your game finished. Do you want to play again? Type 'y' or 'n': ") == 'y' else -1


game()
