import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(cards):
    score = sum(cards)
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


def compare(player_score, computer_score):
    if player_score > 21:
        return "You lose."
    elif computer_score > 21:
        return "You win!"
    elif player_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "You lose."
    elif player_score == 0:
        return "You win!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose."
