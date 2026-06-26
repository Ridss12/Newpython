#list and tuples

#list #mutable
marks=[58,"Riddhi",21,5,56,56]
print(marks[0])
print(type(marks))
print(len(marks))
print(marks[1:3])
print(marks[:5])
print(marks[1:])

#list methods
list=[2,1,3]
print(list.sort())
print(list)

list.append(4)
print(list)

list.sort() 
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list2=['a','p','q','l']#same for strings
list2.sort()
print(list2)

list.insert(1,6)
print(list)

list.pop(2)
print(list)

list.remove(1)
print(list) #or i can wite like this print(list.remove(1)) in all this


#Tuples

tup =(1,5,12,28)
print(type(tup))
print(tup[0])
print(tup[1])

tup1=(1,)#otherwise it would be an integer so couma is important to give in sigle value for multiple us couma
print(type(tup1))

#slicing in tuple same as all
print(tup[:5])

#tuple methods

t = (12,45,28,3,98,3)

print(t.index(28)) #this will print when that tuple occure on the index for first time

print(t.count(3))#this will count that how many times the 3 is repeating


#problem 1 
#WAP to ask the user to enter names of their 3 favorite movies and store them it a list

list=[]
movie =input("enter your first favorite move:")
print(list.append(movie))

movie =input("enter your second favorite move:")
print(list.append(movie))

movie =input("enter your third favorite move:")
print(list.append(movie))


print(list)



#WAP to count the number of students with grade a in following tuple
grade=["c","d","a","a","b","b","a"]
print(grade.count("a"))


#WAPstore the above value in a list and sort them  frome "a" to "b"

grade.sort()
print(grade)


#WAP to check if a list contains a palidrome of element of element(use copy() method)

l1 =[1,2,1]

copy_l1=l1.copy()
copy_l1.reverse()
 
if(copy_l1==l1):
    print("palidrome")
else:
    print("not palindrome")


