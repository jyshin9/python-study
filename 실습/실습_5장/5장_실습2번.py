#5-2. "Good words cost nothing" 문장에서 입력 받은 단어가 몇 번 나오는지, 횟수를 출력하는 script 작성할 것(출력시 포맷팅은 %operator 사용)
s = "Good words cost nothing"

word = input("찾는 단어 입력 : ")
a = s.count(word)

print("Good words cost nothing 문장에서는 %s 단어가 %d 번 있습니다."%(word, a))
