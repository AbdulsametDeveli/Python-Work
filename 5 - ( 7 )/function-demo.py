# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.
def yazdir(kelime, adet):
    print(kelime * adet)

# Örnek kullanım
yazdir('Merhaba\n', 5)


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.
def listeyeCevir(*params):
    liste = []
    for param in params:
        liste.append(param)
    return liste

# Örnek kullanım
result = listeyeCevir(10, 20, 30, 'Merhaba')
print(result)


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

# Örnek kullanım
asalSayilariBul(10, 30)


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürün.
def tamBolenleriBul(sayi):
    tamBolenler = []
    for i in range(1, sayi + 1):
        if (sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler

# Örnek kullanım
print(tamBolenleriBul(20))