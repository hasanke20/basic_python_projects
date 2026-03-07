import random
import art
import game_data
guess_right = True

play_again = True
def compare():
    print(art.logo)
    print(f'You have {count} true guesses.')
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(art.vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")
    return input("Who has more followers? Type 'A' or 'B':")
while play_again == True:
    count = 0
    entered = ''
    option_a = random.choice(game_data.data)
    option_b = random.choice(game_data.data)
    if option_a['follower_count'] == option_b['follower_count']:
        option_a = random.choice(game_data.data)
        option_b = random.choice(game_data.data)
    while guess_right:
        if option_a['follower_count'] > option_b['follower_count']:
            answer = 'A'
        elif option_a['follower_count'] < option_b['follower_count']:
            answer = 'B'
        entered = compare().upper()
        if answer == 'A' and entered == 'A':
            count += 1
            option_b = random.choice(game_data.data)
        elif answer == 'B' and entered == 'B':
            count += 1
            option_a = option_b
            option_b = random.choice(game_data.data)
        else:
            print(f"You're wrong! Your make {count} right guesses.")
            guess_right = False
    go_on = input("Type 'y' to play again. 'n' to exit the game.").lower()
    if go_on == 'n':
        play_again = False
    if go_on == 'y':
        guess_right = True