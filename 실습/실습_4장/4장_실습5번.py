#4-5. num = 3.1415926; x = "123“; y = "abc” 변수에 값을 주고, 다음과 같이 출력하는 script 작성할 것.
#주어진 변수만 사용하여 출력할 것/4개의 print() 문의 출력 형식을 지킬 것/문자열의 메소드 format() 을 사용하여 출력할 것
num = 3.1415926; x = "123"; y = "abc"

#변수 x에서 추출하여 출력
print(x[2],',',x[0],',',x[1])
#변수 num을 10자리 소수점 이후 2자리 실수 출력
print("{:10.2f}".format(num))
#정수 123출력(10자리)
print("{:10d}".format(int(x)))
#변수 y(10자리)
print("{:10s}".format(y))
