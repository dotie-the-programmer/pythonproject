class Person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age


    def movement(self):
        print("person is walking")

person1 = Person("Evans","Male",32)
print(person1.name)

person2 = Person("Faith","Female",23)
print(person2.name)

person3 = Person("Gladys","Female",14)
print(person3.name)