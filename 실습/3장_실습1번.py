#어느 학생의 과제 점수가 21.9, 37, 13.6일 때, 학생의 평균 과제 점수를 구하는 script를 작성할 것
#각 점수는 변수에 저장, 평균 값의 소수점 이하는 버리고 출력, math 모듈함수를 사용
#출력/ average: 24
import math

score1 = 21.9
score2 = 37
score3 = 13.6

avg = math.floor((score1 + score2 + score3)/3)

print('average: '+str(avg))
