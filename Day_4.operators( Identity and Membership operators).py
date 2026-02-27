Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Identity Operation:Identity operators are used to compare the objects,not if they are equal, but 
... #if they are actually the same object, with the same memory location:
... #two types:is,is not
... x=5
... y=5
... print(x is y) #here we can the x and y variable both are same then it will print True, else  diff print False
... print(x is not y) #here we can the x and y variable both are different then it will print True, else  diff print False
... 
... x=["koti","sandeep"]
... y=x=["koti","sandeep"]
... print(x is y) #here we can the x and y variable both are same then it will print True, else  diff print False
... print(x is not y) #here we can the x and y variable both are different then it will print True, else  diff print False
... print(x==y) #in this operation it will compare the two variable
... 
... #Membership Operation:it is used to check the value is present or not.
... #two types:in,not in
... x=["Dog","Cat","Snake","Rat"]
... print("Rat" in x)#it returns true when the value is present in the object,else it shows False
... 
... print("Elephant" not in x)#it returns true when the value is not present in the object,else it shows False
... #for Membership operation
... n=input("enter the value")
... print("koti" in n)
