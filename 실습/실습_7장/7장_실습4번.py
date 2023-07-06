#7-4. 사용자로부터 숫자 월을 입력 받아 그것에 대한 영문 이름을 출력하는 코드를 작성하시오.
#2가지 버전으로 코드를 작성한다. 리스트 없이, if 조건문을 사용하여 작성하시오. if조건문 없이, 리스트를 사용하여 작성하시오.
print("***** if조건문으로 작성 *****")

m = int(input("월을 입력하세요: "))

if m == 1:
    eng = 'January'
elif m == 2:
    eng = 'Feburary'
elif m == 3:
    eng = 'March'
elif m == 4:
    eng = 'April'
elif m == 5:
    eng = 'May'
elif m == 6:
    eng = 'June'
elif m == 7:
    eng = 'July'
elif m == 8:
    eng = 'August'
elif m == 9:
    eng = 'September'
elif m == 10:
    eng = 'October'
elif m == 11:
    eng = 'November'
elif m == 12:
    eng = 'December'
else:
    print("1부터 12까지 입력하세요.")
print(m,"월은", eng,"입니다")

print("***** 리스트로 작성 *****")
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
L2 = ['January','Feburary','March','April','May','June','July','August','September','October','November','December']

n = int(input("월을 입력하세요: "))

print(L1[n-1],"월은 ",L2[n-1],"입니다")