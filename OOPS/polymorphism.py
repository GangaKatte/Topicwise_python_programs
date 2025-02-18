# Parent Class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Child Class 1 (Dog)
class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Child Class 2 (Cat)
class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Create objects of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the same method on different objects
dog.sound()  # Calls the sound() method from Dog
cat.sound()  # Calls the sound() method from Cat
