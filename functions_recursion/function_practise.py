"""
1️⃣ Write a function to find the factorial of a number.
2️⃣ Write a function that checks if a number is prime.
3️⃣ Write a function that returns the reverse of a string.
4️⃣ Write a function that counts vowels in a sentence.
5️⃣ Write a function to find the greatest common divisor (GCD) of two numbers.
"""

#1
def factorial(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f

print(factorial(5))

#2
def Prime(n):
    f=False
    if n>1:
        for i in range(2,n):
            if(n%i==0):
                f=True
                break
               

  
    if f == True:
       print("Not prime")    
    else:
       print("prime")             

Prime(11)

#3
def revestr(n):
    return f"reverserd string :{n[::-1]}"

n=input("enter the string:")
print(revestr(n))

#4
def vowels(n):
    count = 0
    for char in n.lower():  # Convert to lowercase to handle both cases
        if char in "aeiou":  # Check if character is a vowel
            count += 1
    return f"Number of vowels: {count}"

# Testing
print(vowels("My name is Ganga"))  # Output: Number of vowels: 6

#5
def gcd(a,b):
    while b!= 0:
       a,b=b,a%b
    return a
print(gcd(12,18))