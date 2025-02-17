# Create a list of 5 numbers, find the sum and max value.
a=[10,50,80,90,70]
print(sum(a))
print(max(a))

# Create a list of your 3 favorite movies and add one more movie to it.
a=["Ham sath sath hai","Happy New Year","Hum Apke Hai Kaun"]
a.append("Kabhi Khushi Kabhi gam")
print(a)

#Write a program to remove duplicates from a list.
a=[1,2,5,8,7,2,5]
duplicates = []
for num in a:
    if num not in duplicates and a.count(num) > 1:
        duplicates.append(num)
    
print("Duplicates:", duplicates)



