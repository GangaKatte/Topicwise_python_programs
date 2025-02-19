"""
Read (r)	"r"	Opens file for reading (default mode)
Write (w)	"w"	Opens file for writing, overwrites existing content
Append (a)	"a"	Opens file for writing, adds new data without deleting old content
Read & Write (r+)	"r+"	Opens file for both reading and writing
Write & Read (w+)	"w+"	Opens file for writing and reading, overwrites file
Append & Read (a+)	"a+"	Opens file for appending and reading
"""


#f=open("E:\Python_Practise\error_file_handling\myfile.txt","x") #create the file

f=open("E:\Python_Practise\error_file_handling\myfile.txt","w")#write to file
f.write("Hello  moto......")
f=open("E:\Python_Practise\error_file_handling\myfile.txt","a")#append the text at last
f.write("hi mumma......")

f=open("E:\Python_Practise\error_file_handling\myfile.txt","r")#readfile
c=f.read()
print(c)

f=open("E:\Python_Practise\error_file_handling\myfile.txt","a")
f.write("I am here..i am searching u both form last an hour")

#f.close()


f=open("E:\Python_Practise\error_file_handling\myfile.txt","a")
name=input("enter the name:")
year=int(input("enter the year"))
roll_no=int(input("enter the roll_no"))
age= int(input("enter the age") ) 
f.write(f"\nName:{name }\nClass:{year}\nroll_no:{roll_no}\nage:{age}")

f=open("E:\Python_Practise\error_file_handling\myfile.txt","r")#readfile
c=f.read()
print(c)

#count number of lines

f=open("E:\Python_Practise\error_file_handling\myfile.txt","r")
c=f.readlines()
print(len(c))

#count no of words and spaces
f=open("E:\Python_Practise\error_file_handling\myfile.txt","r")
c=f.read()
words =c.split() 
spaces = c.count(" ") 
print(len(words))
print(spaces)


#vowels,consonants
c5=0
c6=0
for i in  c:
    for j in i:
        if j in "aeiou":
            c5+=1
        else:
            c6+=1
            
print("vowels",c5) 
print("constant",c6)  
