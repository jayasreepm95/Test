a=(int(input("enter the first number :")))
b=(int(input("enter the second number :")))

print("1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION ")
choice=(input("please enter your choice ,1,2,3,4 = "))
match choice:
    case '1'  |"+":
        print(a+b)
    case  '2' |"-":
        print(a-b)
    case  '3' |"*":
        print(a*b)
    case   '4'|"/":
        print(a/b)
    case __:
        print("invalid input")
