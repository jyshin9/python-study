#해당연도가 윤년인지 확인하기
#논리연산자 공부
year=2002
if((year%4==0)and(year%100!=0)or(year%400==0)):
    print(str(year)+"년은 윤년입니다") #str: year변수를 문자열로 변환
else:
    print(str(year)+"년은 윤년이 아닙니다")
