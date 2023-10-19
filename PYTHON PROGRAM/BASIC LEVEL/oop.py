#class 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday! Now I am {self.age} years old.")
# Create instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
# Call methods on the instances
person1.greet()
person2.greet()
person1.celebrate_birthday()
person1.greet()
person2.celebrate_birthday()
person2.greet()
