"""
Set: It represents group of values in curly braces.
If we want to represent a group of values 
 without duplicates 
 insertion order is not preserved
 Heteregenous objet is allowed 
 indexing concept not applicable 
 slicing concept not applicable 
 mutable 



"""
s={10,70}
#Mutable
s.add(20)
print(s)
s.remove(70)
print(s)
#Insertion order not preserved
s.add(30)
s.add(40)
s.add(50)
print(s)
#Heteregenous objects are allowed 
s.add(True)
s.add(2.222)
s.add('max')
print(s)
#assining value is not possible due to no insertion order 
"""s[0]=11
print(s)    not possible"""
#Slicing concept not applicable 



"""
Frozenset 
exactly as set but it is immuutable 


"""
a={10}
fs=frozenset(a)

print(type(fs))
#cannot add and remove anything from set 



"""
tuples are also immutable 
 in which case will you use tuples and frozen set 
 If order important ====tuples 
 if order not imp ===frozenset 

 duplicates needed ====tuples 
 duplicates not needed ====frozenset 

 indexing, slicing needed====tuples 
 indexing slicing not needed=== frozen set 
"""

