#Identity Operator: is
""" 
x = y = [1,2,3]
z = [1,2,3]

print (x==y)  # True  (değerler aynı mı?)
print(x==z)  # True  (değerler aynı mı?)
print(x is y) # True  (aynı nesne mi?)
print(x is z) # False (aynı nesne mi?) """

x= [1,2,3]
y = [2,4]
del x[2]
y[1] =1
y.reverse()
print (x==y)  # True  (değerler aynı mı?)
print (x is y) # True (aynı nesne mi?)
print (x is not y) # False (aynı nesne değil mi?)

# Membership Operator: in
x = ['apple', 'banana']
print ('banana' in x)  # True

name ='Çınar'
print ('a' in name)   # True
print ('a' not in name) # False