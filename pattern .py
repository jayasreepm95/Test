#type1

for n in range(1,6):
    print("* " * n)
print("_____________________________________________")
#type2

rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print(j, end=' ')
    # new line after each row
    print("\r")
print("_____________________________________________")
#type3

for n in range(1, 6):
    for c in range(1,n+1):
        print(c, end=' ')
    print(" ")
print("_____________________________________________")
#type4

for j in range(5,0,-1):
    print("* " * j)
#type5
print("_____________________________________________")
star=1
for row in range(1,6):
    for sp in range(5-row):
        print(" " ,end=" ")
    for column in range(star):
        print("*",end=" ")
    star=star+1
    print(" ")
print("_____________________________________________")    
#type6
star=1
for row in range(1,6):
    for sp in range(5-row):
        print(" " ,end=" ")
    for column in range(star):
        print("*",end=" ")
    star=star+2
    print(" ")