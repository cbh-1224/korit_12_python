print('Hello, Python!')
# 주석(comment): 한줄 주석 / python 인터프리터가 코드로 인식하지 않음
# 사후 주석  : ctrl + /
'''
다중 주석: 작은따옴표 세개 - 얘는 다중  str 입력할 때 쓰는 기호에 해당
그런데 얘를 변수에 대입하지 않았기 때문에 그냥 다중 주석용으로 쓰는 편
'''

print(1) # 숫자 자료형
print('1') # 문자열 자료형
print(1+2)
print('1' + '2')
print(type('1')) # <class 'str'>
print(type(1)) # <class 'int'>
print(type(1.1)) # <class 'float'>
'''
print(): 콘솔에 출력하는 '함수'
type():  소괄호  내에 있는 arguement가  어떤 자료형인지 알려주는 명령어
    - JS에서는 typeof가 연산자였기 때문에 ()가 없었죠.
    - Java에서는 객체 instanceof 클래스명이라는 연산자로 사용하지만
        문법이 다르죠.
'''
print('이거 쓰고 나면 다음 명령어 쓸때 자동 개행')
print('이거 쓰고 나면 다음 명령어 쓸때 자동 개행')
print('하지만 end=라는 구문을 사용하면', end=' / ')
print('끝에 나오는 부분을 통제할 수 있습니다.')

name = '김영'
age = 20 # 변수 선언할 때 선언자도 없고 자료형도 없습니다.
print('안녕하세요. 제 이름은 ' + name + '이고', '나이는 ' + str(age) + '살입니다.')
'''
이상의 코드에서 Java와 유사하게 작성할 수 있지만 맨 처음이 문자열이면 뒤에 나오는 정수
데이터가 자동으로 바뀌는 Java와는 달리 python에서는 자료형이 일치해야 합니다. 
str() : 다른 데이터를  문자열 자료형으로 바꿔주는 함수
int() : 문자열/실수 자료형을 정수형으로 바꿔주는 함수
float() : 실수 자료형으로 바꿔주는 함수

이상의 방식은 귀찮고 번거롭다
-> f-string 개념 사용
'''
print(f'안녕하세요. 제 이름은 {name}이고, 나이는 {age + 1}살 입니다.')
'''
JS에서의 template literal과 유사 JS = ${}

Java에서의 scanner와 유사한 기능
'''
# name2 = input('이름을 입력하세요 >>> ')
# print(name2)
age2 = input('나이를 입력하세요 >>> ')
print(type(age2)) # 결과값 : <class 'str'>


