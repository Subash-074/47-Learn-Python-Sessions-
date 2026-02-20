"""
Range 
Range data types represents sequence of numbers.
They are immutable 
"""
r=range(10)
print(type(r))

print(r)

for i in r:
      print(i)


a=range(10,20, 1)
for i in a:
      print(i)
b=range(40,60,2)
for i in b:
      print(i)

c=range(30,10,-2)
for i in c:
      print(i)

r=range(20,10,-1)
print(r[0])
#slicing applicable
print(r[0:3])