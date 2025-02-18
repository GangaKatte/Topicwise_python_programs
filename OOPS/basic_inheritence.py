"""
🔹Types of Inheritance
Single Inheritance → One child inherits from one parent.
Multiple Inheritance → One child inherits from multiple parents.
Multilevel Inheritance → A child inherits from another child class.
Hierarchical Inheritance → Multiple child classes inherit from the same parent.
Hybrid Inheritance → Combination of two or more types.

"""
#single
class Animal():
      def __init__(self,name):
            self.name=name
      def speak(self):
           print(f"{self.name} i am animal.." )   

class Dog(Animal):
      def speak(self):  #overriding
            print(f"{self.name} barks...")
            
dog=Dog("Buddy") 
dog.speak()      

#multiple
class Person():
      def eat(self):
          print(" Person is Eating..") 
class Employee():
      def work(self):
          print(" Employee is working..") 
class Manager(Person,Employee):
      def boss(self):
          print(" Boss is bossing..") 

m1=Manager()
m1.boss()
m1.eat()
m1.work()          
                
#multilevel
class Device():
      def __init__(self,name):
          self.name=name
      def power_on(self):
           print("Power on your", self.name) 
class Phone (Device):
      def call(self):
           print("Calling by", self.name) 
              
class Smartphone(Phone):
    def browse_internet(self):
        print("browsing on ", self.name) 

s1=Smartphone("Iphone")
s1.power_on()
s1.call()
s1.browse_internet()
                        
#Hierarchical

class Vehicle():
       def __init__(self,name):
           self.name=name
       def start(self):
            print("start the race with >>>>",self.name)
class Car (Vehicle):
       def drive(self):
            print("Let's Drive >>>>",self.name)

class Truck(Vehicle):
      def load_cargo(self):
            print("Load is loaded  >>>>",self.name)
c1=Car("BMW")
c1.drive()
t1=Truck("XYZ")
t1.load_cargo()
v1=Vehicle("Honda")
v1.start()            

                 
#Hybird
# Parent Class 1
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Parent Class 2
class Vehicle:
    def move(self):
        print("Vehicle is moving")

# Child Class (inherits from both Animal and Vehicle)
class Car(Animal, Vehicle):
    def drive(self):
        print("Car is driving")

# Create object of Car class
car = Car()
car.sound()    # ✅ Inherited from Animal
car.move()     # ✅ Inherited from Vehicle
car.drive()    # ✅ Defined in Car
                
                      
      
