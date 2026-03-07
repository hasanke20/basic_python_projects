import random
import art
print(art.logo)
target = random.randint(1, 100)
diff = input("Welcome to Guess the Number.\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard':")
if diff == 'easy':
    attempt = 10
elif diff == 'hard':
    attempt = 5
while attempt > 0:
    number = int(input(f"\nYou have {attempt} attempts remaining to guess the number.\nGuess the number:"))
    if number == target:
        print(f"Congratulations, you guessed the number right!!!")
        attempt = 0
    if number > target:
        print("High Guess")
    if number < target:
        print("Low Guess")
    attempt -= 1
if attempt == 0:
    print(f"You're out of guesses, the number was {target}.")