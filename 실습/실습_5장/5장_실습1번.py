#5-1. 세 개의 수를 입력 받아 그 합과 평균을 출력하는 script를 작성할 것(평균은 소수점 한자리까지 출력)
a, b, c = input("정수 숫자 3개를 입력 : ").split()

a = int(a); b = int(b); c = int(c)

sum = a + b + c
avg = sum / 3

print("입력 받은 값 :",a,b,c) 
print("총합 :{:4}".format(sum))
print("평균 :{:4.1f}".format(avg))
