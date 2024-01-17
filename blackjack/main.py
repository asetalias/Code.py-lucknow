import random
import os
from art import logo

game_on = True
while game_on:
    wanna_play = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if wanna_play == 'n':
        print("Gameover.")
        game_on = False
        break
    else:
        # os.system('cls')
        os.system('cls')
        print(logo)

    def add_card(deck):
        card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        deck.append(random.choice(card))

    user_deck = []
    add_card(user_deck)
    add_card(user_deck)
    computer_deck = []
    add_card(computer_deck)
    add_card(computer_deck)

    def calculate_score(deck):
        if 11 in deck and 10 in deck:
            return 0
        elif 11 in deck:
            if sum(deck) > 21:
                deck.remove(11)
                deck.append(1)
                return sum(deck)
            else:
                return sum(deck)
        else:
            return sum(deck)

    def blackJack_check():
        # The `global run` statement is used to indicate that the variable `run` is a global variable,
        # meaning it can be accessed and modified from anywhere in the code. In this case, it is used
        # to control the main game loop by checking if the game should continue running or not.
        global run # just declare in once in the script no need to declare multiple times
        if calculate_score(computer_deck) == 0:
            print("Computer got a blackjack")
            print("Computer wins. Gameover \U00002639\U0000FE0F")
            run = False
        elif calculate_score(user_deck) == 0:
            print("You got a blackjack")
            print("You win. \U0001F60A")
            run = False
        else:
            run = True

    def result_of_game():
        global run 
        blackJack_check()
        if calculate_score(user_deck) > 21:
            print("You went over you lose. Gameover \U00002639\U0000FE0F")
            run = False
        elif calculate_score(user_deck) == calculate_score(computer_deck):
            print("Match Draw \U0001F91D")
            run = False 
        elif calculate_score(computer_deck) > 21:
            print("Computer went over. You win \U0001F60A")
            run = False
        elif calculate_score(computer_deck) > calculate_score(user_deck):
            print("You lose. Gameover \U00002639\U0000FE0F")
            run = False 
        elif calculate_score(computer_deck) < calculate_score(user_deck):
            print("You win. \U0001F60A")
            run = False
        else:
            run = True

    def display():
        print(
            f"\tYour cards: {user_deck}, current score = {calculate_score(user_deck)}"
        )
        print(f"\tComputer's first card: {computer_deck[0]}")

    def final_hand():
        print(
            f"\tYour final hand: {user_deck}, Your final score: {calculate_score(user_deck)}"
        )
        while calculate_score(computer_deck) <= 16:
            add_card(computer_deck)
        print(
            f"\tComputer's final hand: {computer_deck}, Computer's final score: {calculate_score(computer_deck)}"
        )

    display()
    run = True
    blackJack_check()
    while run:
        wanna_play = input("Type 'y' to get another card, type 'n' to pass: ")
        if wanna_play == 'y':
            add_card(user_deck)
            if calculate_score(user_deck) > 21:
                print(user_deck)
                print("You went over you lose. Gameover \U00002639\U0000FE0F")
                run = False 
                break
            display()
        else:
            final_hand()
            result_of_game()
            run = False
