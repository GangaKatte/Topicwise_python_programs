class Car:
    def __init__(self,model,name):
        self.model=model
        self.name=name

    def Purchases(self):
        print(f"The car  {self.name} is of model {self.model} " ) 

c1=Car("3 Series","BMW")  
c1.Car()

