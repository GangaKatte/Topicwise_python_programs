"""
1️⃣ Create a tuple with at least 6 elements.
2️⃣ Find the index of an element in the tuple.
3️⃣ Count the occurrences of an element.
4️⃣ Find the minimum and maximum values in the tuple.
5️⃣ Sort the tuple using sorted() and print the result.
"""
#1
b=(1,2,5,8,3,2,5,7)
print(b)

#2
print(b.index(5))

#3
print(b.count(2))

#4
print(min(b))
print(max(b))

#5
print(sorted(b))