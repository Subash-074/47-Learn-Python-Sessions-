"""
Versions of Python:
Identifiers(variables)
python is case sensitive 
underscore can be used in naming 
spacing is not allowed 

reserved words or key words cannot be used as identifiers 

_a private variable
_ _a protected/strongly private variable
_ _ a_ _ Magic variables or Dunder Variables 


Reserved words/ Key Words 
 Mainly 33 Reserved words (True False and or not is if , elif, else, while, for, break, continue return, in, yield , async, try ,except, finally, raise assert, import ,from ,as ,class ,def, pass, global nonlocal, import, as, class ,def ,pass ,global, non local, lamda, del ,with  )

"""

""" Data Types """
a= 10
print(a)
print(type(a))
a=10.5
print(a)
print(type(a))

"""
Python contains 14 data types:
int , float, complex, bool, str, byte, bytearray, range , list , tuple, set, frozenset, dict, none





"""

b=0x103BEEf   #Hexadecimal number representation can be done in variable by putting 0x in front 
print(b)
print(type(b))

#This gives output in binary but if we want it in same number system 
f=0b1001 #Binary Number 
print(f)
c=0xface #Hexadecimal number 
print(bin(c))# we want output in binary 
print(oct(c))#we want output in octal 
 
print(c)  #by default every output is in decimal 

e=1.2E3   #1.2*10 power 3 is represented in such way 
print(e)
