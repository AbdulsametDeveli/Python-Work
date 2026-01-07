'''
Soru: Girilen bir sayının asal olup olmadığını kontrol eden bir Python programı yazın.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.
'''
sayi = int(input('Bir sayı girin: '))
if sayi < 2:
    print(f'{sayi} asal sayı değildir.')
else:
    asal = True
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            asal = False
            break
    if asal:
        print(f'{sayi} asal sayıdır.')
    else:
        print(f'{sayi} asal sayı değildir.')