from dis import print_instructions
from random import choice

a=(int(input("enter the first number :")))
b=(int(input("enter the second number :")))

print("1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION ")
choice=(input("please enter your choice ,1,2,3,4 = "))



if choice=='1':
    c=a+b
    print("THE SUM IS:",c)
elif choice=='2':
    c=a-b
    print("THE DIFFERENCE IS:",c)
elif choice=='3':
    c=a*b
    print("THE PRODUCT IS:",c)
elif choice=='4':

    c=(a/b)
    print("THE QUOTIENT:",c)
else:
    print("error")

