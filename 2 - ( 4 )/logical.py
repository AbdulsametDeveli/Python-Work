x = 6

hak = 5
devam = 'e'

result = 5 < x < 10  # True

#and
result = (x > 5) and (x < 10)  # True
result = (hak > 0) and (devam == 'e')  # True
 
#or
result = (x > 0) or (x % 2== 0)  # True
result = (hak > 0) or (devam == 'e')  # True

#not
result = not(x > 0) # False

# x, 5-10 arasında olan bir çift sayı mı?
result = (x >= 5) and (x <= 10) and (x % 2 == 0)


print(result)
