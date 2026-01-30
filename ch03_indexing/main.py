str_example = 'Hello, Python!'


for i in range(len(str_example)):
    print(str_example[i], end='')

print()

for letter in str_example:
    print(letter, end='')

'''
마이너스 인덱스: 문자열의 뒤에서부터 부여하는 번호. 
맨 마지막 데이터의 인덱스 넘버는 -1

문자열 슬라이싱(slice): 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된
단어나 문장을 추출할 때 사용하는 방법
    추출하고자 하는 단어나 문장의 시작 인덱스와 종료 인덱스를 통해
    그 사이 문자들을 추ㅜ출하는 것이 가능함.
    
형식 :
변수명[시작인덱스 : 종료인덱스 : 증감값]
시작인덱스: 생략하면 처음부터 추출
종료인덱스: 생략하면 끝까지 추출
증감값: 생략하면 1씩 증가함(인덱스 넘버가 0부터 1씩 증가한다는 의미)
'''
print()
print(str_example[:-3:])
# 0번지부터 뒤에서 3번째 인덱스 미만까지만 출력

print(str_example[-1])
print(str_example[-2])
print(str_example[-3])
print(str_example[-4])
print(str_example[-5])
print(str_example[-6])
'''
근데 잘 생각해보면 range(시작값, 종료값, 증감값)이랑
변수명[시작인덱스:종료인덱스:증감값]이랑 똑같아보입니다.
, / : 함수냐 아니냐의 차이
'''
numbers = input('네자리 숫자를 입력하세요 >>> ')
print(f'맨 마지막 숫자는 {numbers[-1]}입니다.')

if int(numbers[-1]) % 2 == 0:
    print(f'맨 마지막 숫자는 {numbers[-1]}이며 짝수입니다.')
else:
    print(f'맨 마지막 숫자는 {numbers[-1]}이며 홀수입니다.')

'''
python 삼항 연산자
if - else 구조를 한 줄로 줄여서 쓴다
[참일때값] if [조건] else [거짓일때값].
'''
result = '짝수' if int(numbers[-1]) % 2 == 0 else '홀수'

print(f'맨 마지막 숫자는 {numbers[-1]}이며 {result}입니다.')




