import random
from hangman_arts import * # hangman_arts 파일의 전체 데이터를 가지고 오겠다는 의미
from hangman_word_list import word_list # hangman_word_list 파일 내에서 word_list 변수만 가지고 오겠다는 의미

print(logo)

chosen_word = random.choice(word_list)
print(f'테스트 단어: {chosen_word}')
display = []

for _ in range(len(chosen_word)):
    display.append('_')

lives = 6
end_of_game = False

while not end_of_game:
    print(stages[lives])
    print(' '.join(display))
    print(f'기회가 {lives} 번 남았습니다.')
    print()
    guess = input('알파벳을 추측해서 입력하세요 >>> ').lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    print(f'기회가 {lives} 번 남았습니다.')

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print(f'모든 기회를 잃었습니다.')
            end_of_game = True
            print(f'정답은 {chosen_word}입니다.')

    if '_' not in display:
        print()
        print(' '.join(display))
        print('정답입니다 !!')
        end_of_game = True