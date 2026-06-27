#dictionary and keys

#dictionary
from typing import Dict


info ={
    "name":"Rids",
    "age": 19,
    "marks":83.20,
    "favorite_sub":["maths","english"],#we can use list
    "cgpa":(9,8,10)#we can use tuplesa
}
#dictionaries are mutable
print(info)

#nexted in dictionaries

student = {
    "std_name":"Riddhi",
    "std_age":19,
    "std_score":{
        "eng":95,
        "phy":86,
        "maths":99,
        "chem":87,
        "cs":180
    }
}
print(student)
print((student)["std_score"]["maths"])


#methods in dic

# .keys()

print(student.keys())#dic keys

#type casting

#list

print(len(list(student.keys())))#len

#tuples

print(tuple(student.keys()))

# .value()

print(student.values())

print(list(student.values()))#list

#.items
print(student.items())
print(list(student.items()))

pair = list(student.items())
print(pair[1])

pair = list(student.items())
print(pair[0])

# .item("key")

# print(student["name"]) #error
# print(student.get("name")) #none

# print(student["std_name"]) #it will print name
# print(student["std_name1"]) #error
print(student.get("std_name"))#none

#.dict()
new_dict = {"city":"Mumbai","phone":2}
student.update(new_dict)
print(student)

# new_dict = {"name":"Rridddhiii","phone":2}#name will be same key in dictionary key cant be change
# student.update(new_dict)
# print(student)


#sets (sets are mutable and elements in sets are inmuttable )

set1 ={1,2,2,3,4,5,5,"hello"}
print(set1)
print(len(set1))
print(type(set1))

#empty set
# collection = set()
# print(type(collection))



#sets methods

#set.add()
coll = set()
coll.add(1)
coll.add(2)
coll.add(2)

print(coll)

#set.clear()
# coll.clear()
# print(coll)


#set.pop()

set3 = {"hell", "Rids", "cod", "python"}
print(set3.pop())
print(set3)


#set.remove()

set4 = {"hell", "Rids", "cod", "python"}
set4.remove("cod")
print(set4)

#sety.union()

s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))
print(s1)
print(s2)

#intersection #this will highlight the mid scection
s4 ={1,2,3}
s5 ={2,3,4}
print(s4.intersection(s5))

#practice questions
#stroe following words meanining in python dictionary
# table:"a piece of furniture", c
# cat:"a small animal"

dictionary = {
    "table": ["a piece of furniture", "list of facts and figures"],
    "cat": "a small animal"
}

print(dictionary)


# you are given alist of sub for students same one classrooms is require for subjects, how many classrooms are needed by all students
#python java c++ python js java pyhon java c++

sub ={"python", "java","c++", "python", "js", "java", "pyhon","java", "c++"}

print(sub)
print(len(sub))


#WAP to enter marks of 3 sub from the users and store them in a dictionaries, start an empty dictionaries and add one by one sue sub name as key and marks as values
marks ={}

x = int(input("Enter phy:"))
marks.update({"phy":x})

x = int(input("Enter math:"))
marks.update({"math":x})

x = int(input("Enter chem:"))
marks.update({"chem":x})

print(marks)


#figure ou a way to store 9 and 9.0 as separate va;lues in the set (you can take help of built in dat type )

v1={9,"9.0"}
print(v1)


#or

val ={
    ("float",9.0),
    ("int",9)
}
print(val)
