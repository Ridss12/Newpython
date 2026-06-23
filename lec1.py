print("welcome to python Rids","you are the best")
print(12)
print(12+28)                                                                   

#variables
name="riddhi" #this is a variable
age=19 #this is a variable
price=28.12 #this is a variable

print("my name is:",name)
print("my age is:",age)
print("price of chocolate is:",price)

age2=age
print(age2)


#datatypes
print(type(name))
print(type(age))
print(type(price))

old=True 
a=None
print(type(old))
print(type(a))

x=12 
y=28
sum = x+y
print(sum)

s=122
t=44
diff= s-t
print(diff)
# same for others
# operations like multiplying or division

"""this is how we can write multiline comments
"""

 #operators

 #1)arithmatic 

p=36
q=12

print(p-q)
print(p+q)
print(p*q)
print(p/q)
print(p%q)
print(p**q)


#relational operators
#it gives only true or false

s=56
l=14

print(s==l)
print(s!=l)
print(s>=l)
print(s<=l)
print(s<l)
print(s>l)


#assignment operators

no = 58
no += 45
print("no:",no)

no2 = 58
no2 -= 45
print("no2:",no2)

no3 = 58
no3 *= 45
print("no3:",no3)

no4 = 58
no4 /= 45
print("no4:",no4)

no5 = 58
no5 %= 45
print("no5:",no5)

no6 = 58
no6 **= 45
print("no6:",no6)



#logical operators

u = 28
m = 12
print(not False)
print(not (u > m))

print("OR operator:",u==m or u>m)


val1 = True
val2 = False
print("AND operator:",val1 and val2)

print("OR operator:",val1 or val2)


#type conversion 

hello1 = 28
hello2 = 12.28

sum = hello1 + hello2
print(sum)#automatic converted in into float


#type casting

hel1 = float ("12") #manually convert
hel2 = 12.28

print(type(hel1))
print(hel1 + hel2)

#converting integer into string

hell3 = 3.14
hell3= str(hell3)

print(type(hell3))

#input from users

#input() 

name = input("Ente your name: ") 
print("welcome ",name)

#-> ()result for input() is always a str

valu = input("enter some value:")
print(type(valu),valu)

#int & flozt inputs

int("12")
valu = int(input("enter some value:"))#same for float we can do
print(type(valu),valu)


name = input("enter your name:")
age = int(input("Enter your age:"))
marks = float(input("enter your marks:"))

print("welcom0e",name)
print("age=", age)
print("marks=", marks)

#practice questions
#write a program to input 2 numbers and print their sum

num1 = int(input("enter first no:"))
num2 = int(input("Enter second no:"))

print("sum =" ,num1 + num2)


#WAP to input side of a sqaure and input its area

side = int(input("Enter your number:"))
print("area=",side**2)


#wap to input 2 floating points number and print thier avg

z = float(input("Enter your no1:"))
x = float(input("Enter your no2:"))
print("avg=",(z+x)/2)

#wap to input 2 int numbers a and b print true if a greater than or equal to b if not print false

n1 = int(input("enter first no:"))
n2 = int(input("Enter second no:"))

print(n1>=n2)






