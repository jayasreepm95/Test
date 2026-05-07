s=input("enter the string=")
c_count=dict()
for k in s:
    print(k)
    if k in c_count:
        c_count[k] = c_count[k]+1
    else:
        c_count[k] = 1
    print(c_count)
    for key in c_count:
        print(key,"=" ,c_count[key])