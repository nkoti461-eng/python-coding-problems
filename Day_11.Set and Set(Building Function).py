Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #set:
... >set is unordered collection of unique element.
... >it defind as the curly braces{} or set().
... >it is mutable.
... >in this set duplicate element are automatically remove.
... a={12,13}
... type(a)
... b={'qwe','qwerty','asdfg'}
... print(b)
... b.add('zxcv')
... print(b)
... b.pop()
... print(b)
... a={12,13,14.45,5,'sharma',(123,1)}
... allow allow hashable datatypes
... if the datastructure is mutable is unhasable
... #set building Function:-
... a={1,2,3,90,'kl'}
... # a.add(70)
... # print(a)
... # a.update('ghi')
... # print(a)
... a.update('7') # it is adding and up
... print(a)
... # b=a.pop() # removing the element 
... # print(b)
... # a.clear() # remove whole set
... # print(a)
... a={12,13,14} 
... # # a.remove(14) # it remove the element
... # # print(a)
... a.discard(12) # it will remove specific element
... print(a)
... # # b={15,13,14} #it arrange in order
... # # sorted(b)
... a={11,12,13}
... b={12,14,15,16}
print(a.union(b),a|b)                                      #this |,&,-,\& are used in bitwise
print(a.intersection(b),a&b)
print(a.difference(b),b.difference(a),a-b)
