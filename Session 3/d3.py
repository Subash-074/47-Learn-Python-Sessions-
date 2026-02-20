"""
Complex data type to represent complex numbers 

"""
a=5+2j
print(a)

print(type(a))

#we can also do different complex number operations 

c=3+3j
d=4+7j
print(c+d)
print(c/d)



"""
Boolean Data Type
bool 
True, False
"""

g=10
h=20
i=g>h
print(i)
print(type(i))


"""
Str data type

characters enclosed by single double or triple quotation is string data type

 

"""
n='apple'
print(type(n))

"""
Slicing of String 
Position fo string start form 0 
We can also use negative indexing to access certain portion of text from string.
"""

o="Learning Python Is Fun"

print(o[9])
print(o[-1])
print(o[:])


p='#'*10
print(p)
print(len(o))



z='hello'
print(z[0].upper()+z[1:])



"""
Type Casting


"""

v=15.8
print(v)
print(type(v))
print(int(v))
print(complex(v))
print(str(v))
m=str(v)
print(type(m))

n='20'
print(n)
print(type(n))
print(int(n))




"""
Fundamental Data Types Vs Immutability 

All fundamental data types are immutable.
Once we create an object , we cannot perform any changes in that object, if we try to change with those changes a new object is created. 

For example: you create a vote casting application, there are several instances where many citizens has same city or municipality. In such cases there must be something that seperates same city people from different city people. Therefore concept of immutability is important. 


For all same city single object id is there for different one different id will be there. 


"""

l=10
print(l)
print(id(l))#first id 
l=l+2
print(l)
print(id(l))#new id after change 

n='python'
x='python'
print(id(n))
print(id(x))
print(n is x)


