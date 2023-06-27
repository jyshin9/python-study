from math import *

##파이썬 실습 과제
##No.1 어느 학생의 과제 점수가 21.9, 37, 13.6 일 때, 학생의 평균 과제 점수를 구하는 script 작성 할 것

grade1= 21.9
grade2= 37
grade3= 13.6

sumit = abs(grade1)+ grade2 +abs(grade3)

average = sumit / 3

print("1번 문제 답")
print(trunc(average))
print("-----------------------------")

##No.2 3928원의 금액을 500원 동전으로 교환하고 나머지 금액을 100원 동전으로 교환하고자 한다. 500원 동전, 100원 동전의 개수를 계산하여 출력하고 남은 금액을 출력하는 script 작성하라.

total = 3928
cnt500 = 0
cnt100 = 0

while total > 0:
    if total >= 500:
        cnt500 += 1
        total -= 500
    elif total >= 100:
        cnt100 += 1
        total -= 100
    else: 
        break

print("2번 문제 답")

print("500원짜리 동전 :", cnt500, "개")
print("100원짜리 동전 :", cnt100, "개")
print("남은 금액 :", total, "원")

