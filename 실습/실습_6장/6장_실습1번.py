#6-1. 세 개의 정수를 입력 받아 내림차순으로 정렬하여 출력하는 script 작성하라. (한개의 입력 함수만 사용 할 것)
a, b, c = input("세 개의 정수를 입력하시오 : ").split()
a, b, c = int(a), int(b), int(c)

if(a >= c and a >= b):
    if(b >= c):
        print("내림차순 정렬: ",a,b,c)
    else:
        print("내림차순 정렬: ",a,c,b)
elif(b >= a and b >= c):
    if(a >= c):
        print("내림차순 정렬: ",b,a,c)
    else:
        print("내림차순 정렬: ",b,c,a)
elif(c >= a and c >= b):
    if(a >= b):
        print("내림차순 정렬: ",c,a,b)
    else:
        print("내림차순 정렬: ",c,b,a)
