"""
    Day2 5min Challenge
"""

# 1. 사용자로부터 파이썬 점수, 자바 점수, C 점수 입력받는다(실수-realnumber)
# 2. 입력한 값들의 합계와 평균을 구한다.
# 3. 결과를 출력한다.
#   총 점수합계는 *.*점, 총 점수평균은 *.*점

# a = input('파이썬 점수 :')
# b = input('자바 점수 :')
# c = input('C 점수 :')
a, b, c = input("파이썬, 자바, C점수 각각 몇점이냐? 공백으로 구분해서 입력해봐 : ").split(' ') # split : 문자열의 기능
a, b, c = input("파이썬, 자바, C점수 각각 몇점이냐? 쉼표로 구분해서 입력해봐 : ").split(',')

#입력한 값 합계
#실수로 입력값 바꿔주기
d = float(a) + float(b) + float(c)

# 총 점수 평균
e = d / 3

print('총 점수합계는 {}점, 평균은 {}점이네요.'.format(d, e)) # format : 문자열의 기능
print(f'총 점수합계는 {d}점, 평균은 {e}점이네요.')
