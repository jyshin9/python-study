#6-3. 십의 자리 정수 두 개를 입력 받아 각 자리 수를 교차 비교하여 같은 수 인지, 자리 값만 다른지, 하나의 수만 일치하는지, 또는 모두 일치하지 않는지를 구분하여 출력하는 script 작성하라.
a, b = input("두 자리 정수 두개를 입력 : ").split()
a = int(a); b = int(b)

a1 = a // 10; a2 = a % 10
b1 = b // 10; b2 = b % 10


if a == b:
    print("두 정수는 모두",a,"로 같은 정수입니다.")
elif (a1 == b1) and (a2 != b2) or (a1 != b1) and (a2 == b2):
    print(a,",",b,": 하나의 숫자만 일치합니다.")
elif (a1 == b2) and (a2 == b1):
    print(a,",",b,": 자리 값만 다른 정수입니다.")
else:
    if(a1 == b2) and (a2 != b1):
        print(a, ",", b, ": 하나의 숫자만 일치합니다.")
    elif (a1 != b2) and (a2 == b1):
        print(a, ",", b, ": 하나의 숫자만 일치합니다.")
    else:
        print(a,",", b, ": 일치하지 않는 정수입니다.")
