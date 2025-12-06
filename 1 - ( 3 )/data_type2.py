'''
    Daire Alanı : r²π
    Daire Çevresi : 2rπ
    
    *Yarı çapı verilen bir dairenin alanını
    ve çevresini hesapla.(π=3.14)
'''
pi = 3.14
r = float (input (" yarı çap:"))
alan = pi * (r ** 2)
print(type(alan))

cevre = 2 * pi * r
print(type(cevre))

# print ('Alan:', alan)
# print ('Çevre', cevre) 
print ("alan: "+ str(alan) + "cevre: " + str(cevre)) #(floattan stringe dönüştürme)