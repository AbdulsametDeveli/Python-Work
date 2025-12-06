# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi = float(input('Sayı: '))
result = (sayi > 0) and (sayi <= 100)
print(f"Sayı 0-100 arasında mı: {result}")


# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayi = int(input('Sayı: '))
result = (sayi > 0) and (sayi % 2 == 0)
print(f"Sayı pozitif çift sayı mı: {result}")


# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = "email@sadikturan.com"
parola = "abc123"

girilen_email = input("Email: ")
girilen_parola = input("Parola: ")

result = (email == girilen_email) and (parola == girilen_parola)
print(f"Giriş Başarılı mı: {result}")


# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

# Burada "if" olmadığı için her ihtimali ayrı ayrı sorguluyoruz.
# Sadece en büyük olan "True" dönecektir.
print(f"a en büyük mü: {(a > b) and (a > c)}")
print(f"b en büyük mü: {(b > a) and (b > c)}")
print(f"c en büyük mü: {(c > a) and (c > b)}")


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
vize1 = float(input("Vize 1: "))
vize2 = float(input("Vize 2: "))
final = float(input("Final: "))

ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
print(f"Ortalamanız: {ortalama}")

# a-) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
gecme_durumu_a = (ortalama >= 50) and (final >= 50)
print(f"Geçme Durumu (Final en az 50 kuralı): {gecme_durumu_a}")

# b-) Finalden 70 alındığında ortalamanın önemi olmasın.
# Mantık: (Normal geçme şartı) VEYA (Final 70 üstüyse direkt geç)
gecme_durumu_b = (ortalama >= 50) or (final >= 70)
print(f"Geçme Durumu (Final 70 kuralı): {gecme_durumu_b}")


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
ad = input("Adınız: ")
kg = float(input("Kilonuz: "))
hg = float(input("Boyunuz (m): "))

index = kg / (hg ** 2)
print(f"{ad} kilo indeksin: {index}")

# Hangi aralıkta olduğunu True/False olarak döküyoruz:
zayif = (index >= 0) and (index <= 18.4)
normal = (index > 18.4) and (index <= 24.9)
kilolu = (index > 24.9) and (index <= 29.9)
obez = (index > 29.9) and (index <= 34.9)

print(f"Zayıf mı: {zayif}")
print(f"Normal mi: {normal}")
print(f"Fazla Kilolu mu: {kilolu}")
print(f"Şişman mı: {obez}")