#4-1. 두 개의 문자열이 다음과 같이 주어졌을 때, 문자열에서 숫자 부분을 분리하여 앞의 문자 부분을 숫자만큼 반복 출력하는 script 작성 할 것
#str1="Computer 4", str2="Science#5"/"computer"문자열을 4번, "science"문자열을 5번 연속 출력/두개의 print()함수 사용, *연산자 사용

str1="Computer 4"
str2="Science#5"

print(str1[:8]*int(str1[-1:]))
print(str2[:7]*int(str2[-1:]))
