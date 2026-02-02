import random
# numbers = [1,2,3,4,5]
# chosen_number = random.choice(numbers)
# # random이라는 객체 같은 것에 choice라는 메서드가 있고
# # 내부에 list 자료형을 넣으면 하나를 뽑아서 변수에 저장
# print(chosen_number)

word_list = ['apple', 'banana', 'camel']

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input('알파벳을 추측해서 입력하세요 >>> ').lower()

for word in chosen_word:
    if word == guess:
        print(f'{guess}', end=' ')
    else:
        print('_', end=' ')

