name = 'Samet'
surname = 'Develi'
age = 20  # (istersek 20 yi '20'yazarsak hata olmuyo)
 
greeting = 'My name is '+name + ' ' + surname + 'and I am '+str(age) +'years old.'
length = len(greeting)

#print(greeting)
print(greeting[0])
print(greeting[3])
print(len(greeting)) #(toplam karekter sayısı)
print(greeting[-1])

print(greeting[2:5])  #2 ile 5 arasındaki karakterleri verir

print(greeting[2:])   #2 den başlar cümle sonuna kadar verir  