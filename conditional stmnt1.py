#conditionl statements
#if and if else


"""age=int(input("Enter your age:"))
if age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")"""
"""mark=int(input("Enter your mark:"))
if mark>=95:
     print("excellent ")

elif mark>=75:
     print("very good")
elif mark >=50:
     print("good")
else:
     print("not good")"""
age=int(input("Enter your age:"))
is_member=True
if age>=60:
    if is_member:
        print("congrats you got 30% discnt")
    else:
        print("you are eligible for 10% discnt")
    print("eligible for discount")
else:
    print("not eligible for discount")
