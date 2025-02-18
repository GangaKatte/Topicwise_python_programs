#1way
def add(a,b):
    sum=a+b
    return sum

c=add(5,6)
print(c)
#2way
def add(a,b):
    sum=a+b
    return sum

print(add(5,8))

#Function with Default Arguments
def give(a="Guest"):
    return f"Hello {a}"

print(give())

#Variable Arguments (*args-allows multiple arguments and **kwargs-allows multiple keyword arguments)
def addition(*num):
    return sum(num)

print(addition(1,2,3,5))



def details(**data):
    for key,value in  data.items():
        print(f"{key} : {value}")
        
details(name="G",age=12)        

#Higher-Order Functions (Function Taking Another Function)
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16]
