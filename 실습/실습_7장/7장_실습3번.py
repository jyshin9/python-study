#7-3. 리스트 method 중 append()를 사용하여 아래의 조건을 만족하는 script를 작성할 것.
#L = [1,2,3,4,5]에 새로 추가할 원소를 입력 받을 것, 추가할 원소의 데이터형은 정수로 제한
L = [1, 2, 3, 4, 5]

n = input("리스트 L에 추가할 data를 입력 : ")

try:
    n = int(n)
except ValueError:
    print("data는 정수값으로 입력해주세요")
    exit()

L.append(n)

print(L)


