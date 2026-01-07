""" def changeName(n):
    n = "ada"
    name = 'yiğit'
    
    changeName(name)
    print(name)
    
    def change(n):
        n[0] = 'istanbul'
    sehirler = ['ankara', 'izmir']
    #change(sehirler)
    #print(sehirler)
    #n = sehirler[:] #slicing ile kopyalama
    #n[0] = 'istanbul'
    print(sehirler)
    print(n)   
    
    def add(*params):
       sum = 0
       for n in params:
           sum += n
           return sum
       print(add(10, 20))
       print(add(10, 20, 30, 40, 50)) """
       
def displayUser(**args):
    for key, value in args.items():
        print(f'{key} : {value}')
displayUser(name = 'Çınar', age = 2, city = 'istanbul')
displayUser(name = 'Ada', age = 12, city = 'kocaeli',phone = '123132')
displayUser(name = 'yiğit', age = 14, city = 'ankara',phone = '123132', email = 'yigit@gmail.com')

def myfunc(a, b,*args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    
myfunc(10, 20, 30, 40, 50, key1 = 'value1', key2 = 'value2')
    