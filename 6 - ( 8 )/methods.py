#class
class Person:
    #class attributes
    address = "No information"
    def __init__(self, name, surname, birthday):
        #instance attributes
        self.name = name
        self.surname = surname
        self.birthday = birthday
    #methods
    def calculateAge(self, current_year):
        return current_year - self.birthday
#creating instances
person1 = Person("John", "Doe", 1990)
age1 = person1.calculateAge(2024)
person2 = Person("Jane", "Smith", 1985)
age2 = person2.calculateAge(2024)
#updating attributes
person1.name = "Ahmet"
person1.address = "Kocaeli"
#printing outputs
print(f"{person1.name} {person1.surname} is {age1} years old. Address: {person1.address}")
print(f"{person2.name} {person2.surname} is {age2} years old. Address: {person2.address}")

class Circle:
    #class object attribute
    pi = 3.14
    def __init__(self, yaricap=1):
        self.yaricap = yaricap
    def area(self):
        return Circle.pi * (self.yaricap ** 2)
    def circumference(self):
        return 2 * Circle.pi * self.yaricap
    
#creating instance
c1 = Circle()
c2 = Circle(5)

print(f"c1 :alan {c1.yaricap} has area: {c1.area()} and circumference: {c1.circumference()}")
print(f"c2 :alan {c2.yaricap} has area: {c2.area()} and circumference: {c2.circumference()}")

