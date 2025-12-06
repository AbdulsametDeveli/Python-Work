# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ['Bmw', 'Mercedes', 'Opel', 'Mazda']

# 2- Liste Kaç elemanlıdır ?
result = len(arabalar)

# 3- Listenin ilk ve son elemanı nedir ?
ilk_eleman = arabalar[0]
son_eleman = arabalar[-1]

# 4- Mazda değerini Toyota ile değiştirin.
# Mazda son eleman olduğu için:
arabalar[-1] = 'Toyota'

# 5- Mercedes listenin bir elemanı mıdır ?
result = 'Mercedes' in arabalar

# 6- Listenin -2 indeksindeki değer nedir ?
result = arabalar[-2]

# 7- Listenin ilk 3 elemanını alın.
result = arabalar[0:3] # veya arabalar[:3]

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
# Not: Görselde "Totoya" yazılmış ancak "Toyota" olarak düzelttim.
arabalar[-2:] = ['Toyota', 'Renault']

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
# Yöntem 1: + operatörü ile
arabalar = arabalar + ['Audi', 'Nissan']
# Yöntem 2: .extend() veya .append() metodu ile de yapılabilir.

# 10- Listenin son elemanını silin.
del arabalar[-1]
# Alternatif: arabalar.pop()

# 11- Liste elemanlarını tersten yazdırınız.
result = arabalar[::-1]

# 12- Aşağıdaki verileri bir liste içinde saklayınız.
# studentA: Yiğit Bilgi 2010, (70,60,70)
# studentB: Sena Turan  1999, (80,80,70)
# studentC: Ahmet Turan 1998, (80,70,90)

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

# Hepsini tek bir listede toplamak isterseniz:
students = [studentA, studentB, studentC]

# Sonuçları görmek için yazdırma işlemi:
print(arabalar)
print(students)

# 13- Liste elemanlarını ekrana yazdırınız.
result = studentA[0]
result = studentB[1]
result = studentC[3][1]

# Yaş hesabı için süslü parantez içine matematiksel işlem ekledik:
# (Şu anki yıl - Doğum Yılı)
result = f"{studentA[0]} {studentA[1]} {2025 - studentA[2]} yaşında ve not ortalaması 66"

print(result)# Output:
# ['one', 'two', 'three', 'four', 'five', 'six']  # 6
# one