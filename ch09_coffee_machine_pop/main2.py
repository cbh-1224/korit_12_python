MENU = {
    '에스프레소': {
        '재료': {
            '물': 50,
            '커피': 18,
        },
        '가격': 1.5,
    },
    '라떼': {
        '재료': {
            '물': 200,
            '우유': 150,
            '커피': 24,
        },
        '가격': 2.5,
    },
    '카푸치노': {
        '재료': {
            '물': 250,
            '우유': 100,
            '커피': 24,
        },
        '가격': 3.0,
    },
}

resources = {
    '물': 300,
    '우유': 200,
    '커피': 100,
}

profit = 0

def report():
    print(f'물: {resources['물']}ml')
    print(f'우유: {resources['우유']}ml')
    print(f'커피: {resources['커피']}g')
    print(f'돈: ${profit}')


def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'죄송합니다. {item}이(가) 부족합니다.')
            return False
    return True


def process_coins():
    total = 0.0

    total += int(input('쿼터 동전을  몇개 넣으시겠습니까? >>> ')) * 0.25
    total += int(input('다임 동전을  몇개 넣으시겠습니까? >>> ')) * 0.1
    total += int(input('니켈 동전을  몇개 넣으시겠습니까? >>> ')) * 0.05
    total += int(input('페니 동전을  몇개 넣으시겠습니까? >>> ')) * 0.01
    return total


def is_transction_succssful(money_received, drink_cost):
    global profit
    change = 0
    if money_received < drink_cost:
        print(f'돈이 부족합니다. ${money_received}을 반환합니다.')
    else:
        change = round(money_received - drink_cost, 2)
        print(f'여기 ${change}의 잔돈이 있습니다')
        profit += drink_cost
        return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'주문하신 {drink_name} 나왔습니다.👍')


is_on = True
while is_on:
    choice = input('어떤 음료를 드시겠습니까? 에스프레소 / 라떼 / 카푸치노 >>>> ')
    if choice == 'off':
        print('자판기가 종료되었습니다.')
        is_on = False
    elif choice == 'report':
        report()
    elif choice in ['에스프레소', '라떼', '카푸치노']:
        drink = MENU[choice]
        if is_resource_enough(drink['재료']):
            money_received = process_coins()
            if is_transction_succssful(money_received, drink['가격']):
                make_coffee(choice, drink['재료'])
    else:
        print('잘못 입력 하셨습니다.')
        continue


