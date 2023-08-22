import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
computer_cards = []
endgame = False

# counter = 0
def setup_game():
    for x in range(2):
        player_cards.extend(random.choices(cards))
        computer_cards.extend(random.choices(cards))

       

# while endgame == False:
#     start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
#     if start == "y" and counter == 0:
#         setup_game()
#         counter += 1
#     elif start == "n":
#         endgame = True
#     sum_of_player_cards = sum(player_cards)
#     sum_of_computer_cards = sum(computer_cards)
#     print(f"your cards: {player_cards}, current score: {sum_of_player_cards}")
#     print(f"Computer's first card: {computer_cards[0]}")
#     another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#     if another_card == "y":
#         player_cards.extend(random.choice(cards))
#         computer_cards.extend(random.choice(cards))
#     elif another_card == "n":
#         if sum_of_computer_cards < 21:
#             computer_cards.extend(random.choice(cards))

start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if start == "y":
    setup_game()

    print(f"Your cards: {player_cards}, current score: ")
    print(f"Computer's first card: {computer_cards[0]}")
elif start == "n":
    endgame = True
another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
if another_card == "y":
    player_cards.extend(random.choices(cards))
    computer_cards.extend(random.choices(cards))
    print(f"Your cards: {player_cards}, current score: ")
    print(f"Computer's first card: {computer_cards[0]}")










