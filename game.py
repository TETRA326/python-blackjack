"""

ASCII Art created using:
https://patorjk.com/software/taag
https://emojicombos.com/card-ace-spades-ascii-art

"""

import random
import time
import shutil

ascii_art_1 = """

    ___       ___       ___       ___       ___       ___       ___       ___       ___   
   /\  \     /\__\     /\  \     /\  \     /\__\     /\  \     /\  \     /\  \     /\__\  
  /::\  \   /:/  /    /::\  \   /::\  \   /:/ _/_   _\:\  \   /::\  \   /::\  \   /:/ _/_ 
 /::\:\__\ /:/__/    /::\:\__\ /:/\:\__\ /::-"\__\ /\/::\__\ /::\:\__\ /:/\:\__\ /::-"\__\\
 \:\::/  / \:\  \    \/\::/  / \:\ \/__/ \;:;-",-" \::/\/__/ \/\::/  / \:\ \/__/ \;:;-",-"
  \::/  /   \:\__\     /:/  /   \:\__\    |:|  |    \/__/      /:/  /   \:\__\    |:|  |  
   \/__/     \/__/     \/__/     \/__/     \|__|               \/__/     \/__/     \|__|  


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⢠⣾⡿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣷⣀⢀⠀⣀⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣏⣀⣘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡟⣼⣆⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡿⣰⣿⣿⡄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⢡⣭⣭⣭⣭⡀⠸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⠿⠋⠸⢿⣿⣿⡿⠷⠀⠹⢿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡍⠉⣹⣿⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠉⠀⠁⠉⢿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣾⡿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

"""
ascii_art_2 = """

  ___ _      _   ___ _  __  _  _   ___ _  __
 | _ ) |    /_\ / __| |/ / | |/_\ / __| |/ /
 | _ \ |__ / _ \ (__| ' < || / _ \ (__| ' < 
 |___/____/_/ \_\___|_|\_\__/_/ \_\___|_|\_\\
                                            
                    .------.
                    |A.--. |
                    | (\/) |
                    | :\/: |
                    | '--'A|
                    `------'
"""

# Get the terminal size
terminal_size = shutil.get_terminal_size()
columns, lines = terminal_size.columns, terminal_size.lines

# Print artwork
if columns > 100:
    print(ascii_art_1)
elif 50 < columns < 100:
    print(ascii_art_2)

# Create and shuffle a deck of cards
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♠', '♥', '♦', '♣']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Calculate the total score of a hand, considering Aces
def calculate_score(cards):
    score = 0
    num_aces = 0

    for card in cards:
        if card['rank'] == 'A':
            num_aces += 1
            score += 11
        elif card['rank'] in ['K', 'Q', 'J']:
            score += 10
        else:
            score += int(card['rank'])

    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1

    return score

# Display the game board, including player and opponent hands
def display_board(player_cards, computer_cards, final=False):
    time.sleep(1)
    print("\nYou:", display_hand(player_cards), " = ", calculate_score(player_cards))
    time.sleep(1)
    if final:
        print("Opponent:", display_hand(computer_cards), " = ", calculate_score(computer_cards))
    else:
        print("Opponent:", display_hand([computer_cards[0]]))

# Make the hand readable
def display_hand(cards):
    return ' + '.join([f"{card['rank']}{card['suit']}" for card in cards])

# The game itself
def blackjack():
    print("Welcome to Blackjack!")
    time.sleep(1)

    player_cards = []
    computer_cards = []
    deck = create_deck()

    # Initial deal: each player gets two cards
    for _ in range(2):
        player_cards.append(deck.pop())
        computer_cards.append(deck.pop())

    game_over = False

    # Player's turn to draw cards
    while not game_over:
        display_board(player_cards, computer_cards)

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        # Check for game-ending conditions
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            draw_card = input("Type 'y' to get another card, 'n' to pass: ")
            if draw_card == 'y':
                player_cards.append(deck.pop())
            else:
                game_over = True
                break

    # Computer's turn to draw cards. Continue drawing cards till score is above 17
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deck.pop())
        computer_score = calculate_score(computer_cards)

    # Display final hands and determine the winner
    display_board(player_cards, computer_cards, final=True)
    print(compare(player_score, computer_score))

# Compare player and computer scores and determine the winner
def compare(player_score, computer_score):
    if player_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif player_score == computer_score:
        return "It's a draw!"
    elif player_score == 21:
        return "Blackjack! You win!"
    elif computer_score == 21:
        return "Computer has Blackjack. You lose!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

# Run the game
blackjack()
