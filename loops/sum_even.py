n=int(input("enter the num : "))
count=0
sum=0
for i in range(1,n+1):
    if(i%2==0):
        sum+=i
        count+=1
print("The sum is :",sum ,"and count is :",count)        