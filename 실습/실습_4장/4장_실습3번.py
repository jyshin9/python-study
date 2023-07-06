#4-3. sample = "abcABCdEFaBCDeFAbC" 문자열이 주어졌을 때, 대소문 자 구분 없이 “abc”, “def” 문자열이 처음 시작하는 인덱스, 반복 횟 수를 다음과 같이 출력하는 script 작성할 것(출력시 포맷팅은 % operator 사용)
sample = "abcABCdEFaBCDeFAbC"

index_abc=sample.lower().find('abc')
num_abc=sample.lower().count('abc')

index_def=sample.lower().find('def')
num_def=sample.lower().count('def')

print("\"abc문자열 : %d 인덱스, %d 번 존재\""%(index_abc, num_abc))
print("\"def문자열 : %d 인덱스, %d 번 존재\""%(index_def, num_def))
