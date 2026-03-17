Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #check it is leap year or not
... year=int(input("enter a year:"))
... if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
...     print("it's Leap year")
... else:
