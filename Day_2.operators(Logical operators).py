Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Logical Operators: and, or, not
... 
... # ---------------- AND Operator ----------------
... x = 5
... print(x > 3 and x > 4)  
... # True because both conditions are True
... 
... a = 0
... b = 1
... print(a and b)  
... # 0 because in AND, if first value is 0 (False), it returns 0
... 
... a = True
... b = False
... print(a and b)  
... # False because both conditions must be True
... 
... 
... # ---------------- OR Operator ----------------
... a = 10
... print(a > 11 or a < 11)  
... # True because at least one condition is True
... 
... 
... # ---------------- NOT Operator ----------------
... x = 5
... print(not (x > 3 and x > 4))  
... # False because (True and True) = True, NOT True = False
... 
... a = False
... print(not a)  
