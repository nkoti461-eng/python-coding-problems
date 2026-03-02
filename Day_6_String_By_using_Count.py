Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #take input from the user count the characters are how many times it repeated.
... from collections import Counter
... a=input("enter the char")
... d=Counter(a)
... for key in d:
