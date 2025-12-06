website = "https://www.sadikturan.com/"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (2024)"

# 1- 'course' karakter bulunmaktadır ?
result = len(course)
length = len(website)

# 2- 'website' içinden www karakterlerini alın.
result = website[7:10]

# 3- 'website' içinden com karakterlerini alın.
result = website[22:25]
result = website[length-3:length]

# 4- 'course' içinden ilk 15 ve son 15 karakterini alın.
result = course[0:15]
result = course[:15]   
result = course[-15:]

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
result = course[::-1]
name, surname, age, job = 'Samet', 'Develi', 20, 'Developer'

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Samet Develi, Yaşım 20 ve Mesleğim Developer'
result = 'Benim adım {} {}, Yaşım {} ve Mesleğim {}'.format(name, surname, age, job)
result = f'Benim adım {name} {surname}, Yaşım {age} ve Mesleğim {job}'

# 7- 'Hello World' ifadesindeki w harfini 'W' yapın.
result = 'Hello world'
result = result.replace('w', 'W')   

print(result)

#8- 'abc' ifadesini yan yana 3 defa yazdırın.
result = 'abc' * 3
     
print(result)