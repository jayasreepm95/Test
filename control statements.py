#break
"""for num in range(1,10):
    if num==5:
        break
    print(num,end=" ")"""

#continue
for num in range(1,10):
    if num==5:
       continue
    print(num,end=" ")

#to implement contl stmnts using while loop

cnt = 5
while True:
    print(cnt)
    cnt = cnt-1
    if cnt == 0:
        print("Countdown finished!")
        break # Exit the loop