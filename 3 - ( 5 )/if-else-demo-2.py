'''
#1.Soru: Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
'''
sayi = float(input('Sayı: '))

if (sayi >= 0) and (sayi <= 100):
    print('Sayı 0-100 arasındadır.')
else:
    print('Sayı 0-100 arasında değildir.')
    
'''
#2.Soru: Girilen bir sayının pozitif, negatif veya nötr olduğunu kontrol ediniz.
'''
sayi = int(input('Sayı: '))


'''
# Pozitif olması için > 0, Çift olması için % 2 == 0
'''

if (sayi > 0) and (sayi % 2 == 0):
    print('Girilen sayı pozitif çift sayıdır.')
else:
    print('Girilen sayı pozitif çift sayı değildir.')
    

'''
#3.Soru Email ve parola bilgileri ile sisteme giriş kontrolü yapınız.  
'''

sys_email = 'email@sadikturan.com'
sys_password = 'abc123'

girilenEmail = input('Email: ')
girilenPassword = input('Parola: ')

if (girilenEmail == sys_email) and (girilenPassword == sys_password):
    print('Uygulamaya giriş başarılı.')
else:
    print('Email veya parola yanlış.')

'''
#4.Soru Girilen 3 sayıyı büyüklük olarak karşılaştırıp en büyüğünü ekrana yazdırınız.
'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if (a > b) and (a > c):
    print(f'En büyük sayı a: {a}')
elif (b > a) and (b > c):
    print(f'En büyük sayı b: {b}')
elif (c > a) and (c > b):
    print(f'En büyük sayı c: {c}')
else:
    print('Sayılar eşittir.')
    
'''
#5.Soru Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.

#Kural 1: Ortalama 50 veya üstü olsa bile final notu en az 50 olmalıdır.

#Kural 2: Finalden 70 alındığında ortalamanın önemi olmaksızın geçilsin.
'''

vize1 = float(input('Vize 1: '))
vize2 = float(input('Vize 2: '))
final = float(input('Final: '))

# Vize ortalamasının %60'ı + Finalin %40'ı
ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

print(f'Ortalamanız: {ortalama}')

# Geçme koşulu: (Ortalama ve Final 50'den büyükse) VEYA (Final 70'den büyükse)
if ((ortalama >= 50) and (final >= 50)) or (final >= 70):
    print('Tebrikler, geçtiniz.')
else:
    print('Maalesef kaldınız.')
    
    
'''
#6.Soru: Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.

Formül: (Kilo / boy uzunluğunun karesi)

Aralıklar: 0-18.4 => Zayıf, 18.5-24.9 => Normal, 25.0-29.9 => Fazla Kilolu, 30.0-34.9 => Şişman (Obez).
'''
ad = input('Adınız: ')
kg = float(input('Kilonuz (kg): '))
hg = float(input('Boyunuz (m): ')) # Örn: 1.75

# Kitle indeksi hesaplama
index = kg / (hg ** 2)
print(f'{ad}, Kilo İndeksiniz: {index:.2f}')

if 0 <= index <= 18.4:
    print("Durum: Zayıf")
elif 18.5 <= index <= 24.9:
    print("Durum: Normal")
elif 25.0 <= index <= 29.9:
    print("Durum: Fazla Kilolu")
elif 30.0 <= index <= 34.9:
    print("Durum: Şişman (Obez)")
else:
    print("Durum: Aşırı Obez veya hatalı giriş.")