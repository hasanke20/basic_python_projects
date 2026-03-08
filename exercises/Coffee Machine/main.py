import data
import art
def get_order(given_order):
    if given_order == "report":
        print(f"Water: {data.resources['water']}ml")
        print(f"Milk: {data.resources['milk']}ml")
        print(f"Coffee: {data.resources['coffee']}g")
        print(f"Money: ${data.money}")
    elif given_order == "latte" or given_order == "cappuccino" or given_order == "espresso":
        if data.resources['water'] < data.MENU[f'{given_order}']['ingredients']['water']:
            print("Sorry, we don't have enough water. Money refunded.")
        elif data.resources['milk'] < data.MENU[f'{given_order}']['ingredients']['milk']:
            print("Sorry, we don't have enough milk. Money refunded.")
        elif data.resources['coffee'] < data.MENU[f'{given_order}']['ingredients']['coffee']:
            print("Sorry, we don't have enough coffee. Money refunded.")
        elif data.resources['water'] >= data.MENU[f'{given_order}']['ingredients']['water'] and data.resources['milk'] >= data.MENU[f'{given_order}']['ingredients']['milk'] and data.resources['coffee'] >= data.MENU[f'{given_order}']['ingredients']['coffee']:
            print("Please insert coins.")
            quarters = int(input("How many quarters?:"))
            dimes = int(input("How many dimes?:"))
            nickles = int(input("How many nickles?:"))
            pennies = int(input("How many pennies?:"))
            given_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            if given_money >= data.MENU[f'{given_order}']['cost']:
                given_money -= data.MENU[f'{given_order}']['cost']
                given_money = round(given_money, 2)
                print(f"Here is ${given_money} in change.\nHere is your {given_order}, enjoy.")
                data.resources['water'] -= data.MENU[f'{given_order}']['ingredients']['water']
                data.resources['milk'] -= data.MENU[f'{given_order}']['ingredients']['milk']
                data.resources['coffee'] -= data.MENU[f'{given_order}']['ingredients']['coffee']
                data.money += data.MENU[f'{given_order}']['cost']
    elif given_order == "refound":
        data.resources['water'] += 300
        data.resources['milk'] += 200
        data.resources['coffee'] += 100
        print("The Coffe Machine has refounded.")
    else:
        print("Please type valid coffee names.")
print(art.logo)
while True:
    order = input("What would you like? (espresso/latte/cappuccino):")
    get_order(order)