#Write a program in python print the prime number 1 to 100
for i in range(1,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")