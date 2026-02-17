from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True


while is_on:
   options = menu.get_items()
   choice = input(f"What would u like to order? {options}: ") 
   
   if choice == "report":
        coffee_maker.report()
        money_machine.report()

   elif choice == "off":
        break
   else:
        drink = menu.find_drink(choice)
        check_resources = coffee_maker.is_resource_sufficient(drink)
        if check_resources == True:
             cost = drink.cost
             payment = money_machine.make_payment(cost)
             if payment == True:
                deduct = coffee_maker.make_coffee(drink)
        
        
