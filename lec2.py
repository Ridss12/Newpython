#strings

str1 = "Riddhi"
str2 = "mestry"
print(str1+str2)

#or we can do 
# str1 = "Riddhi"
# str2 = "mestry"
# final_str = str1+str2
# print(final_str)


#printing length
print(len(str1))

len2 = len(str2)
print(len2)

final_str =str1 +" "+ str2
print(final_str)
print(len(final_str))


#indexing
str16 = "riddhi mestry"
ch = str16[3]
print(ch)


#slicing
str12 ="Riddhi mestry"
print(str12[:5])
print(str12[3:7])
print(str12[2:])



#negative slicing
str15 ="apple"
print(str15[-5:-2])

print(str15[-1:-5])#not working


#string functions()
#endswith
str ="i am studying python"
print(str.endswith("app"))
print(str.endswith("on"))

#capitalize
print(str.capitalize())#it creates new string and assign it the value
print(str)#original string stays same

#for modifying original string we should assign it like this
str =str.capitalize()
print(str)

#find()
print(str.find("y"))

print(str.find("python"))

#count
print(str.count("y"))
print(str.count("python"))

#practice questions

#WAPto input users first name and print its length

name =input("Enter your name:")
print("length of your name is:",len(name))


#WAP to find the occurences of $ in a string

naav = "i have a lots of $ also i love $"
print(naav.count("$"))


#if,else,elif statement

#if and else

no =int(input("enter your age.:"))
if(no>=18):
    print("your are adult")
else:
    print("you are underage")    

# if,elif

light =input("what is the colour of light?")
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")

#if,elif,else

marks=int(input("enter your marks:"))
if (marks >= 90):
    print("your grade is: 'A'")
elif(marks>=80 and marks<90):
    print("your grade is: 'B'")
elif(marks>=70 and marks<80):
    print("your grade is: 'C'")
elif(marks>=60 and marks<70):
    print("your grade is: 'D'") 
elif(marks>=50 and marks<60):
    print("your grade is: 'E'") 
else:
    print("Failed")


# practice questions

#WAR TO CHECK IF A NUMBER ENTERED BY THE USER IS ODD OR EVEN

num=int(input("Enter your number:"))
if (num%2==0):
    print("the number is even")
else:
    print("the number is odd")



#WAP TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER
num1=int(input("Enter your number:"))
num2=int(input("Enter your number:"))
num3=int(input("Enter your number:"))

if(num1>num2 and num1>num3):
    print("number one the greatest",num1)
elif(num2>num3):
    print("number two is the greatest",num2)
else:
    print("nuber three is the greater",num3)

#WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7 OR NOT

x = int(input("enter your number:"))
if(x%7==0):
    print("Your number is divisible by 7")
else:
    print("your number is not divisible by 7")