sayilar = [1, 3, 5, 7, 9, 12, 19, 21]
# 1- Sayilar listesindeki hangi sayilar 3 un katidır?
for sayi in sayilar:
    if sayi % 3 == 0:
        print(f'3 un katı olan sayi: {sayi}')
# 2- Sayilar listesindeki sayilarin toplamini bulunuz.
toplam = 0
for sayi in sayilar:
    toplam += sayi
print(f'Sayilarin toplami: {toplam}')
        
# 3- Sayilar listesindeki tek sayilarin karesini alınız.
for sayi in sayilar:
    if sayi % 2 != 0:
        print(f'Tek sayi: {sayi}, Karesi: {sayi**2}')  
    
    
sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']
# 4- Sehirlerden hangileri en fazla 5 karakterlidir?
for sehir in sehirler:
    if len(sehir) <= 5:
        print(f'5 karakterden az veya eşit olan şehir: {sehir}')
        
urunler = [
    {'name': 'samsung S6', 'price': '3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'},
]
# 5- Urun fiyatlari toplamı nedir?
toplam_fiyat = 0
for urun in urunler:
    toplam_fiyat += int(urun['price'])
print(f'Urun fiyatlari toplami: {toplam_fiyat}')
#6 - Fiyati en fazla 5000 olan urunleri gösteriniz.
for urun in urunler:
    if int(urun['price']) <= 5000:
        print(f'Fiyati en fazla 5000 olan urun: {urun["name"]} - Fiyat: {urun["price"]}')
numbers = [1, 2, 3, 4, 5]
