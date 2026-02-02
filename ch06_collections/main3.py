hope_trip_set = set()
num_of_students = 3

for i in range(num_of_students):
    student = input('희망하는 수학여행지를 입력하세요 >>> ')
    hope_trip_set.add(student)

print(f'조사된 수학여행지는 {hope_trip_set}입니다.')

num = int(input('몇 개의 숫자를 입력할까요? >>> '))

nums_list = []
even_list = []

for i in range(num):
    num = int(input(f'{i + 1} 번째 숫자를 입력하세요 >>> '))
    nums_list.append(num)
    if num % 2 == 0:
        even_list.append(num)

print(f'입력 받은 숫자는 {nums_list}입니다.')
print(f'입력 받은 숫자들 중 짝수는 {even_list}입니다.')

phone_dict = {}
users = 3

for i in range(users):
    name = input(f'{i + 1} 번째 사람의 이름을 입력하세요 >>> ')
    phone_number = input(f'{i + 1} 번째 사람의 연락처를 입력하세요 >>> ')
    phone_dict[i] = {
        name: phone_number
    }

print(f'입력 받은 연락처는 {list(phone_dict.values())} 입니다.')

def add_numbers(n):
    numbers1 = []
    for i in range(n):
        num = int(input('숫자를 입력하세요>>> '))
        numbers1.append(num)
    print(numbers1)

add_numbers(10)

last_num = int(input('숫자 몇 까지 입력하시겠습니까? >>> '))
def add_numbers1(last_num):
    numbers1 = []
    for i in range(last_num):
        num = int(input('숫자를 입력하세요>>> '))
        numbers1.append(num)
    print(numbers1)


def add_numbers2(last_num):
    numbers2 = []
    for i in range(last_num):
        num = int(input('숫자를 입력하세요 >>> '))
        numbers2.append(num)

    return numbers2

add_numbers1(last_num)
print(add_numbers2(last_num))


hello = ['안','녕','하','세','요']

def add_numbers3(n, hello):
    for i in range(n):
        hello.insert(i, i + 1)
    print(hello)

add_numbers3(10, hello)






