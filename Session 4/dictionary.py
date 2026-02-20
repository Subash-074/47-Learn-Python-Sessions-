"""
Dictionary 
It represents group of information as key value pair. There is comma in between each key value pair. 


"""
a={100:'Subash'}
#Mutable
a[200]='Sagar'

print(a)

#can replace values 
a[200]='Brinda'
print(a)

#Order is not preserved 
a[300]='Bunu'
a[400]='Bimala'
a[500]='Bimal' 
print(a)
#duplicates in key is not allowed but in values there can be duplicates