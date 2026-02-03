# class Korean:
#     country = '한국' # 클래스 변수 #1
#     def __init__(self, name, age, address):
#         self.name = name # 인스턴스 변수 #1
#         self.age = age # 인스턴스 변수 #2
#         self.address = address # 인스턴스 변수 #3
#
# korean = Korean('김일', 21, '서울특별시 마포구')
# print(korean.name) # 인스턴스 변수 참조
#
# #클래스 변수 참조
# print(korean.country) # 객체명.클래스 변수명으로 접근 가능
# print(Korean.country) # 클래스명.클래스 변수명으로 접근 가능
#
# class Korean2:
#     country = '대한민국' #클래스 변수 선언 및 초기화
#     #클래스 메서드 정의 방법
#     @classmethod
#     def trip(cls, travelling_site):
#         if cls.country == travelling_site:
#             print('국내 여행입니다.')
#         else:
#             print('해외 여행입니다.')
#
# Korean2.trip('대한민국')
# Korean2.trip('미국')
#
# person2 = Korean2()
# person2.trip('일본') # 권장 X
#
# class Korean3:
#     country = '한국'
#
#     @staticmethod
#     def slogan():
#         print('Imagine Your Korea!')
#
#     @staticmethod
#     def slogan2(str_example):
#         print(f'Imagine Your Korea! {str_example}')
#
# Korean3.slogan()
# Korean3.slogan2('안녕하세요')
#
# class Bag:
#     count = 0
#
#     def __init__(self):
#         Bag.count += 1
#         print('가방 객체가 생성되었습니다.')
#
#     @classmethod
#     def sell(cls):
#         print('가방이 팔렸습니다.')
#         cls.count -= 1
#
#     @classmethod
#     def remain_bag(cls):
#         return cls.count
#
# bag1 = Bag()
# print(f'현재 가방 재고: {Bag.count}')
# bag2 = Bag()
# bag3 = Bag()
# print(f'현재 가방 재고: {Bag.count}')
# bag1.sell()

class Person:
    count = 0
    def __init__(self, name):
        Person.count += 1
        self.name = name
        print(f'{name}이(가) 태어났습니다.')

    @classmethod
    def get_population(cls):
        return cls.count

    def __del__(self):
        print(f'RIP {self.name}')
        Person.count -= 1

man = Person('김일')
woman = Person('김이')
print(f'전체 인구수: {Person.get_population()}')
del man
print(f'전체 인구수: {Person.get_population()}')