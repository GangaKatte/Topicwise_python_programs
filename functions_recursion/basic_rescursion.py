def factorial(n):
    if n==0 or n==1:#base case-stop recurrsion
        return 1
    else:
        return n*factorial(n-1)   #recursive case-function call itself 
    
print(factorial(5))    

# Simple recursion: Countdown from n to 1
def countdown(n):
    if n == 0:  # Base case (stopping condition)
        print("Done!")
        return
    print(n)
    countdown(n - 1)  # Recursive call

countdown(5)  
