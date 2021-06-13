Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #print a value:
>>> print("30 days 30 hour challenge")
30 days 30 hour challenge
>>> 
>>> # assigning a string
>>> hours=thirty
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    hours=thirty
NameError: name 'thirty' is not defined
>>> hours = "thirty"
>>> print(hours)
thirty
>>> 
>>> #string indexing
>>> hours = "thirty"
>>> print(hours[0])
t
>>> rock = "indestructible"
>>> print(rock[-1])
e
>>> print(rock[3:6])
est
>>> print(rock[-2-5])
u
>>> print(rock[-3:-4])

>>> print(rock[-3:-4])

>>> print(rock[::-1])
elbitcurtsedni
>>> #reversing the whole string
>>> 
>>> # length of string
>>> ash = "hfjkhjhlwoifuwljlk"
>>> print(len(ash))
18
>>> # lower character:
>>> print(ash.lower())
hfjkhjhlwoifuwljlk
>>> #upper character:
>>> print(ash.upper())
HFJKHJHLWOIFUWLJLK
>>> 
>>> 
>>> #string concatenation
>>> a="30 days"
>>> b="30 hours"
>>> print (a+b)
30 days30 hours
>>> 
>>> # adding space during concatenation:
>>> c = a+""+b
>>> print(c)
30 days30 hours
>>> c = a+" "+b
>>> print(c)
30 days 30 hours
>>> 
>>> #casefold:
>>> text = "thirty days and thirty hours"
>>> print(text.casefold())
thirty days and thirty hours
>>> 
>>> #------------------------------------------------------------------------------------------------------
>>> 
>>> 
>>> sample = "DON'T TROUBLE UNTIL TROUBLE TROUBLES YOU."
>>> y = sample.capitalize()
>>> print(y)
Don't trouble until trouble troubles you.
>>> 
>>> y = sa
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    y = sa
NameError: name 'sa' is not defined
m
>>> y = sample.find('T')
>>> print(y)
4
>>> 
>>> y = sample.isalpha()
>>> print(y)
False
>>> 
>>> sample = 2135465
>>> y = sample.isalnum()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    y = sample.isalnum()
AttributeError: 'int' object has no attribute 'isalnum'
>>> y = sample.isnum()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    y = sample.isnum()
AttributeError: 'int' object has no attribute 'isnum'
>>> sample = "DON'T TROUBLE UNTIL TROUBLE TROUBLES YOU."
>>> y = sample.isalnum()
>>> print(y)
False
>>> 