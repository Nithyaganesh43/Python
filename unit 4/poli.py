class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

def make_sound(animal):
    print(animal.sound())

dog = Dog()
cat = Cat()
print(dog.sound()) #null
make_sound(dog)  # Output: Bark
make_sound(cat)  # Output: Meow
