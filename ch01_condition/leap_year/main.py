year = int(input('연도를 입력하세요: '))

# if int(year) % 4 == 0 and int(year) % 400 == 0:
#     print(f'{year}년은 윤년입니다.')
# else:
#     print(f'{year}년은 윤년이 아닙니다.')

# if int(year) % 400 == 0:
#     print(f'{year}년은 윤년입니다.')
# elif int(year) % 100 == 0:
#     print(f'{year}년은 윤년이 아닙니다.')
# elif int(year) % 4 == 0:
#     print(f'{year}년은 윤년입니다.')
# else:
#     print(f'{year}년은 윤년이 아닙니다.')

leap_year = '윤년입니다.'
if int(year) % 400 == 0:
    leap_year
elif int(year) % 100 == 0:
    leap_year ='윤년이 아닙니다.'
elif int (year) % 4 == 0:
    leap_year
else:
    leap_year = '윤년이 아닙니다.'

print(f'{year}년은 ' + leap_year)