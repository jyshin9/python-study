Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input("Enter your name:")
Enter your name:Eric
>>> name
'Eric'
>>> a = input("djWjrn")
djWjrnrr
>>> a
'rr'
>>> b = input("ff")
ffe
>>> ff
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ff
NameError: name 'ff' is not defined
>>> e
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> b
'e'
>>> name = input(your name?)
SyntaxError: invalid syntax
>>> name = input("what's ypur name?")
what's ypur name?주영
>>> name
'주영'
>>> n = input("enter two names")
enter two names주영 석호
>>> n1, n2 = n.split()
>>> print(n1,n2)
주영 석호
>>> q,w=input("enter two names").split()
enter two names주 석
>>> print(n1,n2,q,w)
주영 석호 주 석
>>> a = int(input("enter int"))
enter int123
>>> print(a)
123
>>> b = input("enter int")
enter int123
>>> b
'123'
>>> print("First Person.:, end ='');print("Second Person.")
      
SyntaxError: invalid syntax
>>> a=1/4
>>> print('My name is {1}. Iam {0} years ole.'.format('Mario',40))
My name is 40. Iam Mario years ole.
>>> print('The light was {:10}.'.format('good'))
The light was good      .
>>> print('The light was {10:}.'.format('good'))
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print('The light was {10:}.'.format('good'))
IndexError: Replacement index 10 out of range for positional args tuple
>>> number = 3
>>> print("I eat {:10} appels.".format(number))
I eat          3 appels.
>>> i = 123; f = 3.14; s = 'Hello'
>>> print('i: %d, f: %d, s: %s' %(i, f, s))
i: 123, f: 3, s: Hello
>>> print('i: %9d, f: %5.2f, s: %7s' %(i,f,s))
i:       123, f:  3.14, s:   Hello
>>> print('i: %09d, f: %05.2f, s: %7s' %(i,f,s))
i: 000000123, f: 03.14, s:   Hello
>>> print('i :{}, f:{}, s:{}'.format(i,f,s))
i :123, f:3.14, s:Hello
>>> print('f:{1}, i:{0}, s:{2}'.format(i,f,s))
f:3.14, i:123, s:Hello
>>> 
KeyboardInterrupt
>>> print('i: %9d, f: %5.2f, s: %7s' %(i,f,s))
i:       123, f:  3.14, s:   Hello
>>> 
KeyboardInterrupt
>>> print('i: %9d, f: %5.2f, s: %7s' %(i,f,s))
i:       123, f:  3.14, s:   Hello
>>> print('f: {ff}, i: {ii}, s: {ss}'.format(ii=i, ff=f, ss=s))
f: 3.14, i: 123, s: Hello
>>> print('a is {a}, b is {b}'.format(a='apple', b =banana'))
				  
SyntaxError: EOL while scanning string literal
>>> print('a is {a}, b is {b}'.format(a='apple', b ='banana'))
a is apple, b is banana
>>> 