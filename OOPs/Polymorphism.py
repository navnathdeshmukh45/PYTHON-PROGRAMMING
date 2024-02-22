class Animal:
    def make_sound(self):
        return "Some generic sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"


def animal_sound(animal):
    return animal.make_sound()


dog = Dog()
cat = Cat()


print(animal_sound(dog))  # 
print(animal_sound(cat))  # 
