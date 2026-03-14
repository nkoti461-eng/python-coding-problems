Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Write a Python program that:
... Takes student marks as input.Prints the grade based on marks using conditional statements.
... marks=eval(input("enter the marks"))
... if marks<100 and marks>79:
...     print("grade A")
... elif marks>78 and marks<51:
...     print("grade B")
... elif marks>50 and marks<36:
...     print("grade c")
... elif marks>35 and marks<34:
...     print("grade D")
... elif marks>34 and marks<1:
...     print("you fail")
... else:
