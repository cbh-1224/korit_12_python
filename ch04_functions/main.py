'''
1. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드(methods)
    3) 사용자 정의 함수
2. 함수 용어 정리
    1) 함수 정의 : 사용자 정의 함수를 새로 만드는 것을 의미(def: define)
    2) 인수(argument) : 함수에 전달할 입력값(input)
    3) 매개변수(parameter) : argument를 받아서 저장하는 변수를 의미
    4) 반환값 / 결과값 / return값 : 함수의 출력 값(output)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것을 의미
3. (사용자 정의) 함수의 형식 :
    1) 함수 정의 부분
def 함수_이름(매개변수1, 매개변수2):
    실행문
    return

    2) 함수 호출 부분
변수 = 함수_이름(argument1, argument2)
'''

# eng_name = input('당신의 이름을 영어로 입력하세요. >>> ')
# eng_name_low = eng_name.lower()
# eng_name_upper = eng_name.upper()
# print(f'{eng_name_low} / {eng_name_upper}')
'''
str 자료형에 딸려있는 .메서드명()으로 호출하는 애들이 메서드
.lower() 데이터 -> 소문자 .upper() 데이터 -> 대문자
특정 클래스에 종속되어 있는 함수는 method / 함수는 독립적인 사용 가능
Java / JS 때와 마찬가지로 call1() ~ call4() 유형으로 정의할 수 있습니다.
'''
# # 함수 정의
# def multiply(dan):
#     for i in range(1, 10):
#         print(f'{dan} x {i} = {dan * i}')
#
# #함수 호출
# dan = int(input('몇 단을 출력하시겠습니까? >>> '))
# multiply(dan)

'''
파이썬에만 있는 연산자
// : 몫 연산자
'''
def vending_machine(money):
    price = 700
    for i in range(money // price + 1):
        print(f'음료수 = {i}개, 잔돈 = {money}원')
        money -= price

vending_machine(3600)



