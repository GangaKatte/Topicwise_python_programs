"""
1️⃣ Create a set with at least 6 numbers.
2️⃣ Perform add, remove, union, intersection, and difference operations.
3️⃣ Print results in a formatted way.
4. check set is subset of another
"""
#1
s={1,2,3,4,5,6}
print(s)
#2
s.add(20)
print(s)
s.remove(2)
print(s)
s1={1,2,3}
s2={1,2,3,4}
print(s1|s2)
print(s1 & s2)
print(s1-s2)

#3
s={1,2,3,4,5,6}
print(s)

#4
print(s1.issubset(s2))