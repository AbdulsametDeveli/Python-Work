class Person:
    # 'pass' ifadesini sildik, çünkü aşağıda kodlar var.
    
    # Class Attributes (Tüm nesnelerde varsayılan)
    address = "No information" 

    def __init__(self, name, surname, birthday):
        # Instance Attributes (Her nesneye özel)
        self.name = name
        self.surname = surname
        self.birthday = birthday

    # Methods
    def calculateAge(self, current_year):
        return current_year - self.birthday

# Nesne Oluşturma (Instance)
person1 = Person("John", "Doe", 1990)
age1 = person1.calculateAge(2024) # Değişken ismini age1 yaptım karışmasın diye

person2 = Person("Jane", "Smith", 1985) 
age2 = person2.calculateAge(2024)

# Özellik Güncelleme
person1.name = "Ahmet"
person1.address = "Kocaeli"

# Çıktılar
print(f"{person1.name} {person1.surname} is {age1} years old. Address: {person1.address}")
print(f"{person2.name} {person2.surname} is {age2} years old. Address: {person2.address}")