Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Count Vowels in a String
... # Problem Statement:
... #  Write a program that counts the number of vowels (a, e, i, o, u) present in a given string using a for loop.
... n=input("enter the char")
... a="aeiouAEIOU"
... count=0
... for ch in n:
...     if ch in a:
...         count+=1
...         print("it is vowel")
...     
