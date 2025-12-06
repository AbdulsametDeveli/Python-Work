x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
a = int(input("1. Sayı: "))
b = int(input("2. Sayı: "))

result = (a * b) - (x + y + z)
print(f"Soru 1 Sonuç: {result}")

# 2- y' nin x' e kalansız bölümünü hesaplayınız.
result = y // x
print(f"Soru 2 Sonuç: {result}")

# 3- (x,y,z) toplamının mod 3' ü nedir ?
toplam = (x + y + z)
result = toplam % 3
print(f"Soru 3 Sonuç: {result}")

# 4- y' nin x. kuvvetini hesaplayınız.
result = y ** x
print(f"Soru 4 Sonuç: {result}")

# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?
# Burada numbers listesini ayırıyoruz.
# x ilk elemanı (1), z son elemanı (6) alır.
# *y ise aradaki diğer tüm elemanları liste olarak alır ([5, 7, 10]).
x, *y, z = numbers
result = z ** 3
print(f"Soru 5 Sonuç (z'nin küpü): {result}")

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?
# y değişkeni [5, 7, 10] listesi oldu
result = sum(y) #veya y[0] + y[1] + y[2]
print(f"Soru 6 Sonuç (y'nin toplamı): {result}")