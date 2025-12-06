message = 'Hello There.My name is Samet Develi'

#message = message.upper()   #tüm harfler büyük olur
#message = message.lower()   #tüm harfler küçük olur
#message = message.title()   #her kelimenin ilk harfi büyük olur
#message = message.capitalize()  #sadece ilk harf büyük olur

#message = message.strip()   #başındaki ve sonundaki boşlukları siler
message = message.split('.')   #kelimeleri ayırır liste yapar

message = ' '.join(message)   #listeyi tekrar stringe çevirir

index = message.index('Samet')  #Samet ifadesinin başladığı indexi verir
index = message.find('Samet')   #Samet ifadesinin başladığı indexi

""" isFound = message.startswith('H')  #H ile başlıyormu True/False
print(isFound)
isFound = message.endswith('i')    #i ile bitiyormu True/False      
print(isFound) """

message = message.replace('Samet', 'Çınar')  #Samet ifadesini Çınar ile değiştirir
message = message.replace(' ', '_')  #boşlukları _ ile değiştirir

message = message.center(50, '*')  #ifadenin başına ve sonuna * ekler toplam uzunluk 50 olur

print (index)
print(message)
print(message[1])  #2.indeksteki karakteri verir