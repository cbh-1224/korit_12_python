import random

word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(f'테스트 단어 :  {chosen_word}')

display = []

# display.append('김')
# display.append('영')
# print(display)
# display[1] = 1
# print(display)
# display[4] = 4 # 인덱스 없으면 대입 불가
# print(display)

for letter in chosen_word:
    display.append('_')

guess = input('알파벳을 추측해서 입력하세요 >>> ').lower()

for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        display[i] = chosen_word[i]

print(display)




