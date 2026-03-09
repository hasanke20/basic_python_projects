from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_coffee_maker = CoffeeMaker()
my_menu = Menu()
coffee_options = my_menu.get_items()
my_money_machine = MoneyMachine()
while True:
    order = input(f"What would you like? {coffee_options}:")
    if order == 'report':
        my_coffee_maker.report()
    elif order == 'reload':
        my_coffee_maker.reload_resources()
    else:
        choosen_drink = my_menu.find_drink(order_name=order)
        if choosen_drink is not None:
            can_make = my_coffee_maker.is_resource_sufficient(drink=choosen_drink)
            if can_make:
                check_money =my_money_machine.make_payment(cost=choosen_drink.cost)
                if check_money:
                    my_coffee_maker.make_coffee(order=choosen_drink)

