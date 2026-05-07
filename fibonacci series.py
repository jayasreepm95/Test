#for loop
seq_count=10
a=0
b=1
print(a,b)
for k in range(seq_count-2):
    c = a + b
    a=b
    b=c

    print(c)
#while loop
"""number=int(input("Enter the sequence count : "))
num=1
first,second=0,1
print(first , second)
while num<=number-2:
    third=first+second
    print(third)
    first,second=second,third
    num=num+1
"""
"""#for loop
nterms = int(input("Enter a number: "))

n1 = 0
n2 = 1

print("\n The fibonacci sequence is :")
print(n1, ",", n2)

for i in range(2, nterms):
    next = n1 + n2
    print(next)

    n1 = n2
    n2 = next"""