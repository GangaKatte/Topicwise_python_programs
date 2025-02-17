a=["Grapes",100,"Mango",500,"Banana",102.50]
c=[10,50,30,95,78,89]

print(a)
print(a[4])
print(a[-2])

#add element
a.append("Apple")
print(a)
a.insert(1,"Blueberry")
print(a)

#remove
a.remove("Apple")
print(a)
b=a.pop(2)
print(b)
del a[2]
print(a)


#methods

c.sort()
print(c.sort())
print(sorted(c))


c.reverse()
print(c)

print(len(a))
print(sum(c))

#loops
for i in a:
    print(i)

i=1
while i<len(a):
      print(a[i]) 
      i +=1
