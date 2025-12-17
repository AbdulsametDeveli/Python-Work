# 1- Kullanıcıdan ismini, yaşını ve eğitim durumunu alarak ehliyet alabilme
# durumunu kontrol edin.Ehliyet alma koşulu en az 18 ve eğitim durumu
# Lise ya da Üniversite olmalıdır.

isim = input("İsminiz: ")
yas = int(input("Yaşınız: "))
egitim = input("Eğitim durumunuz (Lise / Üniversite / Diğer): ").lower() # Küçük harfe çevirdik

# Koşulları kontrol ediyoruz (Yaş en az 18 VE eğitim Lise ya da Üniversite olmalı)
if (yas >= 18) 
    if (egitim == "lise" or egitim == "üniversite"):
        print(f"Sayın {isim}, ehliyet alabilirsiniz.")
    else:
        print(f"Sayın {isim}, ehliyet alamazsın eğitim durumun yetersiz.")
else:
    print(f"Sayın {isim}, ehliyet alamazsın yaşınız tutmuyor.")
    
    
# 2- Kullanıcıdan 2 yazılı ve 1 sözlü notunu alarak ortalamasını hesaplayın ve
# aşağıdaki tabloya göre not karşılığını ekrana yazdırın.
yazili1 = float(input("1. Yazılı Notu: "))
yazili2 = float(input("2. Yazılı Notu: "))
sozlu = float(input("Sözlü Notu: "))

# Ortalamayı hesaplıyoruz
ortalama = (yazili1 + yazili2 + sozlu) / 3

print(f"Ortalamanız: {ortalama:.2f}") # Virgülden sonra 2 basamak göster

# Aralıklara göre notu belirliyoruz
if 0 <= ortalama <= 24:
    print("Not Karşılığı: 0")
elif 25 <= ortalama <= 44:
    print("Not Karşılığı: 1")
elif 45 <= ortalama <= 54:
    print("Not Karşılığı: 2")
elif 55 <= ortalama <= 69:
    print("Not Karşılığı: 3")
elif 70 <= ortalama <= 84:
    print("Not Karşılığı: 4")
elif 85 <= ortalama <= 100:
    print("Not Karşılığı: 5")
else:
    print("Hesaplanan ortalama geçersiz bir aralıkta (0-100 dışı).")
    
    
    