import random
from art import logo

# Values for deck of cards
# Includes face cards as 10 and Ace as either 11 or 1
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Function to deal a single card
def deal_card():
    return random.choice(cards)


# Function to calculate the score of a hand
def calculate_score(cards):
    score = sum(cards)
    # Switch Ace from 11 to 1 if total score exceeds 21
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


# Function to compare player's score with computer's score
def compare(player_score, computer_score):
    # Various game outcomes
    if player_score > 21:
        return "\nYou lose."
    elif computer_score > 21:
        return "\nYou win!"
    elif player_score == computer_score:
        return "\nIt's a draw."
    elif computer_score == 0:
        return "\nYou lose."
    elif player_score == 0:
        return "\nYou win!"
    elif player_score > computer_score:
        return "\nYou win!"
    else:
        return "\nYou lose."


# Main function to play the game
def play_game(round_number, computer_wins, player_wins):
    print(f"\n---------------------  ROUND {round_number}  ---------------------\n")
    player_cards = []
    computer_cards = []
    game_over = False

    # Initial dealing of two cards to each player
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        # Check for instant win/lose conditions
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            # Show player's hand and dealer's first card
            print(f"Your cards: {player_cards}, current score: {player_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            # Player decision to draw another card
            draw_card = input("Do you want to draw another card? Type 'y' or 'n': ")
            if draw_card == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    # Dealer draws cards until reaching score of 17 or more
    while computer_score < 17 and not game_over:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Display final hands, scores and results
    print(f"\nYour final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    result = compare(player_score, computer_score)
    print(result)

    # Update win counts
    if result == "\nYou win!":
        player_wins += 1
    elif result == "\nYou lose.":
        computer_wins += 1

    # Display total wins
    print(f"Total rounds won by computer: {computer_wins}")
    print(f"Total rounds won by player: {player_wins}")

    return computer_wins, player_wins


# Initialize score counters and round number
computer_wins = 0
player_wins = 0
round_number = 1
play_again = "y"

# Display game logo and house rules
print(logo)
print(
    "------------------   HOUSE RULES   ------------------\n1. The deck is unlimited in size.\n2. There are no jokers.\n3. The Jack/Queen/King all count as 10.\n4. The the Ace can count as 11 or 1.\n5. Cards are not removed from the deck as they are drawn.\n6. The computer is the dealer.\n\n---------------------   START   ---------------------"
)

# Main game loop
while play_again == "y":
    computer_wins, player_wins = play_game(round_number, computer_wins, player_wins)
    round_number += 1
