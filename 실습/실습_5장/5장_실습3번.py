#5-3. 두 점의 좌표 값을 순서대로 입력받아(x1, y1, x2, y2) 다음과 같이 처리하는 script 작성할 것
import math

x1, y1, x2, y2 = input("두 점의 좌표 값을 x1, y1, x2, y2 순서대로 입력 : ").split()
x1 = float(x1); y1 = float(y1); x2 = float(x2); y2 = float(y2)

a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("두 점 사이의 거리는 %.2f 입니다." %a)

dis = a <= 5

print("두 점 사이의 거리가 5 이하 입니까? {}".format(dis))

