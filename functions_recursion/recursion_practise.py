"""
📝 Practice Questions
1️⃣ Write a recursive function to find the sum of digits of a number.
2️⃣ Write a recursive function to find the GCD (HCF) of two numbers.
3️⃣ Write a recursive function to reverse a string.

"""

def sum_recursive(a, b):
    if b == 0:
        return a
    return sum_recursive(a + 1, b - 1)  # Increment a, decrement b

print(sum_recursive(5, 6))  # Output: 11
