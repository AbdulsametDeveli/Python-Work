""" def sayHello(name = 'user'):
    print('Hello ' + name )
    
sayHello('Cınar')
sayHello('Ada')
sayHello() """

def sayHello(name = 'user'):
    return 'Hello ' + name
msg = sayHello('Cınar')
msg = sayHello('Ada')
print(msg)

def total(num1, num2):
    return num1 + num2
result = total(10, 20)
result = total(5, 20)
print(result)

def yasHesapla(dogumYili):
    return 2019 - dogumYili
ageCinar = yasHesapla(2017)
ageAda = yasHesapla(2010)
ageSena = yasHesapla(1999)
print(ageCinar, ageAda, ageSena)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    Docstring for EmekliligeKacYilKaldi
    
    Input:param dogumYili: Açıklama
    Output:param isim: Açıklama
    '''
    
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f'{isim} emekliliğe {emeklilik} yıl kaldı.')
    else:
        print(f'{isim} zaten emekli oldu.')
        
EmekliligeKacYilKaldi(1985, 'Ali')
EmekliligeKacYilKaldi(1950, 'Ahmet')
EmekliligeKacYilKaldi(1974, 'Yağmur')

print(help(EmekliligeKacYilKaldi))

list = [1, 2, 3]
print(help(list.append))

