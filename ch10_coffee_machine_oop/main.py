from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 기본 생성자
menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()



is_on = True
while is_on:
    choice = input(f'어떤 음료를 드시겠습니까 ?{menu.get_items()} >>>> ')
    if choice == '종료':
        is_on = False
        print('자판기를 종료합니다.')
    elif choice == '정산':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is None:
            continue
        if coffe_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)




