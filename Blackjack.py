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

computer_score = 0
player_score = 0
       
start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if start == "y":
    setup_game()
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    print(f"Your current cards: {player_cards} your current score: {player_score}")
    print(f"Computers first card: {computer_cards[0]}, computers current score: {computer_score}")
    while endgame == False:
        player_score = sum(player_cards)
        computer_score = sum(computer_cards)
        if player_score == 21:
            endgame = True
            print("You have a blackjack, you win!")
        elif computer_score == 21:
            endgame = True
            print("Computer has a blackjack, you Lose!")
        elif player_score == 21 and computer_score == 21:
            print("It's a draw")       
        if 11 in player_cards and player_score > 21:
            index = player_cards.index(11)
            player_cards[index] = 1
            print(f"if ace is a 1, still over 21? {player_score}")
            if player_score > 21:
                endgame = True
                print("It's a bust, you lose!")
        elif player_score > 21:
            endgame = True
            print("It's a bust, you lose!2")
            endgame = True
        new_card = input("Do you want to draw another card? Type 'y' or 'n'. ").lower()
        if new_card == 'n': 
            while computer_score < 17:
                computer_cards.extend(random.choices(cards))
                computer_score = sum(computer_cards)
            if computer_score > 21:
                print("You win!")
                endgame = True
            elif player_score > computer_score:
                print("You lose!")
                endgame = True
            elif player_score < computer_score:
                print("You win!")
                endgame = True
            elif player_score == computer_score:
                print("Its a draw")
        elif new_card == "y":
            player_cards.extend(random.choices(cards))
else:
    print("Goodbye")







#     print(f"Your cards: {player_cards}, current score: ")
#     print(f"Computer's first card: {computer_cards[0]}")
# elif start == "n":
#     endgame = True
# another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
# if another_card == "y":
#     player_cards.extend(random.choices(cards))
#     computer_cards.extend(random.choices(cards))
#     print(f"Your cards: {player_cards}, current score: ")
#     print(f"Computer's first card: {computer_cards[0]}")










