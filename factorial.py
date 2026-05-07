
#for loop
"""n=int(input("enter a number="))
fact=1
for n in range(1,n+1):
    fact=fact*n
print("factorial of a number is =",fact)"""
from math import factorial

#while loop

num = int(input("Enter a number: "))
fact = 1
i=num
while i > 0:
    fact=fact * i
    i =i-1
print(f"The factorial of {num} is {fact}")
