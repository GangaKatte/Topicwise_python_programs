#basic program

try:
    n1=int(input("enter the value 1:"))
    n2=int(input("enter the value 2:"))
    x=n1/n2
    print(x)
except Exception as x:
    print(f"The error is : {x}")    

#self raise error
age=int(input("enter the age:"))
if age>100:
    raise ValueError(f"You cannot enter age greater than 100")

 
"""
Create a simple calculator that asks the user for two numbers and an operator (+, -, *, /).
Use try-except to handle:
ZeroDivisionError (if the user divides by zero).
ValueError (if the user enters a non-numeric value).
Invalid Operator (if the user enters an operator that is not +, -, *, /).
"""
try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    if operator in ["+", "-", "*", "/"]:
        if operator == "+":
            print("Result:", n1 + n2)
        elif operator == "-":
            print("Result:", n1 - n2)
        elif operator == "*":
            print("Result:", n1 * n2)
        elif operator == "/":
            if n2 == 0:  # Handling division by zero
                print("Error: Cannot divide by zero!")
            else:
                print("Result:", n1 / n2)
    else:
        print("Error: Invalid operator! Please enter one of (+, -, *, /)")

except ValueError:
    print("Error: Please enter a valid number!")
except Exception as x:
    print("An error occurred:", x)




    
    
    
     

