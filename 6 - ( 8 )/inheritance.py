# Inheritance (Kalıtım): Miras Alma
#Person => name,lastname,age,eat(),run(),drink
#Student(Person), Teacher(Person)
#Animal => Dog(Animal). Cat(Animal)


class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')
        
    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        # Üst sınıfın (Person) init metodunu çağırıyoruz
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print('Student Created')

    # Override: Person'daki who_am_i metodunu eziyoruz
    def who_am_i(self):
        print('I am a student')
        
    def say_hello(self):
        print('Hello I am a student')

# --- Kullanım ---

p1 = Person('Ali', 'Yılmaz')
s1 = Student('Çınar', 'Turan', 1256)

print("-" * 20)

# İsimleri ve s1'in numarasını yazdırma
print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

print("-" * 20)

# Metotları çağırma
p1.who_am_i()  # I am a person
s1.who_am_i()  # I am a student (Override edildiği için)

p1.eat()       # I am eating
s1.eat()       # I am eating (Miras aldığı için)