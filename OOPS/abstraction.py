"""
Abstraction is the concept of hiding the internal details of an object and exposing only the necessary parts. In Python, abstraction can be implemented using abstract classes and abstract methods. These abstract methods are declared in the abstract class but are meant to be implemented by subclasses.
"""
"""
🎯 Assignment for Abstraction:
Create a class hierarchy:

Shape class as an abstract class with an abstract method area().
Rectangle class that inherits from Shape and implements the area() method.
Circle class that inherits from Shape and implements the area() method.
Create objects of Rectangle and Circle, and call their area() methods.


"""
from abc import ABC,abstractmethod
class Shape ():
       def __init__(self):
          pass
       @abstractmethod    
       def area():
             pass
class Rectangle(Shape):
      def area(self) :
           print("The area is l*b")
class Circle(Shape):
      def area(self) :
           print("The area is 3.14*(r**2)")

re=Rectangle()
re.area()
re=Circle
c1=Circle()
c1.area()
