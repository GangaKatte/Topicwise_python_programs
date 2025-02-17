"""
1️⃣ Create a dictionary with at least 5 key-value pairs.
2️⃣ Iterate through keys, values, and key-value pairs using loops.
3️⃣ Print the dictionary in a formatted way.

"""
#1
a={
    "name":"abc",
    "age":20,
    "grade":"A",
    "marks":90,
    "class":"B"
}
print(a)

#2
for key in a:
    print(key)
for values in a.values():
    print(values)  
for key,value in a.items():
    print(key,value)  

#3 
for key,value in a.items():
    print(key,":",value)  
     
