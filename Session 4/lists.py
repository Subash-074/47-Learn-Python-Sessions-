"""
Lists are mutable
"""
a=[10,20,30,40]
print(id(a))
print(a)
a[0]=100
print(id(a))

"""
List: 
If we want to represent a group of values as as single entity where insertion order is preserved and duplicates are allowed we should go for list. 
"""
b=[10,20,30,40,10]
print(b)
print(type(b))

#Heterogeneous objects are allowed 
c=[10, 20, 30, True,'Ram', 'Marco', 10.9 ]
print(c)
#Indexing concept applicable 
print(c[3])
#Slicing concept applicable 
print(c[1:3])
#can add value easily in list 
c.append(55)
print(c)
#can change values easily
c[0]=1
print(c)
