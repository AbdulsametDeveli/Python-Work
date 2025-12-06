"""x = input('1.sayı: ')
y = input('2.sayı: ')

print(type(x))
print(type(y))
toplam = int(x) +int(y)

print (toplam)  (int olarak toplar)
"""""
x = 5             #int
y = 2.5           #float
name = 'Çınar'    #string
isOnline = True   #bool

# print(type(x))   
# print(type(y))
# print(type(name))
# print(type(isOnline))  

# Type Conversion
# int to float   (Integer değeri float yapar)
# x = float(x)
# print(x)
# print(type(x))

# float to int   (Float değerin ondalık kısmı gider integer yapılır)
# y = int(y)
# print(y)
# print(type(y))

# result = x + y 
# print(result)
# print(type(result))   #(int ve float toplanınca sonuç float olur)

# result = str(x) + str(y) 
# print(result)
# print(type(result))    #(int ve float stringe çevrilip yan yana yazılır)

#bool to str
# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))     #(bool stringe çevrilir)

#bool to int 
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))      #(True 1, False 0 olarak int yapılır) 

