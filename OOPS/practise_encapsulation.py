"""


🔹 Q1: Public Attribute Access**  
Create a `Student` class with public attributes **name** and **age**. Print the values and modify them outside the class.  

🔹 **Expected Output:**
```
Student Name: Alice
Student Age: 20
Updated Name: Bob
Updated Age: 21
```

---

### **🔹 Q2: Protected Attribute Access**  
Create a `Company` class with a protected attribute **_revenue**. Inherit this class into `Subsidiary` and access the protected attribute inside the subclass.  

🔹 **Expected Output:**
```
Company Revenue: 500000
Subsidiary Revenue: 500000
```

---

### **🔹 Q3: Private Attribute Access**  
Create a `BankAccount` class with a **private attribute** `__balance`. Add a public method `get_balance()` to access the private attribute.  

🔹 **Expected Output:**
```
Account Balance: 1000
Trying to access balance directly... ERROR!
```

---

### **🔹 Q4: Modify Private Attribute using Name Mangling**  
Modify the private attribute `__balance` of `BankAccount` using **name mangling** (`_ClassName__variable`).  

🔹 **Expected Output:**
```
Old Balance: 2000
New Balance: 5000
```

---

### **🔹 Q5: Use Getter & Setter for Private Attribute**  
Modify `BankAccount` to include a **getter (`get_balance()`) and setter (`set_balance()`)** method for `__balance`, allowing controlled access.  

🔹 **Expected Output:**
```
Old Balance: 1000
Updated Balance: 3000


"""

#1
class Student():
     def __init__(self,name,age):
         self.name=name
         self.age=age
         print(self.name,self.age)

s1=Student("Ganga",20)         
s1.name="Ishu"
s1.age=21
print(s1.name,s1.age)

#2
class Company():
      def __init__(self,_revnue):  
          self._revnue=_revnue
          print(f"Company Revenue:{self._revnue}")

class Subsidiary(Company) :
      def rev(self):
          print(f"Subsidiary Revenue:{self._revnue}") 

c1=Subsidiary(500000) 
c1.rev()

                
#3
class BankAccount():
      def __init__(self,__balance):
          self.__balance=__balance
          print("Account Balance:",self.__balance)


def get_balance(self):
           print(f"The balance is :{self.__balance}") 

c1=BankAccount(10000)   
print(c1.__balance())
c1.get_balance() 

#4
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):
        print(f"Old Balance: {self.__balance}")

c1 = BankAccount(2000)
c1.get_balance()


c1._BankAccount__balance = 5000# Modify private attribute using name mangling


print(f"New Balance: {c1._BankAccount__balance}")# Check updated balance

#5
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def get_balance(self):  # Getter method--
        return self.__balance

    def set_balance(self, new_balance):  # Setter method
        if new_balance >= 0:  # Validation: balance cannot be negative
            self.__balance = new_balance
        else:
            print("Balance cannot be negative!")

c1 = BankAccount(1000)
print(f"Old Balance: {c1.get_balance()}")

c1.set_balance(3000)  # Updating balance using setter method
print(f"Updated Balance: {c1.get_balance()}")

