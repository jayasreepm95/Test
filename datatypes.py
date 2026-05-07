#DATATYPES IN PYTHON



# Python datatype can be classified into Numbers,String,List,Tuple,Dictionary,Set,Boolean
# Number

# int
age=27
# Float
p=3.14
# complex
d=7j

#String
language="Python"    # To access t from language --->    language[2]
print(type(language))


#List Ordered , Mutable or Changeable
my_list=['Python',45,8.2,[34,'Kochi']]
#           0      1  2     3
print(my_list[3][1])
my_list[1]=57
print(my_list)

#Tuple Immutable
s=('Python',45,8.2,[34,'Kochi'])
print(s[2])
l=(78,)
print(type(l))

# Set Unordered ,
k={67,'Kochi',12.4,"Python",12.4}

print(k)

# Dictionary
# data is stored has key : value pairs
# Values are accessed by key
my_dict={"name":"Ebin","age":27,56:12,"hobbies":["Cycling","Coding",34,12]}
print(my_dict["hobbies"][1])
print('------------------------------')
# Boolean
True
False
print('------------------------------')
name=input("Enter your name : ")
age=int(input("Enter your age : "))
print(type(age))

#print(f"My name is ",name,"and I am ",age," years old")
print(f"My name is {name} and I am {age} years old")
