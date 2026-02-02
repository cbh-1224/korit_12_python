import random

word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
display = []

for _ in range(len(chosen_word)):
    display.append('_')
print(chosen_word)
'''
''.join(반복가능객체) method: '.'앞에 있는 문자열을 기준으로 
반복 가능 객체의 element들을 합쳐서 str로 만들어주는 method
'''
# temp = ['s', 'q', 'l', 'd']
# test = ''.join(temp)
# test = '/'.join(temp)
# test = ' '.join(temp)
# print(test)

while True:
    guess = input('알파벳을 추측해서 입력하세요 >>> ').lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    print(' '.join(display))

    if ' '.join(display) == ' '.join(chosen_word):
        print('정답입니다 !! ')
        break

while _ in display:
    guess = input('알파벳을 추측해서 입력하세요 >>> ').lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    print(' '.join(display))

    print('정답입니다 !! ')








