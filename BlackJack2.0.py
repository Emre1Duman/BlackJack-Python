import random, os, art
clear = lambda: os.system('clear')

def blackjack():
    print(art.logo)

    def deal_card():
        """Returns a random card from the deck."""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2): #Deals 2 random cards to user & computer to set up the game.
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(cards):
        """Takes a list of cards and returns the total score."""
        total_score = sum(cards)
        if total_score == 21 and len(cards) == 2: #Checking for a blackjack (a hand with only 2 cards: 11 + 10).
            return 0 # 0 represents the blackjack
        if total_score > 21 and 11 in cards: #The ACE in the deck is 11, if the score is over 21 with 11 in your hand it can be changed to 1.
            cards.remove(11), cards.append(1)
        return total_score

    while not is_game_over: #While is_game_over is False contiue with loop.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21: #If any of these conditions are met the game ends.
            is_game_over = True
        else:
            another_card = input(" Type 'y' to get another card or 'n' to pass: ")
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17: #If the computer does'nt have a blackjack, and its score is less than 17 deal cards.
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)            

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "It's a draw! 🙃"
        elif user_score == 0:
            return "You have a blackjack. You win! 😎"
        elif computer_score == 0:
            return "Opponent has a blackjack. You lose! 😱"
        elif user_score > 21:
            return "You went over. You lose! 😭"
        elif computer_score > 21:
            return "Opponent went over. you win! 😀"
        elif user_score > computer_score:
            return "You have the larger hand. You win! 😀"
        else:
            return "Oppenent has the larger hand. You lose 😤"

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    
    go_again = input("Type 'y' to play again or 'n' to stop ")
    if go_again == 'y':
        clear()
        blackjack() #The whole game is within the blackjack function, if the user wants to play again the function is called within itself (recursion).
    else: 
        print("Goodbye...")

blackjack()