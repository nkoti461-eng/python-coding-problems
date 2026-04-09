Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Problem Statement:
... #  Write a program that reverses a given number using a for loop.
...  num = int(input("Enter a number: "))
... rev = 0
... for i in range(len(str(num))):
...     digit = num % 10
...     rev = rev * 10 + digit
...     num = num // 10
