users=input("enter the name :")
print(users[::-1]) #way1
rev=""
for i in users:
    rev=i+rev
print(rev)#way2