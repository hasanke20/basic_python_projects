#The Password Generator generates a random password for you.
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ''
print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like? "))
nr_numbers = int(input("How many numbers would you like? "))
nr_symbols = int(input("How many symbols would you like? "))
total = nr_letters + nr_numbers + nr_symbols

for j in range(total):
    is_it_printed = False
    while not is_it_printed:
        a = random.randint(1,3)

        if a == 1 and nr_letters > 0:
            password += random.choice(letters)    #print(random.choice(letters), end="") end="" yan yana yazdırır
            nr_letters -= 1
            is_it_printed = True

        elif a == 2 and nr_numbers > 0:
            password += random.choice(numbers)
            nr_numbers -= 1
            is_it_printed = True

        elif a == 3 and nr_symbols > 0:
            password += random.choice(symbols)
            nr_symbols -= 1
            is_it_printed = True

print(f"Your password is: {password}")
