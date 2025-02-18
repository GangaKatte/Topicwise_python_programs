#public :Public variables and methods can be accessed from anywhere (inside or outside the class).
class Car:
    def __init__(self,model,name):
        self.model=model
        self.name=name

    def Purchases(self):
        print(f"The car  {self.name} is of model {self.model} " ) 

c1=Car("3 Series","BMW") 
print(c1.model)
print(c1.name) 
c1.Purchases()

#private:🔹 Private members are only accessible inside the class and not from outside. They cannot be accessed in subclasses.

class Car:
    def __init__(self,__life):
        self.__life=__life
        

    def Purchases(self):
        print(f"The car has {self.__life} life" ) 

c1=Car("20") 
#print(c1.__life)#cannot access
c1.Purchases()

#protected:Protected variables and methods are meant to be used within the class and subclasses.🔹 They can be accessed outside the class (Python doesn’t strictly enforce it), but it’s not recommended.
class Car:
    def __init__(self,_life):
        self._life=_life

class Showrooms(Car):        
      def Purchases(self):
          print(f"The car has {self._life} life" ) 

c1=Showrooms("20") 
print(c1._life)# allowed not recommanded
c1.Purchases()