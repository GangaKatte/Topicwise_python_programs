my_dict={
    "name":"Ganga",
    "age":21,
    "College":"WIT"
}
#access
print(my_dict["name"])
print(my_dict.get("name"))

#add
my_dict["city"]="Solapur"
print(my_dict)
#update
my_dict['age']=30
print(my_dict)

#remove
del my_dict["city"]
print(my_dict)

print(my_dict.pop("age")) 

#methods
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())


for key in my_dict:
    print(key)
for values in my_dict.values():
    print(values)
for key,value in my_dict.items():
    print(key,value)

key_list=list(my_dict.keys())
i=0
while i<len(key_list):
      print(key_list[i])
      i +=1