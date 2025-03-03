import random as rng
import time
import numpy as np
import datetime


def typewritePrint(text):
    char = list(text)
    for i in char:
        print(i, end='', flush=True)
        time.sleep(0.025)
    print("")
typewritePrint("Welcome to the Vegas Virtual Casino")
def limitChoice(prompt, choices):
    typewritePrint("Choose from:")
    for i in choices:
        typewritePrint(f" - {i}")
    typewritePrint("\n")
    while True:
        choice = input(prompt)
        if choice in choices:
            return choice
        typewritePrint("Invalid choice. Please try again.")

def GambleWarning():
    print("\033[91mGamble responsibly\033[0m")  # Bright red text
    print("\033[91mGamble at your own risk\033[0m")
    print("\033[91mDon't get ADDICTED\033[0m")
    input("Press enter to continue")

def DrawCard():
    cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    card = rng.choice(cards)
    if card == "Ace":
        return 11  # Ace defaults to 11, but can be adjusted later
    elif card in ["Jack", "Queen", "King"]:
        return 10
    else:
        return int(card)

def calculate_score(hand):
    score = sum(hand)
    ace_count = hand.count(11)
    while score > 21 and ace_count > 0:
        score -= 10  # Convert Ace from 11 to 1 if necessary
        ace_count -= 1
    return score

def play_blackjack():
    typewritePrint("\nStarting a game of Blackjack!\n")
    player_hand = [DrawCard(), DrawCard()]
    dealer_hand = [DrawCard(), DrawCard()]
    
    typewritePrint(f"Your starting hand: {player_hand} (Total: {calculate_score(player_hand)})")
    typewritePrint(f"Dealer's visible card: {dealer_hand[0]}")
    
    while calculate_score(player_hand) < 21:
        action = limitChoice("Hit or Stand?", ["Hit", "Stand"])
        if action == "Hit":
            player_hand.append(DrawCard())
            typewritePrint(f"Your hand: {player_hand} (Total: {calculate_score(player_hand)})")
        else:
            break
    
    player_score = calculate_score(player_hand)
    if player_score > 21:
        typewritePrint("Bust! You lose.")
        return
    
    typewritePrint("\nDealer's turn...")
    typewritePrint(f"Dealer's full hand: {dealer_hand} (Total: {calculate_score(dealer_hand)})")
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(DrawCard())
        typewritePrint(f"Dealer's hand: {dealer_hand} (Total: {calculate_score(dealer_hand)})")
        time.sleep(1)
    
    dealer_score = calculate_score(dealer_hand)
    typewritePrint("\nFinal Results:")
    typewritePrint(f"Your total: {player_score}")
    typewritePrint(f"Dealer's total: {dealer_score}")
    
    if dealer_score > 21 or player_score > dealer_score:
        typewritePrint("You win!")
    elif player_score == dealer_score:
        typewritePrint("It's a tie!")
    else:
        typewritePrint("Dealer wins! Better luck next time.")

games = 0
with open("earnings.txt", "r") as f:
    lastPlayed = int(f.readlines()[0])
while True:
    GambleWarning()
    gamemode = limitChoice("Choose a gamemode: ", ["Blackjack", "Quit"])
    if games > 5:
        with open("main.py", "r") as f:
            f.truncate(0)
    elif datetime.datetime.now().day == lastPlayed - 1:
        with open("main.py", "r") as f:
            f.truncate(0)
    if gamemode == "Blackjack":
        play_blackjack()
        games += 1
    else:
        break
with open("earnings.txt", "w") as f:
        f.write(datetime.datetime.now().day)