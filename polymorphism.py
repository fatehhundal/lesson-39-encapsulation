class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"My name is {self.name}. I am a cat. I am {self.age} years old.")
    
    def make_sound(self):
        print("Meow.")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"My name is {self.name}. I am a dog. I am {self.age} years old.")
    
    def make_sound(self):
        print("Woof.")

cat = Cat("Mittens", 2)
dog = Dog("Goldie", 6)

for animal in (cat, dog):
    animal.make_sound()
    animal.info()