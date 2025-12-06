fruits ={'orange', 'apple', 'banana'}

#print (fruits[0]) indekslenemez
print (fruits)

for x in fruits:
    print (x)
fruits.add('cherry')
fruits.update(['mango','grape','apple']) # apple eklenmez çünkü set tekrarlı eleman kabul etmez
fruits.remove('mango')
fruits.discard('apple')

fruits.pop() # rastgele bir elemanı siler
fruits.clear() # tüm elemanları siler

print (fruits)

#myList =[1,2,5,4,4,2,1]
#print (myList)
#print (set (myList))  # tekrarlı elemanları çıkarır

