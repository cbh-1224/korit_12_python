'''
for 반복문 :
python에서의 default for문의 경우 enhanced for가 기본

range() 함수
'''
# 1 ~ 10 까지 출력
for i in range(10):
    print(i+1, end=' ')
print()
'''
이상에서 중요한 것은 i가 0부터 시작한다는 점
range(): 몇 번 반복할 것인가를 지정하는 함수 
-> 특히 for문과 연계되어 함께 쓰이는 편

range() 함수의 응용
range((시작값), 한계값, (증감값))

시작값: 생략 가능, 생략하면 0부터 시작
한계값: 명시하지 않으면 끝까지 진행
증감값: 생략 가능, 생략할 경우에 1씩 증가
'''
for i in range(1, 11):
    print(i, end=' ')
print()
print(i) # 결과값: 10
'''
Java에서는
for(int i = 0 ...) 후 출력하면 오류 발생
python은 지역 변수의 범위가 다르다는 점을 알 수 있다.

default 형태의 python for-loop 형식 :
for 변수명(자유롭게 가능) in iterable(반복가능객체):
    반복실행문
'''

nums = [1,2,3,4,5]
for i in nums:
    print(i, end='  ')

print()
if 5 in nums:
    print('5가 nums 리스트 내에 있습니다.')
else:
    print('5가 nums 리스트 내에 없습니다.')
'''
in이라는 애가 생각보다 엄청 중요하다.
in이 적용된 결과값의 자료형은 -> True / False가 나오는 '연산자'
A in B라고 했을 때 A라는 요소가 B라는 반복가능 객체 내에 존재하는지를
True / False로 뽑아주게 됩니다.
'''
print(5 in nums)    # 결과값: True