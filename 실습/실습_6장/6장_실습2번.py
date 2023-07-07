#6-2. 수식을  입력  받아  연산  결과를  출력하는  script 작성하라. (+, -, *, / 연산자만  구현, 그  외의  연산자는  허용하지  않는다는  메시지  출력)
s = input("수식입력(예: 20 * 40) : ")
a, b, c = s.split()
a, c = float(a), float(c)

if b == '+':
    r = a + c
elif b == '-':
    r = a - c
elif b == '*':
    r = a * c
elif b == '/':
    if c != 0:
        r = a / c
    else:
        print("0.000000 로 나누기를 수행할 수 없습니다.")
        exit()
else:
    print(b, "지원하지 않는 연산자입니다.")
    exit()

print("{:.6f} {} {:.6f} = {:.6f}".format(a, b, c, r))
