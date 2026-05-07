for i in range(1, 6):
    k = 4
    a = i
    for j in range(i, i+i):
        if(i == j):
            print(j, end=" ")
        else:
            a = a + k
            print(a, end=" ")
            k =k- 1
    print()