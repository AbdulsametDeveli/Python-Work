""" # x = 5
# y = 10
# z = 20

x,y,z = 5,16,20
#x,y = y,x  # swap işlemi
x = x + 5
#x += 5      # x = x + 5 ile aynı
x-= 5        # x = x - 5 ile aynı
x *= 5       # x = x * 5 ile aynı
x /= 5       # x = x / 5 ile aynı
x %= 5       # x = x % 5 ile aynı

y //=5     # y = y // 5 ile aynı
y **= 5    # y = y ** 5 ile aynı
y **= z   # y = y ** z ile aynı

#print(x,y,z) """

values  = 1,2,3,4,5  # tuple olarak atama yapar
print (values)
print (type (values))
x,y,*z = values
print(x, y, z)
print(x, y, z[1])