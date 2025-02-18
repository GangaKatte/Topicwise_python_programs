"""
The super() function in Python is used to call a method from a parent class. It allows you to access methods and attributes from the parent class, even if they are overridden in the child class.
"""
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# Child Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed

    def speak(self):
        super().speak()  # Call the parent class method
        print(f"{self.name} barks")

# Create object of Dog class
dog = Dog("Buddy", "Golden Retriever")
dog.speak()
