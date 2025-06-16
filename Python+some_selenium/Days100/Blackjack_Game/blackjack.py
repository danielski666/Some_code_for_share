import random


def get_card():
    """Returns a random card from the infinity deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card = random.choice(cards)
    return chosen_card


def calculate_score(cards):
    """Take a list of cards and returns the score calculated from cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score == 0:
        return "You win with a Blackjack"
    elif u_score > 21:
        return "You went over. You lose."
    elif c_score > 21:
        return "Opponent went over. You win."
    elif u_score > c_score:
        return f"You win! {u_score} VS {c_score}"
    else:
        return f"You lose... {u_score} VS {c_score}"

def play_blackjack():
    """Function for process the Blackjack game."""
    player_cards, computer_cards, is_game_over = [], [], False
    player_score, computer_score = -1, -1

    for _ in range(2):
        player_cards.append(get_card())
        computer_cards.append(get_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards is: {player_cards}, current score: {player_score}")
        print(f"Computer cards is: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            player_next_card = input("Type 'y' to get another card or type 'n' to pass: ")
            if player_next_card == 'y':
                player_cards.append(get_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(get_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards is: {player_cards}, and final score: {player_score}")
    print(f"Computer's final cards: {computer_cards}, and final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a geme of Blackjakc? Type 'y' or 'n': ") == 'y':
    print("\n" * 20)
    play_blackjack()