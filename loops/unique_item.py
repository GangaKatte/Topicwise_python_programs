items=["apple","banana","cherry","dragon","apple"]
uniqueitems=set(items)
print(uniqueitems)

#way2
unique_items=[]
for i in items:
    if i in unique_items:
        break
    unique_items.append(i) 

print(unique_items)       