#global scope
x = 'global x'

def function():
    #local scope
    #x = 'local x'
    print(x)
    function()
    print(x)
 
 
 ####################
 
name = 'Çınar'

def changeName(new_name):
    # Bu fonksiyon içinde 'name' adında yeni bir (local) değişken oluşur.
    name = new_name
    print(name)  # Burası 'Ada' yazar

changeName('Ada')
print(name)      # Burası global değişkendir, değişmez ve 'Çınar' yazar

print("-" * 20)

#####################
name = 'global string'

def greeting():
    # enclosing scope
    name = 'enclosing string'
    
    def hello():
        # local scope
        name = 'local string'
        print('Hello ' + name) # 'Hello local string' yazar
    
    hello()
    print('Hello ' + name) # 'Hello enclosing string' yazar

greeting()
print('Hello ' + name)     # 'Hello global string' yazar