import random

# 1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
# ** "random modülü" kullanın.
# ** 100 üzerinden puanlama yapın. (Her soru belirtilen can sayısı üzerinden hesaplansın)
# ** Hak bilgisini kullanıcıdan alın.

sayi = random.randint(1, 100)
can = int(input('Toplam hak sayısı: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 - (100/can) * (sayac-1)}')
        break
    elif sayi > tahmin:
        print('Yukarı')
    else:
        print('Aşağı')

    if hak == 0:
        print(f'Hakkınız bitti. Tutulan sayı: {sayi}')