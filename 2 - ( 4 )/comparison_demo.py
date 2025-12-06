# 1- Girilen 2 sayıdan hangisi büyüktür?

a= int(input("a: "))
b= int(input("b: "))

result = (a > b)
print(f"a: {a} b: {b} 'den büyüktür: {result}")


# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
vize1 = float(input("1. Vize: "))
vize2 = float(input("2. Vize: "))
final = float(input("Final: "))

# İki vizenin ortalaması alınıp %60'ı, finalin %40'ı hesaplanır.
ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
print(f"Ortalamanız: {ortalama} ve durumu:{ortalama >= 50}")
# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
sayi = int(input("Bir sayı giriniz: "))
tek_cift = (sayi % 2 == 0)
print(f"Girdiğiniz sayı: {sayi} ve çift mi?: {tek_cift}")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
sayi = int(input("Bir sayı giriniz: "))
neg_pos = (sayi >= 0)
print(f"Girdiğiniz sayı: {sayi} ve pozitif mi?: {neg_pos}")

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com parola: abc123)

sys_email = "email@sadikturan.com"
sys_parola = "abc123"

girilen_email = input("Email: ")
girilen_parola = input("Parola: ")

email_dogruluk = (girilen_email == sys_email)
parola_dogruluk = (girilen_parola == sys_parola)
print(f"Email doğru mu?: {email_dogruluk} Parola doğru mu?: {parola_dogruluk}")