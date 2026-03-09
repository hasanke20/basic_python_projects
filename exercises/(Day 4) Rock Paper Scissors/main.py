import random

rock = '''     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''
paper = '''     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''
scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
list = [rock, paper, scissors]
user = 0
computer = 0
user = int(input("Welcome to the place which boys become men.Choose one and START THE BATTLE!!!\nRock = 1\nPaper = 2\nScissors = 3\n"))-1
computer = random.randint(0,2)
print(f"Your choose{list[user]}")
print(f"Computer's choose{list[computer]}")
print("\nAND THE RESULT OF THE GAME\n")
if user == computer:
    print("It's a tie!")
elif user == 0 and computer == 2:
    print("You win!")
elif user == 1 and computer == 0:
    print("You win!")
elif user == 2 and computer == 1:
    print("You win!")
else:
    print("You lose!")


