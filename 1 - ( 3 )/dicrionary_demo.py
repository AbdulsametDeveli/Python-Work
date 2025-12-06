


""" ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '0532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '0532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '0532 000 00 03'
    }
}
       #1-Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgerlerle
         #dictionary içinde saklayınız.
         
       #2-Öğrenci numarasını kullanıcıdan alıp ilgili öğrencinin bilgilerini gösterin.
       
       # 1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
 """
ogrenciler = {}

# 1. Öğrenciyi Ekleme
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

# update metodu veya direkt atama ile eklenebilir:
ogrenciler[number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone
}

# 2. Öğrenciyi Ekleme 
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler[number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone
}

# 3. Öğrenciyi Ekleme 
number = input("öğrenci no: ")
name = input("öğrenci adı: ")
surname = input("öğrenci soyad: ")
phone = input("öğrenci telefon: ")

ogrenciler[number] = {
    'ad': name,
    'soyad': surname,
    'telefon': phone
}

# Oluşan listeyi görelim
print('*'*50)
print(ogrenciler)
print('*'*50)


# 2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrencinin bilgilerini gösterin.

ogrNo = input('aramak istediğiniz öğrenci no: ')
ogrenci = ogrenciler[ogrNo]

print(f"Aradığınız {ogrNo} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")