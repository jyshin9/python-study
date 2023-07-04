Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> intL = [4,1,8,6]
>>> mixes = [1, 2.2, "Mickey" , "민수", [8,4,"Python"]]
>>> NintL = len(intL)
>>> print(NintL, len(mixed))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(NintL, len(mixed))
NameError: name 'mixed' is not defined
>>> print(NintL, len(mixes))
4 5
>>> print(intL[-3], mixed[-2], mixed[-1])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(intL[-3], mixed[-2], mixed[-1])
NameError: name 'mixed' is not defined
>>> mixed = mixed
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    mixed = mixed
NameError: name 'mixed' is not defined
>>> mixed =  mixes
>>> print(intL[-3], mixed[-2], mixed[-1])
1 민수 [8, 4, 'Python']
>>> print(intL[0], mixed[1], mixed[4])
4 2.2 [8, 4, 'Python']
>>> print(mixed[4][0], mixed[4][1])
8 4
>>> print(mixed[4][0], mixed[4][2][0])
8 P
>>> list a = [0,1,2,3,4]
SyntaxError: invalid syntax
>>> a = [0,1,2,3,4]
>>> a[1:3]
[1, 2]
>>> print(a)
[0, 1, 2, 3, 4]
>>> a[1:3]=[]
>>> print(a)
[0, 3, 4]
>>> a[0] = 1
>>> a = [0,1,2,3,4]
>>> a[1]=['a','b']
>>> print(a)
[0, ['a', 'b'], 2, 3, 4]
>>> a[1]=1
>>> a[1:2] = ['a','b','c']
>>> print(a)
[0, 'a', 'b', 'c', 2, 3, 4]
>>> a = [0,1,2,3,4]
>>> a[1:1]=['a','b']
>>> print(a)
[0, 'a', 'b', 1, 2, 3, 4]
>>> len(a)
7
>>> L=[1,2,3,4]
>>> L.append(5) #5를 끝에 추가. L=[len(L):len(L)]=[5]
>>> print(L)
[1, 2, 3, 4, 5]
>>> L.insert(2,10) #10을 인덱스2에 삽입. L[2:2]=[10]
>>> print(L)
[1, 2, 10, 3, 4, 5]
>>> L.pop()
5
>>> print(L)
[1, 2, 10, 3, 4]
>>> L.pop(2)
10
>>> print(L)
[1, 2, 3, 4]
>>> len(L)
4
>>> L.removw(3)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    L.removw(3)
AttributeError: 'list' object has no attribute 'removw'
>>> L = ['M','a','r','a','n','a','t','h','a']
>>> L.index('a')
1
>>> L.count('a')
4
>>> A = [] #빈 리스트
>>> A.append('red')
>>> A.append('blue')
>>> A.append('yellow')
>>> print(A)
['red', 'blue', 'yellow']
>>> A.clear()
>>> print(A)
[]
>>> A = ['red', 'blue', 'yellow']
>>> del A[:]
>>> del A
>>> print(A)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(A)
NameError: name 'A' is not defined
>>> L=[1,5,3]
>>> M = [19,2]
>>> L.extend(M)
>>> print(L)
[1, 5, 3, 19, 2]
>>> L.sort()
>>> print(L)
[1, 2, 3, 5, 19]
>>> L.sort(reverse=True)
>>> print(L)
[19, 5, 3, 2, 1]
>>> L=[4,6,2,9,1]
>>> L.reverse()
>>> print(L)
[1, 9, 2, 6, 4]
>>> 
>>> all[1,2,3]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    all[1,2,3]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
>>> 
>>> all([1,2,3])
True
>>> all([])
True
>>> all([0,0])
False
>>> any[(0,0)]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    any[(0,0)]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> any([0,0])
False
>>> any([])
False
>>> any([1,0,0])
True
>>> L=[11,22,33]
>>> enumerate(L)
<enumerate object at 0x0000018317E21080>
>>> for x in enumerate(L):
	print(x)

	
(0, 11)
(1, 22)
(2, 33)
>>> L=[1,9,4]
>>> L = sorted(L, reverse=True)
>>> print(L)
[9, 4, 1]
p
>>> print(sum(L))
14
>>> L=["Jan","Apr","Sep"]
>>> print(min(L),max(L))
Apr Sep
>>> S=sorted(L)
>>> print(S)
['Apr', 'Jan', 'Sep']
>>> M=list(enumerate(L))
>>> print(M)
[(0, 'Jan'), (1, 'Apr'), (2, 'Sep')]
>>> L=[1,'2',3,'4']
>>> print(max(L),min(L))
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    print(max(L),min(L))
TypeError: '>' not supported between instances of 'str' and 'int'
>>> 