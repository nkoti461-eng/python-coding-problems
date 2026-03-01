Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #String:
... # >it is immutable
... # >it is in sequence order
... # >it is heterogeous
... # >And it is nested list
... # >String in python are surrounded by either single(or)double quotations marks.
... # a='mahesh'
... # a[0]
... # a="sham"
... a[0]+a[1]+a[2]+a[3]
... #silcing:is a way to extract a portion of a sequence (like a list, tuple, string, or range) using the syntax:
... # slicing([start:stop:step])
... # a="karishma"
... # a[0:7:2]
... a='christmas is around the corner'
... print(a[-9])
... print(a[::2])
... print(a[:5])
... print(a[::-1])
... print(a[-7:-3:1])
... print(a[-7:23:1])
... print(a[23:-7:1])
... print(a[-7:3:-1])
... print(a[-7:-3:-1])
... #String:Buliding function
... a="Sandeep is my name"
... len("a")
... print(a.count("m"))
... print(a.upper())#it gives the captial letters
... print(a.lower())#it convert into Z to z
... print(a.capitalize())#it will conert only first letter as the captial 
... print(a.title())#in this in word 1 letter become as captial
... print(a.find('a'))#there we count the letter who many times it written
... print(a.index('z'))#it will show the index position
... print(a.replace("a","z"))#here we can change the word
... print(a.split())#it will split by word by word
print(a.strip("my"))# it will cut or remove only first and last character
print(a.isdigit())#it will inthat digit or not in(true or false)
print(a.isalpha())#it will check the char is alpha or not.
print(a.isalnum())#it is both alpha and digit in the varible
print(a.endswith("my"))#it will say the word ends that string given word or not
print(a.startswith("Fayaz"))
print(a.swapcase())#it gives first letter as the captial remaing as the captial
