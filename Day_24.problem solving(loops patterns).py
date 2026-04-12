Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a Python program using nested loops to print a symmetric number pattern where each row increases from 1 to the row number and then decreases back to 1 (for n = 5).
>>> for i in range(1,6):
...     for j in range(1,i+1):
...         print(j,end=" ")
...     for j in range(j-1,0,-1):
...         print(j,end=" ")
