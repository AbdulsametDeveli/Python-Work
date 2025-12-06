names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')

# 2- "Sena" değerini listenin başına ekleyiniz.
names.insert(0, 'Sena')

# 3- "Deniz" ismini listeden siliniz.
# names.remove('Deniz') 
# (Not: 4. soruyu denemek için bu satırı şimdilik yorum satırlı 

# 4- "Deniz" isminin indeksi nedir ?
index = names.index('Deniz')
print("Deniz'in indeksi:", index)

# 5- "Ali" listenin bir elemanı mıdır ?
result = 'Ali' in names
print("Ali listede var mı?:", result)

# 6- Liste elemanlarını ters çevirin.
names.reverse()

# 7- Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()

# 8- years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()

# 9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str_data = "Chevrolet,Dacia"
list_data = str_data.split(',')

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
min_val = min(years)
max_val = max(years)
print(f"En küçük: {min_val}, En büyük: {max_val}")

# 11- years dizisinde kaç tane 1998 değeri vardır ?
count = years.count(1998)
print("1998 sayısı:", count)

# 12- years dizisinin tüm elemanlarını siliniz.
years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []

m1 = input("1. Marka: ")
markalar.append(m1)

m2 = input("2. Marka: ")
markalar.append(m2)

m3 = input("3. Marka: ")
markalar.append(m3)

print("Girdiğiniz markalar:", markalar)