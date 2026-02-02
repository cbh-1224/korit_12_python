'''
응용 예제

list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 요소로부터 7번째 요소만 추출한 결과, 그리고 그
list에서 2 번째 요소를 출력하는 프로그램을 작성하시오.

실행 예
3 번째 요소로부터 7 번째 요소 = [30, 40, 50, 60, 70]
3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = 40


'''
import calendar

list1 = []

for num in range(1, 11):
    num *= 10
    list1.append(num)

print(f'3 번째 요소로부터 7 번째 요소 = {list1[2:7]}')
print(f'3 번째 요소로부터 7 번째 요소 중 2 번째 요소 =  {list1[2:7][1]}')

year = 2026
month_dict = {}

for i in range(1, 13):
    last_day_of_month = calendar.monthrange(year, i)[1]
    month_dict[i] = last_day_of_month

month = int(input('월을 입력하세요 >>> '))

if month in month_dict:
    print(f'{month}월은 {month_dict[month]}일까지 입니다.')
else:
    print('1에서 12 사이의 숫자를 입력하세요.')




