"""
Bytes:Collection of bytes 
Indexing, slicing is possible 
Heterogenous objects not possible
immutable


"""
b=[10,20,30,40]
by=bytes(b)

print(type(by))
for i in by:
      print(i)

""" Bytes array


Exactly same as bytes but mutable. 
"""
c=[10,20,30,40]
byy=bytearray(c)
byy[0]=11
print(type(byy))
for i in byy:
      print(i)


""""
There is one more data type which is None 

when there is output as None """
