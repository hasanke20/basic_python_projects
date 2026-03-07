import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
wanna_continue = True
players_hand = []
computers_hand = []
while wanna_continue:
    check = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n':\U0001f447\U0001f447\U0001f447")
    print('\n'*100)
    print(art.logo)
    if check == "n":
        wanna_continue = False
    elif check == "y":
        players_hand = []
        computers_hand = []
        players_hand.append(random.choice(cards))
        players_hand.append(random.choice(cards))
        computers_hand.append(random.choice(cards))
        player_total = sum(players_hand)
        computer_total = sum(computers_hand)
        if player_total == 21:
            print(f"Your final hand: {player_total}, final score: {player_total}\nComputer's final hand:{computers_hand}, final score:{computer_total}\n You win with BlackJack! \U0001f631")
        elif player_total < 21:
            another_card = input(f"Your hand:{players_hand}, current score: {player_total} \nComputer's first hand:{computers_hand}\nType 'y' to get another card, type 'n' to pass:")
            while another_card == 'y':
                players_hand.append(random.choice(cards))
                player_total = sum(players_hand)
                computer_total = sum(computers_hand)
                if player_total > 21:
                    another_card = 'n'
                    print(f"\nYour hand:{players_hand}, final score: {player_total} \nComputer's first hand:{computers_hand}, final score: {computer_total}\nYou went over. You lose.\U0001F923")
                elif player_total < 21:
                    another_card = input(f"Your hand:{players_hand}, current score: {player_total} \nComputer's first card:{computers_hand}\nType 'y' to get another card, type 'n' to pass:")
                elif player_total == 21:
                    print(f"\nYour hand:{players_hand}, final score: {player_total} \nComputer's final hand:{computers_hand}, final score: {computer_total}\nYou win.\U0001fae3")
        if player_total < 21:
            computers_hand.append(random.choice(cards))
            computer_total = sum(computers_hand)
            if computer_total < 17:
                while computer_total < 17:
                    computers_hand.append(random.choice(cards))
                    computer_total = sum(computers_hand)
                if computer_total > 21:
                    print(f"\nYour hand:{players_hand}, final score: {player_total} \nComputer's final hand:{computers_hand}, final score: {computer_total}\nYou win.\U0001fae3")
                elif computer_total ==21:
                    print(f"\nYour hand:{players_hand}, final score: {player_total} \nComputer's first hand:{computers_hand}, final score: {computer_total}\nYou lose.\U0001F923")
                elif player_total == computer_total:
                    print(f"\nYour hand:{players_hand}, final score: {player_total} \nComputer's first hand:{computers_hand}, final score: {computer_total}\nIt's a draw.\U0001fae4")
                elif player_total > computer_total:
                    print(f"\nYour hand:{players_hand}, final score: {player_total} \nComputer's first hand:{computers_hand}, final score: {computer_total}\nYou win.\U0001fae3")
                elif player_total < computer_total:
                    print(f"\nYour hand:{players_hand}, final score: {player_total} \nComputer's first hand:{computers_hand}, final score: {computer_total}\nYou lose.\U0001F923")
            elif computer_total == 21:
                print(
                    f"Your final hand: {player_total}, final score: {player_total}\nComputer's final hand:{computers_hand}, final score:{computer_total}\n You lost against a BlackJack! \U0001f631")
            elif player_total == computer_total:
                print(
                    f"\nYour hand:{players_hand}, final score: {player_total} \nComputer's first hand:{computers_hand}, final score: {computer_total}\nIt's a draw.\U0001fae4")
            elif player_total > computer_total:
                print(
                    f"\nYour hand:{players_hand}, final score: {player_total} \nComputer's first hand:{computers_hand}, final score: {computer_total}\nYou win.\U0001fae3")
            elif player_total < computer_total:
                print(
                    f"\nYour hand:{players_hand}, final score: {player_total} \nComputer's first hand:{computers_hand}, final score: {computer_total}\nYou lose.\U0001F923")