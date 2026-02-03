def count_even_odd(numbers):
    even = 0
    odd = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'짝수의 개수: {even}')
    print(f'홀수의 개수: {odd}')

count_even_odd([1,2,3,4,5,6,7,8,9,10])





