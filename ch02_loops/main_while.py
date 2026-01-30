'''
1. while 반복문
    while 다음에 나오는 조건식이 참이라면 이하의 실행문이 반복 실행됨
    조건이 False가 될 때 까지

형식 :
while 조건식1:
    반복실행문1

특정 시점에 while 반복문이 종료될 수 있도록 지정해야 한다. 중첩 while문 가능
'''

n = 1
while n < 11:
    print(n, end=' / ')
    n += 1

print()

n2 = 10
while n2 > 0:
    print(n2, end=' / ')
    n2 -= 1

dan = 2
number = 1

while dan < 10:
    number = 1
    while number < 10:
        print(f'{dan} x {number} = {dan * number}')
        number += 1
    dan += 1
    print()

print(number) # 전역 / 지역 변수의 개념이 java랑 다르다

