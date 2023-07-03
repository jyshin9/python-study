n = int(input("Enter a number : ")) 
s = "even"
if n % 2 :    # n이 홀수일 때 True 
    s = "odd" # "even"이었던 s가 "odd"로 바뀜.
print("{} is {}.".format(n,s))
